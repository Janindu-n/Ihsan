import tkinter as tk
from random import randint
from tkinter import messagebox
import math

class Person:
    def __init__(self, age=0, health_status=100, time_to_reach=24):
        self.age = age
        self.health_status = health_status
        self.time_to_reach = time_to_reach

class GridApp:
    def __init__(self, root):
        self.root = root
        self.grid_size = 0
        self.grid = []
        self.weight_grid = []  # Weight grid for clustering
        
        self.create_input_gui()
        
    def create_input_gui(self):
        self.root.configure(background='#F0F0F0')  # Set background color
        
        input_frame = tk.Frame(self.root, bg='#F0F0F0')  # Set background color
        input_frame.grid(row=0, column=0, padx=20, pady=20)  # Add padding
        
        size_label = tk.Label(input_frame, text="Grid Size (Max 6):", bg='#F0F0F0')  # Set background color
        size_label.grid(row=0, column=0, padx=(0, 10))
        self.size_entry = tk.Entry(input_frame, width=10)
        self.size_entry.grid(row=0, column=1)
        
        create_button = tk.Button(input_frame, text="Create Grid", command=self.create_grid, bg='#008080', fg='white', padx=10)  # Set background and text color
        create_button.grid(row=0, column=2, padx=(10, 0))
        
        randomize_button = tk.Button(input_frame, text="Randomize Distribution", command=self.randomize_distribution, bg='#008080', fg='white')  # Set background and text color
        randomize_button.grid(row=1, column=0, columnspan=3, pady=(10, 5))
        
        initial_clustering_button = tk.Button(input_frame, text="Initial Clustering", command=self.initial_clustering, bg='#008080', fg='white')  # Set background and text color
        initial_clustering_button.grid(row=2, column=0, columnspan=3, pady=5)
        
    def create_grid(self):
        try:
            self.grid_size = int(self.size_entry.get())
            if self.grid_size <= 0 or self.grid_size > 6:
                raise ValueError("Grid size must be between 1 and 6")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return
        
        if self.grid:
            for row in self.grid:
                for cell in row:
                    cell.grid_forget()
        
        self.grid = [[None for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.weight_grid = [[None for _ in range(2)] for _ in range(2)]  # Initialize weight grid
        
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                cell_frame = tk.Frame(self.root, width=100, height=100, borderwidth=1, relief="solid", bg='#D3D3D3')  # Set background color
                cell_frame.grid(row=i+1, column=j, padx=5, pady=5)  # Add padding
                
                age_label = tk.Label(cell_frame, text="", bg='#D3D3D3')  # Set background color
                age_label.grid(row=0, column=0)
                
                status_label = tk.Label(cell_frame, text="", bg='#D3D3D3')  # Set background color
                status_label.grid(row=1, column=0)
                
                time_to_reach_label = tk.Label(cell_frame, text="", bg='#D3D3D3')  # Set background color
                time_to_reach_label.grid(row=2, column=0)

                cell_button = tk.Button(cell_frame, text="Edit", command=lambda i=i, j=j: self.edit_person(i, j), bg='#008080', fg='white')  # Set background and text color
                cell_button.grid(row=3, column=0, pady=(5, 0))
                
                self.grid[i][j] = cell_frame
    
    def randomize_distribution(self):
        if not self.grid:
            tk.messagebox.showwarning("Warning", "Please create the grid first")
            return
        
        for row in self.grid:
            for cell in row:
                cell.grid_slaves(row=0, column=0)[0].config(text="")
                cell.grid_slaves(row=1, column=0)[0].config(text="")
                cell.grid_slaves(row=2, column=0)[0].config(text="")
                if randint(0, 1):
                    age = randint(1, 100)
                    status = randint(0, 100)
                    time_to_reach = randint(1, 24)
                    person = Person(age, status, time_to_reach)
                    age_label = cell.grid_slaves(row=0, column=0)[0]
                    age_label.config(text="Age: " + str(age))
                    status_label = cell.grid_slaves(row=1, column=0)[0]
                    status_label.config(text="Health Status: " + str(status) + "%")
                    time_to_reach_label = cell.grid_slaves(row=2, column=0)[0]
                    time_to_reach_label.config(text="Time to reach: " + str(time_to_reach) + "h")

    def initial_clustering(self):
        if not self.grid:
            messagebox.showwarning("Warning", "Please create the grid first")
            return
        
        # Calculate weights for clustering
        for i in range(2):
            for j in range(2):
                cell = self.grid[i * 3 // 2][j * 3 // 2]
                if cell:
                    weight = self.calculate_weight(i, j)
                    self.weight_grid[i][j] = weight
        
        # Display weight grid
        weight_frame = tk.Frame(self.root, bg='#F0F0F0')  # Set background color
        weight_frame.grid(row=self.grid_size + 1, column=0, columnspan=self.grid_size, pady=10)  # Add padding
        
        for i in range(2):
            for j in range(2):
                weight_label = tk.Label(weight_frame, text=f"Weight: {self.weight_grid[i][j]:.2f}", bg='#D3D3D3', width=15, height=2, relief="solid")  # Set background color
                weight_label.grid(row=i, column=j, padx=10, pady=10)  # Add padding

        
    def calculate_weight(self, i, j):
        total_value = 0.0
        num_cells = self.grid_size // 2
        for y in range(i * num_cells, (i + 1) * num_cells):
            for x in range(j * num_cells, (j + 1) * num_cells):
                person = self.get_person(x, y)
                if person:
                    sigmoid_health = self.sigmoid(person.health_status)
                    sigmoid_time = self.sigmoid(person.time_to_reach)
                    total_value += 0.8 * sigmoid_health + 0.2 * sigmoid_time
        return total_value / (num_cells ** 2)
    
    def sigmoid(self, x):
        return 1 / (1 + math.exp(-x))
    
    def get_person(self, x, y):
        cell = self.grid[y][x]
        if cell:
            age_label = cell.grid_slaves(row=0, column=0)[0].cget("text")
            status_label = cell.grid_slaves(row=1, column=0)[0].cget("text")
            time_label = cell.grid_slaves(row=2, column=0)[0].cget("text")
            if age_label and status_label and time_label:
                age = int(age_label.split(": ")[1])
                status = int(status_label.split(": ")[1].rstrip("%"))
                time = int(time_label.split(": ")[1].rstrip("h"))
                return Person(age, status, time)
        return None
        
    def edit_person(self, i, j):
        edit_window = tk.Toplevel(self.root)
        edit_window.title("Edit Person")
        
        age_label = tk.Label(edit_window, text="Age:")
        age_label.grid(row=0, column=0, padx=(10, 5), pady=(10, 5), sticky="e")
        age_entry = tk.Entry(edit_window, width=15)
        age_entry.grid(row=0, column=1, padx=(0, 10), pady=(10, 5))
        
        status_label = tk.Label(edit_window, text="Health Status (%):")
        status_label.grid(row=1, column=0, padx=(10, 5), pady=5, sticky="e")
        status_entry = tk.Entry(edit_window, width=15)
        status_entry.grid(row=1, column=1, padx=(0, 10), pady=5)
        
        time_to_reach_label = tk.Label(edit_window, text="Time to reach:")
        time_to_reach_label.grid(row=2, column=0, padx=(10, 5), pady=(5, 10), sticky="e")
        time_to_reach_entry = tk.Entry(edit_window, width=15)
        time_to_reach_entry.grid(row=2, column=1, padx=(0, 10), pady=(5, 10))

        submit_button = tk.Button(edit_window, text="Submit", command=lambda: self.update_person(i, j, age_entry.get(), status_entry.get(), time_to_reach_entry.get(), edit_window), bg='#008080', fg='white')  # Set background and text color
        submit_button.grid(row=3, column=0, columnspan=2, pady=10)
    
    def update_person(self, i, j, age, status, time_to_reach, edit_window):
        try:
            age = int(age)
            status = float(status)
            time_to_reach = int(time_to_reach)
            if status < 0 or status > 100:
                raise ValueError("Health Status must be between 0 and 100")
            if time_to_reach < 1 or time_to_reach > 24:
                raise ValueError("Time to reach must be between 1 and 24")
        except ValueError as e:
            tk.messagebox.showerror("Error", str(e))
            return
        
        age_label = self.grid[i][j].grid_slaves(row=0, column=0)[0]
        age_label.config(text="Age: " + str(age))
        
        status_label = self.grid[i][j].grid_slaves(row=1, column=0)[0]
        status_label.config(text="Health Status: " + str(status) + "%")
        
        time_to_reach_label = self.grid[i][j].grid_slaves(row=2, column=0)[0]
        time_to_reach_label.config(text="Time to reach: " + str(time_to_reach))

        edit_window.destroy()

def main():
    root = tk.Tk()
    root.title("Grid App")
    window_width = 600
    window_height = 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coordinate = (screen_width / 2) - (window_width / 2)
    y_coordinate = (screen_height / 2) - (window_height / 2)
    root.geometry(f'{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}')
    
    app = GridApp(root)
    
    root.mainloop()

if __name__ == "__main__":
    main()
