#for a in range(1,11):
#    print("*"*a)

#1부터 100까지 수를 2의 배수, 3의 배수, 5의 배수로 분류
#2의 배수는 numbers_1의 리스트에
#3의 배수는 numbers_2의 리스트에
#5의 배수는 numbers_3의 리스트에 저장하는 코드를 작성

numbers_1 = []
numbers_2 = []
numbers_3 = []
for a in range (1,101):
    if a%2==0 :
        numbers_1.append(a)
        if a%3==0:
            numbers_2.append(a)
    elif a%3==0 :
        numbers_2.append(a)
    elif a%5==0:
        numbers_3.append(a)

print(numbers_1)
print(numbers_2)
print(numbers_3)
