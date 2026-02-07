
def retmycharwithtime(s):
    newstr = s.lower() # Good
    myfreq = {} #naming could have been relevnat
    for char in newstr: 
        if char.isalpha(): # good but for beginneres to build uisng fundamentals something to think
            myfreq[char]=myfreq.get(char,0)+1
    return myfreq


def stud_details(students,studentname="all"):
    
    student_list_lower = []
    for items in students:
        student_list_lower.append(items.lower())
    
    mydict = {}
    for everyname in student_list_lower:
        subdict={}
        for char in everyname:
            subdict[char]=subdict.get(char,0)+1
        mydict[everyname]=subdict

    if studentname.lower() in mydict:
        print(f"{everyname}:{mydict[studentname.lower()]}")
    elif studentname=="all":
        for key,value in mydict.items():
            print(f"{key}:{value}")
    else:
        print("Name not found")

        






















if __name__ == "__main__":
    # s = "abcd"
    # newstr = s.lower()
    # print(retmycharwithtime(newstr))



    students = ["divya", "Kavya", "dipya", "dopya"]
    stud_details(students,"Dopya")
    # stud_details(students)

    # handle print inside the function so that client has comfort
    # char_time(list, "divya") --> divya records
    # if unspecified ---> return all
    # in what form i must return so that it makes sense to the client


    