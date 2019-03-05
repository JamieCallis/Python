from sys import argv
from time import sleep
import socket

class State:
    state = None # abstract class
    CurrentContext = None
    def __init__(self, Context):
        self.CurrentContext = Context

class StateContext:
    stateIndex = 0
    CurrentState = NoneavailableStates = []
    availableStates = {} 

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

    def synSent(self):
        print "Error can't transition to synSent!"
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

    def finWait_1(self):
        print "Error can't transition to finwait_1!"
        return False
    
    def finWait_2(self):
        print "Error can't transition to finwait_2!"
        return False

    def lastAck(self):
        print "Error can't transition to lastAck!"
        return False

    def timedWait(self):
        print "Error can't transition to timedWait!"
        return False


class Closed(State, Transition):
    def __init__(self, Context):
        State.__init__(self, Context)

    def closed(self):
        pass

    def synSent(self):
        # if active open
        # then send syn request, and transition to synSent.
        pass
    
    def listen(self):
        # listen for a command and transition to the listen state.
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

class SynSent(State, Transition):
    def __init__(self, Context):
        State.__init__(self, Context)

    def closed(self):
        pass

    def established(self):
        pass
    
    def Trigger(self):
        pass

class Established(State, Transition):
    def __init__(self, Context):
        State.__init__(self, Context)
    
    def closeWait(self):
        pass

    def finWait_1(self):
        pass

    def Trigger(self):
        pass

class FinWait_1(State, Transition):
    def __init__(self, Context):
        State.__init__(self, Context)

    def finWait_2(self):
        pass

    def Trigger(self):
        pass

class FinWait_2(State, Transition):
    def __init__(self, Context):
        State.__init__(self, Context)

    def timedWait(self):
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

class TimedWait(State, Transition):
    def __init__(self, Context):
        State.__init__(self, Context)

    def closed(self):
        pass

    def Trigger(self):
        pass

class TCPIPSimulator(StateContext, Transition):
    
    def __init__(self):
        self.host = "127.0.0.1"
        self.port = 5000
        self.availableStates["CLOSED"] = Closed(self)
        self.availableStates["LISTEN"] = Listen(self)
        self.availableStates["SYNRECVD"] = SynRecvd(self)
        self.availableStates["SYNSENT"] = SynSent(self)
        self.availableStates["ESTABLISHED"] = Established(self)
        self.availableStates["FINWAIT-1"] = FinWait_1(self)
        self.availableStates["FINWAIT-2"] = FinWait_2(self)
        self.availableStates["CLOSEDWAIT"] = CloseWait(self)
        self.availableStates["LASTACT"] = LastAck(self)
        self.availableStates["TIMEDWAIT"] = TimedWait(self)
        self.setState("CLOSED")
        self.connection_addr = 0
        self.connection = None
        self.socket = None
        
    
    def closed(self):
        return self.CurrentState.closed()

    def listen(self):
        return self.CurrentState.listen()

    def synRecvd(self):
        return self.CurrentState.synRecvd()

    def synSent(self):
        return self.CurrentState.synSent()
    
    def established(self):
        return self.CurrentState.established()
    
    def finWait_1(self):
        return self.CurrentState.finWait_1()
    
    def finWait_2(self):
        return self.CurrentState.finWait_2()
    
    def closeWait(self):
        return self.CurrentState.closeWait()
    
    def lastAck(self):
        return self.CurrentState.lastAck()

    def timedWait(self):
        return self.CurrentState.timedWait()

    def listen_for_connection(self):
        ''' this method initiates a listen socket '''
        # server
        self.socket = socket.socket()
        try:
            print "waiting for a connection"
            self.socket.bind((self.host, self.port))
            self.socket.listen(1)
            self.connection, self.connection_address = self.socket.accept()
            # connection acceptance
            return True
        except Exception as err: 
            print err
            exit()
       
    def make_connection(self):
        # client
        ''' this method initiates an outbound connection '''
        print "making a connection"
        self.socket = socket.socket()
        try:
            self.socket.connect((self.host, self.port))
            self.connection_address = self.host
            return True
        except Exception as err:
            print err
            exit()
    
    def read_commands(self):
        # The client should be able to read commands from a file
        # called client_commands.txt that will be in the same directory
        pass

if __name__ == "__main__":
    if len(argv) < 2:
        print "Error: too few arguments"
        exit()

    TCPIPSimulator = TCPIPSimulator()
    if argv[1] == "server":
        TCPIPSimulator.listen()
    else:
        pass
