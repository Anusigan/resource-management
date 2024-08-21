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

def add_entry(manager, tree, experiment_name_entry, date_entry, researcher_entry, data_points_entry):
    # Collect data from user input
    experiment_name = experiment_name_entry.get()
    date = date_entry.get()
    researcher = researcher_entry.get()
    data_points = data_points_entry.get()

    # Add entry to manager
    manager.add_entry(experiment_name, date, researcher, data_points)
    
    # Clear the input fields
    experiment_name_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)
    researcher_entry.delete(0, tk.END)
    data_points_entry.delete(0, tk.END)
    
    # Refresh the table view
    refresh_table(manager, tree)

def refresh_table(manager, tree):
    # Clear current table contents
    for row in tree.get_children():
        tree.delete(row)
    
    # Insert all entries into the table
    for entry in manager.get_entries():
        tree.insert("", "end", values=(entry['experiment_name'], entry['date'], entry['researcher'], entry['data_points']))

def search_entries(manager, tree, search_var):
    search = search_var.get().lower()
    filtered_entries = [entry for entry in manager.get_entries() if any(search in str(value).lower() for value in entry.values())]
    refresh_table_with_entries(tree, filtered_entries)

def refresh_table_with_entries(tree, entries):
    # Clear current table contents
    for row in tree.get_children():
        tree.delete(row)
    
    # Insert filtered entries into the table
    for entry in entries:
        tree.insert("", "end", values=(entry['experiment_name'], entry['date'], entry['researcher'], entry['data_points']))

def sort_by_column(tree, col, descending):
    # Get the data in the table
    data = [(tree.set(child, col), child) for child in tree.get_children()]

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
    root.geometry("800x500")
    
    # Style configuration
    style = ttk.Style()
    style.configure("Custom.TFrame", background="blue")
    style.configure("Treeview", font=("Times New Roman", 12), background="black")
    style.configure("Treeview.Heading", font=("Times New Roman", 14, "bold"))
    
    # Main frame
    frame = ttk.Frame(root, style="Custom.TFrame")
    frame.pack(fill=tk.BOTH, expand=True)
    
    # Scrollbars
    scrollbar_y = tk.Scrollbar(frame, orient="vertical")
    scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
    scrollbar_x = tk.Scrollbar(frame, orient="horizontal")
    scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
    
    # Treeview setup
    columns = ("experiment_name", "date", "researcher", "data_points")
    tree = ttk.Treeview(frame, columns=columns, show="headings", yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)
    tree.heading("experiment_name", text="Experiment Name", command=lambda: sort_by_column(tree, "experiment_name", False))
    tree.heading("date", text="Date", command=lambda: sort_by_column(tree, "date", False))
    tree.heading("researcher", text="Researcher", command=lambda: sort_by_column(tree, "researcher", False))
    tree.heading("data_points", text="Data Points", command=lambda: sort_by_column(tree, "data_points", False))
    
    tree.column("experiment_name", width=200, anchor="center")
    tree.column("date", width=100, anchor="center")
    tree.column("researcher", width=150, anchor="center")
    tree.column("data_points", width=200, anchor="center")
    
    tree.pack(fill=tk.BOTH, expand=True)
    
    scrollbar_y.config(command=tree.yview)
    scrollbar_x.config(command=tree.xview)
    
    # Input fields and labels
    tk.Label(frame, text="Experiment Name:", background="lightgrey").pack(pady=5)
    experiment_name_entry = tk.Entry(frame, width=50)
    experiment_name_entry.pack(pady=5)
    
    tk.Label(frame, text="Date:", background="lightgrey").pack(pady=5)
    date_entry = tk.Entry(frame, width=50)
    date_entry.pack(pady=5)
    
    tk.Label(frame, text="Researcher:", background="lightgrey").pack(pady=5)
    researcher_entry = tk.Entry(frame, width=50)
    researcher_entry.pack(pady=5)
    
    tk.Label(frame, text="Data Points:", background="lightgrey").pack(pady=5)
    data_points_entry = tk.Entry(frame, width=50)
    data_points_entry.pack(pady=5)
    
    # Add entry button
    add_button = tk.Button(frame, text="Add Entry", command=lambda: add_entry(manager, tree, experiment_name_entry, date_entry, researcher_entry, data_points_entry))
    add_button.pack(pady=10)
    
    # Search bar and button
    search_var = tk.StringVar()
    search_entry = tk.Entry(frame, textvariable=search_var, width=50)
    search_entry.pack(pady=5)
    
    search_button = tk.Button(frame, text="Search", command=lambda: search_entries(manager, tree, search_var))
    search_button.pack(pady=10)
    
    # Start the GUI loop
    root.mainloop()

if __name__ == "__main__":
    main()
