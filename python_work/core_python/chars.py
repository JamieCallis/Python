if __name__ == '__main__':
    """
     By default, python chars can be thought of as
     immutable values this means that whenever a char
     variable needs to change, a new value is assigned
     rather changing what is there.
     Consequently, chars will always operate under a
     'by valye' i.e. copies are always made when transfering values
    """
    first_char = 'a'

    second_char = first_char
    """
        ord function returns ascii value of chr.
        chr converts ascii value into a char here,
        only second_value is incremented because it
        'copied' first value.
    """
    second_char = chr(ord(first_char) + 1)

    print "\nChar assignment example:"
    print "second_char =", second_char, "first_char=", first_char

    first_list = ['a']
    second_list = first_list #by default. Python lists are references
    """
        here, both first_list and second_list are incremented.
        Because they both reference the same list
    """
    second_list[0] = chr(ord(second_list[0]) +1)

    print "\nDefault list assignment example"
    print "second_list =", second_list, "first_list", first_list

    first_list[0] = 'a'
    """
        [:] is the python slice operator can be used to make
        sub lists but, crucially, it also makes a copy
    """
    second_list = first_list[:]

    """
    here, only second_list is incremented because it
    merely took a copy of first_list
    """
    second_list[0] = chr(ord(second_list[0]) +1)

    print "\nSliced (copied) list assignment example"
    print "second_list", second_list, "first_list =", first_list, "\n"
