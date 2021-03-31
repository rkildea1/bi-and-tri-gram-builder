
f = open('Moby_dick.txt', 'r+')
words1 = f.read()
q3_words_list = words1.split()

def bigram(file,n=2,i=0):
    while len(file[i:i+n]) == n:
        yield file[i:i+n]
        i += 1
bigrams_lists = list(bigram(q3_words_list, n=2)) #this is my bigram list. list inside a list

#print(bigrams_lists)

bigrams_2 = []
for il in bigrams_lists: #for inner list in 
    bigrams_2.append((il[0],il[1]))
#print(bigrams_2)

my_dict_il = {} #create a blank dictionary to write the word list to

for item in bigrams_2:
    if item in my_dict_il.keys(): #if the word in the wordlist is already a key in the dictionary then...
        my_dict_il[item]+=1 #increase the count by one
    else:
        my_dict_il[item]=1 #add to dictionary and make count 1

#print(my_dict_il)
