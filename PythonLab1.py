#Python lab 1
#Learn from the online interactive tutorial and finish below tasks
#You can edit in this file by filling blanks after each question.
#Submit the .py file for your own reference
#This practice is graded only on submission. 
#It will help you to get started on Python for the homework

#####
#Example function
#####
def example(): #def is function definition
    print("I am the example code")
#Now, go to the end of this file and you will find the main function & how to run your code there
#Around line #94


#####
#1. function in python
####

def printHello(): 
    print("Hello")
#Remove the # at the begining of this line.
#tab is IMPORTANT in python. tab in python replaces {} in C++
#print string hello world. One line of code here. Make sure it is indented to show it belongs to this function


#####
#2. variable definition in python
#####

def someVars():
    num1 = int(21)
    num2 = int(13)
    num3 = float(9.2)
    num4 = float(5.3)
    result = num1 + num2
    result2 = num3+num4
    print("the sum of num1",num1,"and num2",num2, " is ", result )
    print("the sum of float",num3,"and num2",num4, " is ", result2 )
    #define a few integer and float numbers, add them together and print result out

#call the function to run it in the main function at the end of the file

#####
#3. define a list in python
#####

def mylis():
    # Define a list with 5 numbers and print it out
    list1 = [0, 1, 2, 3, 4]
    print("List 1:", list1)

    # Define an empty list and append a few numbers into it, then print it out
    list2 = []
    list2.append(5)
    list2.append(6)
    list2.append(7)
    print("List 2:", list2)
#call your mylis func to execute in the main function at the end of the file

#####
#4. string output
#####

def printstr(input_str1, input_int1):
    print(input_str1+ str(input_int1))
    #convert int into string and append the int with the string to form a long string
    #(technical googling practice -- google what func to use)
    #print the long str out

#In the main function, define an input string and an input int.
#Pass them in as parameters to the function. Call and run the function to see results.

####
#5. passing var to func and return
####

def funcvars(inputvar1, inputvar2):
    result = inputvar1 + inputvar2
    print(result)
    return result
    #add the input numbers together
    #returen the result

#Define the input variables in main, pass them into the function.
#In main, use a result variable to receive the result from funcvars and print the result out

####
#6. for loop
####

def go_over_list(mylis):
    for x in mylis:
        print(x)
    #use for loop to go over the input list and print out items one by one

def go_over_list1():
    for x in range(10,19):
        print(x)
    #use for loop to directly print out numbers from 10 to 17

def go_over_list2(mylis):
    for i,x in enumerate(mylis):
        mylis[i] = (x*2)
    print(mylis)
    #use for loop & go over your list
    #multiply 2 to every item in your list, print results out

def go_over_list3(mylis):
    resLis = []
    for x in mylis:
        resLis.append(x*2)
    print(resLis)
    
    #create an empty list resLis
    #go over items in the input list, multiply 2 to every item
    #add result one by one to resLis
    #return resLis

#Call all the functions in main. Provide necessary inputs to the functions.
#For those with return values, print the return values out in main.

####
#7. while loop
####
def whileloop_go_over_list(mylis):
    index = 0 
    while index < len(mylis):
        print(mylis[index])
        index +=1

def whileloop_go_over_list1():
    index = 10
    while index < 19:
        print(index)
        index+=1

def whileloop_go_over_list3(mylis):
    resLis = []
    index = 0
    while index < len(mylis):
        result = mylis[index] * 2
        resLis.append(result)
    return resLis
#do all the problems in 6 using while loop instead


#####
#Here is the main function
#You can have only 1 main function in 1 script
#Left click on the green arrow next to the line number of the line of the main function definition
#Your code would run.
if __name__ == '__main__': #a quick way to type this line is: type "main" and then tab
    print("****Question 1****")
    printHello()
    print("****Question 2****")
    someVars()
    print("****Question 3****")
    mylis()
    print("****Question 4****")
    printstr("how many girlfriends you got?:",6)
    print("****Question 5****")
    funcvars(3.2, 8)
    print("****Question 6 list: 0****")
    dre_list = [342,123,4353,24,24,52,1,4,5,353,24]
    go_over_list(dre_list)
    print("****Question 6 list: 1****")
    go_over_list1()
    print("****Question 6 list: 2****")
    go_over_list2(dre_list)
    print("****Question 6 list: 3****")
    go_over_list3(dre_list)
    print("****Question 7****")
    #you can start call and run your functions here


######
#Python is an easier PL to learn than C++ and looks like C++
#From this lab experience, reflect and summary what it feels like
#when you are learning a new PL that is similar to a PL that you already know?
#Your answer here:

#In this case, when you want to learn a new PL that looks like a PL that you already know,
#how can you learn the new PL quickly? Any steps?
#Your answer here:
