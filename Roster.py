from kivy.uix.gridlayout import GridLayout
from kivy.properties import ListProperty
from kivy.uix.button import Button
from kivy.uix.label import Label
from WeightClass import WeightClass
import json

class Roster(GridLayout):
 
    wList = ListProperty([])
    
    def __init__(self,**kwargs):
        super(Roster,self).__init__(**kwargs)
        
        self.buttons = []
        self.cols = 3
        self.rows = 16
        self.name = ' '
                            
        wts = [106,113,120,126,132,138,145,152,160,170,182,195,220,285]
        
        for i in range(14):
            
            self.wList.append(WeightClass())
            self.wList[i].name = str(wts[i])
            self.add_widget(Label(text=str(wts[i]), size_hint_x=0.05))
            
            self.buttons.append(Button(text='+', size_hint_x=0.05))            
            self.add_widget(self.buttons[i])            
            self.add_widget(self.wList[i])
            self.buttons[i].bind(on_press=self.wList[i].addWrestler)
            
        self.add_widget(Label(size_hint_x=0.05))
        self.add_widget(Label(size_hint_x=0.05))
        self.saveButton = Button(text='Save')    
        self.add_widget(self.saveButton)
        self.saveButton.bind(on_press=self.saveRoster)
        
        self.add_widget(Label(size_hint_x=0.05))
        self.add_widget(Label(size_hint_x=0.05))
        self.loadButton = Button(text='Load')    
        self.add_widget(self.loadButton)
        self.loadButton.bind(on_press=self.loadRoster)
    
    def saveRoster(self,value):
        
        data = {}
        
        for wclass in self.wList:
            
            weight = wclass.name
            
            data[weight] = []
            
            for name in wclass.nameList:
                
                data[weight].append(name)
                
            
        
    def loadRoster(self,value):
        
        pass