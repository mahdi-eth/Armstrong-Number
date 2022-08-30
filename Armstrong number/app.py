def armstrong_checker(n):
    result = 0
    list_num = []
    for i in n:
        list_num.append(i)
    for j in list_num:
        result += pow(int(j),len(n))
    if result == int(n): print(True, ",This is an armstrong number.")
    else: print(False,",sorry , this is not an armstrong number. BTW the answer is ",result)

n = int(input("Enter a number to see if it's an armstrong number : "))
armstrong_checker(str(n))