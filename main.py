from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import NumericProperty, ListProperty, ObjectProperty

class weightClass(GridLayout):
    num = NumericProperty(0)
    weightList = ListProperty([])
    
    def addWrestler(self):
        self.weightList.append(TextInput(text='Name'))
        self.add_widget(self.weightList[self.num])
        self.num = self.num + 1
        
        
    
#class roster(BoxLayout):
#    pass

class WrestlingApp(App):
    
    def build(self):
        home = weightClass()
        return home

if __name__ == '__main__':
    WrestlingApp().run()
