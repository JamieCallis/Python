if __name__ == '__main__':
    number_list = [1,2,3,4,5] #list of numbers
    char_list = ['1', '2', '3', '4', '5'] # ;ost pf ascii characters

    for number in number_list:
        # comma in the print command indicates everything should be
        # on the same line.
        print number,
    # print command without parameters tell the interpreter to move to next line
    print
    index = 0
    while index < len(char_list): # len function return lenght of a list
        print char_list[index], # we can use traditional array syntax to access list elements
        index += 1 # rquigalent to index = index + 1
