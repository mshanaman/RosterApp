from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.properties import ListProperty, ObjectProperty, NumericProperty, DictProperty
from collections import deque
from ClassScoreBar import ClassScoreBar

class DualMeet(BoxLayout):
    
    ScoreBarList = DictProperty({})
    UsRoster = ObjectProperty(None)
    ThemRoster = ObjectProperty(None)
    Daddy = ObjectProperty(None)
    Differ = NumericProperty(0)
    
    def __init__(self,**kwargs):
        super(DualMeet,self).__init__(**kwargs)
        
        scoreSize = 0.1
        self.weights = deque([106,113,120,126,132,138,145,152,160,170,182,195,220,285])
        
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

        for i in self.weights:
            
            self.ScoreBarList[i] = ClassScoreBar()
            self.add_widget(self.ScoreBarList[i])
            self.ScoreBarList[i].UsRoster = self.UsRoster
            self.ScoreBarList[i].ThemRoster = self.ThemRoster
            self.ScoreBarList[i].setWeight(i)
            
        for j in self.weights:
            
            self.ScoreBarList[j].bind2Neighbors()
            
        self.Totals = BoxLayout()
        self.Totals.add_widget(Label(size_hint_x=scoreSize))
        self.Totals.add_widget(Label())
        self.PredTotUs = Label(text='0', size_hint_x=scoreSize)
        self.Totals.add_widget(self.PredTotUs)
        self.ActTotUs = Label(text='0', size_hint_x=scoreSize)
        self.Totals.add_widget(self.ActTotUs)
        self.Totals.add_widget(Label(size_hint_x=scoreSize))
        self.startVals = ['Starting at 106','Starting at 113','Starting at 120','Starting at 126','Starting at 132','Starting at 138','Starting at 145','Starting at 152','Starting at 160','Starting at 170','Starting at 182','Starting at 195','Starting at 220','Starting at 285']
        self.StartWeight = Spinner(values=self.startVals,text_autoupdate=True)
        self.Totals.add_widget(self.StartWeight)
        self.Totals.add_widget(Label(size_hint_x=scoreSize))
        self.PredTotThem = Label(text='0', size_hint_x=scoreSize)
        self.ActTotThem = Label(text='0', size_hint_x=scoreSize)
        self.Totals.add_widget(self.ActTotThem)        
        self.Totals.add_widget(self.PredTotThem)
        self.Totals.add_widget(Label())
        self.Totals.add_widget(Label(size_hint_x=scoreSize))        
        self.add_widget(self.Totals)
        
        self.StartWeight.bind(text=self.RotateWeights)

    def RotateWeights(self,ID,value):
        
        idx = self.startVals.index(value)
        self.weights.rotate(-idx)
        
        for w, o in self.ScoreBarList.items():
            
            self.remove_widget(o)
            
        self.remove_widget(self.Totals)
        
        for w in self.weights:
            
            self.add_widget(self.ScoreBarList[w])
        
        self.add_widget(self.Totals)
        
    def updateWCs(self):

        for k in self.weights:
            
            self.ScoreBarList[k].updateNames('nothing','nothing')

    def totalScores(self,instance,text):
        
        UsPredTot = 0
        UsActTot = 0
        ThemPredTot = 0
        ThemActTot = 0
        
        for i in self.weights:
            
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

        