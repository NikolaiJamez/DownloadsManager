from flet import (
    Row,
    TextField,
    IconButton,
    icons,
    colors,
    MainAxisAlignment
)

class Rule_Row(Row):
    def __init__(self, idx, on_click, data):
        super().__init__()
        self.controls = [
            TextField(label = 'Label', value = data[0]),
            TextField(label = 'Relative Directory Path', value = data[1]),
            TextField(label = 'Pattern', value = data[2]),
            IconButton(
                icon = icons.DELETE,
                icon_color = colors.RED,
                tooltip = 'Delete Rule',
                on_click = on_click,
                data = idx
            )
        ]
        self.alignment = MainAxisAlignment.CENTER
        self.data = idx
    
    def build(self):
        return self