import tkinter as tk
from tkinter.ttk import * 
from tkinter import ttk, StringVar
import tkinter
import sys, os, subprocess
from sys import path
from start import Open_f
from datetime import datetime
from tkinter.font import Font
from tkinter import *


class Main:
	def __init__(self, _typ, mod, enc):
		self.typ = _typ
		self.mod = mod
		self.enc = enc
		self.app = tk.Tk()##########################################################################################
		self.s = Style()
		self.s.configure('My.TFrame', background='black')
		self.frame1 = ttk.Frame(self.app, style="My.TFrame", padding=12)
		self.menubar = tk.Menu(self.app)
		self.filemenu = tk.Menu(self.menubar)
		self.hen_menu = tk.Menu(self.menubar)
		self.hel_menu = tk.Menu(self.menubar)
		self.jik_menu = tk.Menu(self.menubar)
		self.v1 = StringVar()
		self.txt = Text(self.frame1, fg="white", insertbackground="red", height=15, width=90)
		self.entryExample = Text(self.frame1, height=10, width=20)
		self.now = datetime.now().time()
		self.scrollbar = ttk.Scrollbar(self.frame1, orient=VERTICAL, command=self.txt.yview)


	def ru(self):
		app = tk.Tk()
		app.title(self.typ)

		fontStyle = self.f

		labelExample = tk.Label(app, text="20", font=fontStyle)

		def increase_label_font():
			fontsize = fontStyle['size']
			self.s1 += 2
			labelExample['text'] = self.s1 + 2
			fontStyle.configure(size=fontsize + 2)

		def decrease_label_font():
			fontsize = fontStyle['size']
			self.s1 -= 2
			labelExample['text'] = self.s1 - 2
			fontStyle.configure(size=fontsize-2)
		
		buttonExample1 = tk.Button(app, text="+", width=30, command=increase_label_font)
		buttonExample2 = tk.Button(app, text="-", width=30, command=decrease_label_font)

		buttonExample1.pack(side=tk.LEFT)
		buttonExample2.pack(side=tk.LEFT)
		labelExample.pack(side=tk.RIGHT)
		app.mainloop()

	def jikp(self, event=None):
		ji = subprocess.run(["Omega", self.typ],shell=True)

	def jikb(self, event=None):
		proc = subprocess.run(["gcc", self.typ],stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell=True)
		print(proc.stdout.decode("cp932"))
		print("{}のコンパイルが完了。".format(self.typ))
		ji = subprocess.run(["a"],shell=True)

	def de(self, event=None):
		self.app.destroy()


	def insert(self, event=None):
		pass


	def op(self, event=None):
		from funcs import func
		fu = func
		fu._pr_s(self)
		self.app.destroy()
		main()


	def run(self):
		from funcs import func
		self.s1 = 20
		self.s2 = 15
		fu = func(self.typ, self.txt, self.s1, self.s2)
		self.l_f = Font(font="Consolas", size=15)
		self.f = Font(family="Consolas", size=20)
		self.app.title('D - Field-[ {} ] +New'.format(self.typ))
		self.app.minsize(120, 120)
		self.app.columnconfigure(0, weight=1)
		self.app.rowconfigure(0, weight=1)

		self.frame1.rowconfigure(1, weight=1)
		self.frame1.columnconfigure(0, weight=1)
		self.frame1.grid(sticky=(N, W, S, E))
		
		self.filemenu.add_separator()
		self.filemenu.add_command(label="新規作成/開く", font = self.l_f, command=self.op)
		self.filemenu.add_command(label="ディレクトリを作成", font = self.l_f,  command=fu.ne_d)
		self.filemenu.add_command(label="保存(Ctrl+s)", font = self.l_f,  command=fu._pr_s)
		self.filemenu.add_command(label="名前をつけて保存", font = self.l_f,  command=self._pr)
		self.filemenu.add_command(label="設定", font = self.l_f,  command=self.ru)
		self.filemenu.add_command(label="閉じる", font = self.l_f,  command=self.app.destroy)
		self.filemenu.add_command(label="終了", font = self.l_f,  command=fu.cl)

		self.hel_menu.add_separator()
		self.hel_menu.add_command(label="エディターについて", font = self.l_f,  command=fu.ab)

		self.jik_menu.add_separator()
		self.jik_menu.add_command(label="このエディターのフルパス", font = self.l_f,  command=fu.pa)
		self.jik_menu.add_command(label="このエディターの一覧", font = self.l_f,  command=fu.ran)
		self.jik_menu.add_command(label="Omega言語のコードの実行(F5)", font = self.l_f,  command=self.jikp)
		self.menubar.add_cascade(label="ファイル", font = self.l_f, menu=self.filemenu)
		self.menubar.add_cascade(label="ヘルプ", font = self.l_f, menu=self.hel_menu)
		self.menubar.add_cascade(label="実行", font = self.l_f, menu=self.jik_menu)
		
		self.txt.configure(font=self.f, background="black")
		self.txt.bind("<Control-F5>", self.jikp)
		self.txt.bind("<Control-s>", fu._pr_s)
		self.txt.bind("<Control-o>", self.op)
		self.txt.bind("<Control-e>", self.de)

		if self.mod == 1:

			print(self.typ)
			try:
				#self.txt2.configure(font=self.f)
				self.o_f = open(self.typ, encoding=self.enc)
				self.data = self.o_f.read()
				self.txt.insert(1.0, self.data)
				
			except FileNotFoundError as e:
				print("{}:{}".format(e, self.typ))


		else:#既存ファイルの展開
			print(self.typ)
			try:
				#self.txt2.configure(font=self.f)
				self.o_f = open(self.typ, encoding=self.enc)
				self.data = self.o_f.read()
				self.txt.insert(1.0, self.data)
				
			except FileNotFoundError as e:
				print("{}:{}".format(e, self.typ))

		self.txt.grid(row=1, column=0)
		self.txt["yscrollcommand"] = self.scrollbar.set
		self.scrollbar.grid(row=1, column=1, sticky=(N, S))
		self.app.config(menu=self.menubar)

		self.app.mainloop()


	def n_st(self):
		print("new")


	def st(self):
		pass


	def _pr(self):
		from funcs import func
		fu = func(self.typ, self.txt, self.s1, self.s2)
		fu._pr()


class Sett:
	def __init__(self, s1, s2):
		self.s1 = s1             #エディター
		self.s2 = s2             #ラベル
	
	def r1(self):
		self.s1 = 10
		print(self.s1)
		return self.s1

	def r2(self):
		self.s1 = 15
		print(self.s1)
		return self.s1
		

	def r3(self):
		print(self.s1)
		return self.s1

	def run(self):
		tki = tkinter.Tk()
		# 画面サイズ
		tki.geometry('300x200')
		# 画面タイトル
		tki.title('ラジオボタン')

		var = tkinter.IntVar()
		# value=0のラジオボタンにチェックを入れる
		var.set(0)

		# ラジオボタン作成
		rdo1 = tkinter.Radiobutton(tki, value=0, variable=var, text='10', command=self.r1)
		rdo1.place(x=70, y=40)

		rdo2 = tkinter.Radiobutton(tki, value=1, variable=var, text='15', command=self.r2)
		rdo2.place(x=70, y=70)

		rdo3 = tkinter.Radiobutton(tki, value=2, variable=var, text='20', command=self.r3)
		rdo3.place(x=70, y=100)

		tk.Label(tki, text="エディターの文字サイズを指定").place(x=70, y=10)

		tki.mainloop()


def main(event=None):
	start = Open_f()
	start.run()

