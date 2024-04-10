from kivy.app import App
from kivy.uix.widget import Widget



class AgriWidget(Widget):
    pass

class AgriApp(App):
    def build(self):
        return AgriWidget()

if __name__ == '__main__':
    print('Hello from agri/__main__.py!')
    app = AgriApp()
    app.run()