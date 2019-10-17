from PyQt4 import QtCore
from time import *
from GameClient import *
# defines a thread which emits signals with the message
class PlayThread(QtCore.QThread,GameClient):

    message_signal = QtCore.pyqtSignal(str)       # create signal
    
    def __init__(self,parent=None):
        
        super(PlayThread,self).__init__(parent)
        
        GameClient.__init__(self)
        #QtCore.QThread.__init__(self,parent)
        
    def run(self):          #send executed when start() method called
        #for i in range(100):
        #sleep(0.15)    # wait a little before emitting next signal
            
        try:
            while True:
                msg = GameClient.receive_message(self)
                if len(msg): 
                    #self.handle_message(msg)
                    self.message_signal.emit(msg)
                else: break
        except Exception as e:
            print('ERROR:' + str(e) + '\n')
            self.log('ERROR:' + str(e) + '\n')                                             