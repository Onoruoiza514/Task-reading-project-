import pandas as pd
from datetime import datetime, timedelta

from google.colab import drive
drive.mount("/content/drive")

file_path = "/content/drive/MyDrive/tasks.csv"
#tasks = pd.read_csv(file_path)
#tasks.head()

#Lets create a module to handle all our stuffs

class TaskManager:
    def __init__(self , csv_file):
        self.csv_file = tasks
        #self.tasks = pd.read_csv(self.csv_file)
        self.csv_file["Deadline"] = pd.to_datetime(self.csv_file["Deadline"])
        self.csv_file["Status"] = "Pending"


    def Add_tasks(self, task_name, deadline , email, status="Pending"):
        """add a new task to the list using this function"""
        new_task = {
                        "Task Name" : task_name,
                        "Deadline" : deadline,
                        "Email" : email,
                        "Status" : status
                        }
        self.csv_file = pd.concat([self.csv_file,pd.DataFrame([new_task])],ignore_index=True)
        #self.csv_file.to_csv(self.csv_file , index = False)
        #self.save_task()
        print(f"Task '{task_name}' added successfully!")


    def get_due_tasks(self):
        """Get a list of tasks that are due or overdue """
        now = datetime.now()
        due_tasks = self.csv_file[(self.csv_file["Deadline"] <= now) & (self.csv_file["Status"] == "Pending")]
        return due_tasks


    def mark_tasks_as_done(self,task_name):
         """Mark a task as complete"""
         task_index = self.csv_file[self.csv_file["Task Name"] == task_name].index
         if not task_index.empty:
             self.csv_file.loc[task_index, "Status"] = "Done"
             #self.save_tasks()
             print(f"Task '{task_name}' marked as done!")
         else:
             print(f"Task '{task_name}' not found!")


    def delete_task(self):
        """Delete a task that is done from the list of tasks"""
        if "Done" in self.tasks["Status"].values:
            self.tasks.drop(self.tasks[self.tasks["Status"] == "Done"].index,inplace= True)
            self.save_tasks()
            print("Done tasks deleted successfully!")
        else:
            print("No done task found")


    def save_tasks(self):
        """Save the updated tasks back to the to-do list"""
        self.tasks.to_csv(self.csv_file, index=False)
        print("Tasks saved successfully")

    def display_tasks(self):
        """Display all tasks in the to-do list"""
        print(self.csv_file)


#So all our functions are completely created, remaining to be usedh

if __name__ == "__main__":
    task_manager = TaskManager(tasks)
    task_manager.display_tasks()


    #Now lets try adding a task to our to do list
    task_manager.Add_tasks(task_name = "Attend Religious services" , deadline = (datetime.now() + timedelta(hours = 5)).strftime("%Y-%m-%d %H:%M"), email = "blahblahblah@gmail.com" )

    task_manager.display_tasks()

    task_manager.mark_tasks_as_done("Submit Assignment")

    task_manager.display_tasks()
