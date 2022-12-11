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
              
                
        for j in green:
            
            if(i[j]!=green[j]):
                flag = 1
           
        for j in yellow:
            for k in yellow[j]:
            
                if(i[k]==j):
                    flag=1
                elif j not in i:
                    flag=1  
        if flag==0:
            wordle.append(i)
        flag = 0
            
    return wordle

def exercise10(green,yellow,gray):             


    exercise10_list = []
    answer = exercise9(green,yellow,gray)
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
                        yellow2[i[k]]={k}
                    else:
                        gray2.add(i[k])
            x = exercise9(green2,yellow2,gray2)
            word_idk.append(len(x))
        exercise10_list.append(sum(word_idk))
        word_idk = []
        
    print(min(exercise10_list))

exercise10(green = {1:'i',3:'c'}, yellow = {'e':{3}},gray = {'r','a','s','d','f'})
    
