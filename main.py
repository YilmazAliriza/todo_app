import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("The time is bellow:")
print("It's",now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        task = user_action[4:] + "\n"

        to_do_list = functions.get_todos()

        to_do_list.append(task)

        functions.write_todos(to_do_list)

    elif user_action.startswith('show'):

        to_do_list = functions.get_todos()

        for number, to_do in enumerate(to_do_list):
            print("{}. {}".format(number + 1, to_do.capitalize().strip("\n")))

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number -= 1
            new_task = input('Enter new ToDo: ') + "\n"

            to_do_list = functions.get_todos()

            to_do_list[number] = new_task

            functions.write_todos(to_do_list)

        except ValueError:
            print('Your command is not valid.')
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            to_do_list = functions.get_todos()

            index = number - 1
            toDo_to_remove = to_do_list[index].strip("\n")
            to_do_list.pop(index)

            functions.write_todos(to_do_list)

            message = f"***ToDo {toDo_to_remove} was removed from the list***"
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid.")

print("See You!")
