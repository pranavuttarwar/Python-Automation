#Approch 1 Import package file in the new file

import Calculator

Calculator.add(10,20) #Call function
Calculator.mult(10,20) #Call function

cal=Calculator.demo()  #Creting object from pacakage file.
cal.m1()
cal.m2()
print("Class Variable", cal.num1)  #Calss variable call

print("Global Variable",Calculator.num)  #Access the global varibale

