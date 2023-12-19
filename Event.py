from Application import Application 
import datetime
class Event(Application):
    def __init__(self):
        self.date = datetime.datetime.strftime(self.current_day(), '%Y-%m-%d')
    
    type_of_event = ["test", "online-interview", "office-interview", "phonecall"]
    tag = ["important", "more-important", "importantest"]
    
event = Event()
print(event.date)

