subject = ["I","We"]        #To store subjects in list
verb = ['play','watch']     #To store verbs in list
objects = input().split()   #To store input objects in list

#To generate sentences.
sentence = ''
for i in subject:
    for j in verb:
        for k in objects:
            print(i,j,k+'.')
