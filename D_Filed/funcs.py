import sys
import os
from sys import path
import tkinter as tk
from tkinter import Entry, Tk, ttk, wantobjects
from tkinter.constants import END
from MAIN import Main
from op import Op_f
from tkinter import Toplevel
from sett import Sett

#エディターの機能
class func:
	#初期化
	def __init__(self, _typ, txt, s1, s2):
		self.txt = txt
		self.typ = _typ
		self.enc = "utf_8"
		self.path = os.getcwd()
		self.s1 = s1 
		self.s2 = s2	#ファイルを開く
	
	def op(self):
		# 各種ウィジェットの設置
		self.r_op = Tk()#######################################################################
		self.r_op.title("開く");
		self.r_op.geometry("250x100");
		self.fr_1 = ttk.Frame(self.r_op)
		self.fr_1.grid(column=0, row=0, sticky=tk.NSEW, padx=5, pady=10);
		self.la_1 = ttk.Label(self.fr_1, text="ファイル名:")
		self.ent_1 = ttk.Entry(self.fr_1)
		self.bu_e = ttk.Button(self.fr_1, text="開く", command=self.op)
		self.b_el = ttk.Button(self.fr_1, text="新しいファイル", command=self.op)
		self.la_1.grid(row=0, column=0);
		self.ent_1.grid(row=0, column=1);
		self.bu_e.grid(row=1, column=1);
		self.b_el.grid(row=2, column=1);
		
		self.r_op.mainloop()
	
	def _pr(self):
		op = Op_f(self.typ, self.txt)
		op.run()
	
	def _pr_s(self, event=None):
		self.fileobj = open(self.typ, "w", encoding=self.enc)
		self.fileobj.write(self.txt.get(1.0, END))
		self.fileobj.close()
		print("上書き完了")
	
	def ab(self):
		self.ab = tk.Tk()
		self.ab.geometry("300x200")
		self.b_1 = tk.Button(self.ab, text="close", command=self.ab.destroy).grid()
		self.ab.mainloop()
	
	def op_n(self):
		from start import Open_f
		s = Open_f()
		s.run()
	
	def pa(self):
		self.s_w = Toplevel(background = "white", borderwidth = 10, relief = "sunken", padx = 10, pady = 10, highlightcolor = "red", highlightthickness = 5,)
		self.s_w.geometry("500x200")
		self.ent_3 = ttk.Entry(self.s_w, width=50)
		self.bu_e_3 = ttk.Button(self.s_w, text="実行", command=self.cd)
		self.b_ex = ttk.Button(self.s_w, text="閉じる", command=self.s_w.destroy).grid()
		self.ent_3.grid(row=0, column=1)
		self.bu_e_3.grid(row=1, column=1)
		self.ent_3.insert(tk.END, self.path)
	
	def cd(self):
		os.chdir(self.ent_3.get())
		self.c_d = os.getcwd()
		print(self.c_d)
		self.ent_3.delete(0, tk.END)
	
	def ne_d(self):
		self.s_w_2 = Toplevel(
			background = "white",
			borderwidth = 10,relief = "sunken",
			padx = 10,
			pady = 10,
			highlightthickness = 5)
		self.s_w_2.geometry("300x200")
		self.txt_2 = tk.Entry(self.s_w_2, width=50)
		self.txt_2.grid()
		self.txt_2.insert(tk.END, os.getcwd())
		self.b_o = ttk.Button(self.s_w_2, text = 'OK', padding = (30, 0), command = self.d_m).grid()
		self.button = ttk.Button(self.s_w_2, text = '閉じる', width = str('閉じる'), padding = (30, 0), command = self.s_w_2.destroy).grid()
	
	def d_m(self):
		self.path_2 = self.txt_2.get()
		os.makedirs(self.path_2)
	
	def cl(self):
		sys.exit()
	
	def ran(self):
		print(os.listdir(os.getcwdb()))
		self.su_w = tk.Tk()
		self.su_w.title("Entry Test")
		self.su_w.columnconfigure(0, weight=1)
		self.su_w.rowconfigure(0, weight=1)
		self.t_w = tk.Text(self.su_w)
		self.t_w.grid(column=0, row=0, sticky=(tk.NSEW))
		self.t_w.insert(1.0, os.listdir(os.getcwd()))
		self.su_w.mainloop()
	
	def st(self):
			_typ = self.entry.get()
			#print(_typ)
			mod = 0
			self.root_op.destroy()
			enc = "utf_8"
			main = Main(_typ, mod, enc)
			main.run()
	
	def n_st(self):
		_typ = self.entry.get()
		#print(_typ)
		mod = 1
		self.root_op.destroy()
		enc = "utf_8"
		print("1")
		main = Main(_typ, mod, enc)
		main.run()
	
	def sett(self):
		sett = Sett(self.s1, self.s2)
		sett.run()
	
	def test(self):
		print("OK")

def main():
	fu = func()
	fu._pr()

if __name__ == "__main__":
	main()
