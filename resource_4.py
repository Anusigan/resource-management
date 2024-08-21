import tkinter as tk
from tkinter import ttk

class ResearchDataManager:
    def __init__(self):
        self.entries = []

    def add_entry(self, experiment_name, date, researcher, data_points):
        entry = {
            'experiment_name': experiment_name,
            'date': date,
            'researcher': researcher,
            'data_points': data_points
        }
        self.entries.append(entry)

    def get_entries(self):
        return self.entries


def add_entry(manager, tree):
    # Collect data from user input
    experiment_name = input("Enter experiment name: ")
    date = input("Enter date: ")
    researcher = input("Enter researcher: ")
    data_points = input("Enter data points: ")

    # Add entry to manager
    manager.add_entry(experiment_name, date, researcher, data_points)
    
    # Refresh the table view
    refresh_table(manager, tree)

def refresh_table(manager, tree):
    # Clear current table contents
    for row in tree.get_children():
        tree.delete(row)
    
    # Insert all entries into the table
    for entry in manager.get_entries():
        tree.insert("", "end", values=(entry['experiment_name'], entry['date'], entry['researcher'], entry['data_points']))


def sort_by_column(tree, col, descending):
    # Get the data in the table
    data = [(tree.set(child, col), child) for child in tree.get_children('')]

    # Sort the data
    data.sort(reverse=descending)
    
    # Rearrange the items in sorted positions
    for i, item in enumerate(data):
        tree.move(item[1], '', i)
    
    # Reverse sort next time
    tree.heading(col, command=lambda: sort_by_column(tree, col, not descending))


def main():
    manager = ResearchDataManager()
    root = tk.Tk()
    root.title("Research Data Manager")

    # Table setup
    columns = ("experiment_name", "date", "researcher", "data_points")
    tree = ttk.Treeview(root, columns=columns, show="headings")
    tree.heading("experiment_name", text="Experiment Name", command=lambda: sort_by_column(tree, "experiment_name", False))
    tree.heading("date", text="Date", command=lambda: sort_by_column(tree, "date", False))
    tree.heading("researcher", text="Researcher", command=lambda: sort_by_column(tree, "researcher", False))
    tree.heading("data_points", text="Data Points", command=lambda: sort_by_column(tree, "data_points", False))
    
    tree.pack(fill=tk.BOTH, expand=True)

    # Add entry button
    add_button = tk.Button(root, text="Add Entry", command=lambda: add_entry(manager, tree))
    add_button.pack()

    # Start the GUI loop
    root.mainloop()


if __name__ == "__main__":
    main()
