#source code


import random, time, sys

#for printing characters
def print_(__list__):
    for i in __list__:
        print(i, end = '')
        time.sleep(0.04)
        sys.stdout.flush()
    print()


#for getting initial movie name
def initial_name(original_movie):
    __list__ = []
    for i in original_movie:
        if i == ' ': __list__.append(' ')
        else: __list__.append('_')
    return rand_fill(__list__, original_movie)


#for selecting and filling some random letters
def rand_fill(__list__, original_movie):
    _len_ = len(original_movie)
    temp = [random.randint(0, _len_-1) for x in range(_len_//4)]
    for i in temp: __list__[i] = original_movie[i]
    return __list__

    
#for selecting a movie from external files
def select_movie(movie_column):
    movie_col = 'mv_ls_' + movie_column + '.txt'
    f = open(movie_col, "r")
    if f.mode == 'r':
        content = f.read()
    movie = content.split('\n')
    return movie[random.randint(0, len(movie)-1)].lower()


#for checking letter is allowed in movie name or not
def allowed(__list__, original_movie, letter):
    p = [pos for pos, char in enumerate(original_movie) if char == letter]
    for i in p:
        if __list__[i] == '_': return True
    return False


#for checking win or lose
def result(__list__, original_movie):
    for i in range(len(__list__)):
        if __list__[i] != original_movie[i]:
            return False
    return True


#play again or not
def play_again():
    print('Wanna play again, Y or N?')
    z = input().lower()
    if z == 'y': return True
    return False




#main code


test = True
print_('Initializing...')
time.sleep(2)
print('\n\n\n')
movie_company = 'hollywood'
movie_list = ['a-c', 'd-f', 'g-i', 'j-l', 'm-o', 'p-s', 't-v', 'w-z']
flag = False
flag_ = False
flag2 = False

while(test):

    if flag == True:
        print('\n\n\n\n')
        print_('Initializing new game...')
        time.sleep(2)
        print('\n\n\n')
        flag = False

    print_(movie_company)
    movie_column = random.choice(movie_list)
    movie_name = select_movie(movie_column)
    temp_name = initial_name(movie_name)
    print_(temp_name)
    temp = []
    j = 0

    while(len(temp) < 9):

        if flag2: print_('Infer next letter:')
        else: print_('Infer a letter in the movie name:')
        letter = input()
        print()
        flag2 = True

        if letter == 'quit' or letter == 'exit': sys.exit()
        elif letter == 'new':
            flag = True
            break
        
        elif allowed(temp_name, movie_name, letter):
            print('\n\n')
            print('Great!!')
            print_(''.join(temp) + movie_company[j:])
            p = [pos for pos, char in enumerate(movie_name) if char == letter]
            for i in p: temp_name[i] = letter
            print_(temp_name)
            
        else:
            temp.append('-')
            j += 1
            print('\n\n')
            print('Ooops!!')
            print_(''.join(temp) + movie_company[j:])
            print_(temp_name)

        if result(temp_name, movie_name):
            flag_ = True
            break
        

    if flag == True: continue
    elif flag_: print_('Nice Work!! you Won...')
    else:
        print_('You Lose!! better luck next time')
        print_('Movie Name: ' + ''.join(movie_name))
                
        
    
    flag = True
    if play_again(): continue
    else: sys.exit()


    
