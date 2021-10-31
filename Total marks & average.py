total = []
average = []
for i in range(4):          #Using 2D list to store the marks.
    marks = input().split()     
    t = 0
    for j in marks:         #To find total marks and average.
        t += int(j)     
    total.append(t)         #To store total marks in list.
    average.append(round(t/3,1))    #To find & store average marks in list.

#Print final Result
for i in range(4):
    print(f"Total: {total[i]} Average: {average[i]}")
