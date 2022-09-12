import glob
import os
import csv



CPU = ["Intel Core i3-12100", "Ryzen 5 5600X", "Intel Core i7-12700K", "Intel Core i9-12900KS", "Ryzen 7 5800X3D"]
RAM = ["8GB DDR4", "16GB DDR4", "32GB DDR4", "64GB DDR4", "128GB DDR4"]
GPU = ["RX 6400", "RTX 3050", "RX 6600XT", "RTX 3070", "RX 6800XT"]
SSD = ["120GB SSD", "256GB SSD", "512GB SSD", "1TB SSD", "2TB SSD"]


class Commands(): 
    """quality of life when importing the commands to another module"""
    

    def view_list(self, file_name: str) -> None:
        
        with open(file_name, "r") as f:
            
            csvreader = csv.reader(f)
            header = next(csvreader)
            components = next(csvreader)
            
        for i in range(len(header)):
            print(f"{header[i]}: {components[i]}")

        print()


    def show_files(self) -> None:

        csv_list = glob.glob("*.csv")
        print(f"Here are the available component lists: {csv_list} \n")
    
      
    def delete_file(self, file_name: str) -> None:

        if ".csv" not in file_name:
            file_name += ".csv"

        if os.path.exists(file_name):
            os.remove(file_name)
            print("The file was found and removed! \n")
        else:
            print("File not found! \n")


    def create_list(self) -> None:
       
        header = ["CPU", "RAM", "Video Card", "Storage", "Motherboard"]
        component_list = []
        hint = "(Type in its position in the list)"    
       
        cpu_choice = int(input(f"Please pick a CPU from the following list: {CPU} {hint} "))
        component_list.append(CPU[cpu_choice - 1])
       
        ram_choice = int(input(f"Please pick a RAM value from the following list: {RAM} {hint} "))
        component_list.append(RAM[ram_choice - 1])
       
        gpu_choice = int(input(f"Please pick a video card from the list: {GPU} {hint} "))
        component_list.append(GPU[gpu_choice - 1])

        ssd_choice = int(input(f"Please pick a storage unit from the list: {SSD} {hint} "))
        component_list.append(SSD[ssd_choice - 1])

        mobo_list = ["MSI B550 Tomahawk Wi-Fi", "MSI MAG Z690 Tomahawk Wi-Fi"]
        
        if "Ryzen" in component_list[0]:
            component_list.append(mobo_list[0])
        else:
            component_list.append(mobo_list[1])

        created_list_name = input("Please insert the name of the list you've created: ")
        created_list_name += ".csv"
        print()
        print(f"Congratulations, you're now the proud owner of these components: {component_list} \n")

        with open(created_list_name, 'w', newline = "") as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(header)
            csv_writer.writerow(component_list)

    
    def upgrade_list(self, list_name: str) -> None:

        mobo_list = ["MSI B550 Tomahawk Wi-Fi", "MSI MAG Z690 Tomahawk Wi-Fi"]
        upgradable_components = ["CPU", "RAM", "Video Card", "SSD"]
        hint = "(Type in the position of the component you wish to improve)"

        upgradable = True

        with open(list_name, 'r') as f:
            csvreader = csv.reader(f)
            header = next(csvreader)
            components = next(csvreader)
            
        option = int(input(f"Please select which component you'd like to upgrade: {upgradable_components} {hint} "))
        
        if option == 1:
            if CPU.index(components[0]) < 4:
                new_cpu = CPU[CPU.index(components[0]) + 1]
                components[0] = new_cpu
            else:
                print("You already own the best CPU in the list.")
                upgradable = False

        elif option == 2:
            if RAM.index(components[1]) < 4:
                new_ram = RAM[RAM.index(components[1]) + 1]
                components[1] = new_ram
            else: 
                print("You already own the highest RAM quantity available.")
                upgradable = False

        elif option == 3:
            if GPU.index(components[2]) < 4:
                new_gpu = GPU[GPU.index(components[2]) + 1]
                components[2] = new_gpu
            else: 
                print("You already own the strongest available video card.")
                upgradable = False
            
        elif option == 4:
            new_storage = SSD[int(input(f"Please select how much storage you wish to add: {SSD} {hint} ")) - 1]
            components[3] = components[3] + " + " + new_storage

        else:
            print("Invalid option, please select a valid position.")
        
        if "Ryzen" in components[0]:
            components[4] = mobo_list[0]
        else:
            components[4] = mobo_list[1]

        if upgradable:
            print(f"Here's your new list: {components} \n")
        else:
            print("Your component list hasn't been modified. \n")

        with open(list_name, 'w', newline = "") as f:
            csvwriter = csv.writer(f)
            csvwriter.writerow(header)
            csvwriter.writerow(components)

    
    def delete_all_lists(self) -> None:

        current_dir = os.getcwd()
        list_for_deletion = glob.glob(os.path.join(current_dir, "*.txt"))

        user_prompt = input("Are you sure you want to delete all the lists in this directory? Y/N \n")

        if user_prompt in "yYYesYESyes":    
            for f in list_for_deletion:
                os.remove(f)
            print("All the items have been deleted. Better hope you don't need them in the future, because I've not implemented backups. \n")
        
