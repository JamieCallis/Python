class Multiply:
    # the name __init__ is reserved and designates
    # the class constructor
    def __init__(self):
        pass


    """
        The name __del__ is reserved and designates
        the class destructor. We don't need to do anything
        in the constructor / destructor but all python methods
        and functions must contain something,
        so we've included a 'pass' command. Which indicates
        there is nothing to be done all python methods have to
        include the 'self' parameter, which is used to pass the
        pointer to object instance currently in use.
    """
    def __del__(self):
        pass

    """
        All python methods have to include the 'self'
        paramter. Which is used to pass the pointer to
        object instance currently in use.
    """
    def these_numbers(self, number1, number2):
        return number1 * number2




if __name__ == '__main__':
    # The brackets after the class name are important.
    # They tell the interpreter to instantiate an object.
    multiply = Multiply()

    # Python handles all memory management so we don't
    # need to worry about deallocating object resources. ect.
    print multiply.these_numbers(2,2)
