file = open("filename")
data = file.read()
wordsstripped = data.split()
print(len(wordsstripped))
paragraphs=len(data.split("\n\n"))
count = 0
number = 0
spaces = 0
punctuationforwords = ['.','?','!',',',"'"]
punctuation = ['.','?','!']
splchars = ['-', "'", '.', '.','-', ',', "'", '-',"'", '.']
c_splchars = 0
#words = 0
sentences = 0
#paragraphs = 0
countofpunctuation = 0
for i in range(len(data)):
    if(data[i].isalpha()):
        count+=1
    if(data[i].isdigit()):
        number+=1
    if data[i]==' ':
        spaces+=1
    if data[i] in punctuation:    
        sentences+=1
    if data[i] in punctuationforwords:
        countofpunctuation +=1
    if data[i] in splchars:
        c_splchars+=1
        
countofpunctuation-=1
words = len(wordsstripped)+countofpunctuation
print(data[i])
output = (count,number,splchars,words,sentences)


