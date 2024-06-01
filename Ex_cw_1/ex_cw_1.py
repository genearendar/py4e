def digit_to_string(digit):
        '''Turn a single digit to an English sting'''
        nums_to_str = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 
                  'four': 4, 'five': 5, 'six':6,
                  'seven': 7, 'eight': 8, 'nine': 9}
        for(key,value) in nums_to_str.items():
            if value == digit:
                return key        
    
def number_to_string (num):
    '''Turn the whole number to a sting of English words'''
    word_string = ''
    for letter in str(num):
        word_string += digit_to_string(int(letter))
    return word_string
    
def calc_path(num):
    '''Create a list of stringified numbers with first element
    being based on the argument's, and each next item - on
    previous item's length. Will run until it reaches equilibrium 
    where last items length = its word in english. 
    Eg. length of 'four' is 4 characters'''
    #get the initial value from input
    init_str = number_to_string (num)
    current_num = num
    path = [init_str]
    # Repeat until equilibrium
    while True:
        ch_num = len(path[len(path) - 1])
        current_st = number_to_string(ch_num)
        #stop when equilibrium
        if current_st == path[len(path) - 1]:
             break
        #add a new item
        path.append(current_st)
        print(path)
    return(path)


num = input('Type a number: ')
calc_path(num)
