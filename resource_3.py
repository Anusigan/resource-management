import avro.schema
import avro.io
import os
import io


class ResearchDataManager:
    def __init__(self):
        self.entries = {}
        self.filename = "research_data.avro"
        schema_file = "research_data_schema.avsc"

        # Attempt to load the schema file with error handling
        try:
            if not os.path.exists(schema_file):
                raise FileNotFoundError(f"Schema file '{schema_file}' not found.")
            
            with open(schema_file, "r") as file:
                self.schema = avro.schema.Parse(file.read())
            print(f"Schema '{schema_file}' loaded successfully.")
            
        except FileNotFoundError as e:
            print(e)
            # Provide a correctly formatted JSON as a fallback
            schema_json = '''
            {
                "type": "record",
                "name": "Experiment",
                "fields": [
                    {"name": "e_name", "type": "string"},
                    {"name": "e_date", "type": "string"},
                    {"name": "res", "type": "string"},
                    {"name": "dp", "type": "float"}
                ]
            }
            '''
            self.schema = avro.schema.Parse(schema_json)
            print("Using placeholder schema instead.")
        
        except Exception as e:
            print(f"An error occurred while loading the schema: {e}")
            raise
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

    def view_entries(self):
        if self.entries:
            for e_name, entry_data in self.entries.items():
                print(f"\nExperiment Name: {e_name}\n")
                for number, entry in enumerate(entry_data, start=1):
                    print(f"{number}. Experiment Date: {entry['e_date']}\n   Researcher Name: {entry['res']}\n   Data Point: {entry['dp']}\n")
        else:
            print("No experiment entries available")

    def save_entries_to_file(self):
        with open(self.filename, "wb") as file:
            writer = avro.io.DatumWriter(self.schema)
            for e_name, entry_data in self.entries.items():
                for entry in entry_data:
                    datum = {
                        "e_name": entry["e_name"],
                        "e_date": entry["e_date"],
                        "res": entry["res"],
                        "dp": entry["dp"]
                    }
                    bytes_writer = io.BytesIO()
                    encoder = avro.io.BinaryEncoder(bytes_writer)
                    writer.write(datum, encoder)
                    raw_bytes = bytes_writer.getvalue()
                    file.write(raw_bytes)

    def load_entries_from_file(self):
        try:
            with open(self.filename, "rb") as file:
                reader = avro.io.DatumReader(self.schema)
                while True:
                    try:
                        bytes_reader = io.BytesIO(file.read())
                        decoder = avro.io.BinaryDecoder(bytes_reader)
                        datum = reader.read(decoder)
                        entry = {
                            "e_date": datum["e_date"],
                            "res": datum["res"],
                            "dp": datum["dp"]
                        }
                        e_name = datum["e_name"]
                        if e_name in self.entries:
                            self.entries[e_name].append(entry)
                        else:
                            self.entries[e_name] = [entry]
                    except EOFError:
                        break
        except FileNotFoundError:
            print("File not found. Starting with an empty dataset.")
        except ValueError:
            print("Error in file format. Please check the file contents.")

    def analyze_data(self):
        a_name = input("\nEnter the experiment name to be analyzed: ")
        if a_name in self.entries:
            entry_data = self.entries[a_name]
            i = len(entry_data)
            print(f"\nThe total number of tests carried out: {i}")

            unique_researchers = set(entry['res'] for entry in entry_data)
            print("\nThe researchers who participated in the experiment are:")
            for count, researcher in enumerate(unique_researchers, start=1):
                print(f"{count}. {researcher}")

            t_dp = sum(entry['dp'] for entry in entry_data)
            print(f"\nAverage data point is: {t_dp / i:.2f}")

            data_points = sorted(entry['dp'] for entry in entry_data)
            if i % 2 != 0:
                m_dp = data_points[i // 2]
            else:
                m_dp = (data_points[i // 2 - 1] + data_points[i // 2]) / 2
            print(f"Median data point is: {m_dp:.2f}")
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
