from dataclasses import dataclass
import flet as ft
from custom_controls.rule_row import Rule_Row

@dataclass
class variables:
    RULE_COUNTER: int = 0
    RULES_FILENAME: str = 'rules.csv'


def main(page: ft.Page) -> None:

    def close_app(e: ft.ControlEvent) -> None:
        page.window_close()

    def add_rule(e: ft.ControlEvent = None, rule_data = ['', '', '']) -> None:
        rules_column.controls.append(
            Rule_Row(variables.RULE_COUNTER, delete_rule, rule_data)
        )
        variables.RULE_COUNTER = variables.RULE_COUNTER + 1
        rules_column.update()

    def refresh_rules(e: ft.ControlEvent = None) -> None:
        rules_column.controls = []
        with open(variables.RULES_FILENAME, 'r') as in_file:
            for row in in_file:
                items = row.strip().split(',')
                add_rule(rule_data = items)
        
    def save_rules(e: ft.ControlEvent) -> None:
        with open(variables.RULES_FILENAME, 'w') as out_file:
            for row in rules_column.controls:
                items = [control.value for control in row.controls[:-1]]
                out_file.write(','.join(items))
                out_file.write('\n')
    
    def delete_rule(e: ft.ControlEvent) -> None:
        for idx, control in enumerate(rules_column.controls):
            if control.data != e.control.data:
                continue
            rules_column.controls.pop(idx)
            rules_column.update()
            return
    
    def delete_all_rules(e: ft.ControlEvent) -> None:
        rules_column.controls = []
        rules_column.update()

    def run_rules(e: ft.ControlEvent) -> None:
        raise NotImplementedError('Running rules has not been implemented yet!')

    
    page.window_height = 600
    page.window_width = 1000
    page.window_resizable = False
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    last_run_value = 'Never'
    last_run_control = ft.Text(last_run_value)

    page.appbar = ft.AppBar(
        leading = ft.Icon(ft.icons.DOWNLOADING_ROUNDED),
        leading_width = 40,
        title = ft.Text('Downloads Manager'),
        center_title = False,
        bgcolor = ft.colors.SURFACE_VARIANT,
        actions = [
            ft.Text('Last Run: '),
            last_run_control,
            ft.IconButton(
                icon = ft.icons.PLAY_ARROW_ROUNDED,
                icon_color = ft.colors.GREEN,
                tooltip = 'Run Now',
                on_click = run_rules,
            ),
            ft.IconButton(
                icon = ft.icons.CLOSE,
                icon_color = ft.colors.RED,
                tooltip = 'Close App',
                on_click = close_app,
            ),
            ft.VerticalDivider(),
        ],
    )

    rules_column = ft.Column()

    page.add(
        ft.Text('Rules', size = 30),
        ft.Row(
            [
                ft.IconButton(
                    icon = ft.icons.ADD_ROUNDED,
                    tooltip = 'Add Rule',
                    on_click = add_rule,
                ),
                ft.IconButton(
                    icon = ft.icons.REFRESH_ROUNDED,
                    tooltip = 'Refresh Rules',
                    on_click = refresh_rules,
                ),
                ft.IconButton(
                    icon = ft.icons.SAVE,
                    icon_color = ft.colors.GREEN,
                    tooltip = 'Save Rules',
                    on_click = save_rules,
                ),
                ft.IconButton(
                    icon = ft.icons.DELETE_FOREVER_ROUNDED,
                    icon_color = ft.colors.RED,
                    tooltip = 'Delete All Rules',
                    on_click = delete_all_rules,
                ),
            ],
            alignment = ft.MainAxisAlignment.CENTER
        ),
    ft.Divider(opacity = 0),
    rules_column,
    ft.Divider(opacity = 0, height = 40),
    )
    refresh_rules()
    page.update()

if __name__ == '__main__':
    ft.app(target = main)