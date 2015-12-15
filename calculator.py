import math
#total_bill = float(raw_input("How much is your restaurant bill?"))
#tip_value = float(raw_input("What percent tip would you like to leave?"))
#num_friends = int(raw_input("How many people are in your group?"))
#tip_percent = tip_value / 100
#def calculate_tip(total_bill, tip_percent):
#    return total_bill*tip_percent
#def tips_with_friends (total_bill, tip_percent, num_friends):
#    return (total_bill*tip_percent)/num_friends
#print "Each person should pay", str(tips_with_friends(total_bill, tip_percent, num_friends)) +"." 

num1 = int(raw_input("What is your first number?"))
num2 = int(raw_input("What is your second number?"))

def add(num1,num2):
    return num1+num2
#print add(num1, num2)

def subtract(num1, num2):
    return num1 - num2
#print subtract(num1,num2)

def multiply(num1,num2):
    return num1 * num2
#print multiply(num1,num2)

def divide(num1, num2):
    return num1 / num2
#print divide(num1,num2)

#def power(num1,num2):
#    return num1 ^ num2
#print power(num1,num2)
age = add(30,4)
height = subtract(78,2)
weight = multiply(6,24)
iq = divide(100,2)
print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)
