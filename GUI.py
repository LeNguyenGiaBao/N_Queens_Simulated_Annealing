import tkinter as tk 
from PIL import Image, ImageTk
from N_Queens import *
import time
listButton=[]

size = 0

def createTable():
	global size
	if(entrySize.get().isdigit()):		#check input is a number
		size = int(entrySize.get())
	global listButton
	listButton=[]
	for i in range(size):
		li = []
		for j in range(size):
			bt = tk.Button(frame, bg='white')		#create button
			if((i+j)%2==0):
				bt['bg']='gray'
			bt.place(relx=j/size, rely=i/size, relwidth=1/size, relheight=1/size)	
			bt['state']='disable'	
			li.append(bt) 				#append in the temp list
		listButton.append(li)			#append in the list button


def ClickOK():
	for i in range(size):
		for j in range(size):
			listButton[i][j]['image']=''		#set default image
	no_of_queens = size
	problem1 = NQueensProblem(size)				#create N Queen Problem
	start = time.time()							#start time
	solution = simulated_annealing(problem1)	#find solution
	end =time.time()							#end time
	lbTime['text'] = "{:.12f}".format(float(end-start))		#print time to label time
	for i in range(size):
		if(solution[i]!=-1):									
			listButton[i][solution[i]]['state']='normal'		#state is normal to show image
			if((i+solution[i])%2==0):							#background is gray
				listButton[i][solution[i]]['image']=photo_gray		#image with background is gray
			else:
				listButton[i][solution[i]]['image']=photo_white		#image with background is white 



root = tk.Tk()
root.title('N Queens')

canvas = tk.Canvas(root, height=500, width=550)
canvas.pack()

frame = tk.Frame(root, bg='gray')
frame.place(relwidth=0.8, relheight=1)


rightFrame = tk.Frame(root, bg='#8ad4e1')
rightFrame.place(relwidth=0.2, relheight=1, relx=0.8, rely=0)


lbEnterSize = tk.Label(rightFrame, text='Enter size: ')
lbEnterSize.place(relx=0.1, rely=0.05)

entrySize = tk.Entry(rightFrame)
entrySize.place(relx=0.1, rely=0.1, width=80, height=30)

btSetUp = tk.Button(rightFrame, text='Set Up',command = createTable)		#click to create NxN button
btSetUp.place(relx=0.1, rely=0.17)

btOK =tk.Button(rightFrame, text='Run', command=ClickOK)					#click to run the game
btOK.place(relx=0.1, rely=0.25)


lbTime1 = tk.Label(rightFrame, text = "Time: ")
lbTime1.place(relx=0.1, rely=0.33)

lbTime = tk.Label(rightFrame)									#show time 
lbTime.place(relx=0.1, rely=0.37)

image = Image.open("images/queen_white.png")
image = image.resize((50, 50), Image.ANTIALIAS)
photo_white = ImageTk.PhotoImage(image)							#queen with white background
image2 = Image.open("images/queen_gray.png")
image2 = image2.resize((50, 50), Image.ANTIALIAS)
photo_gray = ImageTk.PhotoImage(image2)							#queen with gray background


root.mainloop()