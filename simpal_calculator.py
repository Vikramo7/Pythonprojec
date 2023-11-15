print('''+ Add
       - subtruct
       * multiple
       / divide''')
num1 = int (input('enter the first num :-'))
num2 = int (input('enter the secand num:-'))
opr = (input('enter the operator..'))
if opr == '+':
    print(num1+num2)
elif opr == '-':
    print(num1-num2)
elif opr == '*':
    print(num1*num2)
elif opr == '/':
    print(num1 / num2)
else :
   print("invailed opr")