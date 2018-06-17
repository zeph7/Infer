#source code


import random, time, sys, os

#for printing delayed string
def print1(__list__):
    for i in __list__:
        print(i, end = '')
        time.sleep(0.04)
        sys.stdout.flush()
    print()


#for printing spaced string
def print2(__list__):
    temp = ' '.join(__list__)
    print(temp.center(60))


#for printing unspaced string
def print3(__list__):
    temp = ''.join(__list__)
    print(temp.center(60))

 
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
        f.close()
    movie = content.split('\n')
    return movie[random.randint(0, len(movie)-1)].lower()


#for getting leadership board
def score_board(name, net_score):
    f = open("leadership.txt", "r+") #file read/write
    content = f.read()
    f = open("leadership.txt", "w").close #erasing file
    f = open("leadership.txt", "r+") #recreating file
    c = content.split('\n')
    l = len(c)
    for i in range(l+1):
        if i == l or c[i] == '':
            y = name+' '+str(net_score)
            c.insert(i, y)
            break
        x = c[i].split(' ')
        if net_score > int(x[1]):
            y = name+' '+str(net_score)
            c.insert(i, y)
            break
    content = '\n'.join(c)
    f.write(content)
    f.close()


#for displaying leadership board
def display_board():
    f = open("leadership.txt", "r")
    if f.mode == 'r': content = f.read()
    c = content.split('\n')
    print('Leadership Board'.center(60))
    print('_'*60, end = '\n\n')
    print('Rank'.center(20)+'Player Name'.center(20)+'Score'.center(20))
    print('_'*60, end = '\n\n')
    for i in range(min(10, len(c))):
        x = c[i].split(' ')
        print(str(i+1).center(20)+str(x[0]).center(20)+str(x[1]).center(20))
    print('_'*60, end = '\n\n')


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
round_test = True
print1('Initializing...')
time.sleep(2)
print('\n\n\n')

movie_company = 'HOLLYWOOD'
movie_list = ['a-c', 'd-f', 'g-i', 'j-l', 'm-o', 'p-s', 't-v', 'w-z']

flag = False
flag2 = False
flag3 = False

name = input('PLAYER NAME :  ')
temp_score = 0
net_score = 0
round_ = 1
display_board()
print('Infer the letters of the upcoming movie names')
print('type anytime : new -> new game | quit -> quit game')
input('\nPRESS ENTER TO START THE SERIES OF 5 ROUNDS ->')


while(test):

    if flag == True:
        time.sleep(1)
        os.system('cls')
        print1('Initializing new game...')
        time.sleep(2)
        print('\n\n\n')
        flag = False
            
        name = input('PLAYER NAME :  ')
        temp_score = 0
        net_score = 0
        round_ = 1
        display_board()
        input('\nPRESS ENTER TO START THE SERIES OF 5 ROUNDS ->')


    while(round_test):

        time.sleep(1)
        os.system('cls')
        x = 'Round: '+str(round_)
        
        temp_score = 0
        movie_column = random.choice(movie_list)
        movie_name = select_movie(movie_column)
        temp_name = initial_name(movie_name)
        temp = []
        j = 0
        flag_ = False
        flag = False

        while(len(temp) < 9):

            print('\n\n'+x.center(60)+'\n\n')
            print()
            flag2 = True
            print('\n\n')
            print2(''.join(temp) + movie_company[j:])
            print()
            print2(temp_name)
            letter = input()

            
            if letter == 'quit' or letter == 'exit': sys.exit()
            elif letter == 'new':
                flag = True
                break
            elif allowed(temp_name, movie_name, letter):
                p = [pos for pos, char in enumerate(movie_name) if char == letter]
                for i in p: temp_name[i] = letter  
            else:
                temp.append('-')
                j += 1

            if result(temp_name, movie_name):
                flag_ = True
                break
            
            if len(temp) != 9: os.system('cls')


        if flag: break
        elif flag_:
            print1('\n\nNice Work!! You WON The Round...\n\n')
            print()
            print1('Movie Name: ' + ''.join(movie_name)+'\n\n')
        else:
            print1('\n\nYou LOSE The Round!!')
            print()
            print1('Movie Name: ' + ''.join(movie_name)+'\n\n')
            
        temp_score = 150*(9-j)
        net_score += temp_score
        print()
        print1('\n'+str(name)+', your round score : '+str(temp_score)+'\n\n')
        
        round_ += 1
        
        if round_ > 5:
            time.sleep(1)
            os.system('cls')
            print1('\n'+str(name)+', your net score : '+str(net_score)+'\n\n')
            score_board(name, net_score)
            print('\n\n')
            display_board()
            print('\n\n')
            flag = False
            break
        input('PRESS ENTER -> NEXT ROUND')


    if flag: continue
    elif play_again():
        flag = True
        continue
    else: sys.exit()



