import csv
from datetime import datetime,timedelta
from google.colab import files

#Initiaize the file name that would be holding our tasks
file_name = "tasks.csv"

#Create imaginary tasks
tasks = [
      {"Task Name": "Submit Assignment", "Deadline": (datetime.now() + timedelta(hours=2)).strftime("%Y-%m-%d %H:%M"), "Email": "ahmadtijani735@gmail.com", "Status": "Pending"},
          {"Task Name": "Renew Subscription", "Deadline": (datetime.now() + timedelta(hours=5)).strftime("%Y-%m-%d %H:%M"), "Email": "nomanazmarlianz@gmail.com", "Status": "Pending"},
              {"Task Name": "Prepare Presentation", "Deadline": (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d %H:%M"), "Email": "abdulonoruoiza410@gmail.com", "Status": "Pending"},
                  {"Task Name": "Pay Electricity Bill", "Deadline": (datetime.now() + timedelta(days=2)).strftime("%Y-%m-%d %H:%M"), "Email": "tijanijelilat56@gmail.com", "Status": "Pending"}
                  ]

#Create file and as well write tasks to it 

with open(file_name, mode='w', newline='') as our_file:
    writer = csv.DictWriter(our_file , fieldnames = ["Task Name", "Deadline", "Email", "Status"])
    writer.writeheader()
    writer.writerows(tasks)

print(f"The test task files {file_name} created successfully")

#Lets download the created file to our local device
files.download(file_name)
