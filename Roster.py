from kivy.uix.gridlayout import GridLayout
from kivy.properties import ListProperty
from kivy.uix.button import Button
from kivy.uix.label import Label
from WeightClass import WeightClass

class Roster(GridLayout):
 
    wList = ListProperty([])
    
    def __init__(self,**kwargs):
        super(Roster,self).__init__(**kwargs)
        
        self.buttons = []
        self.cols = 3
        self.rows = 14
                            
        wts = [106,113,120,126,132,138,145,152,160,170,182,195,220,285]
        
        for i in range(14):
            
            self.wList.append(WeightClass())
            
            self.add_widget(Label(text=str(wts[i]), size_hint_x=0.05))
            
            self.buttons.append(Button(text='+', size_hint_x=0.05))            
            self.add_widget(self.buttons[i])            
            self.add_widget(self.wList[i])
            self.buttons[i].bind(on_press=self.wList[i].addWrestler)