#!/usr/bin/env python
# coding: utf-8

# In[ ]:


l = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

name_p1 = input('Player 1 give yor name , you will start first with X ')
name_p2 = input('Player 2 give yor name , you will be second and you have O ')

print(' 1','|','2','|','3')
print('---+---+---')
print(' 4','|','5','|','6')
print('---+---+---')
print(' 7','|','8','|','9')

x = 0
moves = 0

def move_X():
    print ('Player 1 make your move')
    index = int(input())-1
    if l[index]=='X':
        print ('You have already played this move!, Try again')
        move_X()
    elif l[index]=='O':
        print (name_p2,' has already occupied that square , NO cheating')
        move_X()
    else:
        l[index]='X'
        print(l[0],' |',l[1],'|',l[2])
        print('---+---+---')
        print(l[3],' |',l[4],'|',l[5])
        print('---+---+---')
        print(l[6],' |',l[7],'|',l[8])
            
def move_O():
    print('Player 2 make your move')
    index = int(input()) - 1
    if l[index] == 'O':
        print('You have already played this move, Try again')
        move_O()
    elif l[index] == 'X':
        print(name_p1,' has already occupied that square , NO cheating')
        move_O()
    else:
        l[index] = 'O'
        print(l[0],' |',l[1],'|',l[2])
        print('---+---+---')
        print(l[3],' |',l[4],'|',l[5])
        print('---+---+---')
        print(l[6],' |',l[7],'|',l[8])
        
                 
while moves<10:
    move_X()
    if l[0] == l[1] == l[2] == 'X':
        print(name_p1,' wins')
        break
    elif l[0] == l[4] == l[8] == 'X':
        print(name_p1,' wins')
        break
    elif l[0] == l[3] == l[6] == 'X':
        print(name_p1,' wins')
        break
    elif l[6] == l[7] == l[8] == 'X':
        print(name_p1,' wins')
        break
    elif l[8] == l[5] == l[2] == 'X':
        print(name_p1,' wins')
        break
    elif l[3] == l[4] == l[5] == 'X':
        print(name_p1,' wins')
        break
    elif l[1] == l[4] == l[7] == 'X':
        print(name_p1,' wins')
        break
    elif l[2] == l[5] == l[8] =='X':
        print(name_p1,' wins')
        break
    elif l[2] == l[4] == l[6] =='X':
        print(name_p1,' wins')
        break
    elif (' ') in l:
        pass
    elif (' ') not in l:
        print('Draw')
        break
    
    move_O()
    if l[0] == l[1] == l[2] == 'O':
        print(name_p2,' wins')
        break
    elif l[0] == l[4] == l[8] == 'O':
        print(name_p2,' wins')
        break
    elif l[0] == l[3] == l[6] == 'O':
        print(name_p2,' wins')
        break
    elif l[6] == l[7] == l[8] == 'O':
        print(name_p2,' wins')
        break
    elif l[8] == l[5] == l[2] == 'O':
        print(name_p2,' wins')
        break
    elif l[3] == l[4] == l[5] == 'O':
        print(name_p2,' wins')
        break
    elif l[1] == l[4] == l[7] == 'O':
        print(name_p2,' wins')
        break
    elif l[2] == l[5] == l[8] =='O':
        print(name_p2,' wins')
        break
    elif l[2] == l[4] == l[6] =='O':
        print(name_p2,' wins')
        break
    elif (' ') in l:
        pass
    elif (' ') not in l:
        print('Draw')
        break
   


# In[ ]:




