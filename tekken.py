import xboxkeymap as xbox
import logger

app_logger = logger.getLogger(printToScreen=True)

class Fighter:
    def __init__(self, name):
        self.Name = name

    def _getLogCtx(self):
        return {"Name": self.Name}

    def leftPunch(self):
        xbox.pressX()
        app_logger.info( self._getLogCtx())

    def rightPunch(self):
        xbox.pressY()
        app_logger.info( self._getLogCtx())

    def leftKick(self):
        xbox.pressA()
        app_logger.info( self._getLogCtx())
    
    def rightKick(self):
        xbox.pressB()
        app_logger.info( self._getLogCtx())

    def jump(self):
        xbox.pressLJoyUp()
        app_logger.info( self._getLogCtx())
    
    def crouch(self):
        xbox.pressLJoyDown()
        app_logger.info( self._getLogCtx())

    def moveFront(self):
        xbox.pressLJoyRight()
        app_logger.info( self._getLogCtx())

    def moveBack(self):
        xbox.pressLJoyLeft()
        app_logger.info( self._getLogCtx())



def main():
    fighter = Fighter("Law")
    fighter.leftPunch()
    fighter.rightPunch()
    fighter.leftKick()
    fighter.rightKick()

    fighter.jump()
    fighter.crouch()
    fighter.moveFront()
    fighter.moveBack()

if __name__ == '__main__':
    main()  
        