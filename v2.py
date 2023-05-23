import os
import subprocess
import time
import threading
from plyer import notification

current_date = time.strftime("%Y-%m-%d")

def viewtask(filename):

    with open(filename, 'r') as file:
        for line in file:
            print(line.rstrip())  # Use rstrip() to remove trailing newline character

def addtask(taskname, filename):
    text = taskname

    with open(filename, 'a') as file:
        file.write(f'\n--> {text}')

def completetask(taskno, filename):
    line_to_remove = taskno+1

    with open(filename, 'r') as file:
        lines = file.readlines()

    if line_to_remove <= len(lines):
        del lines[line_to_remove - 1]

    with open(filename, 'w') as file:
        file.writelines(lines)

def exitprogram():
    print("THANKS FOR USING MY APP!\n")
    exit()

print("\nWELCOME TO MY APP : TODO MANAGER\nBY ADITYA PADHYE")

while True:

    fmenu = int(input("\nMenu-->\n1.View dates and tasks\n2.Modify tasks\n3.Add a file\n4.Exit\n\nEnter your choice in number : "))

    if fmenu == 1:
        print("\n")
        logs = os.listdir()

        print("Your files :\n")
        for log in logs:
            if log.endswith(".txt"):
                print(log)

        while True:
            openlog = input("\nEnter the name of the file you want to open from the list or press q for exit : ")
            
            if openlog == "q":
                print("\n")
                exitprogram()

            if openlog in logs:
                print("\nFile opened!")
                subprocess.call(["notepad.exe", openlog])
                break
            else:
                print("No file found! Try Again.")

    elif fmenu == 2:
        print("\n")
        logs = os.listdir()

        print("Your dates :\n")
        for log in logs:
            if log.endswith(".txt"):
                print(log)

        while True:
            modify = input("\nEnter the name of the file you want to modify from the above list : ")
            
            if modify in logs:
                print("\nFile opened!")
                print("\nYour tasks -->")
                viewtask(modify)

                while True:
                        
                    menu = int(input("\nMENU -->\n1.Add a Task\n2.Mark as complete\n3.Exit\n\nEnter your choice in number : "))
                    print("\n")

                    if menu == 1:
                        taskname = input("Enter the name of your task : ")

                        if_timer = input("\nDo you want to set timer for this task, press Y/N : ").lower()
                        
                        if if_timer == "y":
                            user_timer = int(input("\nEnter the number of minutes : "))
                            
                            timer = 60 * user_timer
                            remainder = timer - 300

                            # icon = "E:\Coding\Python\Projects\TODO - Task Manager\standards.ico"

                            def countdown_timer(seconds):
                                while seconds > 0:
                                    time.sleep(1)
                                    seconds -= 1
                                    
                                    if seconds == 300:                                        
                                        notification.notify(
                                            title = "Its too close...!",
                                            message = "You've just 5 minutes to complete your task.",
                                            app_icon = "standards.ico",
                                            timeout = 7
                                        )
                                    
                                    elif seconds == 0:
                                        notification.notify(
                                            title = "Its over.",
                                            message = f"Your timer for the task {taskname} has ended. Mark it as complete..",
                                            app_icon = "standards.ico",
                                            timeout = 7
                                        )

                            timer_thread = threading.Thread(target=countdown_timer, args=(timer,))

                            timer_thread.start()

                            addtask(taskname, modify)
                            print(f"Task added succesfully. We will notify you after {user_timer - 5} minutes.")

                            # timer_thread.join()

                        elif if_timer == "n":
                            addtask(taskname, modify)
                            print("Task added succesfully.")

                    elif menu == 2:
                        print("Congratulations for completing!\n")
                        print("\nYour tasks -->")
                        viewtask(modify)
                        taskno = int(input("\nEnter the number of task : "))
                        completetask(taskno, modify)
                        print("Marked as completed.")

                    elif menu == 3:
                        exitprogram()

    elif fmenu == 3:
        date = int(input("\nMenu -->\n1.Add for today\n2.Add for special date\n3.Exit\n\nEnter your choice in number : "))

        if date == 1:
            all_files = os.listdir()
            
            new_file = open(f"{current_date}.txt", "w")

            if (f"{current_date}.txt") in all_files:
                new_file1 = open(f"{current_date}[1].txt", "w")
            
            print("\nFile created for today. You can edit it by selecting Modify tasks option below.")

        elif date == 2:
            all_files = os.listdir()
            
            print(f"\nPlease enter a date in this format. Ex. - {current_date}")
            special_date = input("Enter the date here : ")

            new_file = open(f"{special_date}.txt", "w")

            if (f"{special_date}.txt") in all_files:
                new_file1 = open(f"{special_date}[1].txt", "w")
            
            print("\nFile created for today. You can edit it by selecting Modify tasks option below.")

        elif date == 3:
            print("\n")
            exitprogram()

    elif fmenu == 4:
        print("\n")
        exitprogram()