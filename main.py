import tkinter
import tkinter.messagebox
import random

window = tkinter.Tk()
window.title("Tic Tac Toe")

# Create button0-8 and arrange them in a grid
button0 = tkinter.Button(window,            
 text=" ", font='Times 20 bold',
 bg='blue', fg='white',
 height=2, width=4,
 command=lambda: buttonClick(0))
button0.grid(row=0, column=0)

button1 = tkinter.Button(window,            
 text=" ", font='Times 20 bold',
 bg='blue', fg='white',
 height=2, width=4,
 command=lambda: buttonClick(1))
button1.grid(row=1, column=0)

button2 = tkinter.Button(window,            
 text=" ", font='Times 20 bold',
 bg='blue', fg='white',
 height=2, width=4,
 command=lambda: buttonClick(2))
button2.grid(row=2, column=0)

button3 = tkinter.Button(window,            
 text=" ", font='Times 20 bold',
 bg='blue', fg='white',
 height=2, width=4,
 command=lambda: buttonClick(3))
button3.grid(row=1, column=1)

button4 = tkinter.Button(window,            
 text=" ", font='Times 20 bold',
 bg='blue', fg='white',
 height=2, width=4,
 command=lambda: buttonClick(4))
button4.grid(row=1, column=2)

button5 = tkinter.Button(window,            
 text=" ", font='Times 20 bold',
 bg='blue', fg='white',
 height=2, width=4,
 command=lambda: buttonClick(5))
button5.grid(row=0, column=1)

button6 = tkinter.Button(window,            
 text=" ", font='Times 20 bold',
 bg='blue', fg='white',
 height=2, width=4,
 command=lambda: buttonClick(6))
button6.grid(row=0, column=2)

button7 = tkinter.Button(window,            
 text=" ", font='Times 20 bold',
 bg='blue', fg='white',
 height=2, width=4,
 command=lambda: buttonClick(7))
button7.grid(row=2, column=1)

button8 = tkinter.Button(window,            
 text=" ", font='Times 20 bold',
 bg='blue', fg='white',
 height=2, width=4,
 command=lambda: buttonClick(8))
button8.grid(row=2, column=2)
# Add more buttons

# Add the buttons to this list
buttons = [button0, button1, button2, button3, button4, button5, button6, button7, button8]

# This represents the moves on the board as a list
board = [0, 1, 2, 3, 4, 5, 6, 7, 8]


# Copy in your computerMove() function
def computerMove():
    global board
    move = random.randrange(0,9)
    while(board[move] == "O" or board[move] == "X"):
        move = random.randrange(0,9)
    board[move] = "O"
    buttons[move].configure(text = "O") 

# Add in buttons[move].configure(text = "O") to show the O in the right button

# Copy in your checkWin() function
def checkWin():
    if board[0] == board[1] and board[1] == board[2]:
        tkinter.messagebox.showinfo("Title", "Winner!") 
        disableButtons()

    if board[3] == board[4] and board[4] == board[5]:
        tkinter.messagebox.showinfo("Title", "Winner!")
        disableButtons()

    if board[6] == board[7] and board[7] == board[8]:
        tkinter.messagebox.showinfo("Title", "Winner!")
        disableButtons()

    if board[6] == board[4] and board[4] == board[2]:
       tkinter.messagebox.showinfo("Title", "Winner!")
       disableButtons()

    if board[8] == board[4] and board[4] == board[0]:
        tkinter.messagebox.showinfo("Title", "Winner!")
        disableButtons()

    if board[0] == board[3] and board[3] == board[6]:
        tkinter.messagebox.showinfo("Title", "Winner!")
        disableButtons()
        
    if board[1] == board[4] and board[4] == board[7]:
        tkinter.messagebox.showinfo("Title", "Winner!")
        disableButtons()
        
    if board[2] == board[5] and board[5] == board[8]:
        tkinter.messagebox.showinfo("Title", "Winner!")
        disableButtons()

    if board[3] == board[8] and board[8] == board[0]:
        tkinter.messagebox.showinfo("Title", "Winner!")
        disableButtons()

    if board[6] == board[3] and board[3] == board[2]:
        tkinter.messagebox.showinfo("Title", "Winner!")
        disableButtons()

    if board[0] == board[5] and board[5] == board[6]:
        tkinter.messagebox.showinfo("Title", "Winner!")
        disableButtons()

    if board[3] == board[1] and board[1] == board[4]:
        tkinter.messagebox.showinfo("Title", "Winner!")
        disableButtons()

    if board[2] == board[7] and board[7] == board[8]:
        tkinter.messagebox.showinfo("Title", "Winner!")
        disableButtons()

    if board[5] == board[3] and board[3] == board[7]:
        tkinter.messagebox.showinfo("Title", "Winner!")
        disableButtons()

    if board[6] == board[4] and board[4] == board[8]:
        tkinter.messagebox.showinfo("Title", "Winner!")
        disableButtons()
# You can pop up a messagebox instead of printing the winner and call disable buttons

# This function is called when a button with a particular number is clicked
# It replaces playerMove()
def buttonClick(buttonNumber):
    button = buttons[buttonNumber]
    if button["text"] == " ":
        print("Button", buttonNumber, "clicked")
        button.configure(text="X")
        board[buttonNumber] = "X"
        # do button configure to set its text to "X"
        # set board at buttonNumber to "X"
        checkWin()
        computerMove() 
        checkWin() 
    # else pop up a messagebox to say position full

# This will disable all the buttons. Call it when the game is won from checkWin(). 
def disableButtons():
    button0.configure(state=tkinter.DISABLED)
    button1.configure(state=tkinter.DISABLED)
    button2.configure(state=tkinter.DISABLED)
    button3.configure(state=tkinter.DISABLED)
    button4.configure(state=tkinter.DISABLED)
    button5.configure(state=tkinter.DISABLED)
    button6.configure(state=tkinter.DISABLED)
    button7.configure(state=tkinter.DISABLED)
    button8.configure(state=tkinter.DISABLED)

window.mainloop()