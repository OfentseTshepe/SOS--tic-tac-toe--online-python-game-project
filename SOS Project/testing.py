from PyQt4 import QtGui,QtCore
import sys

        
    

class Game(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        
        self.setWindowTitle("Game") 
        self.setWindowState(QtCore.Qt.WindowMaximized)# Opens the game in full screen for better gaming experience
        self.setMinimumSize(1000,800)

        
        
        self.palette	= QtGui.QPalette(self) # Background image 
        self.palette.setBrush(QtGui.QPalette.Background,
                              QtGui.QBrush(
                              QtGui.QPixmap("back.jpg")))
        
        self.setPalette(self.palette)
       
        self.pixmap = QtGui.QPixmap("TribalBlue.png") # picture is uploaded
        self.pixmap = self.pixmap.scaled(100, 300, QtCore.Qt.KeepAspectRatio)
        self.mickey=QtGui.QLabel(self)
        self.mickey.setPixmap(self.pixmap)
        
        self.mickey.move(500,15)
        
        self.red=QtGui.QPixmap("TribalRed.png")
        self.red = self.red.scaled(100, 400, QtCore.Qt.KeepAspectRatio)
        self.reddrag=QtGui.QLabel(self)
        self.reddrag.setPixmap(self.red)
        self.reddrag.move(800,15)
        self.reddrag.updateGeometry()
        
        self.circle=QtGui.QPixmap("circle.png")
        self.circle = self.circle.scaled(120, 120, QtCore.Qt.KeepAspectRatio) #scaling down the image to be uploaded
        self.ci=QtGui.QLabel(self)
        self.ci.setPixmap(self.circle)
        self.ci.move(639,50)
        
        self.sever=QtGui.QLineEdit("SEVER",self)# edit box for the user to enter  ther sever
        self.sever.move(600,20)
        
        self.sever.setMinimumSize(200,20)
        
        self.sever.returnPressed.connect(self.men) # sever will connect when the user presses enter
        
        self.bo=self.bo1=self
        
       
        
       
        
       
        
        self.bo=QtGui.QLabel(self) 
        numb=0
 
        xp=110
        yp=160
        for x in range(0,16): # creating the displayboard 
            if x%2==0:
                n="BoxRed"
            else:
                n="BoxBlue"
                
            if x%4==0:
                xp=250
                yp+=100
                
            else:
                xp+=110
                
                
            self.box=QtGui.QPixmap(n)
            self.box=self.box.scaled(90, 90, QtCore.Qt.KeepAspectRatio)
            self.bo=QtGui.QLabel("{}".format(numb),self) 
            self.bo.mousePressEvent= self.board #connecting signal when board is clicked 
            self.text=self.bo.text()
            self.bo.setPixmap(self.box)   
            self.bo.move(xp,yp)
            self.box=QtGui.QPixmap("BoxRed")
            numb+=1
         
        
        

        
        self.msg=QtGui.QPixmap("BoxRed")
        self.msg = self.msg.scaled(430, 430, QtCore.Qt.KeepAspectRatio)
        self.m=QtGui.QLabel(self)
        self.m.setPixmap(self.msg)
        self.m.move(850,250)
      
      
      
        self.bc=QtGui.QPixmap("bluec")
        self.bc = self.bc.scaled(150,150,  QtCore.Qt.KeepAspectRatio)
        self.bluec=QtGui.QLabel(self)
        self.bluec.setPixmap(self.bc)
        
        
        
        self.redc=QtGui.QPixmap("redc")#UPLOADING image
        self.redc= self.redc.scaled(150, 150, QtCore.Qt.KeepAspectRatio)
        self.redcor=QtGui.QLabel(self)
        self.redcor.setPixmap(self.redc)
        self.redcor.move(1217,0)    
        
        
        
        self.rcb=QtGui.QPixmap("recblue")
        self.rcb= self.rcb.scaled(230, 100, QtCore.Qt.KeepAspectRatio)
        self.rct=QtGui.QLabel(self)
        self.rct.setPixmap(self.rcb)
        self.rct.move(100,15)  
        
        
        self.recb=QtGui.QPixmap("recred")
        self.recb= self.recb.scaled(250, 180, QtCore.Qt.KeepAspectRatio)
        self.rect=QtGui.QLabel(self)
        self.rect.setPixmap(self.recb)
        self.rect.move(1015,15)      
        
        
        
        self.shut=QtGui.QPixmap("shut")#shutdown image/button
        self.shut= self.shut.scaled(100, 100, QtCore.Qt.KeepAspectRatio)
        self.shutd=QtGui.QLabel(self)
        self.shutd.setPixmap(self.shut)
        self.shutd.move(60,600)  
        
        
        self.shut=QtGui.QPixmap("replay")#shutdown image/button
        self.shut= self.shut.scaled(120, 120, QtCore.Qt.KeepAspectRatio)
        self.shutd=QtGui.QLabel(self)
        self.shutd.setPixmap(self.shut)
        self.shutd.move(60,400)            
    
               
    def board(self,event): #testing the board's functionality
        print("Boared clicked")
        x = event.pos().x()
        y = event.pos().y()  
        print(x,y)
        
    def men(self):
        print("Connecting")
        
         
      #pixmap = pixmap.scaled(500, 500, QtCore.Qt.KeepAspectRatio) 

        





app=QtGui.QApplication(sys.argv)
game=Game()
game.show()
sys.exit(app.exec_())

