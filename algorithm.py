#This dictionary acts as a hash table and memory of employess data

df={0: [], 1: [], 2: [14628, "Umer", 32194266, 9233311616], 3: [], 4: [], 5: [16548, "Anas", 34673439, 9239548584],
    6: [10868, "Talha", 37656599, 9230546164], 7: [], 8: [], 9: [], 10: [], 11: [], 12: [], 13: [],
    14: [], 15: [], 16: [], 17: [14572, "Aliya", 39545855, 9230216556], 18: [14715, "Moiz", 32514445, 9230546144], 19: [10597, "Uzair", 34854652, 9326903022],
    20: [], 21: [], 22: [1493, "Ahmed", 32947512, 9234563164], 23: [], 24: [11739, "Abdullah", 34986222, 9231615600],
    25: [], 26: [], 27: [11245, "Ibad", 31417931, 9235215661], 28: [], 29: [], 30: [12810, "Shoiab", 34815555, 9232621654],
    31: [19342, "Murtuza", 33943481, 9234524685], 32: [], 33: [], 34: [17358, "saad", 34586327, 9231849855], 35: [19560, "Tania", 33684816, 9234501566],
    36: [17642, "Osama", 36441531, 9235110564], 37: [], 38: [], 39: [], 40: [], 41: [15803, "Wajahat", 3483193, 9231614144],
    42: [19424, "Sohail", 35618856, 9231654454], 43: [15590, "Usman", 36844559, 9236521665], 44: [], 45: [11547, "Jaffery", 36557515, 9232520416],
    46: [], 47: [], 48: [], 49: [], 50: [], 51: [], 52: [12761, "Faraz", 34585855, 9230531311], 53: [], 54: [],
    55: [], 56: [], 57: [], 58: [], 59: [12768, "Shuraim", 31545555, 9236544165], 60: [], 61: [], 62: [13552, "Babar URF Lifter", 31585566, 9233783216],
    63: [], 64: [], 65: [], 66: [], 67: [18243, "Zeeshan", 34921552, 9230615165], 68: [14694, "Sameer", 31962473, 9230216164],
    69: [], 70: [14767, "Iqbal", 34984526, 9230151644], 71: [], 72: [], 73: [], 74: []}

# This func is used to asked the user the operation
def welcome_note():
    operation=input('enter the operation you wanted to do (insertion/searching)')
    if operation=='insertion':
        insert()   #it will call insert function 
    if operation=='searching':
        search()   #it will call searching function 

#This function is used to search the employee data
def search():
    x=int(input('enter the employee no '))#The employee no whoes data is needed
    count=1                                                                                                              
    hash_key=x % 71 #hash function
    print(hash_key) #hash memory adrress

    if x in df[hash_key]: #employee no is the memory address comes true
        print(df[hash_key]) #it will print data
        print('sucessfull probs=1')#probs will be one 
        
     
    else: #it the if is not true then it will run this
        for i in df.keys(): #loop will iterate in whole memory adrress(dics keys)
            if x in df[i]: #if it will find the employee no matches  it will be true 
                print(df[i])#the employee data
                print(i)#the new memory address after probing
                print('succesfull pobs=',(i+1)-hash_key)#probs will be new memory minus hash_key
                
                
    if x not in df[hash_key] and df[hash_key]==[]: #if the data is not found and the memory is empty the it will true
        print('not found')
        print('unsuccesfull probs=1')#the unsuccesfull probs will be one
    else:           
        while x not in df[hash_key] and df[hash_key]!=[]: #if the data is not found and the memory isnot empty it will iterate untill it come true
            hash_key=hash_key+1#it will increase untill there a free space
            count=count+1
        print('not found')
        print('unsuccesfull probs=',count)#the probs of unsuccesfull search 

#This func is used to insert the a employee data 
def insert():
    d=[]# a empty list which store all the data of an employee
    employee_no=int(input('enter the employee no'))# input statement of employee no
    employee_name=input('enter the employee name')#input statement of employee name
    employee_landline_no=int(input('enter the employee landline no'))#input statement of employee lanline no 
    employee_mobile_no=int(input('enter the employee mobile no'))#input statement of employee of mobile_no
    d=[employee_no,employee_name,employee_landline_no,employee_mobile_no]#all data will store in a list
    print(d)
    probs=1

    hash_key=employee_no % 71#hash function
    print(hash_key)#memory address
    #print(hash_key)
    if hash_key in df.keys() and df[hash_key]==[]: #if the memory adrress in dics and that memory adress is empty
        df[hash_key]=d #it will assign the dat to that employee no
        print(hash_key)
        #print(df)
        print("probs=",probs)#probs will be one
        
        
    else:
        while df[hash_key] !=[]:#if it will not find the memory adress empty it will iterate the memory adress untill it is empty
            
            hash_key=hash_key+1
            probs=probs +1

        print("probs=",probs)#how many it iterate in memory address
            
        df[hash_key]=d
        print(hash_key)

welcome_note()
