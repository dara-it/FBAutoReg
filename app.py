import tkinter as tk
from tkinter import ttk
import os

class CustomGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("darait - Facebook Automation")
        self.root.geometry("1200x800")

        # Top Section: Buttons and Options
        self.top_frame = tk.Frame(self.root, relief=tk.RIDGE, bd=2)
        self.top_frame.pack(fill=tk.X, padx=5, pady=5)

        # Main Section: Status Section
        self.status_frame = tk.Frame(self.root, relief=tk.RIDGE, bd=2)
        self.status_frame.pack(fill=tk.X, padx=5, pady=5)

        tk.Label(self.status_frame, text="Type:", font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=5)
        tk.Checkbutton(self.status_frame, text="Completed").pack(side=tk.LEFT)
        tk.Checkbutton(self.status_frame, text="No Veri").pack(side=tk.LEFT)
        tk.Checkbutton(self.status_frame, text="Veri").pack(side=tk.LEFT)
        tk.Checkbutton(self.status_frame, text="Reg").pack(side=tk.LEFT)

        # Network Options
        self.network_frame = tk.Frame(self.top_frame)
        self.network_frame.pack(side=tk.RIGHT, padx=5)

        tk.Label(self.network_frame, text="Network:").pack(side=tk.LEFT)
        tk.Radiobutton(self.network_frame, text="WiFi", value=1).pack(side=tk.LEFT)
        tk.Radiobutton(self.network_frame, text="WAN Proxy", value=2).pack(side=tk.LEFT)
        tk.Radiobutton(self.network_frame, text="ProxyFB", value=3).pack(side=tk.LEFT)

        # Main Section: Buttons and Device Area
        self.button_frame = tk.Frame(self.top_frame)
        self.button_frame.pack(fill=tk.X, pady=5)

        tk.Button(self.button_frame, text="Start", bg="green", fg="white", width=10).pack(side=tk.LEFT, padx=5)
        tk.Button(self.button_frame, text="Stop", bg="red", fg="white", width=10).pack(side=tk.LEFT, padx=5)
        tk.Button(self.button_frame, text="Reg Nick", bg="orange", fg="white", width=10).pack(side=tk.LEFT, padx=5)
        tk.Button(self.button_frame, text="Devices", bg="blue", fg="white", width=10).pack(side=tk.LEFT, padx=5)
        tk.Button(self.button_frame, text="Check", bg="purple", fg="white", width=10).pack(side=tk.LEFT, padx=5)
        tk.Button(self.button_frame, text="Update", bg="darkgrey", fg="white", width=10).pack(side=tk.LEFT, padx=5)
        tk.Button(self.button_frame, text="Load Account", bg="red", fg="white", width=10).pack(side=tk.LEFT, padx=5)

        # Left Section: Options and Checkboxes
        self.left_frame = tk.Frame(self.root, relief=tk.RIDGE, bd=2)
        self.left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)

        # Specify the folder where the files are located
        self.folder_path = "resulf"
        # Get a list of all .txt files in the folder
        self.entries = [f.replace(".txt", "") for f in os.listdir(self.folder_path) if f.endswith(".txt")]

        # Create the Combobox
        self.day = tk.StringVar()
        self.combobox = ttk.Combobox(self.left_frame, values=self.entries, textvariable=self.day)
        self.combobox.pack(anchor="w", padx=8, pady=5)

        tk.Label(self.left_frame, text="Name of Coutry", font=("Arial", 10, "bold")).pack(anchor="w")
        tk.Checkbutton(self.left_frame, text="Khmer").pack(anchor="w")
        tk.Checkbutton(self.left_frame, text="Thai").pack(anchor="w")
        tk.Checkbutton(self.left_frame, text="Vietnam").pack(anchor="w")
        tk.Checkbutton(self.left_frame, text="USA").pack(anchor="w")
        tk.Checkbutton(self.left_frame, text="Lao").pack(anchor="w")
        tk.Checkbutton(self.left_frame, text="Random").pack(anchor="w")

        tk.Label(self.left_frame, text="Friends", font=("Arial", 10, "bold")).pack(anchor="w", pady=5)
        tk.Checkbutton(self.left_frame, text="Unfriend/Cancel Request").pack(anchor="w")
        tk.Checkbutton(self.left_frame, text="Accept Friend Requests").pack(anchor="w")
        tk.Checkbutton(self.left_frame, text="Add Friend Suggestions").pack(anchor="w")

        tk.Label(self.left_frame, text="Groups", font=("Arial", 10, "bold")).pack(anchor="w", pady=5)
        tk.Checkbutton(self.left_frame, text="Add Group by UID").pack(anchor="w")
        tk.Checkbutton(self.left_frame, text="Find Group Free Approve").pack(anchor="w")

        tk.Label(self.left_frame, text="Profile", font=("Arial", 10, "bold")).pack(anchor="w", pady=5)
        tk.Checkbutton(self.left_frame, text="Change Cover").pack(anchor="w")
        tk.Checkbutton(self.left_frame, text="Change Avatar").pack(anchor="w")
        tk.Checkbutton(self.left_frame, text="Change Info").pack(anchor="w")
        tk.Checkbutton(self.left_frame, text="Login with Timer").pack(anchor="w")
        tk.Checkbutton(self.left_frame, text="Public Posts").pack(anchor="w")
        tk.Checkbutton(self.left_frame, text="Info and Birthday").pack(anchor="w")
        tk.Checkbutton(self.left_frame, text="Import Contact").pack(anchor="w")
        tk.Checkbutton(self.left_frame, text="Change Pass").pack(anchor="w")
        tk.Checkbutton(self.left_frame, text="Change Email").pack(anchor="w")
        tk.Checkbutton(self.left_frame, text="Remove PhonNumber").pack(anchor="w")
        tk.Checkbutton(self.left_frame, text="Report").pack(anchor="w")
        tk.Checkbutton(self.left_frame, text="Create Page").pack(anchor="w")
        
        # Device Table
        self.device_table = ttk.Treeview(self.root, columns=("No", "Name", "UID", "Password", "2Fa", "Status"), show="headings")
        self.device_table.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.device_table.heading("No", text="No")
        self.device_table.heading("Name", text="Name")
        self.device_table.heading("UID", text="UID")
        self.device_table.heading("Password", text="Password")
        self.device_table.heading("2Fa", text="2Fa")
        self.device_table.heading("Status", text="Status")

        # Status label
        self.status_label = tk.Label(self.status_frame, text="Status: Waiting for file selection", font=("Arial", 10, "bold"))
        self.status_label.pack(side=tk.LEFT, padx=5)

        # Bind the combobox to the change file function
        self.combobox.bind("<<ComboboxSelected>>", self.load_file_data)

        # Initial call to load the first file data (if any)
        if self.entries:
            self.load_file_data(None)

        # Set up auto-refresh every 5 seconds (5000 milliseconds)
        self.auto_refresh()

    def load_file_data(self, event=None):
        """Load data from the selected file and populate the table"""
        # Track the previous number of rows before updating the table
        previous_row_count = len(self.device_table.get_children())

        # Clear the current table to ensure it is updated
        for row in self.device_table.get_children():
            self.device_table.delete(row)

        # Get the selected file name
        selected_file = self.day.get()
        file_path = os.path.join(self.folder_path, f"{selected_file}.txt")

        if os.path.exists(file_path):
            row_data = []

            # Read the file and populate row_data
            with open(file_path, 'r') as file:
                for line in file:
                    parts = line.split('|')
                    if len(parts) >= 3:
                        name = parts[0].strip()
                        uid = parts[1].strip()
                        password = parts[2].strip()
                        row_data.append((name, uid, password, "No 2Fa", "Live"))

            # Insert data into the table
            for index, data in enumerate(row_data, start=1):
                self.device_table.insert("", "end", values=(index, *data))

            # Update the status message
            self.status_label.config(text=f"Status: Loaded {len(row_data)} entries from {selected_file}.txt")

            # If new data is added, scroll to the bottom
            if len(self.device_table.get_children()) > previous_row_count:
                self.device_table.yview_moveto(1)  # Scroll to the bottom
        else:
            self.status_label.config(text="Status: File not found.")
            print(f"File {file_path} not found.")

    def auto_refresh(self):
        """Automatically refresh the table every 5 seconds."""
        # Reload data to check if new entries have been added
        self.load_file_data()  # Refresh the table with the latest data
        self.root.after(5000, self.auto_refresh)  # Re-run this method after 5000 ms (5 seconds)

if __name__ == "__main__":
    root = tk.Tk()
    app = CustomGUI(root)
    root.mainloop()
