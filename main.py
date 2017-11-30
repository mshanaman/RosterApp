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

class ClassScoreBar(BoxLayout(orientation='horizontal')):
    
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

class WeightClass(GridLayout(cols=2)):
    
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

class Roster(GridLayout(cols=3, rows=14)):
 
    wList = ListProperty([])
    
    def __init__(self,**kwargs):
        super(Roster,self).__init__(**kwargs)
        
        wts = [106,113,120,126,132,138,145,152,160,170,182,195,220,275]
        self.buttons = []
        
        for i in range(14):
            
            self.wList.append(WeightClass())
            
            self.add_widget(Label(text=str(wts[i]), size_hint_x=0.05))
            
            self.buttons.append(Button(text='+', size_hint_x=0.05))
            self.buttons[i].bind(on_press=self.wList[i].addWrestler())
            self.add_widget(self.buttons[i])
            
            self.add_widget(self.wList[i])

class MainWidget(TabbedPanel):
        
    def __init__(self,**kwargs):
        super(MainWidget,self).__init__(**kwargs)
        
        self.UsRoster = TabbedPanelHeader(text='Our Team')
        self.ThemRoster = TabbedPanelHeader(text='Their Team')
        
        self.UsRoster.content = Roster()
        self.ThemRoster.content = Roster()
        
        self.add_widget(self.UsRoster)
        self.add_widget(self.ThemRoster)
        
        
    
class WrestlingApp(App):
    
    def build(self):
        MainApp = MainWidget()
        return MainApp

if __name__ == '__main__':
    WrestlingApp().run()