from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.tabbedpanel import TabbedPanelHeader
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
    
    UsRoster = ObjectProperty(None)
    ThemRoster = ObjectProperty(None)    
        
    def __init__(self,**kwargs):
        super(ClassScoreBar,self).__init__(**kwargs)
        
        self.orientation='horizontal'
        
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
        self.LNameText = 'default'
        self.RNameText = 'default'
        
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
        
        self.LName.bind(text=self.editNameLists)
        self.RName.bind(text=self.editNameLists)
        
    def setWeight(self,wt):
        wts = [106,113,120,126,132,138,145,152,160,170,182,195,220,275]
        self.weight = wt
        idx = wts.index(wt)
        self.wt_idx = idx
        self.LLabel.text = str(wt)
        self.RLabel.text = str(wt)
        
        if wt is 106:
            
            self.UsRoster.wList[idx].bind(nameList=self.updateNames)
            self.ThemRoster.wList[idx].bind(nameList=self.updateNames)
            
        else:
            
            self.UsRoster.wList[idx].bind(nameList=self.updateNames)
            self.UsRoster.wList[idx-1].bind(nameList=self.updateNames)
            self.ThemRoster.wList[idx].bind(nameList=self.updateNames)
            self.ThemRoster.wList[idx-1].bind(nameList=self.updateNames)
            
    def updateNames(self, instance, names):
        
        if self.weight is 106:
            
            tempList_L = self.UsRoster.wList[self.wt_idx].nameList
            tempList_R = self.ThemRoster.wList[self.wt_idx].nameList
            activeList_L = self.UsRoster.wList[self.wt_idx].activeList
            activeList_R = self.ThemRoster.wList[self.wt_idx].activeList
                           
            tempList_L = [x for x in tempList_L if x not in activeList_L]                
            tempList_R = [x for x in tempList_R if x not in activeList_R]
                
            self.LName.values = tempList_L
            self.RName.values = tempList_R
            
        else:
            
            tempList_L = self.UsRoster.wList[self.wt_idx].nameList + self.UsRoster.wList[self.wt_idx-1].nameList
            tempList_R = self.ThemRoster.wList[self.wt_idx].nameList + self.ThemRoster.wList[self.wt_idx-1].nameList
            activeList_L = self.UsRoster.wList[self.wt_idx].activeList + self.UsRoster.wList[self.wt_idx-1].activeList
            activeList_R = self.ThemRoster.wList[self.wt_idx].activeList + self.ThemRoster.wList[self.wt_idx-1].activeList

            tempList_L = [x for x in tempList_L if x not in activeList_L]                
            tempList_R = [x for x in tempList_R if x not in activeList_R]
                
            self.LName.values = tempList_L
            self.RName.values = tempList_R
    
    def editNameLists(self, spinner, txt):
        
        if spinner is self.LName:
            
            if self.weight is 106:
            
                if self.LNameText is not 'default':
                
                    self.UsRoster.wList[self.wt_idx].deselectWrestler(self.LNameText)
                
                self.LNameText = txt
                self.UsRoster.wList[self.wt_idx].selectWrestler(txt)

            else:                
           
                if self.LNameText is not 'default':
                    
                    if txt in self.UsRoster.wList[self.wt_idx].nameList:
                
                        self.UsRoster.wList[self.wt_idx].deselectWrestler(self.LNameText)
                        self.UsRoster.wList[self.wt_idx].selectWrestler(txt)
                        
                    else:

                        self.UsRoster.wList[self.wt_idx-1].deselectWrestler(self.LNameText)
                        self.UsRoster.wList[self.wt_idx-1].selectWrestler(txt)

                self.LNameText = txt
                
            
        elif spinner is self.RName:
            
            if self.weight is 106:
            
                if self.RNameText is not 'default':
                
                    self.ThemRoster.wList[self.wt_idx].deselectWrestler(self.RNameText)
                
                self.RNameText = txt
                self.ThemRoster.wList[self.wt_idx].selectWrestler(txt)

            else:                
           
                if self.RNameText is not 'default':
                    
                    if txt in self.ThemRoster.wList[self.wt_idx].nameList:
                
                        self.ThemRoster.wList[self.wt_idx].deselectWrestler(self.RNameText)
                        self.ThemRoster.wList[self.wt_idx].selectWrestler(txt)
                        
                    else:

                        self.ThemRoster.wList[self.wt_idx-1].deselectWrestler(self.RNameText)
                        self.ThemRoster.wList[self.wt_idx-1].selectWrestler(txt)

                self.RNameText = txt

class DualMeet(BoxLayout):
    
    ScoreBarList = ListProperty([])
    weights = deque([106,113,120,126,132,138,145,152,160,170,182,195,220,275])
    UsRoster = ObjectProperty(None)
    ThemRoster = ObjectProperty(None)
    
    def __init__(self,**kwargs):
        super(DualMeet,self).__init__(**kwargs)
        
        self.orientation = 'vertical'        
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
        
    def populate(self):

        for i in range(14):
            
            self.ScoreBarList.append(ClassScoreBar())
            self.ScoreBarList[i].UsRoster = self.UsRoster
            self.ScoreBarList[i].ThemRoster = self.ThemRoster
            self.add_widget(self.ScoreBarList[i])
            self.ScoreBarList[i].setWeight(self.weights[i])
        

class Wrestler(Button):
    
    pass

class WeightClass(GridLayout):
    
    num = NumericProperty(0)
    weightList = ListProperty([])
    nameList = ListProperty([])
    activeList = ListProperty([])
    
    def __init__(self,**kwargs):
        super(WeightClass,self).__init__(**kwargs)
        self.cols = 2
        
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

class Roster(GridLayout):
 
    wList = ListProperty([])
    
    def __init__(self,**kwargs):
        super(Roster,self).__init__(**kwargs)        
        
        self.buttons = []
        self.cols = 3
        self.rows = 14
                            
        wts = [106,113,120,126,132,138,145,152,160,170,182,195,220,275]
        
        for i in range(14):
            
            self.wList.append(WeightClass())
            
            self.add_widget(Label(text=str(wts[i]), size_hint_x=0.05))
            
            self.buttons.append(Button(text='+', size_hint_x=0.05))            
            self.add_widget(self.buttons[i])            
            self.add_widget(self.wList[i])
            self.buttons[i].bind(on_press=self.wList[i].addWrestler)
            
class MainWidget(TabbedPanel):
        
    def __init__(self,**kwargs):
        super(MainWidget,self).__init__(**kwargs)
        
        self.UsRoster = TabbedPanelHeader(text='Our Team')
        self.ThemRoster = TabbedPanelHeader(text='Their Team')        
        self.UsRoster.content = Roster()
        self.ThemRoster.content = Roster()        
        self.add_widget(self.UsRoster)
        self.add_widget(self.ThemRoster)
        
        self.VMeet = TabbedPanelHeader(text='Varsity Meet')
        self.JVMeet = TabbedPanelHeader(text='Junior Varsity Meet')
        self.VMeet.content = DualMeet()
        self.JVMeet.content = DualMeet()        
        self.add_widget(self.VMeet)
        self.add_widget(self.JVMeet)
        self.JVMeet.content.UsRoster = self.UsRoster.content
        self.JVMeet.content.ThemRoster = self.ThemRoster.content        
        self.VMeet.content.UsRoster = self.UsRoster.content
        self.VMeet.content.ThemRoster = self.ThemRoster.content
        self.VMeet.content.populate()
        self.JVMeet.content.populate()        
    
class WrestlingApp(App):
    
    def build(self):
        MainApp = MainWidget()
        return MainApp

if __name__ == '__main__':
    WrestlingApp().run()