from State import *
from sys import argv
from time import sleep
import socket

class Transition:
    def idle(self):
        print "Error! Cannot Transition to idle!"
        return False
    
    def connect(self):
        print "Error! Cannot Transition to connect!"
        return False
    
    def active(self):
        print "Error! Cannot Transition to active"
        return False
    
    def open_sent(self):
        print "Error! Cannot Transition to open sent!"
        return False
    
    def open_confirm(self):
        print "Error! Cannot Transition to open confirm!"
        return False
    
    def established(self):
        print "Error! Cannot Transition to established!"
        return False

class Idle(State, Transition):
    '''
        This is the first stage of the BGP FSM. It either tries
        to initiate a TCP connection to the BGP pper (client mode),
        or listens for a new conenct from a peer (server mode).
    '''
    def __init__(self, Context):
        State.__init__(self, Context)

    def idle(self):
        # only called when operating as a server - this is handled by main
        # initiate listening process
        # and transition to connect state when connection made
        self.CurrentContext.listen()
        print "Currently in Idle state, transition to connect state"
        self.CurrentContext.setState("CONNECT")
        return True

    def connect(self):
        # only called when operating as a client
        # initiate connection process
        # and transition to connect state when connection made
        self.CurrentContext.make_connection()
        print "Currently in Idle state, transition to connect state"
        self.CurrentContext.setState("CONNECT")
        return True
    
    def trigger(self):
        # close open socket and reset object
        # return true if succeed. False otherwise
        try: # server
            if(self.CurrentContext.connection != None):
                print "closing down the connection to client from server"
                self.CurrentContext.connection.close()
                self.CurrentContext.s.close()
                # resetting the object
                self.CurrentContext.connect = None
                self.CurrentContext.s = None
            elif(self.CurrentContext.s != None and self.CurrentContext.connection == None):
                print "closing down the socket for the client"
                self.CurrentContext.s.close()
                # resetting the object
                self.CurrentContext.s = None
                
        except:  # client
            print "Error"
        return True


class Connect(State, Transition):
    '''
        The conect state's role is to send out open essage,
        which are used to initiate BGP peer connections. It also
        provides the ability to retry connection attempts that fail
        - i.e. it periodically retry a TCP connection if inital attempts
        fail and times out. This latter functionalit hasn't been implemented
        in this model for the sake of simplicity
    '''
    def __init__(self, Context):
        State.__init__(self, Context)
    
    def idle(self):
        print "currently in connect state, transition to IDLE state"
        self.CurrentContext.setState("IDLE")
        return True
    def connect(self):
        print "Currently in connect state staying in connect state"
        self.CurrentContext.setState("CONNECT")
        return True
    def active(self):
        print "Currently in connect state, transition to active state"
        self.CurrentContext.setState("ACTIVE")
        return True
    def open_sent(self):
        try: 
            if(self.CurrentContext.connection == None and self.CurrentContext.s != None):
                self.CurrentContext.s.send("OPEN")
                print "Sending the open message."
                print "Currently in connect state, transition to open sent state" 
                self.CurrentContext.setState("OPENSENT")   
            else:
                print "server is transition to openSent"
                self.CurrentContext.setState("OPENSENT")
        except: 
            print "error"
        return True

    def trigger(self):
        # display address of the connecting system
        try: 
            if(self.CurrentContext.connection != None):
                print "Connection from: " + str(self.CurrentContext.addr)
            self.open_sent()
        except: 
            print "error"

        return True

class Active(State, Transition):
    '''
    The active state implements the "heartbeat" functionality
    - i.e. it periodically checks to see if the TCP connection 
    is still alive by reconnecting. This functionality
    hasn't been implemented  in this model for the sake of simplicity
    '''
    def __init__(self, Context):
        State.__init__(self, Context)
    
    def idle(self):
        print "Transitioning to idle!"
        self.CurrentContext.setState("IDLE")
        return True
    
    def connect(self):
        print "Transitioning to connect!"
        self.CurrentContext.setState("CONNECT")
        return True
    
    def active(self):
        print "Transitioning to active!"
        self.CurrentContext.setState("ACTIVE")
        return True
    
    def open_sent(self):
        print "Transitioning to open sent!"
        self.CurrentContext.setState("OPENSENT")
        return True

class OpenSent(State, Transition):
    '''
        The open sent state role is to receieve open message
        from BGP peers. It also has the responsibility to verify
        these message - ie. it checks to see if the parameters of 
        the BGP connection are valid. This latter functionality
        hasn't been implemeneted in this model for the sake of simplicyt
    '''
    def __init__(self, Context):
        State.__init__(self, Context)
    
    def idle(self):
        print "Currently in opensent, transition to IDLE state"
        self.CurrentContext.setState("IDLE")
        return True
    def active(self):
        print "Currently in opensent, transition to active state"
        self.CurrentContext.setState("ACTIVE")
        return True
    def open_confirm(self):
        # when open command received, transition to open confirm state
        try:
            if(self.CurrentContext.connection != None):
                command = self.CurrentContext.connection.recv(1024)
                print "The command is: ", command
                if command == "OPEN":
                    print "Currently in open Sent, transition to open Confirm"
                    print "Sending keepalive message to client"
                    self.CurrentContext.connection.send("KEEPALIVE")
                    self.CurrentContext.setState("OPENCONFIRM")
                    return True
            else:
                print "Currently in open Sent, transition to open Confirm"
                self.CurrentContext.setState("OPENCONFIRM")
        except:
            pass  
            return True
        return True

    def trigger(self):
        # display address of system open command was sent to and
        try: # client
            if(not self.CurrentContext.connection):
                print "Adress open message being sent too: ", self.CurrentContext.host
        except: #server
            pass
        # trigger open_confirm method
        self.open_confirm()
        return True

class OpenConfirm(State, Transition):
    '''
    In the BGP protocol, the open confirm state listens
    out for Keepalive or Notification message. Upon receipt of
    a neighbor's keepalive, the state is moved to established.
    If a notification message is received, and the state is moved
    to Idle. This last feature hasn't been implemented in this model 
    for the sake of simplicity.
    '''
    def __init__(self, Context):
        State.__init__(self, Context)
    
    def idle(self):
        print "Currently in open confirm, transition to IDLE state"
        self.CurrentContext.setState("IDLE")
        return True
    def open_confirm(self):
        print "Currently in open confirm, transition to OPENCONFIRM state"
        # state stays the same as OPENCONFIRM
        self.CurrentContext.setState("OPENCONFIRM")
        return True
    def established(self):
       
        # send and receive keepalive messages
        try: # client
            if(self.CurrentContext.connection == None):
                command = self.CurrentContext.s.recv(1024)
                print command
                if(command == "KEEPALIVE"):
                    print "Currently in open confirm, transition to ESTABLISHED state"
                    self.CurrentContext.setState("ESTABLISHED")
            else:
                print "Transition from open confirm, to ESTABLISHED state"
                self.CurrentContext.setState("ESTABLISHED")
        except: # server
            pass
            
        return True
    def trigger(self):
        # trigger established method
        self.established()
        return True

class Established(State, Transition):
    '''
        The established state handles the excahnge of route information.
        This functionality hasn't been implemented in this model for the
        sake of simplicity. The only role the established state has in 
        this model is to terminate the demo via it's trigger method.
    '''
    def __init__(self, Context):
        State.__init__(self, Context)
        
    def idle(self):
        print "Currently in Established, transition to IDLE state"
        self.CurrentContext.setState("IDLE")
        return True
    def established(self):
        print "Currently in Established, staying in Established"
        # state stays the same
        return True
    def trigger(self):
        # terminate demo by transitioning to idle
        self.idle()
        return True

class BGPPeer(StateContext, Transition):
    connection = None
    addr = None
    s = None
    # True = server, False = client
    def __init__(self):
        # add the available states
        self.availableStates["IDLE"] = Idle(self)
        self.availableStates["CONNECT"] = Connect(self)
        self.availableStates["ACTIVE"] = Active(self)
        self.availableStates["OPENSENT"] = OpenSent(self)
        self.availableStates["OPENCONFIRM"] = OpenConfirm(self)
        self.availableStates["ESTABLISHED"] = Established(self)
        self.setState("IDLE")
        self.host = "127.0.0.1"
        self.port = 5000
        
    def idle(self):
        return self.CurrentState.idle()
    
    def connect(self):
        return self.CurrentState.connect()
    
    def active(self):
        return self.CurrentState.active()
    
    def open_sent(self):
        return self.CurrentState.open_sent()
    
    def open_confirm(self):
        return self.CurrentState.open_confirm()
    
    def established(self):
        return self.CurrentState.established()
    
    def listen(self):
        ''' this method initiates a listen socket '''
        # server
        self.s = socket.socket()
        self.s.bind((self.host, self.port))
        self.s.listen(1)
        print "waiting for a connection"
        # connection acceptance
        self.connection, self.addr = self.s.accept() 

    def make_connection(self):
        # client
        ''' this method initiates an outbound connection '''
        print "making a connection"
        self.s = socket.socket()
        self.s.connect((self.host, self.port))
        
if __name__ == '__main__':
    if len(argv) < 2:
        print "Error: too few arguments"
        exit()
    ActivePeer = BGPPeer()
    if argv[1] == "server":
        ActivePeer.idle()
    else:
        ActivePeer.connect()




