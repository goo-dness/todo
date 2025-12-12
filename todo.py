import json
from datetime import datetime                    
#set filename to save files    
TASKS_FILE ="tasks.json"                         
tasks = []                                      
#read tasks from files
def loaf_tasks():
    try:
       with open(TASKS_FILE, 'r') as f:
         return  json.load(f)                        
         
    except FileNotFoundError:                          
      return[]                                   
#save tasks to file                              
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:                   
      json.dump(tasks, f, indent=4)

#Add a new tas                                   
def add_tasks(tasks):
    print("\nAdd New Task")
    description = input("\nTask description: ").st
rip()
    print("Priority: 1-High, 2-Medium, 3-Low")
    priority = input("\nChoose task priority: ").s
trip()
    priority_map={"1":"High", "2":"Medium", "3":"Low"}
    priority = priority_map.get(priority, Medium)
    due_date = input("\nEnter date: YYYY-MM-DD or
enter to skip: ")

#create a dict the new tasks
task = {
    "id": len(tasks) + 1,
    "description": description,
    "priority": priority,
    "due_date": due_date if due_date else "No dead
line",
    "status": "Pending",                             
    "created_at": datetime.now()
       }
#add the new task to tasks list and save
task.append(tasks)
save_tasks(tasks)
print("\nTask added successfully")

#view existing tasks
def view_tasks(tasks, filter_pending=False):
    if not tasks:
      print("\nNo task yet!")
      return
print("■" * 50)                                  
print("YOUR TASKS")
print("□" * 50)
#loop through  tasks, if status is "complete" skip
for task in tasks:                                  
if filter_pending and task['status'] == "Complete":
    continue                                      
   status_icon = "✅️" if task["status"] =="Complet
e" else "🔴",
   print(f"\n[{task['id']}] {status_icon} {task['description']}")                                      
   print(f" Priority:{task['priority']} |Due: {task['due_date']}")                                    
   print(f" Status: {task['status']}|Created: {task['created_at']}")                              
   print("=" * 50)
#Mark tasks as complete
def complete_tasks(tasks):
    view_tasks(tasks)
    try:
      task_id =int(input("\nEnter task ID: "))          
      for task in tasks:                                 
      if task['id'] == task_id:                            
      task("status") == "Comppete"
           save_tasks(tasks)                                
           print("\nTask mark as complete")                
           return
           print("\nTask not found!")
    except ValueError:                                    
    print("\nInvalid input")
                                                 
#Remove task completely
def delete_task(tasks):
   view_task(tasks)
   try:                                                  
   taskid = int(input("\nEnter task ID: "))
        for i,task in enumerate(tasks):                     
        if task['id'] == taskid:
              deleted = tasks.pop(i)
              save_task(tasks)
              print("\nTask deleted!")
              return                                                                                             
              print("\nTask not found")
    except ValueEror:
         print("\nInvalid input")
#the program control center
def main():
    load_task(tasks)
    while True:
       print("\nMENU")
       print("\n1. Add task")
       print("\n2. View all tasks")
       print("\n3. View pending tasks")                
       print("\n4. Complete task")
       print("\n5. Delete task")
       print("\n6. Quit")
    choice = input("\nChoose option 1-6: ")
       if choice == "1":
          add_task(tasks)
       elif choice == "2":
          view_task(tasks)
       elif choice == "3":
          view_task(tasks, filter_pending=True)
       elif choice == "4":
          complete_task(tasks)
       elif choice == "5":
          delete_task(tasks)
       elif choice == "6":                                 
       print("\nGoodbye")                              
       break
       else:
          print("\nInvalid choice")



