from kivy.uix.gridlayout import GridLayout
from kivy.properties import NumericProperty, ListProperty
from kivy.uix.textinput import TextInput
from Wrestler import Wrestler

class WeightClass(GridLayout):
    
    num = NumericProperty(0)
    weightList = ListProperty([])
    nameList = ListProperty([])
    activeList = ListProperty([])
    
    def __init__(self,**kwargs):
        super(WeightClass,self).__init__(**kwargs)
        self.cols = 2
        self.name = ' '
        
    def on_enter(self,value):
        
        self.weightList.append(Wrestler(text=self.t.text))
        self.add_widget(self.weightList[self.num])
        self.weightList[self.num].bind(on_press=self.remWrestler)
        self.nameList.append(self.t.text)
        self.num = self.num + 1
        self.remove_widget(self.t)

    def addWrestler(self, value):
        
        self.t = TextInput(hint_text="Name", multiline=False)
        self.add_widget(self.t)
        self.t.bind(on_text_validate=self.on_enter)
        
    def remWrestler(self,wrest_id):
        name = wrest_id.text
        self.remove_widget(wrest_id)
        self.weightList.remove(wrest_id)
        self.nameList.remove(name)
        self.num = self.num - 1
        
    def selectWrestler(self,name):
        
        self.activeList.append(name)
        
    def deselectWrestler(self,name):
        
        self.activeList.remove(name)