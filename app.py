# Python Program Graphical User Interface (GUI) for a ChatBot

# import library
'''from tkinter import *

# Create the tkinter object (this represents the parent window)
root = Tk()

# Give the window a title
root.title('COVID-19 Q&A Chat Bot')

# Give the window some dimensions or geometry
root.geometry('400x500')

# Create a main menu bar
main_menu = Menu(root)

# Create the submenu
file_menu = Menu(root)
file_menu.add_command(label='New..')
file_menu.add_command(label='Save As...')
file_menu.add_command(label='Exit')

main_menu.add_cascade(label='File', menu=file_menu)
main_menu.add_command(label='Edit')
main_menu.add_command(label='Quit')
root.config(menu=main_menu)
# Adding menu bar to the main window


# Create the Chat window
chatWindow = Text(root, bd=1, bg='black', width=50, height=8)
chatWindow.place(x=6, y=6, height=385, width=370)


# Add a text area for messaging - message window for user input
messageWindow = Text(root, bg='black', width=30, height=4)
messageWindow.place(x=128, y=400, height=88, width=260)


# Create a button to send the message
Button = Button(root, text='Send', bg='blue', activebackground='light blue', width=12, height=5, font='Arial')
Button.place(x=6, y=400, height=88, width=120)

# Add a scroll bar
scrollbar = Scrollbar(root, command=chatWindow.yview())
scrollbar.place(x=375, y=5, height=385)

# Main code
root.mainloop()'''


# import library
from tkinter import *
from chat2 import get_response, bot_name



# Define ChatBot colors and fonts
BG_GRAY = '#ABB2B9'
BG_COLOR = '#17202A'
TEXT_COLOR = '#EAECEE'

FONT = 'Helvetica 14'
FONT_BOLD = 'Helvetica 13 bold'


# Create a class to run the chatbot in the GUI

class ChatApplication:
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()

    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title('EHR Bot')
        self.window.resizable(width=False, height=False)
        self.window.configure(width=490, height=570, bg=BG_COLOR)

        # Head Label
        head_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR,
                           text='Welcome to the EHR Feedback Bot', font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)

        # Tiny divider
        line = Label(self.window, width=450, bg=BG_GRAY)
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        # Text Widget instance variable - area where text is displayed
        self.text_widget = Text(self.window, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR,
                                font=FONT, padx=5, pady=5)
        '''For all text put into this, 20 characters in one line will be displayed, and 2 lines in height.'''
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor='arrow', state=DISABLED)

        # Scroll Bar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview) # whenever we change the scrollbar, it will change the y position of the text widget - allows for scrolling up and down

        # Bottom label - background for bottom area
        bottom_label = Label(self.window, bg=BG_GRAY, height=80)
        bottom_label.place(relwidth=1, rely=0.825)

        # Message Entry Box - where input text goes
        self.msg_entry = Entry(bottom_label, bg="#2C3E50", fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus() # This widget will be selected and ready when GUI started
        self.msg_entry.bind('<Return>', self._on_enter_pressed)

        # Send Button
        send_button = Button(bottom_label, text='Send', font=FONT_BOLD, width=20, bg=BG_GRAY,
                             command=lambda:self._on_enter_pressed(None), activebackground='light blue')
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)


    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, 'Sender')

    def _insert_message(self, msg, sender):
        if not msg:
            return

        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

        # Import Info from the Bot
        msg2 = f"{bot_name}: {get_response(msg)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)

        self.text_widget.see(END)



######################################### GUI RUN ###########################################

if __name__ == "__main__":
    app = ChatApplication()
    app.run()