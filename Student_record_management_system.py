import json
# with open("first_project.json",'w') as f: # once json file created with an empty list.. no need to execute these 2 lines because each time,
#    json.dump([],f) # these line will create an empty list causes loss of previous data
with open("first_project.json",'r') as f:
  student_list=json.load(f)
while True:
  menu=input("1.Add student\n2.view student\n3.Count total student\n4.Search Name\n5.Update student details\n6.Delete student\n7.Exit\nEnter choice here..")
  print("*"*20)
  if menu=='1':
    d={
        "name":input("enter student name:"),
        "roll":input("enter roll number:"),
        "course":input("enter course:"),
    }
    student_list.append(d)
    with open("first_project.json",'w') as f:
      json.dump(student_list,f,indent=4)

  elif menu=='2':
    with open("first_project.json",'r') as f:
      data=json.load(f)
    if data==[]:
      print("Empty list")
    else:
        for student in data: # here, student is element of list i.e a dictionary
            for key,value in student.items(): 
                print(key,":",value)
            print("_"*15)

  elif menu=='3':
    with open("first_project.json",'r') as f:
      data=json.load(f)
    print("total number of students",len(data))
  
  elif menu=='4':
    name=input("enter name:")
    found=False
    with open("first_project.json",'r') as f:
      data=json.load(f)
    for student in data:
      if student["name"]==name:
        found=True
        break
    else:
      found=False
    
      
    if found==True:
      print("found")
      print(student)
    else:
      print("not faound")
  elif menu=='5':
    menu2=input("enter\n1.update name\n2.update course\nenter choice here..")
    if menu2=='1':
      roll=(input("enter roll number:"))
      with open("first_project.json",'r') as f:
        data=json.load(f)
      found=False
      for student in data:
        if student['roll']==roll:
          student["name"]=input("enter new name:")
          found=True
          print("updated successfully")
          break
          
    if found is True:
      with open("first_project.json",'w') as f1:
            json.dump(data,f1,indent=4)
        
    else:
      print("not found")
    if menu2=='2':
      roll=input("enter roll number:")
      found=False
      with open("first_project.json",'r') as f:
        data=json.load(f)
      for student in data:
        if student['roll']==roll:
          student["course"]=input("enter New Course:")
          found=True
          break
    if found is True:
      with open("first_project.json",'w') as f2:
        json.dump(data,f2,indent=4)
    if found is not True:
      print("not found")



    
  elif menu=='6':
    roll=input("enter student roll number to be deleted:")
    found=False 
    with open("first_project.json",'r') as f:
      data=json.load(f)
    for student in data:
      if student["roll"]==roll:
        found=True
        break
    if found is True:
      data.remove(student)
      print(student['name'],"deleted successfully") # this updates json with latest info
      with open("first_project.json",'w') as f:
        json.dump(data,f,indent=4)
    if not found:
      print("not found")
    
 
  elif menu=='7':
    break
    
