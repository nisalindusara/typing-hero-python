import tkinter as tk
import content_manager

index = 0
score = 0

def create_action_window():

    text_content = content_manager.content_list[0]

    def start_timer(count):
        """Start the timer"""
        if count<10:
            timer.config(text=f"00:0{count}")
        elif count<60:
            timer.config(text=f"00:{count}")
        elif count//60<10:
            if count%60<10:
                timer.config(text=f"0{count//60}:0{count%60}")
            else:
                timer.config(text=f"0{count//60}:{count%60}")
        else:
            if count % 60 < 10:
                timer.config(text=f"{count//60}:0{count%60}")
            else:
                timer.config(text=f"{count//60}:{count%60}")

        root.after(100, start_timer, count + 1)

    def change_text_color():
        """Change the text colour when the user correctly types the next character in the text"""
        text.tag_configure("change_color", foreground="#133E87")
        text.config(state=tk.NORMAL)
        text.tag_add("change_color", 1.0, f"1.{index+1}")
        text.config(state=tk.DISABLED)

    def increase_score():
        """Increase the score when user correctly types the next character in the text"""
        label.config(text=f"Score: {score}/{len(text_content)}")

    def on_key_press(event):
        """Triggered when a key is pressed. Identifies the key and if it is correct, change the color of the charactre and increase the score"""
        root.after(1000, start_timer, 1)
        global index, score
        if text_content[index]==event.char:
            change_text_color()
            index+=1
            score+=1
            increase_score()

    #creating and configuring the window
    root = tk.Tk()
    root.focus_set()
    root.title("Typing Hero")
    root.geometry("800x600")
    root.config(bg="#CBDCEB")
    photo = tk.PhotoImage(file="typing-hero-logo.png")
    root.iconphoto(False, photo)

    #timer label on the top of the window
    timer_style = {
        'bg': root.cget('bg'),
        'font': ('Arial', 15),
        'pady': 20
    }
    timer = tk.Label(text="00:00", **timer_style)
    timer.pack()

    #text widget that includes the text to be typed centered onto the screen with expand=True
    text_style = {
        'font': ('Corbel', 25),
        'bg': root.cget('bg'),
        'fg': "#608BC1",
        'height': 10,
        'bd': 0,
        'width': 50,
        'wrap': 'word',
        'relief': 'flat'
    }
    text = tk.Text(root, **text_style)
    text.pack(expand=True)
    text.insert(tk.END, text_content)
    text.config(state=tk.DISABLED, padx=30)
    text.tag_configure("center", justify='center')
    text.tag_add("center", 1.0, tk.END)
    text.focus()

    #Label widget on the bottom of the screen to indicate the score
    label_style = {
        'font': ('Arial', 15),
        'pady': 20,
        'bg': root.cget('bg'),
        'fg': "#133E87",
    }
    label = tk.Label(text=f"Score: {score}/{len(text_content)}", **label_style)
    label.pack()


    root.bind("<KeyPress>", on_key_press)


    root.mainloop()