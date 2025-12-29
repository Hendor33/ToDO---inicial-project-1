#goal of this task is to create to-do list to increase productivity of my days and get better at Python

def todo_list():
    my_goals = []

    while True:
        choice = input("What would you like to do? C - create, R - read, U - update, D - delete: ")
        if choice == "C":
            my_goals.append(input("What is the goal?: "))
        elif choice == "R":
            print(my_goals)
        elif choice == "U":
            for index, goal in enumerate(my_goals):
                print(f"{index}, {goal}")
            update_index = int(input("Which goal you would like to update? "))
            update_goal = input("What is the new goal?")
            my_goals[update_index] = update_goal




todo_list()
