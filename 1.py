what = input ("Что будем делать (+,-,*,/)?")

if what == "+" or what == "-" or what == "*" or what == "/": 
        a = float (input ("Введи первое число: "))
        b = float (input ("Введи второе число: "))

        if what == "+":
	        c = a + b
	        print ("Результат: " + str(c))
        elif what == "-":
	        c = a - b
	        print ("Результат: " + str(c))
        elif what == "*":
	        c = a * b
	        print ("Результат: " + str(c))
        elif what == "/":
	        c = a / b
	        print ("Результат: " + str(c))

else:
	print ("Выбрано неверное действие")

