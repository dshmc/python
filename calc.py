num1 = float(input())
num2 = float(input())


action = input()

if action == '+':
    print(num1+num2)
elif action == '-':
    print(num1+num2)
elif action == '/' and num2 == 0:
    print("Деление на 0!")
elif action == '/' and num2 !=0:
    print(num1 / num2)
elif action == '*':
    print(num1 * num2)
elif action == 'mod' and num2 ==0:
    print("Деление на 0!")
elif action == 'mod' and num2 !=0:
    print(num1 % num2)
elif action == 'pow':
    print(num1 ** num2)
elif action == 'div' and num2 == 0:
    print("Деление на 0!")
elif action == 'div' and num2 != 0:
    print(num1 // num2)
    
    
