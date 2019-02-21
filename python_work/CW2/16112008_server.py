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
        print "Error can't transition to closed!"
        return False
    
    def listen(self):
        print "Error can't transition to listen!"
        return False

    def synRecvd(self):
        print "Error can't transition to synRecvd!"
        return False
    
    def established(self):
        print "Error can't transition to established!"
        return False
    
    def closeWait(self):
        print "Error can't transition to closeWait!"
        return False
    
    def lastAck(self):
        print "Error can't transition to lastAck!"
        return False
    
    def TimedWait(self):
        print "Error can't transition to TimedWait!"
        return False

class Closed(State, Transition):
    def __init__(self, Context):
        State.__init__(self, Context)
    
    def closed(self):
        pass

    def listen(self):
        pass

    def Trigger(self):
        pass

class Listen(State, Transition):
    def __init__(self, Context):
        State.__init__(self, Context)

    def synRecvd(self):
        pass
       
    def Trigger(self):
        pass

class SynRecvd(State, Transition):
    def __init__(self, Context):
        State.__init__(self, Context)

    def established(self):
        pass

    def Trigger(self):
        pass

class Established(State, Transition):
    def __init__(self, Context):
        State.__init__(self, Context)
    
    def closeWait(self):
        pass

    def Trigger(self):
        pass

class CloseWait(State, Transition):
    def __init__(self, Context):
        State.__init__(self, Context)

    def lastAck(self):
        pass

    def Trigger(self):
        pass

class LastAck(State, Transition):
    def __init__(self, Context):
        State.__init__(self, Context)

    def closed(self):
        pass

    def Trigger(self):
        pass
# is timed wait even needed?
class TimedWait(State, Transition):
    def __init__(self, Context):
        State.__init__(self, Context)
        
    def Trigger(self):
        pass

class TCPSimulatorServer(StateContext, Transition):
    def __init__(self):
        # add the available states
        self.availableStates["CLOSED"] = Closed(self)
        self.availableStates["LISTEN"] = Listen(self)
        self.availableStates["SYNRECVD"] = SynRecvd(self)
        self.availableStates["ESTABLISHED"] = Established(self)
        self.availableStates["CLOSEDWAIT"] = CloseWait(self)
        self.availableStates["LASTACT"] = LastAck(self)
        self.availableStates["TIMEDWAIT"] = TimedWait(self)
        self.setState("CLOSED")
        self.host = "127.0.0.1"
        self.port = 5000
    
    def closed(self):
        return self.CurrentState.closed()
    
    def listen(self):
        return self.CurrentState.listen()

    def synRecvd(self):
        return self.CurrentState.synRecvd()
    
    def established(self):
        return self.CurrentState.established()
    
    def closeWait(self):
        return self.CurrentState.closeWait()
    
    def lastAck(self):
        return self.CurrentState.lastAck()
    
    def TimedWait(self):
        return self.CurrentState.timedWait() 

if __name__ == "__main__":
    pass