from re import search
text = "C:/Users/vigne/Downloads/wordle.txt"
f= open(text)
f = f.readlines()
f = [x.strip('\n') for x in f]
wordle = []
def exercise9(green,yellow,gray):
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
                
                
        
    
    
print(exercise9(green = {1:'i',3:'c'}, yellow = {'e':{3}},gray = {'r','a','s','d','f'}))

# green = {'i':1,3:'c'}
# for i in green:
#     print(green[i])