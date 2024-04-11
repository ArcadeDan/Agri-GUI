from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock    
from kivy.lang import Builder
from kivy.config import Config 
from kivy.core.window import Window


from time import strftime   

class AgriStatusScreen(Screen):
    Builder.load_file('agri/kvs/agristatusscreen.kv')

class AgriSettingsScreen(Screen):

    Builder.load_file('agri/kvs/agrisettingsscreen.kv')

class AgriPowerScreen(Screen):
    Builder.load_file('agri/kvs/agripowerscreen.kv')

class AgriVarScreen(Screen):
    Builder.load_file('agri/kvs/agrivarscreen.kv')

class AgriChecksScreen(Screen):
    Builder.load_file('agri/kvs/agrichecksscreen.kv')

class AgriMainWindow(Screen):
    Builder.load_file('agri/kvs/agrimainwindow.kv')

class AgriWindowManager(ScreenManager):
    pass


class AgriApp(App):
    
    # could not for the life of me get the timer to work.

    # for the clock in the settings page
    #def update(self, tick):
    #    self.root.ids.screen_manager.get_screen('AgriSettingsScreen').ids.time.text = strftime('%H:%M:%S')
    #
    #def on_start(self):
    #   Clock.schedule_interval(self.update, 0)

    def build(self):
    
        Window.size = (1024, 600)

        kv = Builder.load_file('agri/kvs/agriwindowmanager.kv')
        return kv
