import tkinter as tk
from tkinter import ttk, messagebox
import random
from datetime import datetime

class ModernNameSelector:
    def __init__(self, root):
        self.root = root
        self.names = []
        self.selected_history = []
        
        # Configure the main window
        self.root.title("Modern Name Selector")
        self.root.geometry("800x700")
        self.root.configure(bg='#1a1a2e')
        self.root.resizable(True, True)
        
        # Configure style
        self.setup_styles()
        
        # Create main container
        self.main_frame = tk.Frame(root, bg='#1a1a2e')
        self.main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        self.create_widgets()
        
    def setup_styles(self):
        """Configure modern styling for ttk widgets"""
        style = ttk.Style()
        
        # Configure button style
        style.configure('Modern.TButton',
                       background='#4a69bd',
                       foreground='white',
                       borderwidth=0,
                       focuscolor='none',
                       font=('Arial', 10, 'bold'))
        
        style.map('Modern.TButton',
                  background=[('active', '#3c5aa6'),
                            ('pressed', '#2f4788')])
        
        # Configure entry style
        style.configure('Modern.TEntry',
                       fieldbackground='#2d2d44',
                       foreground='white',
                       borderwidth=2,
                       insertcolor='white',
                       font=('Arial', 11))
        
        # Configure frame style
        style.configure('Modern.TFrame',
                       background='#1a1a2e',
                       relief='flat')
        
    def create_widgets(self):
        """Create and arrange all GUI widgets"""
        
        # Title
        title_label = tk.Label(self.main_frame, 
                              text="🎯 Modern Name Selector",
                              font=('Arial', 24, 'bold'),
                              fg='#4a69bd',
                              bg='#1a1a2e')
        title_label.pack(pady=(0, 30))
        
        # Input section
        input_frame = tk.Frame(self.main_frame, bg='#1a1a2e')
        input_frame.pack(fill='x', pady=(0, 20))
        
        # Name entry with modern styling
        entry_label = tk.Label(input_frame,
                              text="Enter Names:",
                              font=('Arial', 14, 'bold'),
                              fg='white',
                              bg='#1a1a2e')
        entry_label.pack(anchor='w', pady=(0, 5))
        
        self.name_entry = tk.Entry(input_frame,
                                  font=('Arial', 12),
                                  bg='#2d2d44',
                                  fg='white',
                                  insertbackground='white',
                                  relief='flat',
                                  bd=10)
        self.name_entry.pack(fill='x', ipady=8, pady=(0, 10))
        self.name_entry.bind('<Return>', lambda e: self.add_name())
        
        # Button frame
        button_frame = tk.Frame(input_frame, bg='#1a1a2e')
        button_frame.pack(fill='x')
        
        self.add_btn = self.create_modern_button(button_frame, "➕ Add Name", self.add_name, '#27ae60')
        self.add_btn.pack(side='left', padx=(0, 10))
        
        self.select_btn = self.create_modern_button(button_frame, "🎲 Select Random", self.select_random_name, '#e74c3c')
        self.select_btn.pack(side='left', padx=(0, 10))
        
        self.clear_btn = self.create_modern_button(button_frame, "🗑️ Clear All", self.clear_all, '#f39c12')
        self.clear_btn.pack(side='left')
        
        # Names display section
        display_frame = tk.Frame(self.main_frame, bg='#1a1a2e')
        display_frame.pack(fill='both', expand=True, pady=(20, 0))
        
        # Current names section
        names_label = tk.Label(display_frame,
                              text="📝 Current Names:",
                              font=('Arial', 16, 'bold'),
                              fg='white',
                              bg='#1a1a2e')
        names_label.pack(anchor='w', pady=(0, 10))
        
        # Names listbox with scrollbar
        listbox_frame = tk.Frame(display_frame, bg='#1a1a2e')
        listbox_frame.pack(fill='both', expand=True, pady=(0, 20))
        
        self.names_listbox = tk.Listbox(listbox_frame,
                                       font=('Arial', 11),
                                       bg='#2d2d44',
                                       fg='white',
                                       selectbackground='#4a69bd',
                                       selectforeground='white',
                                       relief='flat',
                                       bd=0,
                                       highlightthickness=0)
        
        scrollbar = tk.Scrollbar(listbox_frame, orient='vertical', command=self.names_listbox.yview)
        self.names_listbox.configure(yscrollcommand=scrollbar.set)
        
        self.names_listbox.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        # Selected name display
        self.result_frame = tk.Frame(display_frame, bg='#16213e', relief='flat', bd=2)
        self.result_frame.pack(fill='x', pady=(0, 20))
        
        self.result_label = tk.Label(self.result_frame,
                                    text="🎯 Selected Name Will Appear Here",
                                    font=('Arial', 18, 'bold'),
                                    fg='#4a69bd',
                                    bg='#16213e',
                                    pady=20)
        self.result_label.pack()
        
        # History section
        history_label = tk.Label(display_frame,
                                text="📚 Selection History:",
                                font=('Arial', 14, 'bold'),
                                fg='white',
                                bg='#1a1a2e')
        history_label.pack(anchor='w', pady=(0, 10))
        
        self.history_text = tk.Text(display_frame,
                                   height=6,
                                   font=('Arial', 10),
                                   bg='#2d2d44',
                                   fg='#cccccc',
                                   relief='flat',
                                   bd=0,
                                   wrap='word',
                                   state='disabled')
        self.history_text.pack(fill='x')
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready to add names...")
        
        status_bar = tk.Label(self.main_frame,
                             textvariable=self.status_var,
                             font=('Arial', 9),
                             fg='#888888',
                             bg='#1a1a2e',
                             anchor='w')
        status_bar.pack(fill='x', pady=(10, 0))
        
    def create_modern_button(self, parent, text, command, color):
        """Create a modern styled button"""
        button = tk.Button(parent,
                          text=text,
                          command=command,
                          font=('Arial', 10, 'bold'),
                          bg=color,
                          fg='white',
                          relief='flat',
                          bd=0,
                          padx=20,
                          pady=8,
                          cursor='hand2')
        
        # Add hover effects
        def on_enter(e):
            button.configure(bg=self.darken_color(color))
            
        def on_leave(e):
            button.configure(bg=color)
            
        button.bind('<Enter>', on_enter)
        button.bind('<Leave>', on_leave)
        
        return button
    
    def darken_color(self, color):
        """Darken a hex color for hover effect"""
        color_map = {
            '#27ae60': '#219a52',
            '#e74c3c': '#c0392b',
            '#f39c12': '#d68910'
        }
        return color_map.get(color, color)
    
    def add_name(self):
        """Add a name to the list"""
        name = self.name_entry.get().strip()
        if name:
            if name not in self.names:
                self.names.append(name)
                self.names_listbox.insert(tk.END, f"• {name}")
                self.name_entry.delete(0, tk.END)
                self.status_var.set(f"Added '{name}' - Total: {len(self.names)} names")
                
                # Auto-scroll to bottom
                self.names_listbox.see(tk.END)
            else:
                messagebox.showwarning("Duplicate Name", f"'{name}' is already in the list!")
                self.status_var.set("Name already exists!")
        else:
            messagebox.showwarning("Empty Name", "Please enter a valid name!")
            self.status_var.set("Please enter a name...")
    
    def select_random_name(self):
        """Select a random name from the list"""
        if not self.names:
            messagebox.showwarning("No Names", "Please add some names first!")
            self.status_var.set("No names available for selection")
            return
        
        # Animate the selection
        self.animate_selection()
        
    def animate_selection(self):
        """Create a selection animation effect"""
        if not self.names:
            return
            
        # Disable button during animation
        self.select_btn.configure(state='disabled')
        
        # Animation parameters
        animation_steps = 15
        current_step = [0]
        
        def animate_step():
            if current_step[0] < animation_steps:
                # Show random name during animation
                temp_name = random.choice(self.names)
                self.result_label.configure(text=f"🎲 {temp_name}")
                current_step[0] += 1
                self.root.after(100, animate_step)
            else:
                # Final selection
                selected_name = random.choice(self.names)
                self.result_label.configure(text=f"🎯 {selected_name}")
                
                # Add to history
                timestamp = datetime.now().strftime("%H:%M:%S")
                self.selected_history.append(f"[{timestamp}] {selected_name}")
                
                # Update history display
                self.update_history_display()
                
                # Update status
                self.status_var.set(f"Selected: {selected_name}")
                
                # Re-enable button
                self.select_btn.configure(state='normal')
                
        animate_step()
    
    def update_history_display(self):
        """Update the history text widget"""
        self.history_text.configure(state='normal')
        self.history_text.delete(1.0, tk.END)
        
        if self.selected_history:
            # Show last 10 selections
            recent_history = self.selected_history[-10:]
            for entry in recent_history:
                self.history_text.insert(tk.END, f"{entry}\n")
        else:
            self.history_text.insert(tk.END, "No selections yet...")
            
        self.history_text.configure(state='disabled')
        self.history_text.see(tk.END)
    
    def clear_all(self):
        """Clear all names and history"""
        if messagebox.askyesno("Clear All", "Are you sure you want to clear all names and history?"):
            self.names.clear()
            self.selected_history.clear()
            self.names_listbox.delete(0, tk.END)
            self.result_label.configure(text="🎯 Selected Name Will Appear Here")
            self.update_history_display()
            self.status_var.set("All data cleared - Ready to add names...")

def main():
    root = tk.Tk()
    app = ModernNameSelector(root)
    
    # Center the window on screen
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
    y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
    root.geometry(f"+{x}+{y}")
    
    root.mainloop()

if __name__ == "__main__":
    main()