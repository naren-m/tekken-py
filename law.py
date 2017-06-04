# from tekken import Fighter

from dummy_tekken import Fighter

class Law(Fighter):

    def __init__(self):
        Fighter.__init__(self, "Marshal Law")
    
    def _fight(self):
        self.leftPunch()
        self.rightPunch()
        self.leftKick()
        self.rightKick()

        self.jump()
        self.crouch()
        self.moveFront()
        self.moveBack()

    def fight(self):
        while True:
            self._fight()

def main():
    law = Law()
    law.fight()

if __name__ == '__main__':
    main()