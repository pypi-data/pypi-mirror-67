import winsound

class simLED:
   

    def __init__(self):
        self.is_lit = False

    def on(self):
        winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS | winsound.SND_LOOP |  winsound.SND_ASYNC)
        self.is_lit = True

    
    def off(self):
        winsound.PlaySound("SystemExclamation",  winsound.SND_ALIAS | winsound.SND_PURGE)
        self.is_lit = False