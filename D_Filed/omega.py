import sys
from reanp import *
import os
from collections import defaultdict

global d, x, y

class Main:
    def __init__(self, inp):
        self.inp = inp
        self.dict = {}
        self.d = defaultdict(list)
        self.inp = self.inp.split("//")[0]   # //を取り外す
        self.inp = self.inp.split("#")[0]    # #を取り外す

    def serf(self):
        if self.inp.startswith("def ") or self.inp.startswith("    "):
            self.inp = self.inp.replace("    ", "")
            self.inp = self.inp.replace(";", "")
            print(self.inp)

            self.run()
        else:
            self.run()
    
    #文字列をprintするときの処理
    def run(self):
        if self.inp.startswith("print{") and "}" in self.inp and '"' in self.inp:
            self.inp = self.inp.replace("print{", "")
            self.inp = self.inp.replace("}", "")
            self.inp = self.inp.replace('"', "")
            print(self.inp)
        
        #変数定義の場合の処理
        elif "=" in self.inp:
            if self.inp.startswith("int "):
                self.inp = self.inp.replace("int", "")#intを取り外す
                self.inp = self.inp.replace(" ", "")
                self.x = self.inp.split("=")[0]
                self.y = eval(self.inp.split("=")[-1])
                self.dict[self.x] = self.y
                f = open("sys\\var.oms", "a", encoding="utf_8")
                f.write(str(self.dict)+"\n")
                f.close()
            
            if self.inp.startswith("void "):
                self.inp = self.inp.replace("void", "")
                self.inp = self.inp.replace(" ", "")


        #変数をprintするときの処理
        elif self.inp.startswith("print{") and "}" in self.inp:
            self.inp = self.inp.replace("print{", "")
            self.inp = self.inp.replace("}", "")
            r = Read(self.inp)
            r.run()
        
        elif self.inp == "\n":
            pass
        
        elif self.inp == "exit{}":
            sys.exit(0)

        else:
            print("Err:No funcsion Error")
"""
def main():
    inp = input(">>")
    m = Main(inp)
    m.run()


if __name__ == "__main__":
    if os.path.exists("sys\\var.oms"):
        os.remove("sys\\var.oms")
    f = open("sys\\var.oms", "x", encoding="utf_8")
    f.close()
    while True:
        main()

#test.om
int x = 12
int y = 21
print{x}
print{y}
"""