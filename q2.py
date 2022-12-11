def exercise2(breed,height,weight,male):
    Bulldog=[15,50,14,40]
    Dalmatian = [24,70,19,45]
    M=[9,7,7,6]
    if(breed=='Bulldog'):
        if(male==True):
            if(height>(Bulldog[0]-(Bulldog[0]*0.1)) and (height <(Bulldog[0]+Bulldog[0]*0.1) ) ):
                if(weight>(Bulldog[1]-(Bulldog[1]*0.1)) and (weight <(Bulldog[1]+Bulldog[1]*0.1) ) ):
                    return 'True'
                else:
                    return 'False'
            else:
                return 'False'
        else:
            if(height>(Bulldog[2]-(Bulldog[2]*0.1)) and (height <(Bulldog[2]+Bulldog[2]*0.1) ) ):
                if(weight>(Bulldog[3]-(Bulldog[3]*0.1)) and (weight <(Bulldog[3]+Bulldog[3]*0.1) ) ):
                    return 'True'
                else:
                    return 'False'
            else:
                return 'False'
    elif(breed=='Dalmatian'):
        if(male==True):
            if(height>(Dalmatian[0]-(Dalmatian[0]*0.1)) and (height <(Dalmatian[0]+Dalmatian[0]*0.1) ) ):
                if(weight>(Dalmatian[1]-(Dalmatian[1]*0.1)) and (weight <(Dalmatian[1]+Dalmatian[1]*0.1) ) ):
                    return 'True'
                else:
                    return 'False'
            else:
                return 'False'
        else:
            if(height>(Dalmatian[2]-(Dalmatian[2]*0.1)) and (height <(Dalmatian[2]+Dalmatian[2]*0.1) ) ):
                if(weight>(Dalmatian[3]-(Dalmatian[3]*0.1)) and (weight <(Dalmatian[3]+Dalmatian[3]*0.1) ) ):
                    return 'True'
                else:
                    return 'False'
            else:
                return 'False'
    else:
        if(male==True):
            if(height>(M[0]-(M[0]*0.1)) and (height <(M[0]+M[0]*0.1) ) ):
                if(weight>(M[1]-(M[1]*0.1)) and (weight <(M[1]+M[1]*0.1) ) ):
                    return 'True'
                else:
                    return 'False'
            else:
                return 'False'
        else:
            if(height>(M[2]-(M[2]*0.1)) and (height <(M[2]+M[2]*0.1) ) ):
                if(weight>(M[3]-(M[3]*0.1)) and (weight <(M[3]+M[3]*0.1) ) ):
                    return 'True'
                else:
                    return 'False'
            else:
                return 'False'
            
print(exercise2('Maltese',9.5,6.7,True))
print(exercise2('Bulldog',16,44,False))
            