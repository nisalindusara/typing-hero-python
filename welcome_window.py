import tkinter as tk

import action_window

def create_welcome_window():

    def close_window():
        """triggered when the 'Get Started' button is clicked. Close the current welcome window
        and create the new action window"""
        root.destroy()
        action_window.create_action_window()

    #Setting up the window with a title, dimensions and an icon
    root = tk.Tk()
    root.title("Typing Hero")
    root.geometry("800x600")
    photo = tk.PhotoImage(file="typing-hero-logo.png")
    root.iconphoto(False, photo)

    #create a frame to include both title and button to get the both widgets centered on the screen
    frame = tk.Frame(root)
    frame.pack(expand=True)
    title_label_styles = {
        'font':('Cascadia Code', 70)
    }
    title_label = tk.Label(frame, text="Typing\nHero", **title_label_styles)
    title_label.pack()
    button_styles = {
        'text': 'Get Started',
        'relief': 'flat',
        'fg': "#133E87",
        'font': ('Cascadia Code', 20),
        'bg': "#CBDCEB"
    }
    button = tk.Button(frame, **button_styles, command=close_window)
    button.pack()

    subtitle_label = tk.Label(text="version 1.0 by Nisal Indusara", font=('Cascadia Code', 10),)
    subtitle_label.pack()

    root.mainloop()