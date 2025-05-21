import tkinter as tk
from tkinter import ttk
import random
import requests
from io import BytesIO
from PIL import Image, ImageTk
from playsound import playsound
import threading

# ---------- Dice Setup ----------
dice_types = {
    "d4": 4,
    "d6": 6,
    "d8": 8,
    "d10": 10,
    "d12": 12,
    "d20": 20,
    "d100": 100
}

# Replace this with any working image URL

SOUND_FILE = "dice-roll.mp3"  # Make sure this file exists in the same folder or give full path

# ---------- GUI App ----------
class DiceRollerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎲 Dice Roller")
        self.root.geometry("420x500")
        self.root.configure(bg="#f2f2f2")
        
        self.load_dice_image()
        self.create_widgets()

    def load_dice_image(self):
        try:
            local_path = "dice.jpg"  # Or use full path like "C:/images/dice.png"   # Feel free to change the image or make it dynamic
            pil_image = Image.open(local_path).resize((100, 100),  Image.Resampling.LANCZOS)
            self.dice_image = ImageTk.PhotoImage(pil_image)
        except Exception as e:
            print("Error loading local dice image:", e)
            self.dice_image = None


    def create_widgets(self):
        style = ttk.Style()
        style.configure("TLabel", background="#f2f2f2", font=("Helvetica", 12))
        style.configure("TButton", font=("Helvetica", 12), padding=6)
        style.configure("TCombobox", font=("Helvetica", 12))
        style.configure("TSpinbox", font=("Helvetica", 12))

        title = ttk.Label(self.root, text="🎲 Dice Roller", font=("Helvetica", 18, "bold"), background="#f2f2f2")
        title.pack(pady=10)

        if self.dice_image:
            self.image_label = ttk.Label(self.root, image=self.dice_image)
            self.image_label.pack()

        # Dice type selection
        frame1 = ttk.Frame(self.root)
        frame1.pack(pady=10)
        ttk.Label(frame1, text="Select Dice Type:").grid(row=0, column=0, padx=5)
        self.dice_choice = ttk.Combobox(frame1, values=list(dice_types.keys()), state="readonly", width=8)
        self.dice_choice.set("d6")
        self.dice_choice.grid(row=0, column=1)

        # Number of rolls
        frame2 = ttk.Frame(self.root)
        frame2.pack(pady=10)
        ttk.Label(frame2, text="Number of Rolls:").grid(row=0, column=0, padx=5)
        self.roll_count = ttk.Spinbox(frame2, from_=1, to=10, width=5)
        self.roll_count.set(1)
        self.roll_count.grid(row=0, column=1)

        # Roll Button
        self.roll_button = ttk.Button(self.root, text="Roll Dice", command=self.roll_dice)
        self.roll_button.pack(pady=15)

        # Result Display
        self.result_text = tk.Text(self.root, height=10, width=45, font=("Courier", 10), bg="#fff", wrap="word", borderwidth=2, relief="sunken")
        self.result_text.pack(padx=10, pady=10)

    def play_sound(self):
        try:
            playsound(SOUND_FILE)
        except Exception as e:
            print("Sound error:", e)

    def roll_dice(self):
        self.result_text.delete("1.0", tk.END)

        dice = self.dice_choice.get()
        try:
            count = int(self.roll_count.get())
        except ValueError:
            self.result_text.insert(tk.END, "Invalid roll count.\n")
            return

        # Play sound in separate thread to avoid blocking UI
        threading.Thread(target=self.play_sound, daemon=True).start()

        sides = dice_types[dice]
        rolls = [random.randint(1, sides) for _ in range(count)]
        total = sum(rolls)

        self.result_text.insert(tk.END, f"🎲 Rolling {dice} {count} time(s)...\n")
        for i, roll in enumerate(rolls, start=1):
            self.result_text.insert(tk.END, f"Roll {i}: {roll}\n")

        self.result_text.insert(tk.END, f"\nAll Rolls: {rolls}\n")
        self.result_text.insert(tk.END, f"Sum of Rolls: {total}\n")


# ---------- Run App ----------
if __name__ == "__main__":
    root = tk.Tk()
    app = DiceRollerApp(root)
    root.mainloop()
