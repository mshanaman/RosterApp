from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.properties import ListProperty, ObjectProperty, NumericProperty
from collections import deque
from ClassScoreBar import ClassScoreBar

class DualMeet(BoxLayout):
    
    ScoreBarList = ListProperty([])
    weights = deque([106,113,120,126,132,138,145,152,160,170,182,195,220,285])
    UsRoster = ObjectProperty(None)
    ThemRoster = ObjectProperty(None)
    Daddy = ObjectProperty(None)
    Differ = NumericProperty(0)
    
    def __init__(self,**kwargs):
        super(DualMeet,self).__init__(**kwargs)
        
        scoreSize = 0.1
        
        self.orientation = 'vertical'        
        self.Title = BoxLayout()
        self.Title.add_widget(Label(text='Wt', size_hint_x=scoreSize))
        self.Title.add_widget(Label(text='Name'))
        self.Title.add_widget(Label(text='Prd', size_hint_x=scoreSize))
        self.Title.add_widget(Label(text='Act', size_hint_x=scoreSize))
        self.Title.add_widget(Label(text='Rec', size_hint_x=scoreSize))
        self.Title.add_widget(Label(text='Odds'))
        self.Title.add_widget(Label(text='Rec', size_hint_x=scoreSize))
        self.Title.add_widget(Label(text='Act.', size_hint_x=scoreSize))
        self.Title.add_widget(Label(text='Prd', size_hint_x=scoreSize))
        self.Title.add_widget(Label(text='Name'))
        self.Title.add_widget(Label(text='Wt', size_hint_x=scoreSize))        
        self.add_widget(self.Title)
        
    def populate(self):
        
        scoreSize = 0.1

        for i in range(14):
            
            self.ScoreBarList.append(ClassScoreBar())
            self.add_widget(self.ScoreBarList[i])
            self.ScoreBarList[i].UsRoster = self.UsRoster
            self.ScoreBarList[i].ThemRoster = self.ThemRoster
            self.ScoreBarList[i].setWeight(self.weights[i])
            
        for j in range(14):
            
            self.ScoreBarList[j].bind2Neighbors()
            
        self.Totals = BoxLayout()
        self.Totals.add_widget(Label(size_hint_x=scoreSize))
        self.Totals.add_widget(Label())
        self.PredTotUs = Label(text='0', size_hint_x=scoreSize)
        self.Totals.add_widget(self.PredTotUs)
        self.ActTotUs = Label(text='0', size_hint_x=scoreSize)
        self.Totals.add_widget(self.ActTotUs)
        self.Totals.add_widget(Label(size_hint_x=scoreSize))
        self.Totals.add_widget(Label())
        self.Totals.add_widget(Label(size_hint_x=scoreSize))
        self.PredTotThem = Label(text='0', size_hint_x=scoreSize)
        self.ActTotThem = Label(text='0', size_hint_x=scoreSize)
        self.Totals.add_widget(self.ActTotThem)        
        self.Totals.add_widget(self.PredTotThem)
        self.Totals.add_widget(Label())
        self.Totals.add_widget(Label(size_hint_x=scoreSize))        
        self.add_widget(self.Totals)
            
    def updateWCs(self):

        for k in range(14):
            
            self.ScoreBarList[k].updateNames('nothing','nothing')

    def totalScores(self,instance,text):
        
        UsPredTot = 0
        UsActTot = 0
        ThemPredTot = 0
        ThemActTot = 0
        
        for i in range(14):
            
            UsAct = int(self.ScoreBarList[i].LAct.text)
            ThemAct = int(self.ScoreBarList[i].RAct.text)
            check = UsAct + ThemAct
            
            UsPred = int(self.ScoreBarList[i].LPred.text)
            ThemPred = int(self.ScoreBarList[i].RPred.text)
            
            if check > 0:
                
                UsPredTot = UsPredTot + UsAct
                ThemPredTot = ThemPredTot + ThemAct
                
            else:
                
                UsPredTot = UsPredTot + UsPred
                ThemPredTot = ThemPredTot + ThemPred
                
            UsActTot = UsActTot + UsAct
            ThemActTot = ThemActTot + ThemAct

        self.ActTotUs.text = str(UsActTot)
        self.ActTotThem.text = str(ThemActTot)
        self.PredTotUs.text = str(UsPredTot)
        self.PredTotThem.text = str(ThemPredTot)
        self.Differ = ThemActTot - UsActTot

        