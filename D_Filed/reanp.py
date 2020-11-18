from ast import literal_eval
from pprint import pprint

class Read:
    def __init__(self, inp):
        self.f = open("sys\\var.oms", "r", encoding="utf_8")
        self.r = self.f.readlines()#                             リスト
        self.inp = inp

    def run(self):
        inp = self.inp
        v = Vpri()
        v.run(inp)
        self.f.close()


class Vpri:
    #inp = printを命じられた変数名 
    #x
    def run(self, inp):
        fil_data = open("sys\\var.oms", encoding="utf_8")
        cov = open("sys\\varconp.oms", "w", encoding="utf_8")
        inp = inp.replace("\n", "")
        for line in fil_data:#一行ずつ読み込まれたデータ
            line = line.replace("{", "").replace("}", "").replace("'", "").replace(" ", "")
            #line = line.rstrip()
            s = line.split(":")[0]#変数名
            i = line.split(":")[-1]#変数にあてられたデータ
            cov.write(s + "," + inp +"\n")
            if inp == s:
                print(i)
                break
            else:
                pass

        fil_data.close()
        cov.close()
"""
r = Read("{a}")
r.run()
"""