#!/usr/bin/env python
# coding: utf-8

# In[1]:

import getch
import random
import os


# In[2]:


def new_2_number(matrix,n):
    while True:
        move = random.randint(1,n**2)
        move = move - 1
        row = move // n
        column = move % n
    
        if matrix[row][column] == 0:
            matrix[row][column] = 2
            break


# In[3]:


def display_grid(matrix):
    bdigit = max_dig(matrix)
    for i in matrix:
        print('|',end = ' ') 
        for j in i:
            number = j
            sdigit = 0
            
            if number == 0:
                sdigit = 1
            while number:
                sdigit = sdigit + 1
                number = number//10
                
            print(j, end = '')
            for count in range(bdigit - sdigit + 1):    
                print(' ', end = '')
                
            print('|',end = ' ')
        print()
    print()


# In[4]:


def max_dig(matrix):
    bignum = 0
    for rows in matrix:
        for cols in rows:
            if bignum < cols:
                bignum = cols
    temp = 0
    if bignum == 0:
        temp = 1
    while bignum:
        temp = temp + 1
        bignum = bignum//10
    return temp


# In[5]:


def rearrange(matrix, Player_Move):
    if Player_Move == 'a' or Player_Move == 'd':
        
        if Player_Move == 'd':
            for rnum, row in enumerate(matrix):
                matrix[rnum] = list(reversed(row))
        matrix  = add_num(matrix)
                
        for rnum, row in enumerate(matrix):
            temp = 0
            for cnum, col in enumerate(row):
                if col == 0:
                    temp = temp + 1
                elif col != 0 and temp != 0:
                    matrix[rnum][cnum-temp] = matrix[rnum][cnum]
                    matrix[rnum][cnum] = 0         
        if Player_Move == 'd':
            for rnum, row in enumerate(matrix):
                matrix[rnum] = list(reversed(row))
        return matrix
                    
    elif Player_Move == 'w' or Player_Move == 's':
        
        transform = []
        for i in range(len(matrix)):
            transform = transform + [[]]
            
        for column in range(len(matrix)):
            
            for row in matrix:
                transform[column] = transform[column] + [row[column]]
        
        if Player_Move == 'w':
            transform = rearrange(transform, 'a')
        else:
            transform = rearrange(transform, 'd')
        for column in range(len(matrix)):
            for rnum, row in enumerate(matrix):
                row[column] = transform[column][rnum]
                
    else:
        print('Play using w,a,s,d keys')


# In[6]:


def add_num(matrix):
        for rnum, row in enumerate(matrix):
            store = False
            for cnum, col in enumerate(row):
                if col != 0 and not store:
                    rtemp = rnum
                    ctemp = cnum
                    store = True
                elif col != 0 and matrix[rtemp][ctemp] == col and store:
                    matrix[rtemp][ctemp] = col*2
                    matrix[rnum][cnum] = 0
                    store = False
                elif col != 0 and matrix[rtemp][ctemp] != col and store:
                    rtemp = rnum
                    ctemp = cnum
        return(matrix)


# In[7]:


def lose(matrix , n):
    moves = ('w','a','s','d')
    
    for move in moves:
        test_matrix = copy(matrix , n)
        rearrange(test_matrix , move)
        if test_matrix != matrix:
            return False
    return True


# In[8]:


def copy(matrix , n):
    copy_matrix = []
    for i in range(n):
        copy_matrix = copy_matrix + [[]]
    for i in range(n):
        for j in range(n):
            copy_matrix[i] = copy_matrix[i] + [0]
            
    for rnum,rows in enumerate(matrix):
        for cnum,cols in enumerate(rows):
            copy_matrix[rnum][cnum] = cols
    return(copy_matrix)


# In[9]:


def grid_detail():
    n = input('Enter size of grid : ')
    if n == '':
        n = 5
        return n
    else:
        try:
            n = int(n)
            if n <= 0:
                print('\nGrid size should be greater than 0')
                return 0
            else:
                return n
        except:
            print('\nInput should be a natural number')
            return 0


# In[10]:


def win_score():
    score = input('Enter winning score as ""nth"" power of two : ')
    if score == '':
        score = 11
        return score
    else:
        try:
            score = int(score)
            if score <= 0:
                print('\nGrid size should be greater than 0')
                return 0
            else:
                return score
        except:
            print('\nInput should be a natural number')
            return 0


# In[11]:


def win(matrix , score):
    for rows in matrix:
        for cols in rows:
            if cols == score:
                return True
    return False


# In[12]:


def main():
    n = grid_detail()
    if not n:
        return True
    score = win_score()
    if not score:
        return True
    else:
        score = 2**score
    print('Grid size :',n,'     ','Winning score :',score)
    matrix = []
    for i in range(n):
        matrix = matrix + [[]]
    for i in range(n):
        for j in range(n):
            matrix[i] = matrix[i] + [0]
            
    os.system('cls')
    new_2_number(matrix , n)
    display_grid(matrix)
    
    while True:
        check = win(matrix , score)
        if check:
            print('You won')
            break
        check = lose(matrix , n)
        if check:
            print('You lost')
            break
    
        copy_matrix = copy(matrix , n)
        inp = getch.getch('Enter your move or enter p to end the game: ')
        if inp == 'p':
            print('Game ended')
            break
        rearrange(matrix , inp)
        os.system('cls')
        if copy_matrix == matrix:
            display_grid(matrix)
            print('Try another move')
            continue
    
        new_2_number(matrix , n)
        display_grid(matrix)
        
    return False


# In[13]:


final = main()
if final:
    print('\nExecute the code again to play 2048 game')


# In[ ]:




