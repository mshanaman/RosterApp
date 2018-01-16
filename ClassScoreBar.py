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
        
        vals = ['0','3','4','5','6']
        scoreSize = 0.1
        
        self.LLabel = Label(size_hint_x=scoreSize)
        self.LName = Spinner()
        self.LPred = Spinner(text='0', values=vals, size_hint_x=scoreSize)
        self.LAct = Spinner(text='0', values=vals, size_hint_x=scoreSize)
        self.LNeed = Label(text='0', size_hint_x=scoreSize)
        self.slider = Slider(min=0, max=10, value=5)
        self.RLabel = Label(size_hint_x=scoreSize)
        self.RName = Spinner()
        self.RPred = Spinner(text='0', values=vals, size_hint_x=scoreSize)
        self.RAct = Spinner(text='0', values=vals, size_hint_x=scoreSize)
        self.RNeed = Label(text='0', size_hint_x=scoreSize)
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
        if wt != 106:
            wtDwn = wts[idx-1]
            self.weightDwn = wtDwn
        self.wt_idx = idx
        self.LLabel.text = str(wt)
        self.RLabel.text = str(wt)
        self.LName.bind(text=self.updateNames)
        self.RName.bind(text=self.updateNames)
        
        if wt == 106:
            
            self.UsRoster.wList[wt].bind(nameList=self.updateNames)
            self.ThemRoster.wList[wt].bind(nameList=self.updateNames)
                        
        else:
            
            self.UsRoster.wList[wt].bind(nameList=self.updateNames)
            self.UsRoster.wList[wtDwn].bind(nameList=self.updateNames)
            self.ThemRoster.wList[wt].bind(nameList=self.updateNames)
            self.ThemRoster.wList[wtDwn].bind(nameList=self.updateNames)
                        
    def bind2Neighbors(self):
               
        self.LName.bind(text=self.parent.Daddy.updateWCs)
        self.LPred.bind(text=self.parent.totalScores)
        self.RPred.bind(text=self.parent.totalScores)
        self.LAct.bind(text=self.parent.totalScores)
        self.RAct.bind(text=self.parent.totalScores)
                        
    def updateNames(self, instance, names):
        
        if self.weight == 106:
            
            tempList_L = self.UsRoster.wList[self.weight].nameList
            tempList_R = self.ThemRoster.wList[self.weight].nameList
            activeList_L = self.UsRoster.wList[self.weight].activeList
            activeList_R = self.ThemRoster.wList[self.weight].activeList
                           
            tempList_L = [x for x in tempList_L if x not in activeList_L]                
            tempList_R = [x for x in tempList_R if x not in activeList_R]
                
            self.LName.values = tempList_L + ['FF']
            self.RName.values = tempList_R + ['FF']
            
        else:
            
            tempList_L = self.UsRoster.wList[self.weight].nameList + self.UsRoster.wList[self.weightDwn].nameList
            tempList_R = self.ThemRoster.wList[self.weight].nameList + self.ThemRoster.wList[self.weightDwn].nameList
            activeList_L = self.UsRoster.wList[self.weight].activeList + self.UsRoster.wList[self.weightDwn].activeList
            activeList_R = self.ThemRoster.wList[self.weight].activeList + self.ThemRoster.wList[self.weightDwn].activeList

            tempList_L = [x for x in tempList_L if x not in activeList_L]                
            tempList_R = [x for x in tempList_R if x not in activeList_R]
                
            self.LName.values = tempList_L + ['FF']
            self.RName.values = tempList_R + ['FF']
    
    def editNameLists(self, spinner, txt):
        
        if spinner is self.LName:
            
            if self.weight == 106:            
                if self.LNameText != 'default':                
                    self.UsRoster.wList[self.weight].deselectWrestler(self.LNameText)
                    
                self.UsRoster.wList[self.weight].selectWrestler(txt)                    
                self.LNameText = txt
            else:           
                if self.LNameText != 'default':                    
                    if self.LNameText in self.UsRoster.wList[self.weight].activeList:                
                        self.UsRoster.wList[self.weight].deselectWrestler(self.LNameText)                        
                    else:
                        self.UsRoster.wList[self.weightDwn].deselectWrestler(self.LNameText)
                if txt in self.UsRoster.wList[self.weight].nameList:                    
                    self.UsRoster.wList[self.weight].selectWrestler(txt)                    
                else:                    
                    self.UsRoster.wList[self.weightDwn].selectWrestler(txt)
                    
                self.LNameText = txt                
            
        elif spinner is self.RName:
            
            if self.weight == 106:            
                if self.RNameText != 'default':                
                    self.ThemRoster.wList[self.weight].deselectWrestler(self.RNameText)
                    
                self.ThemRoster.wList[self.weight].selectWrestler(txt)
                self.RNameText = txt
            else:           
                if self.RNameText != 'default':                    
                    if self.RNameText in self.ThemRoster.wList[self.weight].activeList:                
                        self.ThemRoster.wList[self.weight].deselectWrestler(self.RNameText)                        
                    else:
                        self.ThemRoster.wList[self.weightDwn].deselectWrestler(self.RNameText)
                if txt in self.ThemRoster.wList[self.weight].nameList:                    
                    self.ThemRoster.wList[self.weight].selectWrestler(txt)                    
                else:                    
                    self.ThemRoster.wList[self.weight].selectWrestler(txt)

                self.RNameText = txt