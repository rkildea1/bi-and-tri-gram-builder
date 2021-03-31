
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

def top_word_BOW(n):
    bow_list = [] #making the dictionary a list so create a blank list
    for key, value in n.items(): #for every key/ value in the dictionary..
        vk = (value, key) #store each value and key in opposite order in a variable
        bow_list.append(vk) #write each value and key to the new list

    bow_list = sorted(bow_list) #sort the list
    #bow_list = sorted(bow_list, reverse=True) #reverse sort
    top_word = bow_list[-1] #create varviable from the last item in the list (which is the now highest dict item)
    top_word = list(top_word) #make that pair a list type
    print ("The most frequent word occuring in the text is:             ", top_word[1]) #print the second item in the ist (i.e., the word)
    print ("The most frequent word occurs the following number of times:", top_word[0])
    
top_word_BOW(my_dict_il) #call the function
