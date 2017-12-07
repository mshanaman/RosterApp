from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.properties import ListProperty, ObjectProperty
from collections import deque
from ClassScoreBar import ClassScoreBar

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