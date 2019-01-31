numbers = input("Enter the Data: ")

odd_list = []

for i in numbers.split(','):
    i = int(i)
    if (i % 2 != 0):
        odd_list.append(str(i*i))
        
print(','.join(odd_list))