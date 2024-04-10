from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder





class AgriStatusScreen(Screen):
    pass

class AgriSettingsScreen(Screen):
    pass

class AgriPowerScreen(Screen):
    pass

class AgriVarScreen(Screen):
    pass

class AgriChecksScreen(Screen):
    pass

class AgriMainWindow(Screen):
    pass

class AgriWindowManager(ScreenManager):
    pass


class AgriApp(App):
    def build(self):
        kv = Builder.load_file('agri/agriwindowmanager.kv')
        # Window
        self.window = GridLayout()
        self.window.cols = 1
        self.window.add_widget(Image(source='agri/images/ASD.png'))
        self.window.size_hint = (0.5, 0.5)
        self.window.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        

        # UI elements
        self.greeting = Label(text="Hello, world!")
        self.window.add_widget(self.greeting)
        self.user = TextInput(multiline=False)
        self.window.add_widget(self.user)

        # Buttons
        self.button = Button(text="Greet")
        self.window.add_widget(self.button)
        return kv
