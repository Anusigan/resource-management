import os

class ResearchDataManager:
    def __init__(self):
        self.entries = {}
        self.filename = "research_data.txt"
    def add_entry(self):
        while True:
            e_name=input("\nEnter the experiment name: ")
            if (len(e_name)>0):
                break
            else:
                print("\nExperiment name cannot be empty!.Please give a valid name")
                
            
            while True:      
                e_date=input("\nEnter the experiment date: ")
                if(len(e_date)==10):
                    if e_date[4]!="/" or e_date[7]!="/":
                        print("\nPlease enter the date in YYYY/MM/DD format!")
                        continue
                    else:
                        break
                else:
                    print("The inputted date is invalid! ")

            
            while True:   
                res=input("\nEnter the researcher name: ")
                if (len(e_name)>0):
                    break
                else:
                    print("\nResearcher name cannot be empty!.Please give a valid name")
                    continue

            while True:
                try:
                    dp=float(input("\nEnter the data points of the experiment: "))
                    break

                except ValueError:
                    print("\nThe data points should be a numeral value! Please enter again!")
                    continue

            entry= {"e_name": e_name,
                "e_date": e_date,
                "res": res,
                "dp": dp}
            
            if e_name in entries:
                entries[e_name].append(entry)
            else:
                entries[e_name] = [entry]

            # Saving the transactions to the JSON file
            save_entries_to_file(entries,"research_data.txt")

            print("Experiment entry added Successfully!!")


            while True:
                op=input("\nDo you like to add another experiment entry? [Y/N]: ")
                op=op.capitalize()
                if op=="Y":
                    add_entry(entries)
                    break
                elif op=="N":
                    break
                else:
                    print("\nInvalid option. Please enter [Y/N]!")
                    continue



    def view_entries(self,entries):
        if entries:
        # Iterates all over each category and its transactions
            for e_name, entry_data in entries.items():
                # Printing the category name
                print(f"\nExperiment Name: {e_name}\n")
                number=1
                # Iterating through each and every transaction in the specific category
                for entry in entry_data:
                    # Printing the transaction details
                    print(f"{number}. Experiment Date: {(entry['e_date'])}\n   Researcher Name: {(entry['res'])}\n   Data point: {entry['dp']}\n")
                    number += 1
            
        else:
            # Printing a message if there is no transactions exists
            print("No experiment entries available")




    def save_entries_to_file(self,filename):
        with open(filename, "w") as file:
            for e_name, entry_data in entries.items():
                for entry in entry_data:
                    line = f"{e_name}|{entry['e_date']}|{entry['res']}|{entry['dp']}\n"
                    file.write(line)
    
        
    def load_entries_from_file(self,filename):
        entries = {}
        try:
            with open(filename, "r") as file:
                for line in file:
                    parts = line.strip().split('|')
                    if len(parts) == 4:
                        e_name, e_date, res, dp_str = parts
                        dp = float(dp_str)
                        entry = {"e_date": e_date, "res": res, "dp": dp}
                        if e_name in entries:
                            entries[e_name].append(entry)
                        else:
                            entries[e_name] = [entry]
        except FileNotFoundError:
            print("Error reading file. Ensure the file format is correct.")
        except ValueError:
            print("Entries are not valid please recheck")
            return entries
    


    
    def analyze_data(self):
        pass
    def main():
        manager = ResearchDataManager()
        manager.load_entries_from_file()
        while True:
            print("\nMenu:")
            print("1. Add a research data entry")
            print("2. View all entries")
            print("3. Analyze data")
            print("4. Save entries to file")
            print("5. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                manager.add_entry()
            elif choice == '2':
                manager.view_entries()
            elif choice == '3':
                manager.analyze_data()
            elif choice == '4':
                manager.save_entries_to_file()
            elif choice == '5':
                break
            else:
                print("Invalid choice, please try again.")
            if __name__ == "__main__":
                main()