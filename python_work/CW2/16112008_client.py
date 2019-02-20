class State:
    state = None # abstract class
    CurrentContext = None
    def __init__(self, Context):
        self.CurrentContext = Context

class StateContext:
    stateIndex = 0
    CurrentState = NoneavailableStates = []
    availableStates = []

    def setState(self, newstate):
        self.CurrentState = self.availableStates[newstate]
        self.startIndex = newstate
    
    def getStateIndex(self):
        return self.stateIndex

class Transition:
    def closed(self):
        pass

    def synSent(self):
        pass
    
    def established(self):
        pass
    
    def finWait_1(self):
        pass
    
    def finWait_2(self):
        pass
  
    def TimedWait(self):
        pass

class TCPSimulatorClient(StateContext, Transition):
    pass

if __name__ == "__main__":
    pass