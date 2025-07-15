def display1(Regno,age): 
    print("Regno:", Regno) 
    print("Age:", age) 
print("code-1: positional arguments") 
display1("AIE112",20) 
#Uncomment and execute the below function call statement and observe the output 
#display1(20," AIE112") 
def display2(Regno,age): 
    print("Regno:", Regno) 
    print("Age:", age) 
print("-------------------------------------------------") 
print("code-2: keyword arguments") 
display2(age=19, Regno=" AIE112") 
def display3(Regno, sem=3, roomno="C303"): 
    print(Regno) 
    print(sem) 
    print(roomno) 
print("-------------------------------------------------") 
print("code-3: default arguments") 
display3("AIE112",4) 
#Uncomment and execute the below function call statements one by one and observe the output 
#display3("AIE234") 
#display3("AIE78","4",”C200”) 
def display4(name, *total_marks): 
    print("Passenger name:",name) 
    total=0 
    for i in total_marks: 
        total+=i
    print("Total:", total) 
print("-------------------------------------------------") 
print("code-4: variable argument count") 
display4("Jack",12,8,5) 
#Uncomment and execute the below function call statements one by one and observe the output 
#display4("Chan",20,12) 
#display4("Henry",23)
