from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.properties import ListProperty
from kivy.properties import DictProperty
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from WeightClass import WeightClass
import json
import os

class Roster(BoxLayout):
 
    wList = DictProperty({})
    
    def __init__(self,**kwargs):
        super(Roster,self).__init__(**kwargs)
        
        self.orientation = 'vertical'
        self.buttons = []
        self.name = ' '
                            
        wts = [106,113,120,126,132,138,145,152,160,170,182,195,220,285]
        self.barList = []
        self.teamText = TextInput(hint_text="Team Name", multiline=False, font_size=30)
        self.add_widget(self.teamText)
        
        for i in wts:
            
            self.wList[i] = WeightClass()
            self.wList[i].name = str(i)
            self.barList.append(BoxLayout(orientation='horizontal'))
            self.barList[-1].add_widget(Label(text=str(i), size_hint_x=0.05))
            
            self.buttons.append(Button(text='+', size_hint_x=0.05))            
            self.barList[-1].add_widget(self.buttons[-1])            
            self.barList[-1].add_widget(self.wList[i])
            self.buttons[-1].bind(on_press=self.wList[i].addWrestler)
            self.add_widget(self.barList[-1])
            
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
        
        try:        
            with open('wrestData.dat','r') as db:
                    
                if os.stat('wrestData.dat').st_size != 0:
                    data = json.load(db)
                else:
                    data = {}
        except IOError:
            data = {}
                    
        teamName = self.teamText.text    
        data[teamName] = {}
                
        for weight, wclass in self.wList.items():
                                    
            data[teamName][weight] = []
                    
            for name in wclass.nameList:
                        
                data[teamName][weight].append(name)
                
        with open('wrestData.dat', 'w') as db:
            
            json.dump(data,db)
                
    def loadRoster(self,value):
                
        with open('wrestData.dat','r') as db:
            
            data = json.load(db)
            
        teams = list(data.keys())
               
        content = BoxLayout()
        buttonList = []
        
        def finishLoading(instance):
                
            teamData = data[instance.text]
            self.teamText.text = instance.text
        
            for weight in list(teamData.keys()):
                for name in teamData[weight]:
                            
                    self.wList[int(weight)].addWrestler(1)
                    self.wList[int(weight)].t.text = name
                    self.wList[int(weight)].on_enter(1)
        
        for i in teams:
            
            buttonList.append(Button(text=i))
            buttonList[-1].bind(on_press=finishLoading)
            content.add_widget(buttonList[-1])
        
        popup = Popup(title='Choose Team', content=content, auto_dismiss=False, size_hint=(.5,.5))
        
        for button in popup.content.children:
            
            button.bind(on_press=popup.dismiss)
            
        popup.open()
            

        
        

        
            
            
            