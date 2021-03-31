
f = open('Moby_dick.txt', 'r+')
words1 = f.read()
q3_words_list = words1.split()

def bigram(file,n=2,i=0):
    while len(file[i:i+n]) == n:
        yield file[i:i+n]
        i += 1
bigrams_lists = list(bigram(q3_words_list, n=2)) #this is my bigram list. list inside a list

print(bigrams_lists)
