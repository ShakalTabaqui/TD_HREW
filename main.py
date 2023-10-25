from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.utils import get_color_from_hex

class Interface(BoxLayout):
    def __init__(self, **kwargs):
        super(Interface, self).__init__(**kwargs)
        
        # Создаем виджет Label
        label = Label(
            text="[color=#f55442]T[/color][color=#f59842]D[/color] [color=#f5e342]H[/color][color=#42f55a]R[/color][color=#42cef5]E[/color][color=#1316d1]W[/color][color=#8d42f5]![/color]",
            font_size="32sp",
            markup=True
        )
        
        self.add_widget(label)

class MyApp(App):
    def build(self):
        return Interface()

if __name__ == '__main__':
    MyApp().run()
