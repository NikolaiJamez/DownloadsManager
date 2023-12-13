import flet as ft
from custom_controls.rule_row import Rule_Row


def main(page: ft.Page) -> None:

    def close_app(e: ft.ControlEvent) -> None:
        page.window_close()


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
                    # on_click = ,
                ),
                ft.IconButton(
                    icon = ft.icons.REFRESH_ROUNDED,
                    tooltip = 'Refresh Rules',
                    # on_click = ,
                ),
                ft.IconButton(
                    icon = ft.icons.SAVE,
                    icon_color = ft.colors.GREEN,
                    tooltip = 'Save Rules',
                    # on_click = ,
                ),
                ft.IconButton(
                    icon = ft.icons.DELETE_FOREVER_ROUNDED,
                    icon_color = ft.colors.RED,
                    tooltip = 'Delete All Rules',
                    # on_click = ,
                ),
            ],
            alignment = ft.MainAxisAlignment.CENTER
        ),
    ft.Divider(opacity = 0),
    rules_column,
    ft.Divider(opacity = 0, height = 40),
    )

    page.update()

if __name__ == '__main__':
    ft.app(target = main)