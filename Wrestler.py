from kivy.uix.button import Button
from kivy.properties import NumericProperty, BooleanProperty

class Wrestler(Button):    
    
    wclass = NumericProperty(106)
    locked = BooleanProperty(False)
    
    def lock(self, buttID):
        
        self.locked = True
        
    def unlock(self, buttID):
        
        self.locked = False