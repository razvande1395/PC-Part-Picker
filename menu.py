import os


from commands import Commands


print()
print("Welcome to the Bootleg PC Part Picker! \n")

menu = {}
menu["1."] = "Choose and view a specific list"
menu["2."] = "Create a list of components"
menu["3."] = "Upgrade components from a list"
menu["4."] = "Delete a list"
menu["5."] = "Show all available lists"
menu["6."] = "Delete all lists from the current folder"
menu["7."] = "Exit menu"

command = Commands()

def menu_function(menu: dict) -> None:

    while True:
        options = list(menu.keys())
        options.sort()

        for entry in options: 
            print(entry, menu[entry])
        
        print()
        selection = input("Please select an option: ")

        if selection == "1":
            list_name = input("Please type the name of the list you want to view: ")
            
            if ".csv" not in list_name:
                list_name += ".csv"

            if os.path.exists(list_name):
                command.view_list(list_name)
            else:
                print("The specified file does not exist. \n")
                
        elif selection == "2":
            command.create_list()

        elif selection == "3":
            upgrade_name = input("Please select the list you wish to improve: ")
            
            if ".csv" not in upgrade_name:
                upgrade_name += ".csv"

            if os.path.exists(upgrade_name):
                command.upgrade_list(upgrade_name)
            else:
                print("The specified file does not exist. \n")

        elif selection == "4":
            filename = input("Please type in the name of the file you want to delete: ")
            command.delete_file(filename)

        elif selection == "5":
            command.show_files()

        elif selection == "6":
            command.delete_all_lists()

        elif selection == "7":
            break
        
        else:
            print("Please select a valid option!")
            print()


menu_function(menu)