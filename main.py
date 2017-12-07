from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.tabbedpanel import TabbedPanelHeader
from DualMeet import DualMeet
from Roster import Roster
            
class MainWidget(TabbedPanel):
        
    def __init__(self,**kwargs):
        super(MainWidget,self).__init__(**kwargs)
        
        self.UsRoster = TabbedPanelHeader(text='Our Team')
        self.ThemRoster = TabbedPanelHeader(text='Their Team')        
        self.UsRoster.content = Roster()
        self.ThemRoster.content = Roster()        
        self.add_widget(self.UsRoster)
        self.add_widget(self.ThemRoster)
        
        self.VMeet = TabbedPanelHeader(text='Varsity Meet')
        self.JVMeet = TabbedPanelHeader(text='Junior Varsity Meet')
        self.VMeet.content = DualMeet()
        self.JVMeet.content = DualMeet()        
        self.add_widget(self.VMeet)
        self.add_widget(self.JVMeet)
        self.JVMeet.content.UsRoster = self.UsRoster.content
        self.JVMeet.content.ThemRoster = self.ThemRoster.content        
        self.VMeet.content.UsRoster = self.UsRoster.content
        self.VMeet.content.ThemRoster = self.ThemRoster.content
        self.VMeet.content.populate()
        self.JVMeet.content.populate()        
    
class WrestlingApp(App):
    
    def build(self):
        MainApp = MainWidget()
        return MainApp

if __name__ == '__main__':
    WrestlingApp().run()