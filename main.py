with open('wow.txt','w')as file:
    file.write("hi i am san  attending codingal class")
    file.close() 


with open('wow.txt','r')as file:
    data=file.readlines()
print("words in this file are---")
for line in data :
    word=line.split()
    print(word)
    file.close()
