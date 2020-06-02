import tkinter as tk

window=tk.Tk()
window.title("Tic-Tak-Toe")

windowWidth =400 #change this values to understand how it works
windowHeight =400 
 
# Gets both half the screen width/height and window width/height
positionRight = int(window.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(window.winfo_screenheight()/2 - windowHeight/2)

# Positions the window in the center of the page.
window.geometry("+{}+{}".format(positionRight, positionDown))
window.geometry("300x300")

r1c1=tk.Button(window,text="1")


window.mainloop()