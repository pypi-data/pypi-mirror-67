import msvcrt

class simButton:
    

    def __init__(self,startkey,endkey,on,off):
        self.startkey = startkey
        self.endkey = endkey
        self.on = on
        self.off = off

        while True:
            try:
                if msvcrt.kbhit():
                    key_stroke = msvcrt.getch()
                    print(key_stroke)   # will print which key is pressed

                    if key_stroke.decode("utf-8") == self.startkey:
                        self.on()
                    elif key_stroke.decode("utf-8") == self.endkey:
                        self.off()

            except KeyboardInterrupt as kerr:
                exit(0)

    