import json

df={k:[]  for k in range(75)}
#js = json.dumps(df)
#f = open("filee.json","w")
#f.write(js)
#f.close()
#def hash_func(employee_no):
        #hash_key=employee_no % 7
    #print(hash_key)
    


for i in range(30):
        


    d=[]
    employee_no=int(input('enter the employee no'))
    employee_name=input('enter the employee name')
    employee_landline_no=int(input('enter the employee landline no'))
    employee_mobile_no=int(input('enter the employee mobile no'))
    d=[employee_no,employee_name,employee_landline_no,employee_mobile_no]
    print(d)
    #hash_func(employee_no)
    hash_key=employee_no % 73
    print(hash_key)
    #print(hash_key)
    if hash_key in df.keys() and df[hash_key]==[]:
        df[hash_key]=d
        print(hash_key)
        print(d)
        print(df)
        js = json.dumps(df)
        f = open("filee.json","w")
        f.write(js)
        f.close()
    else:
        while df[hash_key] !=[]:
            
            hash_key=hash_key+11
        df[hash_key]=d
        print(hash_key)
        js = json.dumps(df)
        f = open("filee.json","w")
        f.write(js)
        f.close()
     


#def searchhh():
    #search_key=int(input('enter the user employee no '))
    #key= search_key % 67
    #if key in df.keys():
            #print(df[key])
        
#def Searching():
    #if x==

#hash_func()
#searchhh()    
    
#4548
#4414
#hash_func()

