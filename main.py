from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.pagelayout import PageLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.slider import Slider
from kivy.properties import NumericProperty, ListProperty, ObjectProperty

from collections import deque

class ClassScoreBar(BoxLayout):
    
    app = App.get_running_app()
    
    def __init__(self,**kwargs):
        super(ClassScoreBar,self).__init__(**kwargs)
        
        self.LLabel = Label(size_hint_x=0.05)
        self.LName = Spinner()
        self.LPred = TextInput(text='0', multiline=False, size_hint_x=0.05)
        self.LAct = TextInput(text='0', multiline=False, size_hint_x=0.05)
        self.LNeed = TextInput(text='0', multiline=False, size_hint_x=0.05)
        self.slider = Slider(min=0, max=10, value=5)
        self.RLabel = Label(size_hint_x=0.05)
        self.RName = Spinner()
        self.RPred = TextInput(text='0', multiline=False, size_hint_x=0.05)
        self.RAct = TextInput(text='0', multiline=False, size_hint_x=0.05)
        self.RNeed = TextInput(text='0', multiline=False, size_hint_x=0.05)
        
        self.add_widget(self.LLabel)
        self.add_widget(self.LName)
        self.add_widget(self.LPred)
        self.add_widget(self.LAct)
        self.add_widget(self.LNeed)
        self.add_widget(self.slider)
        self.add_widget(self.RNeed)
        self.add_widget(self.RAct)
        self.add_widget(self.RPred)
        self.add_widget(self.RName)
        self.add_widget(self.RLabel)
        
    def setWeight(self,wt):
        wts = [106,113,120,126,132,138,145,152,160,170,182,195,220,275]
        idx = wts.index(wt)
        self.LLabel.text = str(wt)
        self.RLabel.text = str(wt)
        
        if wt is 106:
            
            self.LName.values = self.app.root.ids.us.wList[idx].nameList
            self.RName.values = self.app.root.ids.them.wList[idx].nameList
            
        else:
            
            self.LName.values = app.root.ids.us.wList[idx].nameList + app.root.ids.us.wList[idx-1].nameList
            self.RName.values = app.root.ids.them.wList[idx].nameList + app.root.ids.them.wList[idx-1].nameList
            
        

class DualMeet(BoxLayout):
    
    ScoreBarList = ListProperty([])
    weights = deque([106,113,120,126,132,138,145,152,160,170,182,195,220,275])
    
    def __init__(self,**kwargs):
        super(DualMeet,self).__init__(**kwargs)
        
        self.Title = BoxLayout()
        self.Title.add_widget(Label(text='Wt', size_hint_x=0.05))
        self.Title.add_widget(Label(text='Name'))
        self.Title.add_widget(Label(text='Prd', size_hint_x=0.05))
        self.Title.add_widget(Label(text='Act', size_hint_x=0.05))
        self.Title.add_widget(Label(text='Rec', size_hint_x=0.05))
        self.Title.add_widget(Label(text='Odds'))
        self.Title.add_widget(Label(text='Rec', size_hint_x=0.05))
        self.Title.add_widget(Label(text='Act.', size_hint_x=0.05))
        self.Title.add_widget(Label(text='Prd', size_hint_x=0.05))
        self.Title.add_widget(Label(text='Name'))
        self.Title.add_widget(Label(text='Wt', size_hint_x=0.05))        
        
        self.add_widget(self.Title)
        
        for i in range(14):
            
            self.ScoreBarList.append(ClassScoreBar())
            self.add_widget(self.ScoreBarList[i])
            self.ScoreBarList[i].setWeight(self.weights[i])
        

class Wrestler(Button):
    
    pass

class WeightClass(GridLayout):
    
    num = NumericProperty(0)
    weightList = ListProperty([])
    nameList = ListProperty([])
        
    def on_enter(self,value):
        
        self.weightList.append(Wrestler(text=self.t.text))
        self.add_widget(self.weightList[self.num])
        self.weightList[self.num].bind(on_press=self.remWrestler)
        self.nameList.append(self.t.text)
        self.num = self.num + 1
        self.remove_widget(self.t)

    def addWrestler(self):
        
        self.t = TextInput(hint_text="Name", multiline=False)
        self.add_widget(self.t)
        self.t.bind(on_text_validate=self.on_enter)
        
    def remWrestler(self,wrest_id):
        
        self.remove_widget(wrest_id)
        self.weightList.remove(wrest_id)
        self.num = self.num - 1
        
    def selectWrestler(self,name):
        
        self.nameList.remove(name)
        
    def deselectWrestler(self,name):
        
        self.nameList.append(name)

class Roster(GridLayout):

    w106 = ObjectProperty(None)
    w113 = ObjectProperty(None)
    w120 = ObjectProperty(None)
    w126 = ObjectProperty(None)
    w132 = ObjectProperty(None)
    w138 = ObjectProperty(None)
    w145 = ObjectProperty(None)
    w152 = ObjectProperty(None)
    w160 = ObjectProperty(None)
    w170 = ObjectProperty(None)
    w182 = ObjectProperty(None)
    w195 = ObjectProperty(None)
    w220 = ObjectProperty(None)
    w275 = ObjectProperty(None)    
    wList = ListProperty([w106,w113,w120,w126,w132,w138,w145,w152,w160,w170,w182,w195,w220,w275])
    
class WrestlingApp(App):
    
    def build(self):
        MainApp = TabbedPanel()
        return MainApp

if __name__ == '__main__':
    WrestlingApp().run()