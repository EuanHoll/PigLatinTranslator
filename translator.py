import tkinter as tk
import re

win = tk.Tk()

def isvowel(c):
	return c == 'a' or c == 'i' or c == 'o' or c == 'u' or c =='e'

def isconst(c):
	return not isvowel(c)

def apply_rules(txt):
	ln = len(txt)
	if ln == 1 and isvowel(txt):
		txt = txt + "way"
	return txt

def translate(txtin, txtout):
	txt_to_trans = txtin.get('1.0', 'end')
	ary = re.split(" |\n", txt_to_trans)
	print(ary)
	out = []
	for i in range(len(ary)):
		out.append(apply_rules(ary[i]))
	print(out)
	txtout.configure(state='normal')
	txtout.delete('1.0', 'end')
	txtout.insert('end', txt_to_trans)
	txtout.configure(state='disabled')

def setup_win():
	win.title("English To Pig Latin")
	win.resizable = False
	sw = win.winfo_screenwidth()
	sh = win.winfo_screenheight()
	win.geometry('800x400+%d+%d' % ((sw / 2) - 250, (sh / 2) - 150))
	frm = tk.Frame(win, height=150, width=500)
	lbl0 = tk.Label(frm, text="English Phrase : ").grid(row=0, pady=10)
	txt0 = tk.Text(frm, width=40, height=20)
	txt0.grid(row=1, column=0)
	lbl1 = tk.Label(frm, text="Pig Latin Phrase : ").grid(row=0, column=2)
	txt1 = tk.Text(frm, width=40, height=20, state='disabled')
	txt1.grid(row=1, column=2)
	go = tk.Button(frm, text="Translate", name="translate", command= lambda: translate(txt0, txt1)).grid(row=1, column=1, padx=5)
	frm.pack()

def main():
	setup_win()
	win.mainloop()

if __name__ == '__main__':
	main()
