import tkinter as tk
from tkinter import filedialog
import os

class Encoder:
    def __init__(self):
        #Set up prompt window
        self.window = tk.Tk()
        self.window.title("Encoder")
        self.window.geometry('1400x600')
        self.frameA = tk.Frame()
        self.frameB = tk.Frame()
        self.frameC = tk.Frame()

        self.opText = tk.Text(self.frameA, height=10)
        self.enText = tk.Text(self.frameB, height=10)
        self.deText = tk.Text(self.frameC, height=10)
        #Encoding key
        self.key = [['A','U'],
                    ['a','I'],
                    ['B','y'],
                    ['b','t'],
                    ['C','8'],
                    ['c','X'],
                    ['D','5'],
                    ['d','A'],
                    ['E','Q'],
                    ['e','h'],
                    ['F','p'],
                    ['f','#'],
                    ['G','M'],
                    ['g','2'],
                    ['H','Y'],
                    ['h','l'],
                    ['I','1'],
                    ['i','a'],
                    ['J','u'],
                    ['j','F'],
                    ['K','R'],
                    ['k','z'],
                    ['L','j'],
                    ['l','K'],
                    ['M','N'],
                    ['m','0'],
                    ['N','m'],
                    ['n','B'],
                    ['O','q'],
                    ['o','d'],
                    ['P','r'],
                    ['p','o'],
                    ['Q','7'],
                    ['q','b'],
                    ['R','g'],
                    ['r','S'],
                    ['S','E'],
                    ['s','P'],
                    ['T','w'],
                    ['t','i'],
                    ['U','J'],
                    ['u','C'],
                    ['V','x'],
                    ['v','s'],  
                    ['W','H'],
                    ['w','9'],
                    ['X','e'],
                    ['x','O'],
                    ['Y','Z'],
                    ['y','4'],
                    ['Z','D'],
                    ['z','3'],
                    ['0','L'],
                    ['1','T'],
                    ['2','6'],
                    ['3','f'],
                    ['4','v'],
                    ['5','k'],
                    ['6','n'],
                    ['7','c'],
                    ['8','W'],
                    ['9','G'],
                    [' ','V'],
                    ['\n','$']]

        self.name = ""
        self.type = ""
        self.data = ""
        self.deData = ""
        self.enData = ""

    def openFile(self):
        filePath = filedialog.askopenfile("r",title="Select '.txt' File",filetypes=[("Text Files","*.txt")]).name #Gets selected .txt file
        #Prints file text in window
        with open(filePath, "r") as file:
            path = os.path.abspath(file.name)
            name = os.path.basename(path)
            split = os.path.splitext(name)
            self.name = split[0]
            self.type = split[1]

            data = file.read()
            print(data)
            self.data = data
            if self.opText.get("1.0",'end-1c') == "":
                self.opText.insert('1.0', data)
    #Encodes the data based on cipher
    def encode(self):
        new = ""
        for char in self.data:
            new += self.matchEn(char)
        if self.enText.get("1.0",'end-1c') == "":
            self.enText.insert('1.0',new)
        self.enData = new
    #Decodes data based on cipher
    def decode(self):
        new = ""
        for char in self.enData:
            new += self.matchDe(char)
        if self.deText.get("1.0",'end-1c') == "":
            self.deText.insert('1.0',new)
        self.deData = new
    #Downloads encoded data
    def downloadEn(self):
        if self.enText.get("1.0",'end-1c') != "":
            file = filedialog.asksaveasfile(defaultextension=".txt",title="Select Folder to Download",filetypes=[("Text Files","*.txt")])
            file.write(self.enData)
    #Downloads decoded data
    def downloadDe(self):
        if self.deText.get("1.0",'end-1c') != "":
            file = filedialog.asksaveasfile(defaultextension=".txt",title="Select Folder to Download",filetypes=[("Text Files","*.txt")])
            file.write(self.deData)
    #Matches decoded data to encoded characters
    def matchEn(self,char = ""):
        for i in self.key:
            if char in i:
                if i[0] == char:
                    return i[1]
        return ""
    #Matches encoded data to decoded characters
    def matchDe(self,char):
        for i in self.key:
            if char in i:
                if i[1] == char:
                    return i[0]   
        return ""
    #Formats the window and runs
    def run(self):
        tk.Button(self.frameA,text="Open File",command=self.openFile).pack(anchor="center")
        self.opText.pack(anchor="center")
        
        tk.Button(self.frameB,text="Encode",command=self.encode).pack()
        self.enText.pack()
        tk.Button(self.frameB,text="Download",command=self.downloadEn).pack()

        tk.Button(self.frameC,text="Decode",command=self.decode).pack()
        self.deText.pack()
        tk.Button(self.frameC,text="Download",command=self.downloadDe).pack()

        self.frameA.grid(column=0,row=0,columnspan=2,sticky="n",padx=10,pady=5)
        self.frameB.grid(column=0,row=1,padx=10,pady=5)
        self.frameC.grid(column=2,row=1,padx=10,pady=5)

        self.window.mainloop()

start = Encoder()
start.run()