import winsound
flag = 1


def play_note(note, btn, btn_key, *argv):
	canv, notes_num = argv

	for i in range(notes_num):
		canv.itemconfig(btn_key[i], fil='black')

	if flag==1:
		file_name="notes/1/"+note+".wav"
	elif flag==2:
		file_name="notes/2/"+note+".wav"
	elif flag==3:
		file_name="notes/3/"+note+".wav"
	elif flag==4:
		file_name="notes/4/"+note+".wav"

	winsound.PlaySound(file_name, winsound.SND_ASYNC)
	canv.itemconfig(btn, fil='white')



def handle(event, btn_key, *argv):
	global flag

	if event.keysym == "z":
		play_note('do', btn_key[0], btn_key, *argv)
	elif event.keysym == "x":
		play_note('re', btn_key[1], btn_key, *argv)
	elif event.keysym == "c":
		play_note('mi', btn_key[2], btn_key, *argv)
	elif event.keysym == "v":
		play_note('fa', btn_key[3], btn_key, *argv)
	elif event.keysym == "b":
		play_note('sol', btn_key[4], btn_key, *argv)
	elif event.keysym == "n":
		play_note('la', btn_key[5], btn_key, *argv)
	elif event.keysym == "m":
		play_note('si', btn_key[6], btn_key, *argv)
	elif event.keysym == "q":
		play_note('do2', btn_key[7], btn_key, *argv)
	elif event.keysym == "w":
		play_note('re2', btn_key[8], btn_key, *argv)
	elif event.keysym == "e":
		play_note('mi2', btn_key[9], btn_key, *argv)
	elif event.keysym == "r":
		play_note('fa2', btn_key[10], btn_key, *argv)
	elif event.keysym == "t":
		play_note('sol2', btn_key[11], btn_key, *argv)
	elif event.keysym == "y":
		play_note('la2', btn_key[12], btn_key, *argv)
	elif event.keysym == "u":
		play_note('si2', btn_key[13], btn_key, *argv)

	elif event.keysym == "1":
		flag=1
	elif event.keysym == "2":
		flag=2
	elif event.keysym == "3":
		flag=3
	elif event.keysym == "4":
		flag=4