from os.path import split
from tkinter import messagebox, filedialog, ttk
from datetime import datetime, time
from tkinter.font import Font
from tkinter import *
import tkinter as tk
import sys, os

class Op_f:
	def __init__(self, _typ, txt):
		self.txt = txt
	
	def file_dialog(self):
		fTyp = [("", "*")]
		iDir = os.path.abspath(os.path.dirname(__file__))
		file_name = tk.filedialog.askopenfilename(filetyps=fTyp, initialdir=iDir)
		if len(file_name) == 0:
			self.file_name.set('選択をキャンセルしました')
		else:
			self.file_name.set(file_name)

	def dir_cl(self):#今はフォルダを開く状態なのでこれをフォルダ　+　ファイル名になるよう頑張る。(1)
		self.iDir = os.path.abspath(os.path.dirname(__file__))
		self.iDirPath = filedialog.askdirectory(initialdir = self.iDir)
		self.en_1.set(self.iDirPath)

	def b_d(self):#(2)
		self.iDir = os.path.abspath(os.path.dirname(__file__))
		self.iDirPath = filedialog.askdirectory(initialdir = self.iDir) + "/" + self.IDirEntry.get()
		print(self.IDirEntry.get())
		self.text=""
		print("1")
		#self.dir_p=self.en_1.get()
		self.root.destroy()
		self.fileobj = open(self.iDirPath, "w", encoding="utf_8")
		self.fileobj.write(self.txt.get(1.0, END))
		self.fileobj.close()
		print("完了")

	def run(self):
		self.root =tk.Tk()
		self.root.title("ファイルの保存")
		frame1 = ttk.Frame(self.root, padding=10)
		frame1.grid(row=0, column=1, sticky=E)

		# 「フォルダ参照」ラベルの作成
		IDirLabel = ttk.Label(frame1, text="ファイル名を入力＞＞", padding=(5, 2))
		IDirLabel.pack(side=LEFT)

		# 「フォルダ参照」エントリーの作成
		self.en_1 = StringVar()
		self.IDirEntry = ttk.Entry(frame1, textvariable=self.en_1, width=30)
		self.IDirEntry.pack(side=LEFT)

		# 「フォルダ参照」ボタンの作成
		IDirButton = ttk.Button(frame1, text="参照", command=self.file_dialog)
		IDirButton.pack(side=LEFT)

		# Frame2の作成
		frame2 = ttk.Frame(self.root, padding=10)
		frame2.grid(row=2, column=1, sticky=E)

		# 「ファイル」ラベルの作成
		IFileLabel = ttk.Label(frame2, text="ファイル>>", padding=(5, 1))
		IFileLabel.pack(side=LEFT)

		# Frame3の作成
		frame3 = ttk.Frame(self.root, padding=10)
		frame3.grid(row=5,column=1,sticky=W)

		# 実行ボタンの設置
		button1 = ttk.Button(frame3, text="保存", command=self.b_d)
		button1.pack(fill = "x", padx=30, side = "left")

		# キャンセルボタンの設置
		button2 = ttk.Button(frame3, text=("やめる"), command=self.root.destroy)
		button2.pack(fill = "x", padx=30, side = "left")
		
		self.root.mainloop()

if __name__ == "__main__":
	c = Op_f()
	c.run()