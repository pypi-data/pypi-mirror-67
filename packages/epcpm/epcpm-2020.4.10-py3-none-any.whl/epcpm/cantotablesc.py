import attr
import epyqlib.utils.general

import epcpm.canmodel


builders = epyqlib.utils.general.TypeMap()


def export(path, can_model):
    builder = builders.wrap(
        wrapped=can_model.root,
        parameter_uuid_finder=can_model.node_from_uuid,
        path=path,
    )

    path.parent.mkdir(parents=True, exist_ok=True)
    builder.gen()


@builders(epcpm.canmodel.Root)
@attr.s
class Root:
    wrapped = attr.ib()
    parameter_uuid_finder = attr.ib()
    path = attr.ib(default=None)

    def gen(self):
        lines = [
            '#include <stdbool.h>',
            '',
            '#include "canInterfaceGen.h"',
            '#include "gridMonitor.h"',
            '#include "utils.h"',
            '#include "IQmathLib.h"',
            '',
            '',
        ]

        table_results = []

        parameter_query = self.wrapped.child_by_name('ParameterQuery')

        for child in parameter_query.children:
            if not isinstance(child, epcpm.canmodel.CanTable):
                continue

            builder = builders.wrap(
                wrapped=child,
                parameter_uuid_finder=self.parameter_uuid_finder,
            )

            table_results.append(builder.gen())

            lines.extend(table_results[-1].table_lines)
            lines.append('')

        content = epyqlib.utils.general.format_nested_lists(lines)

        with self.path.open('w', newline='\n') as f:
            f.write(content)
        return


@attr.s
class TableResults:
    table_lines = attr.ib()


@builders(epcpm.canmodel.CanTable)
@attr.s
class CanTable:
    wrapped = attr.ib()
    parameter_uuid_finder = attr.ib()

    def gen(self):
        parameter_table = self.parameter_uuid_finder(
            self.wrapped.table_uuid,
        )

        return TableResults(
            table_lines=self.table_lines(parameter_table=parameter_table),
        )

    def table_lines(self, parameter_table):
        lines = []

        can_getter = parameter_table.can_getter
        can_setter = parameter_table.can_setter

        for child in self.wrapped.children:
            if not isinstance(child, epcpm.canmodel.Multiplexer):
                continue

            builder = builders.wrap(
                wrapped=child,
                table_name=self.wrapped.name,
                can_getter=can_getter,
                can_setter=can_setter,
                parameter_uuid_finder=self.parameter_uuid_finder,
            )

            for get_or_set in ('get', 'set'):
                new_lines = builder.gen(get_or_set=get_or_set)
                if len(new_lines) > 0:
                    lines.extend(new_lines)
                    lines.append('')

        return lines


# TODO: CAMPid 079549750417808543178043180
def get_curve_type(combination_string):
    # TODO: backmatching
    return {
        'LowRideThrough': 'IEEE1547_CURVE_TYPE_LRT',
        'HighRideThrough': 'IEEE1547_CURVE_TYPE_HRT',
        'LowTrip': 'IEEE1547_CURVE_TYPE_LTRIP',
        'HighTrip': 'IEEE1547_CURVE_TYPE_HTRIP',
    }.get(combination_string)


@builders(epcpm.canmodel.Multiplexer)
@attr.s
class Multiplexer:
    wrapped = attr.ib()
    table_name = attr.ib()
    can_getter = attr.ib()
    can_setter = attr.ib()
    parameter_uuid_finder = attr.ib()

    def gen(self, get_or_set):
        children_lines = []

        curve_group_string, _, _ = self.wrapped.name.partition('_')
        curve_type = get_curve_type(curve_group_string)

        for child in self.wrapped.children:
            builder = builders.wrap(
                wrapped=child,
                table_name=self.table_name,
                can_getter=self.can_getter,
                can_setter=self.can_setter,
                multiplexer_name=self.wrapped.name,
                curve_type=curve_type,
                parameter_uuid_finder=self.parameter_uuid_finder,
            )

            children_lines.extend(builder.gen(
                get_or_set=get_or_set,
            ))

        if len(children_lines) > 0 and all(line is None for line in children_lines):
            return []

        children_lines = [
            line
            for line in children_lines
            if line is not None
        ]

        lines = [
            'void {get_or_set}{table}{mux}(void)'.format(
                get_or_set=get_or_set,
                table=self.table_name,
                mux=self.wrapped.name,
            ),
            '{',
            children_lines,
            '}'
        ]

        return lines

    def point_count(self):
        return len(self.wrapped.children)


@builders(epcpm.canmodel.Signal)
@attr.s
class Signal:
    wrapped = attr.ib()
    table_name = attr.ib()
    multiplexer_name = attr.ib()
    can_getter = attr.ib()
    can_setter = attr.ib()
    curve_type = attr.ib()
    parameter_uuid_finder = attr.ib()

    def gen(self, get_or_set):
        interface_signal = 'ParameterQuery.{table}{mux}.{signal}'.format(
            table=self.table_name,
            mux=self.multiplexer_name,
            signal=self.wrapped.name,
        )

        table_array_element = self.parameter_uuid_finder(
            self.wrapped.parameter_uuid
        )

        original = table_array_element
        while not isinstance(original, epyqlib.pm.parametermodel.Parameter):
            original = original.original

        if original.uses_interface_item():
            return [None]

        if isinstance(original.tree_parent, epyqlib.pm.parametermodel.Group):
            can_getter = original.can_getter
            can_setter = original.can_setter
        elif isinstance(original.tree_parent, epyqlib.pm.parametermodel.Array):
            can_getter = self.can_getter
            can_setter = self.can_setter

        if can_getter is None:
            can_getter = ''

        if can_setter is None:
            can_setter = ''

        axis = table_array_element.tree_parent.axis
        if axis is None:
            axis = '<no axis>'

        curve_index = table_array_element.tree_parent.tree_parent.curve_index

        lines = [
            {
                'get': can_getter,
                'set': can_setter,
            }[get_or_set].format(
                curve_type=self.curve_type,
                interface_signal=interface_signal,
                point_index=table_array_element.index,
                axis=axis,
                upper_axis=axis.upper(),
                curve_index=curve_index,
            )
        ]

        lines = [
            line
            for line in lines
            if len(line.strip()) > 0
        ]

        return lines
