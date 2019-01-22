class State:
    CurrentContext = None
    def __init__(self, Context):
        self.CurrentContext = Context
    def trigger(self):
        return True

class StateContext:
    state = None
    CurrentState = None
    availableStates = {}

    def setState(self, newstate):
        try:
            self.CurrentState = self.availableStates[newstate]
            self.state = newstate
            self.CurrentState.trigger()
            return True
        except KeyError:
            return False
    
    def getStateIndex(self):
        return self.state

class Transition:
    def up(self, newSate):
        print "Lift can not go any higher"
        return False

    def down(self, newSate):
        print "Lift can not go any lower"
        return False
    
    def open(self):
        print "Doors opening ... doors are open"
        return False

    def close(self):
        print "Doors closing ... doors are closed"
        return False

class BottomFloor(State, Transition):  
    def __init__(self, Context):
        State.__init__(self, Context)
    # new state will be a string passed in.
    def up(self, newState):
        # tranisition to middle floor
        if (not self.CurrentContext.openDoorCheck and newState == "MIDDLE"): 
            print "Going to the middle floor"
            self.CurrentContext.setState(newState)
        elif (not self.CurrentContext.openDoorCheck):
            print "Going to somewhere in the middle floors."
        else:
            print "Close the doors first."
        return True
        
    def open(self):
        self.CurrentContext.openDoorCheck = True
        print "The doors are open"
        return True
    
    def close(self):
        self.CurrentContext.openDoorCheck = False
        print "The doors are closed"
        return True

class MiddleFloor(State, Transition):
    def __init__(self, Context):
        State.__init__(self, Context)
    
    def up(self, newState):
        if (not self.CurrentContext.openDoorCheck and newState == "TOP"): 
            print "going to the top floor"
            self.CurrentContext.setState(newState)
        elif (not self.CurrentContext.openDoorCheck):
            print "Going to somewhere in the middle floors."
        else:
            print "Close the doors first."
        return True
        
    def down(self, newState):
        if (not self.CurrentContext.openDoorCheck and newState == "BOTTOM"):
            print "going to the bottom floor"
            self.CurrentContext.setState("BOTTOM")
        elif (not self.CurrentContext.openDoorCheck):
            print "Going to somewhere in the middle floors."
        else:
            print "Close the doors first."
        return True
    
    def open(self):
        self.CurrentContext.openDoorCheck = True
        print "The doors are open"
        return True
    
    def close(self):
        self.CurrentContext.openDoorCheck = False
        print "The doors are closed"
        return True
        
class TopFloor(State, Transition):
    def __init__(self, Context):
        State.__init__(self, Context)
        
    def down(self, newState):
        if (not self.CurrentContext.openDoorCheck and newState == "MIDDLE"):
            print "going to the middle floor"
            self.CurrentContext.setState("MIDDLE")
        elif (not self.CurrentContext.openDoorCheck):
            print "Going to somewhere in the middle floors."
        else:
            print "Close the doors first."
        return True

    def open(self):
        self.CurrentContext.openDoorCheck = True
        print "The doors are open"
        return True
    
    def close(self):
        # self.open = False
        self.CurrentContext.openDoorCheck = False
        print "The doors are closed"
        return True
    

class Lift(StateContext, Transition):
    def __init__(self):
        self.openDoorCheck = False
        self.availableStates["BOTTOM"] = BottomFloor(self)
        self.availableStates["MIDDLE"] = MiddleFloor(self)
        self.availableStates["TOP"] = TopFloor(self)
        self.setState("BOTTOM")
    
    def up(self, newState):
        self.CurrentState.up(newState)
    
    def down(self, newState):
        self.CurrentState.down(newState)
    
    def open(self):
        self.CurrentState.open()
    
    def close(self):
        self.CurrentState.close()

if __name__ == "__main__":
    MyLift = Lift()
    MyLift.up("MIDDLE")
    MyLift.open()
    MyLift.up("MIDDLE")
    MyLift.close()
    MyLift.up("MIDDLE")
    MyLift.up("TOP")
    MyLift.down("MIDDLE")
    MyLift.down("BOTTOM")
