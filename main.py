import flet as ft

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
    page.update()

if __name__ == '__main__':
    ft.app(target = main)