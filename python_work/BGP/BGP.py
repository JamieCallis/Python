from State import *
from socket import socketfrom 
from sysu import agrv
from time import sleep

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
    def __init__(self, Context)
        State.__init__(self, Context)

    def idle(self):
        # only called when operating as a server
        # initiate listening process
        # and transition to connect state when connection made

    def connect(self):
        # only called when operating as a client
        # initiate connection process
        # and transition to connect state when connection made
    
    def trigger(self):
        # close open socket and reset object
        # return true if succeed. False otherwise
    
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
        self.CurrentContext.setState("IDEL")
        return True
    def connect(self):
        self.CurrentContext.setState("CONNECT")
        return True
    def active(self):
        self.CurrentContext.setState("ACTIVE")
        return True
    def open_sent(self):
        # send open command via existing connection
        # and transition to open sent 
        self.CurrentContext.setState("OPENSENT")
        return True

    def trigger(self):
        # display address of the connecting system
        # and trigger open_sent method

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
        self.CurrentContext.setState("IDLE")
        return True
    def active(self):
        self.CurrentContext.setState("ACTIVE")
        return True
    def open_confirm(self):
        # when open command received, transition to open confirm state
        self.CurrentContext.SETsTATE("OPENCONFIRM")
        return True

    def trigger(self):
        # display address of system open command was sent to and
        # trigger open_confirm method

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
        self.CurrentContext.setState("IDLE")
        return True
    def open_confirm(self):
        # state stays the same as OPENCONFIRM
        return True
    def established(self):
        # send and receive keepalive messages
        self.CurrentContext.setState("ESTABLISHED")
    
    def trigger(self):
        # trigger established method

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
        self.CurrentContext.setState("IDLE")
        return True
    def established(self):
        # state stays the same
        return True
    def trigger(self):
        # terminate demo by transitioning to idle

class BGPPeer(StateContext, Transition):
    def __init__(self):
        # add the available states
        self.availableStates["IDLE"] = Idle(self)
        self.availableStates["CONNECT"] = Connect(self)
        self.availableStates["ACTIVE"] = Active(self)
        self.availableStates["OPENSENT"] = OpenSent(self)
        self.availableStates["OPENCONFIRM"] = OpenConfirm(self)
        self.availableStates["ESTABLISHED"] = Established(self)
        self.setState("IDLE")
        
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
    
    def make_connection(self):
        ''' this method initiates an outbound connection '''

if __name__ == '__main__':
    if len(argv) < 2:
        print "Error: too few arguments"
        exit()
    ActivePeer = BGPPeer()
    if argv[1] == "server":
        ActivePeer.idle()
    else:
        ActivePeer.connect()




