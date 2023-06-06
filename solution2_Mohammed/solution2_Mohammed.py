myfile=open("words.txt")
for line in myfile:
        line=line.strip()
        words=line.split(' ')
        for word in words:
                if len(word)>=19:
                        print(word)
