from os.path import split
from tkinter import messagebox, filedialog, ttk
from datetime import datetime, time
from tkinter.font import Font
from tkinter import *
import tkinter as tk
import sys, os

#メニュー画面の生成と表示
class Open_f:

	def __init__(self):
		pass


	def dir_cl(self):
		self.iDir = os.path.abspath(os.path.dirname(__file__))
		self.iDirPath = filedialog.askdirectory(initialdir = self.iDir)
		self.en_1.set(self.iDirPath)


	def fil_cl(self):
		self.ftyp = [("", "*")]
		self.ifile = os.path.abspath(os.path.dirname(__file__))
		self.ifile_p = filedialog.askopenfilename(filetyp = self.ftyp, initialdir = self.ifile)
		self.en_2.set(self.ifile_p)


	def b_d(self):
		self.text=""
		self.dir_p=self.en_1.get()
		self.fil_p=self.en_2.get()
		self.root.destroy()

		if self.bln.get():
			from MAIN import Main
			_typ = self.fil_p
			mod = 1
			enc = "utf_8"
			main = Main(_typ, mod, enc)
			main.run()
		else:
				from MAIN import Main
				_typ = self.fil_p
				mod = 0
				enc = "utf_8"
				main = Main(_typ, mod, enc)
				main.run()


	def run(self):
		self.root =tk.Tk()
		self.root.title("ファイルとワークスペースフォルダを開く")
		frame1 = ttk.Frame(self.root, padding=10)
		frame1.grid(row=0, column=1, sticky=E)

		# 「フォルダ参照」ラベルの作成
		IDirLabel = ttk.Label(frame1, text="フォルダを指定＞＞", padding=(5, 2))
		IDirLabel.pack(side=LEFT)

		# 「フォルダ参照」エントリーの作成
		self.en_1 = StringVar()
		IDirEntry = ttk.Entry(frame1, textvariable=self.en_1, width=30)
		IDirEntry.pack(side=LEFT)

		# 「フォルダ参照」ボタンの作成
		IDirButton = ttk.Button(frame1, text="参照", command=self.dir_cl)
		IDirButton.pack(side=LEFT)

		# Frame2の作成
		frame2 = ttk.Frame(self.root, padding=10)
		frame2.grid(row=2, column=1, sticky=E)

		# 「ファイル参照」ラベルの作成
		IFileLabel = ttk.Label(frame2, text="ファイルを指定＞＞", padding=(5, 2))
		IFileLabel.pack(side=LEFT)

		# 「ファイル参照」エントリーの作成
		self.en_2 = StringVar()
		IFileEntry = ttk.Entry(frame2, textvariable=self.en_2, width=30)
		IFileEntry.pack(side=LEFT)

		# 「ファイル参照」ボタンの作成
		IFileButton = ttk.Button(frame2, text="参照", command=self.fil_cl)
		IFileButton.pack(side=LEFT)

		# Frame3の作成
		frame3 = ttk.Frame(self.root, padding=10)
		frame3.grid(row=5,column=1,sticky=W)

		# 実行ボタンの設置
		button1 = ttk.Button(frame3, text="実行", command=self.b_d)
		button1.pack(fill = "x", padx=30, side = "left")

		# キャンセルボタンの設置
		button2 = ttk.Button(frame3, text=("閉じる"), command=quit)
		button2.pack(fill = "x", padx=30, side = "left")

		self.bln = tk.BooleanVar()
		self.bln.set(False)

		chk = tk.Checkbutton(self.root, variable=self.bln, text='新しく作ったファイル/ディレクトリを使用する') 
		chk.place(x=150, y=80)

		self.root.mainloop()

#実行関数の定義
def main():
	start = Open_f()
	start.run()

#実行関数の実行
if __name__ == "__main__":
	main()

