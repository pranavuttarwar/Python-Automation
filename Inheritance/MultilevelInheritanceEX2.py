class wa1:
    def textmsg(self):
        print("Text Message Feature")

class wa2(wa1):
    def ac(self):
        print("Audio Call Feature")

class wa3(wa2):
    def vc(self):
        print("Video Call Feature")

w3=wa3()
w3.textmsg()
w3.ac()
w3.vc()