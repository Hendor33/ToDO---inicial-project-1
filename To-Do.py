#goal of this task is to create to-do list to increase productivity of my days and get better at Python
import uuid
import json
"""
#1 define functions (tools)
def create_tasks(my_goals):
    my_goals.append(input("What is the goal?: "))

def display_tasks(my_goals):
    for index, goal in enumerate(my_goals, start = 1): #Start = 1 means that first task is going to have number one but index is still the same which has to be handled
        print(f"{index}) {goal}")

def update_tasks(my_goals):
    for index, goal in enumerate(my_goals, start = 1):
        print(f"{index}, {goal}")
    try:
        update_index = int(input("Which goal you would like to update? ")) - 1  # That final -1 is to handle the index X position problem
        test_exists = my_goals[update_index] # check number of goal whether it exists

        update_goal = input("What is the new goal?")
        my_goals[update_index] = update_goal
    except ValueError:
        print("Please enter a number")
    except IndexError:
        print("Please enter a valid number of goal")

#2 define main part of project
def todo_list():
    my_goals = []
    while True:
        choice = input("What would you like to do? C - create, R - read, U - update, D - delete: ").upper().strip()
        if choice == "C":
            create_tasks(my_goals)
        elif choice == "R":
            display_tasks(my_goals)
        elif choice == "U":
            update_tasks(my_goals)

todo_list()
"""

class TodoApp():
    def __init__(self):
        self.my_goals = []
        self.load_tasks()

    def save_tasks(self):
        self.my_goals.sort(key=lambda x: x["priority"], reverse=True)
        with open("goals.json", "w") as file:
            json.dump(self.my_goals, file)

    def load_tasks(self):
        try:
            with open("goals.json", "r") as file:
                self.my_goals = json.load(file)
        except FileNotFoundError:
            self.my_goals = []
    def create_tasks(self):
        new_goal = input("What is the new goal?: ").strip()
        while True:
            try:
                priority = int(input("What is the priority?: 1 - small / 2 - medium / 3 - high "))
                if 1 <= priority <= 3:
                    new_task_data = {
                        "task": new_goal,
                        "priority": priority,
                        "done": False
                    }
                    self.my_goals.append(new_task_data)
                    self.save_tasks()
                    print("Goal added!")
                    break
                else:
                     print("Please enter number in between 1 and 3!")

            except ValueError:
                (print("Priority must be between 1 and 3!"))

    def display_tasks(self):
        #add logic of no goals found

        priority_labels = {
            1: "small",
            2: "medium",
            3: "high"
        }
        self.my_goals.sort(key = lambda x: x["priority"], reverse = True)

        for index, goal in enumerate(self.my_goals, start=1): # Start = 1 means that first task is going to have number one but index is still the same which has to be handled
            task_text = goal["task"]
            if goal["done"]:
                print(f"{index}) [✔] {task_text}")
            else:
                prio_name = prio_name = priority_labels[goal["priority"]]
                print(f"{index}) [ ] {task_text} - priority {prio_name}")

    def update_tasks(self):
        for index, goal in enumerate(self.my_goals, start=1):
            print(f"{index}, {goal}")
        try:
            update_index = int(input("Which number of goal you would like to update? ")) - 1  # That final -1 is to handle the index X position problem
            test_exists = self.my_goals[update_index]  # check number of goal whether it exists

            update_goal = input("What is the new goal?: ")
            self.my_goals[update_index]["task"] = update_goal
            self.save_tasks()
        except ValueError:
            print("Please enter a number! ")
        except IndexError:
            print("Please enter a valid number of goal!")

    def delete_tasks(self):
        self.display_tasks()
        try:
            delete_index = int(input("Which number of goal you would like to delete? ")) - 1  # That final -1 is to handle the index X position problem
            test_exists = self.my_goals[delete_index]  # check number of goal whether it exists
            deleted_goal = self.my_goals.pop(delete_index)
            print(f"Goal {deleted_goal["task"]} was successfully deleted!")
            self.save_tasks()
        except ValueError:
            print("Nothing was deleted! Please enter a valid number!")
        except IndexError:
            print("Nothing was deleted! Please enter a valid number of goal!")

    def mark_done(self):
        self.display_tasks()
        try:
            done_index = int(input("Which number of goal you would like to set as done? ")) - 1
            if self.my_goals[done_index]["done"] == True:
               print("This goal is already done!")
            else:
                self.my_goals[done_index]["done"] = True
                self.save_tasks()
                print("Goal was successfully marked as done!")
        except ValueError:
            print("Please enter a valid number of goal, do not use letters or special characters!")
        except IndexError:
            print("Please enter a valid number of goal!")

    def run(self):
       while True:
           choice = input ("\nC - create, R - read, U - update, D - delete, M - mark, E - exit: ").upper().strip()
           if choice == "C":
                self.create_tasks()
           elif choice == "R":
                self.display_tasks()
           elif choice == "U":
                self.update_tasks()
           elif choice == "D":
                self.delete_tasks()
           elif choice == "M":
                self.mark_done()
           elif choice == "E":
               print("Goodbye!")
               break #End of app
app = TodoApp()
app.run()

