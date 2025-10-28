import pyttsx3, os
from cv2 import waitKey
from threading import Thread
from tkinter.messagebox import *
import tkinter as tk
from describr_core import apicall
from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import filedialog
from PIL import ImageTk, Image


window = Tk()
window.geometry("500x657")
window.config(background="black")

window.title("DeScibr")
icon = ImageTk.PhotoImage(file="image1.png")
window.iconphoto(True, icon)

imageLabel, text = None, None


titleLabel = Label(
    text=" 🧠 DESCRIBR: AI VISUAL HELPER ",
    font=("Arial", 18, "bold"),
    fg="#00AAFF",
    bg="black",
)
titleLabel.pack(pady=30)

filepath = ""


def upload_image() -> None:
    # selecting image from file explorer
    global imageLabel, text
    global filepath
    filepath = filedialog.askopenfilename(filetypes=(("Images", "*.jpg;*.png;*.jpeg"),))
    # clearing previous images and texts
    if imageLabel is not None:
        imageLabel.destroy()
    if text is not None:
        text.destroy()
    uploaded__img = Image.open(filepath)
    uploaded_img_ = uploaded__img.resize(size=(250, 275))
    _uploaded_img = ImageTk.PhotoImage(image=uploaded_img_)
    imageLabel = Label(window, image=_uploaded_img, compound=TOP)
    imageLabel.image = _uploaded_img  # keeping a reference to the img for it to appear

    imageLabel.pack(padx=13, pady=10)
    text = Text(
        window,
        height=20,
        width=100,
        bg="black",
        wrap="word",
        fg="white",
        font=("Segoe UI", 10),
        borderwidth=0,
        highlightthickness=0,
    )

    # threaded function that encapsulates the apicall, working in the background
    def thread_() -> None:
        global result
        engine = pyttsx3.Engine()
        result = apicall(filepath)  # passing image to AI Api and storing its response
        text.update_idletasks()
        text.pack(padx=5, pady=3)
        prog_dow.destroy()  # closes the loading window when apicall is done
        engine.say(result)

        # subthread alerts mainthread(tkinter) to update text
        window.after(0, text.insert(tk.END, result), text.update_idletasks())
        engine.runAndWait()

        replayButton.config(state='normal')
        uploadButton.config(state="normal")
        queryButton.config(state='normal')

        

    # allows for threading
    Thread(target=thread_).start()
    uploadButton.config(state="disabled")

    # loading screen that waits for the api call
    def waiting_screen():
        global prog_dow
        prog_dow = Toplevel()  # instiating another gui class
        prog_dow.geometry("350x45")
        prog_dow.title("Loading...")
        icon_ = PhotoImage(file="image1.png")
        prog_dow.iconphoto(True, icon_)
        prog_dow.resizable(False, False)

        def close_popup():
            showwarning(title="WARNING", message="YOU INTERRUPTED THE PROGRAM!")
            window.destroy()
            os._exit(0) # terminate the program

        prog_dow.protocol("WM_DELETE_WINDOW", close_popup)

        progress = Progressbar(
            prog_dow, orient=HORIZONTAL, mode="indeterminate", length=300
        )
        progress.pack(padx=10, pady=10)
        progLabel = Label(
            prog_dow, text="Making API Call...", font=("Monospace", 5, "bold")
        )
        progLabel.pack(padx=5, pady=5)
        time = 0
        while time < 20:
            progress["value"] = 5
            progress.start(interval=7)
            prog_dow.update_idletasks()
            time += 1

    waiting_screen()


uploadButton = Button(
    window,
    text="UPLOAD IMAGE 📁",
    font=("Arial", 13, "bold"),
    fg="white",
    bg="black",
    command=upload_image,
    activeforeground="#00AAFF",
    # activebackground="white",
    borderwidth=5,
    state="normal",
)
uploadButton.pack(padx=10,pady=7)


#function to replay audio
def replay_audio()->None:
    engine = pyttsx3.Engine()
    engine.say(result)
    engine.runAndWait()

replayButton = Button(
    window,
    text="REPLAY AUDIO 📢",
    font=("Arial", 13, "bold"),
    fg="white",
    bg="black",
    command=replay_audio,
    activeforeground="#00AAFF",
    # activebackground="white",
    borderwidth=5,
    relief=SUNKEN,
    state="disabled",
)
replayButton.pack(padx=10, pady=7)


#ask question section
def submit_query() -> str:
    submit.config(state='disabled')
    def thread_answer()->None:
        query_audio = pyttsx3.Engine()
        answer = apicall(filepath, entry.get())
        query_audio.say(answer)
        query_audio.runAndWait()
        submit.config(state='normal')
    Thread(target=thread_answer).start()
    


def ask_question() -> None:
    global entry, submit
    query = Toplevel()
    query.geometry("325x105")
    query.config(background="black")
    query.title("What's your question? ")
    entry = Entry(query, font=('Verdana', 10), width=200)
    entry.pack(padx=20, pady=10)
    submit = Button(query, text="SUBMIT", command=submit_query)
    submit.pack(padx=10, pady=20)

queryButton = Button(
    window,
    text="GOT QUESTIONS❓",
    font=("Arial", 11, "bold"),
    fg="white",
    bg="black",
    command=ask_question,
    activeforeground="#00AAFF",
    # activebackground="white",
    borderwidth=5,
    relief=SUNKEN,
    state="disabled",
)
queryButton.pack(side=BOTTOM)

window.mainloop()