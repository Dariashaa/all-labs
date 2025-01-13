num = int(input('Введите число: '))
for i in range(1,num+1):
    print(i)
##################################################
num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
if num1 > num2:
    print('Большее число: ', num1)
elif num1< num2:
    print('Большее число: ', num2)
else:
    print('Числа равны')
##################################################
f=open('C:\\Users\\1\\Desktop\\лабы\\example.txt')
s=f.readline()
print(s)