#goal of this task is to create to-do list to increase productivity of my days and get better at Python
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
        try:
            with open("tasks.txt", "r", encoding="utf-8") as file:
                # přečteme řádky a zbavíme se neviditelných znaků \n na konci
                self.my_goals = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            # Pokud soubor ještě neexistuje (první spuštění), nic se neděje
            self.my_goals = []

    def save_tasks(self):
        with open("tasks.txt", "w", encoding="utf-8") as file:
            for goal in self.my_goals:
                file.write(goal + "\n")

    def create_tasks(self):
        new_goal = input("What is the new goal?: ").strip()
        if new_goal:
            self.my_goals.append(new_goal)
            self.save_tasks()
            print("Goal added!")
        else:
            print("Error: Empty goal can't be added!")
    def display_tasks(self):
        for index, goal in enumerate(self.my_goals, start=1):  # Start = 1 means that first task is going to have number one but index is still the same which has to be handled
            print(f"{index}) {goal}")
    def update_tasks(self):
        for index, goal in enumerate(self.my_goals, start=1):
            print(f"{index}, {goal}")
        try:
            update_index = int(input("Which number of goal you would like to update? ")) - 1  # That final -1 is to handle the index X position problem
            test_exists = self.my_goals[update_index]  # check number of goal whether it exists

            update_goal = input("What is the new goal?: ")
            self.my_goals[update_index] = update_goal
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
            print(f"Goal {deleted_goal} was successfully deleted!")
            self.save_tasks()
        except ValueError:
            print("Nothing was deleted! Please enter a valid number!")
        except IndexError:
            print("Nothing was deleted! Please enter a valid number of goal!")

    def run(self):
       while True:
           choice = input ("\nC - create, R - read, U - update, D - delete, E - exit: ").upper().strip()
           if choice == "C":
                self.create_tasks()
           elif choice == "R":
                self.display_tasks()
           elif choice == "U":
                self.update_tasks()
           elif choice == "D":
                self.delete_tasks()
           elif choice == "E":
               print("Goodbye!")
               break #End of app
app = TodoApp()
app.run()

