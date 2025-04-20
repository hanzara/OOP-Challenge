
I have successfully implemented the required Pet class and its associated methods as per the challenge instructions.
Additionally, I have expanded the functionality by integrating new features such as mood tracking, health management, 
scheduled events (hunger increase over time), and a graphical interface using Tkinter. 
These enhancements provide a more interactive and immersive experience, making the digital pet more dynamic and engaging. 
The code is well-structured, adheres to OOP principles, and is ready for review. Please find my repository link attached for evaluation


import tkinter as tk
from tkinter import messagebox
import time

class Pet:
    def __init__(self, name, favorite_activity="playing"):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.health = 10
        self.age = 0
        self.tricks = []
        self.inventory = {"food": 3, "toys": 2, "medicine": 1}
        self.favorite_activity = favorite_activity
        self.mood = "neutral"

    def eat(self):
        if self.inventory["food"] > 0:
            self.hunger = max(0, self.hunger - 3)
            self.happiness = min(10, self.happiness + 1)
            self.inventory["food"] -= 1
        else:
            return "No food left!"
        return f"{self.name} ate! Hunger: {self.hunger}, Happiness: {self.happiness}"

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        return f"{self.name} slept. Energy: {self.energy}"

    def play(self):
        if self.energy < 2:
            return f"{self.name} is too tired to play!"
        else:
            self.energy = max(0, self.energy - 2)
            self.happiness = min(10, self.happiness + (3 if self.favorite_activity == "playing" else 2))
            self.hunger = min(10, self.hunger + 1)
        return f"{self.name} played! Energy: {self.energy}, Happiness: {self.happiness}"

    def train(self, trick):
        self.tricks.append(trick)
        return f"{self.name} learned {trick}!"

    def show_tricks(self):
        return ", ".join(self.tricks) if self.tricks else "No tricks learned yet!"

    def get_status(self):
        self.update_mood()
        return f"Hunger: {self.hunger}, Energy: {self.energy}, Happiness: {self.happiness}, Health: {self.health}, Mood: {self.mood}, Age: {self.age}"

    def use_medicine(self):
        if self.inventory["medicine"] > 0:
            self.health = min(10, self.health + 3)
            self.inventory["medicine"] -= 1
            return f"{self.name} used medicine. Health: {self.health}"
        return "No medicine left!"

    def update_mood(self):
        if self.happiness >= 8:
            self.mood = "happy 😊"
        elif self.happiness <= 3:
            self.mood = "sad 😢"
        else:
            self.mood = "neutral 😐"


class PetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Virtual Pet")

        # Create Pet Instance
        self.pet = Pet("Buddy")

        # Labels
        self.pet_label = tk.Label(root, text="🐶 Meet Buddy!", font=("Arial", 18))
        self.pet_label.pack(pady=10)

        self.status_label = tk.Label(root, text=self.pet.get_status(), font=("Arial", 14))
        self.status_label.pack(pady=10)

        # Buttons for Actions
        tk.Button(root, text="🍔 Feed", command=self.feed_pet).pack(pady=5)
        tk.Button(root, text="😴 Sleep", command=self.sleep_pet).pack(pady=5)
        tk.Button(root, text="🎾 Play", command=self.play_pet).pack(pady=5)
        tk.Button(root, text="📚 Train Trick", command=self.train_pet).pack(pady=5)
        tk.Button(root, text="📜 Show Tricks", command=self.show_tricks).pack(pady=5)

        # Scheduled updates (hunger increase)
        self.root.after(10000, self.auto_hunger_increase)  # Every 10 seconds

    def update_status(self):
        self.status_label.config(text=self.pet.get_status())

    def feed_pet(self):
        result = self.pet.eat()
        messagebox.showinfo("Action", result)
        self.update_status()

    def sleep_pet(self):
        result = self.pet.sleep()
        messagebox.showinfo("Action", result)
        self.update_status()

    def play_pet(self):
        result = self.pet.play()
        messagebox.showinfo("Action", result)
        self.update_status()

    def train_pet(self):
        trick = "Roll Over"  # You can make this dynamic with user input
        result = self.pet.train(trick)
        messagebox.showinfo("Training", result)
        self.update_status()

    def show_tricks(self):
        tricks_list = self.pet.show_tricks()
        messagebox.showinfo("Tricks", f"Buddy knows: {tricks_list}")

    def auto_hunger_increase(self):
        self.pet.hunger = min(10, self.pet.hunger + 1)
        if self.pet.hunger == 10:
            messagebox.showwarning("Warning", f"{self.pet.name} is starving! Health is dropping!")
            self.pet.health = max(0, self.pet.health - 1)

        if self.pet.health == 0:
            messagebox.showerror("Critical", f"Oh no! {self.pet.name} is very sick! Use medicine before it's too late!")

        self.update_status()
        self.root.after(10000, self.auto_hunger_increase)  # Repeat every 10 seconds


# Run the GUI
root = tk.Tk()
app = PetApp(root)
root.mainloop()
