from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from WeightClass import WeightClass
import json

class Roster(BoxLayout):
 
    wList = ListProperty([])
    
    def __init__(self,**kwargs):
        super(Roster,self).__init__(**kwargs)
        
        self.orientation = 'vertical'
        self.buttons = []
        self.name = ' '
                            
        wts = [106,113,120,126,132,138,145,152,160,170,182,195,220,285]
        self.barList = []
        self.teamText = TextInput(hint_text="Team Name", multiline=False, font_size=30)
        self.add_widget(self.teamText)
        
        for i in range(14):
            
            self.wList.append(WeightClass())
            self.wList[i].name = str(wts[i])
            self.barList.append(BoxLayout(orientation='horizontal'))
            self.barList[i].add_widget(Label(text=str(wts[i]), size_hint_x=0.05))
            
            self.buttons.append(Button(text='+', size_hint_x=0.05))            
            self.barList[i].add_widget(self.buttons[i])            
            self.barList[i].add_widget(self.wList[i])
            self.buttons[i].bind(on_press=self.wList[i].addWrestler)
            self.add_widget(self.barList[i])
            
        #self.add_widget(Label(size_hint_x=0.05))
        #self.add_widget(Label(size_hint_x=0.05))
        self.saveButton = Button(text='Save')    
        self.add_widget(self.saveButton)
        self.saveButton.bind(on_press=self.saveRoster)
        
        #self.add_widget(Label(size_hint_x=0.05))
        #self.add_widget(Label(size_hint_x=0.05))
        self.loadButton = Button(text='Load')    
        self.add_widget(self.loadButton)
        self.loadButton.bind(on_press=self.loadRoster)
    
    def saveRoster(self,value):
        
        data = {}
        teamName = self.teamText.text
        
        data[teamName] = []
        
        for wclass in self.wList:
            
            weight = wclass.name
            
            data[weight] = []
            
            for name in wclass.nameList:
                
                data[weight].append(name)            
        
    def loadRoster(self,value):
        
        pass