from PyQt4 import QtCore
import time  
from GameClient import *

# defines a thread which emits signals with values 0 to 99
class LoopThread(QtCore.QThread,GameClient):

    message_signal = QtCore.pyqtSignal(str)       # create signal
    
    def __init__(self,parent=None):
        
        super(LoopThread,self).__init__(parent)
        GameClient.__init__(self)
        
        #QtCore.QThread.__init__(self,parent)
        
        
    def connecter(self,name):
        
        while True:
            try:    
                self.connect_to_server(name) #gets the entered text on the text field and connects to the entered adress
                #print(self.server_field.displayText())
                #GameClient.connect_to_server(self,"localhost")
                break
            except Exception as e:
                print('Error connecting to server!\nERROR:' + str(e) + '\n')
                print("Error connecting") #emits an error message if 
                #self.server_field.setText('')
       # self.connect_to_server(name)
                    
    def message_sender(self, move):
        self.send_message(move)   
        
        
    def run(self):          # run executed when start() method called
        #for i in range(100):
            #sleep(0.15)    # wait a little before emitting next signal
        #msg = "your move"
        #self.message_signal.emit(msg)
        while True:
            
            try:
                while True:
                    msg = self.receive_message()
                    #msg= "your move"
                    if len(msg): 
                        #self.handle_message(msg)
                        #time.sleep(0.2) #wait 0.2 secinds before emmiting
                        f=open("Messages.txt",'w')
                        f.write(str(msg)+"\n")
                    
                        self.message_signal.emit(msg)
                    else: break
                    f.close
                    
            except Exception as e:
                print('ERROR:' + str(e) + '\n')
                #self.log('ERROR:' + str(e) + '\n')