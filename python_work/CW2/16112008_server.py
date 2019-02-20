import socket

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
    
    def listen(self):
        pass

    def synRecvd(self):
        pass
    
    def established(Self):
        pass
    
    def closeWait(self):
        pass
    
    def lastAck(self):
        pass
    
    def TimedWait(self):
        pass


class TCPSimulatorServer(StateContext, Transition):
    pass

if __name__ == "__main__":
    pass