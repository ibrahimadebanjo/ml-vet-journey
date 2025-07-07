task_list = [ ]
options ="""
        1. Add task
        2. view tasks
        3. mark task as done
        4. Exit """

def add_task():
     task = input("Type a task : ")
     dic = {
         "task" : task,
         "done" : False 
         }
     x = task_list.append(dic)
     return x

def view_task():
    if len(task_list) == 0:
        print("No task yet")
    else:
        for task in task_list:
            print(task)    
def mark_done():
    view_task()
    userIndex = int(input("Input Task Number:"))
    if userIndex == int:
        y = int(userIndex) - 1
        
        task_list[y]["done"] = True   
        print("Marked as Done") 
    else:
        print("You Entered Wrong number")      

while True:
    print(options)
    userInput = input("Enter Your Option : ")
    if userInput == "1":
       add_task()
    elif userInput == "2": 
       view_task()

    elif userInput == "3": 
       mark_done()

    elif userInput == "4":
       break
    else:
       print("Invalid Option")


     
