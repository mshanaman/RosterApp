from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.slider import Slider
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty

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
        wts = [106,113,120,126,132,138,145,152,160,170,182,195,220,285]
        self.weight = wt
        idx = wts.index(wt)
        self.wt_idx = idx
        self.LLabel.text = str(wt)
        self.RLabel.text = str(wt)
        self.LName.bind(text=self.updateNames)
        self.RName.bind(text=self.updateNames)
        
        if wt == 106:
            
            self.UsRoster.wList[idx].bind(nameList=self.updateNames)
            self.ThemRoster.wList[idx].bind(nameList=self.updateNames)
                        
        else:
            
            self.UsRoster.wList[idx].bind(nameList=self.updateNames)
            self.UsRoster.wList[idx-1].bind(nameList=self.updateNames)
            self.ThemRoster.wList[idx].bind(nameList=self.updateNames)
            self.ThemRoster.wList[idx-1].bind(nameList=self.updateNames)
                        
    def bind2Neighbors(self):
        
#        if self.weight == 106:
#            
#            self.LName.bind(text=self.parent.ScoreBarList[self.wt_idx+1].updateNames)
#            self.RName.bind(text=self.parent.ScoreBarList[self.wt_idx+1].updateNames)
#            
#        elif self.weight == 285:
#            
#            self.LName.bind(text=self.parent.ScoreBarList[self.wt_idx-1].updateNames)
#            self.RName.bind(text=self.parent.ScoreBarList[self.wt_idx-1].updateNames)                
#            
#        else:
#            
#            self.LName.bind(text=self.parent.ScoreBarList[self.wt_idx-1].updateNames)
#            self.RName.bind(text=self.parent.ScoreBarList[self.wt_idx-1].updateNames)
#            self.LName.bind(text=self.parent.ScoreBarList[self.wt_idx+1].updateNames)
#            self.RName.bind(text=self.parent.ScoreBarList[self.wt_idx+1].updateNames)
        
        self.LName.bind(text=self.parent.Daddy.updateWCs)
                        
    def updateNames(self, instance, names):
        
        if self.weight == 106:
            
            tempList_L = self.UsRoster.wList[self.wt_idx].nameList
            tempList_R = self.ThemRoster.wList[self.wt_idx].nameList
            activeList_L = self.UsRoster.wList[self.wt_idx].activeList
            activeList_R = self.ThemRoster.wList[self.wt_idx].activeList
                           
            tempList_L = [x for x in tempList_L if x not in activeList_L]                
            tempList_R = [x for x in tempList_R if x not in activeList_R]
                
            self.LName.values = tempList_L + ['FF']
            self.RName.values = tempList_R + ['FF']
            
        else:
            
            tempList_L = self.UsRoster.wList[self.wt_idx].nameList + self.UsRoster.wList[self.wt_idx-1].nameList
            tempList_R = self.ThemRoster.wList[self.wt_idx].nameList + self.ThemRoster.wList[self.wt_idx-1].nameList
            activeList_L = self.UsRoster.wList[self.wt_idx].activeList + self.UsRoster.wList[self.wt_idx-1].activeList
            activeList_R = self.ThemRoster.wList[self.wt_idx].activeList + self.ThemRoster.wList[self.wt_idx-1].activeList

            tempList_L = [x for x in tempList_L if x not in activeList_L]                
            tempList_R = [x for x in tempList_R if x not in activeList_R]
                
            self.LName.values = tempList_L + ['FF']
            self.RName.values = tempList_R + ['FF']
    
    def editNameLists(self, spinner, txt):
        
        if spinner is self.LName:
            
            if self.weight == 106:            
                if self.LNameText != 'default':                
                    self.UsRoster.wList[self.wt_idx].deselectWrestler(self.LNameText)
                    
                self.UsRoster.wList[self.wt_idx].selectWrestler(txt)                    
                self.LNameText = txt
            else:           
                if self.LNameText != 'default':                    
                    if self.LNameText in self.UsRoster.wList[self.wt_idx].activeList:                
                        self.UsRoster.wList[self.wt_idx].deselectWrestler(self.LNameText)                        
                    else:
                        self.UsRoster.wList[self.wt_idx-1].deselectWrestler(self.LNameText)
                if txt in self.UsRoster.wList[self.wt_idx].nameList:                    
                    self.UsRoster.wList[self.wt_idx].selectWrestler(txt)                    
                else:                    
                    self.UsRoster.wList[self.wt_idx-1].selectWrestler(txt)
                    
                self.LNameText = txt                
            
        elif spinner is self.RName:
            
            if self.weight == 106:            
                if self.RNameText != 'default':                
                    self.ThemRoster.wList[self.wt_idx].deselectWrestler(self.RNameText)
                    
                self.ThemRoster.wList[self.wt_idx].selectWrestler(txt)
                self.RNameText = txt
            else:           
                if self.RNameText != 'default':                    
                    if self.RNameText in self.ThemRoster.wList[self.wt_idx].activeList:                
                        self.ThemRoster.wList[self.wt_idx].deselectWrestler(self.RNameText)                        
                    else:
                        self.ThemRoster.wList[self.wt_idx-1].deselectWrestler(self.RNameText)
                if txt in self.ThemRoster.wList[self.wt_idx].nameList:                    
                    self.ThemRoster.wList[self.wt_idx].selectWrestler(txt)                    
                else:                    
                    self.ThemRoster.wList[self.wt_idx-1].selectWrestler(txt)

                self.RNameText = txt