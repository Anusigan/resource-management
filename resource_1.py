import os
import json

entries={}

# Function to add a research data entry
def add_entry(entries):
    while True:
      e_name=input("\nEnter the experiment name: ")
      if (len(e_name)>0):
          break
      else:
          print("\nExperiment name cannot be empty!.Please give a valid name")
          continue
      
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

    entry= {"experiment_name": e_name,
        "experiment_date": e_date,
        "experiment_researcher": res,
        "data_point": dp}
    if e_name in entries:
        entries[e_name].append(entry)
    else:
        entries[e_name] = [entry]

    # Saving the transactions to the JSON file
    save_transactions()




   

# Function to view all research data entries
def view_entries(entries):
    if entries.length()>0:
        print('-' *90)
        print(f"{'\nExperiment Name':<25} {'Experiment Date':<25} {'Researcher Name':25} {'Data Points':<25}")
        print('-' *90)
        for entry in entries:
            print(f"{entry['experiment_name']:<25} {entry['experiment_date']:<25} {entry['experiment_researcher']:<25} {entry['data_point']:<10.2f}")
    else:
        print("\nNo entries to view")

# Function to save entries to a text file
def save_entries_to_file(entries, filename):
     with open(filename, "w") as file:
        # Write the transactions dictionary to the file using json.dump()
        json.dump(entries, file, indent=2)
   

# Function to load entries from a text file
def load_entries_from_file(filename):
    global entries
    try:
        with open("transactions.json", "r") as file:
            transactions = json.load(file)
    except FileNotFoundError:
        transactions = {}
 

# Function to perform data analysis
def analyze_data(entries):
    pass
# Main function to interact with the user
def main():
    filename = "research_data.txt"
    entries = load_entries_from_file(filename)




while True:
    print("\nMenu:")
    print("1. Add a research data entry")
    print("2. View all entries")
    print("3. Analyze data")
    print("4. Save entries to file")
    print("5. Exit")
    choice = input("Enter your choice: ")



    if choice == '1':
        add_entry(entries)
    elif choice == '2':
        view_entries(entries)
    elif choice == '3':
       analyze_data(entries)
    elif choice == '4':
        save_entries_to_file(entries, filename)
    elif choice == '5':
        break
    else:
        print("Invalid choice, please try again.")



if __name__ == "__main__":
   main()