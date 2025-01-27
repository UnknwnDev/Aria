from kivy.uix.button import Button


class CustomButton(Button):
    def __init__(self, **kwargs):
        super(CustomButton, self).__init__(**kwargs)
        self.text = "Click Me"
        self.size_hint = (0.2, 0.2)
        self.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        self.bind(on_press=self.on_button_press)

    def on_button_press(self, instance):
        print("Button pressed!")
