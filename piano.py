from tkinter import *
from notes.handle import handle

btn_w=40
btn_h=40
x=100
y=100
pos_dx=10
notes_num=14
btn_key=[]
key=('Z','X','C','V','B','N','M','Q','W','E','R','T','Y','U')

root = Tk()
root.title("Инструмент музыкальный")
canv = Canvas(root, height=350, width=900, bg='#0000ff')
canv.pack()

canv.create_text(450, 50, text="1 - Гитара, 2 - Ударные, 3 - Пианино, 4 - String", justify=CENTER, font="Verdana 14", fill='white')

for i in range (notes_num):
	if i==7:
		x += 10
	btn_key.append(canv.create_oval(x, y, x+btn_w, y+btn_h, fill='black'))
	canv.create_text(x+20, y+60, text=key[i], justify=CENTER, font="Verdana 14", fill='white')
	x += btn_w + pos_dx
def key_handle(event):
	handle(event, btn_key, canv, notes_num)

canv.bind("<KeyPress>", key_handle)
canv.focus_set()

root.mainloop()