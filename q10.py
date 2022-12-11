# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 14:50:44 2022

@author: vigne
"""

from re import search
import copy
text = "C:/Users/vigne/Downloads/wordle.txt"
f= open(text)
f = f.readlines()
f = [x.strip('\n') for x in f]

def exercise9(green,yellow,gray):
    wordle = []
    flag = 0
    for i in f:
        for j in gray:
            if search(j,i):
                flag = 1
                #break
                
    #for i in f:
        for j in green:
            
            if(i[j]!=green[j]):
                flag = 1
                #break
    #for i in f:
        for j in yellow:
            for k in yellow[j]:
                #print(j)
                if(i[k]==j):
                    flag=1
                elif j not in i:
                    flag=1  
        if flag==0:
            wordle.append(i)
        flag = 0
            
    return wordle
#USE THIS FOR QUESTION 10
def exercise10(green,yellow,gray):             

    #green = {1:'i',3:'c'}
    #yellow = {'e':{3}}
    #gray = {'r','a','s','d','f'}
    exercise10_list = []
    answer = exercise9(green,yellow,gray)
    #answer = exercise9(green = {1:'i',3:'c'}, yellow = {'e':{3}},gray = {'r','a','s','d','f'})
    copied_list = copy.deepcopy(answer)
    for i in copied_list:
        word_idk = []
        for j in copied_list:
            green2 = green.copy()
            yellow2 = yellow.copy()
            gray2 = gray.copy()
            if i == j:
                continue
            
            else:
                for k in range(len(i)):
                    if i[k]==j[k]:
                        green2[k]=i[k]
                    elif i[k] in j:
                        #print('Reached here')                    
                        yellow2[i[k]]={k}
                        #print(yellow2[i[k]])
                    else:
                        gray2.add(i[k])
            x = exercise9(green2,yellow2,gray2)
            #print(x)
            #print(green2,yellow2,gray2)
            word_idk.append(len(x))
        exercise10_list.append(sum(word_idk))
        word_idk = []
        
    print(min(exercise10_list))

    
            
#### USE THIS TO RUN THE ENTIRE THING
exercise10(green = {1:'i',3:'c'}, yellow = {'e':{3}},gray = {'r','a','s','d','f'})
    
#print(  

# green = {'i':1,3:'c'}
# for i in green:
#     print(green[i])