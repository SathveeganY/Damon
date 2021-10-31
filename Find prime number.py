input_number = int(input())
while input_number > 0:
    temp_list = []
    if input_number == 1:
        print('non-prime')
    else:
        for i in range(1,input_number+1):
            if input_number % i == 0:
                temp_list.append(i)
        if len(temp_list) == 2:
            print('prime')
        else:print('non-prime')
    input_number = int(input())
