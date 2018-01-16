from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, ListProperty
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from functools import partial
from Wrestler import Wrestler

class WeightClass(GridLayout):
    
    num = NumericProperty(0)
    weightList = ListProperty([])
    nameList = ListProperty([])
    activeList = ListProperty([])
    
    def __init__(self,**kwargs):
        super(WeightClass,self).__init__(**kwargs)
        self.cols = 2
        self.name = ' '
        
    def on_enter(self,value):
        
        self.weightList.append(Wrestler(text=self.t.text))
        self.add_widget(self.weightList[self.num])
        self.weightList[self.num].bind(on_press=self.clickWrestler)
        self.nameList.append(self.t.text)
        self.num = self.num + 1
        self.remove_widget(self.t)
        
    def clickWrestler(self,instance):
        
        vals = ['106','113','120','126','132','138','145','152','160','170','182','195','220','285']
        content = BoxLayout(orientation='vertical')
        lockButton = Button(text='Lock')
        unlockButton = Button(text='Unlock')
        delButton = Button(text='Remove')
        moveButton = Spinner(text=self.name,values=vals)
        
        remCallback = partial(self.remWrestler,instance)
        delButton.bind(on_press=remCallback)
        lockButton.bind(on_press=instance.lock)
        unlockButton.bind(on_press=instance.unlock)
        
        content.add_widget(moveButton)
        content.add_widget(lockButton)
        content.add_widget(unlockButton)
        content.add_widget(delButton)
        
        popup = Popup(title=instance.text, content=content, size_hint=(.5,.5))
        popup.open()

    def addWrestler(self, value):
        
        self.t = TextInput(hint_text="Name", multiline=False)
        self.add_widget(self.t)
        self.t.bind(on_text_validate=self.on_enter)
        
    def remWrestler(self,wrest_id,butID):

        name = wrest_id.text
        self.remove_widget(wrest_id)
        self.weightList.remove(wrest_id)
        self.nameList.remove(name)
        self.num = self.num - 1
        
    def selectWrestler(self,name):
        
        self.activeList.append(name)
        
    def deselectWrestler(self,name):
        
        self.activeList.remove(name)