#source code


import random, time, sys, os, msvcrt


# main code
def main():
    # main screen 1
    os.system('mode con: cols=100 lines=30')
    os.system('color 2f')
    print('\n'*12)
    print('I N F E R'.center(100))
    time.sleep(2)
    
    # main screen 2
    os.system('cls')
    os.system('color 3f')
    print('\n'*12)
    print('---<  I N F E R   U P C O M I N G   M O V I E   N A M E S  >---'.center(100))
    time.sleep(4)

    # main screen 3
    os.system('cls')
    os.system('color 1f')
    print('\n'*12)
    print(' '*30 + 'P L A Y E R  N A M E : ', end = '')
    name = input()
    time.sleep(1)

    # main screen 4
    score = 0
    for i in range(5):
        score += _round_(i+1)
    os.system('cls')
    os.system('color 3f')
    print('\n'*12)
    print((str(name)+' Your Net Score : '+str(score)).center(100))
    time.sleep(4)
    score_board(name, score)
    display_board()       
    play_again()



# for defining a Round
def _round_(num):
    os.system('color 3f')
    movie_company = 'HOLLYWOOD'
    movie_list = ['a-c', 'd-f', 'g-i', 'j-l', 'm-o', 'p-s', 't-v', 'w-z']
    movie_column = random.choice(movie_list)
    movie_name = select_movie(movie_column)
    temp_name = initial_name(movie_name)
    temp = []
    j = 0
            
    # round screen
    while True:
        screen_top(num)
        print('\n'*6)
        print()
        print2(''.join(temp) + movie_company[j:])
        print()
        print2(temp_name)
        letter = msvcrt.getwch()

        if letter == '-': sys.exit()
        elif letter == '+': main()
        elif allowed(temp_name, movie_name, letter):
            p = [pos for pos, char in enumerate(movie_name) if char == letter]
            for i in p: temp_name[i] = letter  
        else:
            temp.append('-')
            j += 1

        if len(temp) == 9 or result(temp_name, movie_name) == 'win':
            screen_top(num)
            print('\n'*6)
            print()
            print2(''.join(temp) + movie_company[j:])
            print()
            print2(movie_name)
            time.sleep(2)
            score = 150 * (9 - len(temp))
            display_result(result(temp_name, movie_name), score)
            return score



# function to display screen set
def screen_top(num):
    os.system('cls')
    print('_'*100)
    print()
    print(('Round : '+ str(num)).center(100))
    print('_'*100)      


# for printing spaced string
def print2(__list__):
    temp = ' '.join(__list__)
    print(temp.center(100))

 
# for getting initial movie name
def initial_name(original_movie):
    __list__ = []
    for i in original_movie:
        if i == ' ': __list__.append(' ')
        else: __list__.append('_')
    return rand_fill(__list__, original_movie)


# for selecting and filling some random letters
def rand_fill(__list__, original_movie):
    _len_ = len(original_movie)
    temp = [random.randint(0, _len_-1) for x in range(_len_//4)]
    for i in temp: __list__[i] = original_movie[i]
    return __list__


# for selecting a movie from external files
def select_movie(movie_column):
    movie_col = 'mv_ls_' + movie_column + '.txt'
    f = open(movie_col, "r")
    if f.mode == 'r':
        content = f.read()
        f.close()
    movie = content.split('\n')
    return movie[random.randint(0, len(movie)-1)].lower()


# for getting leadership board
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


# for displaying leadership board
def display_board():
    os.system('cls')
    os.system('color 9f')
    f = open("leadership.txt", "r")
    if f.mode == 'r': content = f.read()
    c = content.split('\n')
    print('\n'*2)
    print('---<   L E A D E R S H I P   B O A R D   >---'.center(100), end = '\n\n')
    print('-'*100, end = '\n\n\n')
    print('Rank'.center(33)+'Player Name'.center(33)+'Score'.center(34), end = '\n\n\n')
    print('-'*100, end = '\n\n\n')
    for i in range(min(10, len(c))):
        x = c[i].split(' ')
        print(str(i+1).center(33)+str(x[0]).center(33)+str(x[1]).center(34))
    print('\n'*2)
    print('-'*100)
    input()


# for checking letter is allowed in movie name or not
def allowed(__list__, original_movie, letter):
    p = [pos for pos, char in enumerate(original_movie) if char == letter]
    for i in p:
        if __list__[i] == '_': return True
    return False


# for checking win or lose
def result(__list__, original_movie):
    for i in range(len(__list__)):
        if __list__[i] != original_movie[i]:
            return 'lose'
    return 'win'


# function to show result
def display_result(status, score):
    if status == 'win':
        os.system('cls')
        os.system('color 2f')
        print('\n'*12)
        print(('You Won!! Round Score: '+str(score)).center(100))
        time.sleep(3)
    else:
        os.system('cls')
        os.system('color Cf')
        print('\n'*12)
        print(('You Lose the Round!!').center(100))
        time.sleep(3)


# play again or not
def play_again():
    os.system('cls')
    os.system('color 5f')
    print('\n'*12)
    print('Wanna play again : y|n'.center(100))
    z = msvcrt.getwch()
    if z.lower() == 'y': main()
    else: sys.exit()



if __name__ == '__main__':
    main()

