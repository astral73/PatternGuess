import tkinter as tk
import random
import time
from functools import partial

root = tk.Tk()

count = 5
root.geometry("1280x720")
root.title("Number Sequence Guessing Game")
root.configure(bg='red')
quitButton = tk.Button(root,bg='yellow',text = "Quit",width=18, height=4,command = root.destroy)
quitButton.place(relx=0.5, rely=0.95, anchor=tk.CENTER)

num = tk.StringVar()

block = tk.BooleanVar(root,False)

x = []

def destroyWidgets(widget):
    widget.destroy()

def call(num,x,entry):
    num = int(entry.get())
    x.append(num)
    block.set(False)

def game(count,x,num):
    levelLabel = tk.Label(root,bg = 'yellow',text = "Level Starting...")
    levelLabel.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

    root.update_idletasks()
    root.update()
    time.sleep(1)
    destroyWidgets(levelLabel)

    numberList = list(range(1,1000))
    rannum = random.sample(numberList,count)

    placeList = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]

    for i in range(0,count):
        ranplacex = random.sample(placeList,1)
        ranplacey = random.sample(placeList,1)
        countLabel = tk.Label(root,bg = 'yellow',text = rannum[i])
        countLabel.place(relx=ranplacex, rely=ranplacey, anchor=tk.CENTER)
        root.update_idletasks()
        root.update()
        time.sleep(1)
        destroyWidgets(countLabel)

    entryLabel = tk.Label(root,bg='yellow',text = "Input your numbers one by one")
    entryLabel.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

    for a in range(0,count):
        entry = tk.Entry(root,textvariable = num)
        entry.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        enterButton = tk.Button(root,bg='yellow',text = "Enter",command = partial(call,num,x,entry))
        enterButton.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
        block.set(True)
        root.wait_variable(block)

        destroyWidgets(entry)
        destroyWidgets(enterButton)

    destroyWidgets(enterButton)
    destroyWidgets(entry)
    destroyWidgets(entryLabel)

    if x == rannum:
        winLabel = tk.Label(root,bg='yellow',text = "You won the level")
        winLabel.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
        root.update_idletasks()
        root.update()
        time.sleep(1)
        destroyWidgets(winLabel)

        count = count + 1
        x = []

        nextLevel = tk.Label(root,bg='yellow',text = "Be ready for next level...")
        nextLevel.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
        root.update_idletasks()
        root.update()
        time.sleep(1)
        destroyWidgets(nextLevel)
        game(count,x,num)

    else:
        loseLabel = tk.Label(root,bg='yellow',text = "You lost the level")
        loseLabel.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
        root.update_idletasks()
        root.update()
        time.sleep(1)
        destroyWidgets(loseLabel)
        x = []

        sameLevel = tk.Label(root,bg='yellow',text = "Be ready for same level...")
        sameLevel.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
        root.update_idletasks()
        root.update()
        time.sleep(1)
        destroyWidgets(sameLevel)
        game(count,x,num)

root.after(1000,game,count,x,num)

root.mainloop()