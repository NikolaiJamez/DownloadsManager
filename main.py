import flet as ft

def main(page: ft.Page) -> None:
    def check_item_clicked(e):
        e.control.checked = not e.control.checked
        page.update()

    page.window_height = 600
    page.window_width = 1000
    page.window_resizable = False
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER


    page.appbar = ft.AppBar(
        leading = ft.Icon(ft.icons.PALETTE),
        leading_width = 40,
        title = ft.Text("AppBar Example"),
        center_title = False,
        bgcolor = ft.colors.SURFACE_VARIANT,
        actions = [
            ft.IconButton(ft.icons.WB_SUNNY_OUTLINED),
            ft.IconButton(ft.icons.FILTER_3),
            ft.PopupMenuButton(
                items = [
                    ft.PopupMenuItem(text = "Item 1"),
                    ft.PopupMenuItem(),  # divider
                    ft.PopupMenuItem(
                        text = "Checked item",
                        checked = False,
                        on_click = check_item_clicked
                    ),
                ]
            ),
        ],
    )
    page.update()

ft.app(target = main)