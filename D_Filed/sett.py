import tkinter
import sys
import tkinter as tk

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

if __name__ == "__main__":
	s = Sett()
	s.run()