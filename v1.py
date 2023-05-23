logfile = "E:\Coding\Python\Projects\TODO - Task Manager\log.txt"

def viewtask():
    filename = logfile

    with open(filename, 'r') as file:
        for line in file:
            print(line.rstrip())  # Use rstrip() to remove trailing newline character

def addtask(taskname):
    filename = logfile
    text = taskname

    with open(filename, 'a') as file:
        file.write(f'\n--> {text}')

def completetask(taskno):
    filename = logfile
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

print("\nYour tasks -->")
viewtask()

while True:

    menu = int(input("\nMENU -->\n1.Add a Task\n2.Mark as complete\n3.Exit\n\nEnter your choice in number : "))
    print("\n")

    if menu == 1:
        taskname = input("Enter the name of your task : ")
        addtask(taskname)
        print("Task added succesfully.")

    elif menu == 2:
        print("Congratulations for completing!\n")
        print("\nYour tasks -->")
        viewtask()
        taskno = int(input("\nEnter the number of task : "))
        completetask(taskno)
        print("Marked as completed.")

    elif menu == 3:
        exitprogram()