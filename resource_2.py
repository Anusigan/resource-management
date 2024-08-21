import os

class ResearchDataManager:
    def __init__(self):
        self.entries = {}
        self.filename = "research_data.txt"

    def add_entry(self):
        while True:
            e_name = input("\nEnter the experiment name: ")
            if len(e_name) > 0:
                break
            else:
                print("\nExperiment name cannot be empty! Please provide a valid name.")

        while True:      
            e_date = input("\nEnter the experiment date (YYYY/MM/DD): ")
            if len(e_date) == 10 and e_date[4] == "/" and e_date[7] == "/":
                break
            else:
                print("\nPlease enter the date in YYYY/MM/DD format!")

        while True:   
            res = input("\nEnter the researcher name: ")
            if len(res) > 0:
                break
            else:
                print("\nResearcher name cannot be empty! Please provide a valid name.")

        while True:
            try:
                dp = float(input("\nEnter the data points of the experiment: "))
                break
            except ValueError:
                print("\nThe data points should be a numerical value! Please enter again!")

        entry = {
            "e_name": e_name,
            "e_date": e_date,
            "res": res,
            "dp": dp
        }
        
        if e_name in self.entries:
            self.entries[e_name].append(entry)
        else:
            self.entries[e_name] = [entry]

        # Saving the entries to the file
        self.save_entries_to_file()

        print("Experiment entry added successfully!")

        while True:
            op = input("\nDo you want to add another experiment entry? [Y/N]: ").capitalize()
            if op == "Y":
                self.add_entry()
                break
            elif op == "N":
                break
            else:
                print("\nInvalid option. Please enter [Y/N]!")

    def view_entries(self):
        if self.entries:
            for e_name, entry_data in self.entries.items():
                print(f"\nExperiment Name: {e_name}\n")
                for number, entry in enumerate(entry_data, start=1):
                    print(f"{number}. Experiment Date: {entry['e_date']}\n   Researcher Name: {entry['res']}\n   Data Point: {entry['dp']}\n")
        else:
            print("No experiment entries available")

    def save_entries_to_file(self):
        with open(self.filename, "w") as file:
            for e_name, entry_data in self.entries.items():
                for entry in entry_data:
                    line = f"{e_name}|{entry['e_date']}|{entry['res']}|{entry['dp']}\n"
                    file.write(line)

    def load_entries_from_file(self):
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    parts = line.strip().split('|')
                    if len(parts) == 4:
                        e_name, e_date, res, dp_str = parts
                        dp = float(dp_str)
                        entry = {"e_date": e_date, "res": res, "dp": dp}
                        if e_name in self.entries:
                            self.entries[e_name].append(entry)
                        else:
                            self.entries[e_name] = [entry]
        except FileNotFoundError:
            print("File not found. Starting with an empty dataset.")
        except ValueError:
            print("Error in file format. Please check the file contents.")

    def analyze_data(self):
        a_name = input("Enter the experiment name to be analyzed: ")
        if a_name in self.entries:
            entry_data = self.entries[a_name]
            i = len(entry_data)
            print(f"\nThe total number of tests carried out: {i}")

            print("\nThe researchers who participated in the experiment are:")
            for count, entry in enumerate(entry_data, start=1):
                print(f"{count}. {entry['res']}")

            t_dp = sum(entry['dp'] for entry in entry_data)
            print(f"\nAverage data point is: {t_dp / i:.2f}")

            data_points = sorted(entry['dp'] for entry in entry_data)
            if i % 2 != 0:
                m_dp = data_points[i // 2]
            else:
                m_dp = (data_points[i // 2 - 1] + data_points[i // 2]) / 2
            print(f"\nMedian data point is: {m_dp:.2f}")
        else:
            print("No entries available for the given experiment name.")

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
