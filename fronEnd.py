import CPU as cpu
import tkinter as tk
from tkinter import ttk


root= tk.Tk()
root.title("Mano Simulator")
root.geometry("1200x900")
root.resizable(False, False)
root.config(bg="#3c3c3b")

canvas1 = tk.Canvas(root, width=1200, height=900, relief='raised', background="#3c3c3b")
canvas1.pack()

#? micro program
MICROPROGRAMLabel = tk.Label(root, text='Micro Program', background="#3c3c3b", foreground="white")
MICROPROGRAMLabel.config(font=('helvetica', 16, 'bold'))
canvas1.create_window(90, 30, window=MICROPROGRAMLabel)

MICROPROGRAM = tk.Text(root, width=35, height=27, borderwidth=1, relief="solid", highlightbackground="white", font=('helvetica', 12), background="#3c3c3b", foreground="white")
MICROPROGRAM.pack(padx=20, pady=20)
canvas1.create_window(175, 280, window=MICROPROGRAM)


#? program
PROGRAMLabel = tk.Label(root, text='Program', background="#3c3c3b", foreground="white")
PROGRAMLabel.config(font=('helvetica', 16, 'bold'))
canvas1.create_window(65, 550, window=PROGRAMLabel)

PROGRAM = tk.Text(root, width=35, height=18, borderwidth=1, relief="solid", highlightbackground="white", font=('helvetica', 12), background="#3c3c3b", foreground="white")
PROGRAM.pack(padx=10, pady=10)
canvas1.create_window(175, 720, window=PROGRAM)


#? ram
RAMLabel = tk.Label(root, text='RAM', background="#3c3c3b", foreground="white")
RAMLabel.config(font=('helvetica', 16, 'bold'))
canvas1.create_window(400, 170, window=RAMLabel)

RAM = ttk.Treeview(root)
RAM.pack(expand=False)
RAM['column'] = ["I", "OPCODE", "Address", "Row"]
RAM.column("#0",anchor='center', stretch='no', width=0)
RAM.column("#1",anchor='center', stretch='no', width=50)
RAM.heading("#1",anchor='center', text='I')
RAM.column("#2",anchor='center', stretch='no', width=150)
RAM.heading("#2",anchor='center', text='OPCODE')
RAM.column("#3",anchor='center', stretch='no', width=200)
RAM.heading("#3",anchor='center', text='Address')
RAM.column("#4",anchor='center', stretch='no', width=150)
RAM.heading("#4",anchor='center', text='Row')
canvas1.create_window(650, 300, window=RAM)


#? Micro Program Memory
MicroProgramLabel = tk.Label(root, text='MicroProgram Memory', background="#3c3c3b", foreground="white")
MicroProgramLabel.config(font=('helvetica', 16, 'bold'))
canvas1.create_window(490, 520, window=MicroProgramLabel)

MicroProgramMemory = ttk.Treeview(root)
MicroProgramMemory.pack(expand=False)
MicroProgramMemory['column'] = ["F1", "F2", "F3", "CD", "BR", "Address", "Row"]
MicroProgramMemory.column("#0",anchor='center', stretch='no', width=0)
MicroProgramMemory.column("#1",anchor='center', stretch='no', width=90)
MicroProgramMemory.heading("#1",anchor='center', text='F1')
MicroProgramMemory.column("#2",anchor='center', stretch='no', width=90)
MicroProgramMemory.heading("#2",anchor='center', text='F2')
MicroProgramMemory.column("#3",anchor='center', stretch='no', width=90)
MicroProgramMemory.heading("#3",anchor='center', text='F3')
MicroProgramMemory.column("#4",anchor='center', stretch='no', width=70)
MicroProgramMemory.heading("#4",anchor='center', text='CD')
MicroProgramMemory.column("#5",anchor='center', stretch='no', width=70)
MicroProgramMemory.heading("#5",anchor='center', text='BR')
MicroProgramMemory.column("#6",anchor='center', stretch='no', width=200)
MicroProgramMemory.heading("#6",anchor='center', text='Address')
MicroProgramMemory.column("#7",anchor='center', stretch='no', width=150)
MicroProgramMemory.heading("#7",anchor='center', text='Row')
MicroProgramMemory.config(height = 15)

canvas1.create_window(750, 710, window=MicroProgramMemory)

def run():
    
    # micro program value :
    file = open("./memory/microProgram.txt", "r")
    output = file.read()
    file.close()
    MICROPROGRAM.insert(tk.END, output)

    # program value :
    temp = PROGRAM.get("1.0","end-1c")
    if temp=='' :
        temp = """ORG 0
        ADD A1
        ADD A3 
        STORE A2
        HAL
ORG 20
    A1: DEC 28
    A2: BIN 111
    A3: HEX F"""

    file = open("./memory/program.txt", "w")
    file.write(temp)
    file.close()

    # fill assembeled micro program memory  
    microMemory = cpu.MPA.microProgramAssembler()
    for i in microMemory :
        MicroProgramMemory.insert(parent='', index='end', iid=i, text='', values=(f"{i[0]}", f"{i[1]}", f"{i[2]}", f"{i[3]}", f"{i[4]}", f"{i[5]}", f"{i[6]}"))

    # fill assembeled program memory  
    mainMemory = cpu.PA.programAssembler()
    for i in mainMemory :
        RAM.insert(parent='', index='end', iid=i, text='', values=(f"{i[0]}", f"{i[1]}", f"{i[2]}", f"{i[3]}"))
    
    # run backEnd :
    cpu.run()

    # redister values :
    AR.insert(tk.END, cpu.MO.R.AR)
    DR.insert(tk.END, cpu.MO.R.DR)
    AC.insert(tk.END, cpu.MO.R.AC)
    PC.insert(tk.END, cpu.MO.R.PC)
    CAR.insert(tk.END, cpu.MO.R.CAR)
    

#################
runImg = tk.PhotoImage(file='./Images/play.png')
runButton = tk.Button(root, image=runImg, borderwidth=0, highlightthickness=0, command = run, background="#3c3c3b", activebackground="#3c3c3c", cursor="hand2")
canvas1.create_window(500, 88, window = runButton)


#? registers:

# AR
ARLabel = tk.Label(root, text='AR', background="#3c3c3b", foreground="white")
ARLabel.config(font=('helvetica', 16, 'bold'))
canvas1.create_window(1000, 220, window=ARLabel)

AR = tk.Text(root, width=12, height=2, borderwidth=1, relief="solid", highlightbackground="white", font=('helvetica', 12), background="#3c3c3b", foreground="white", cursor="arrow")
AR.pack(padx=10, pady=10)
canvas1.create_window(1000, 260, window=AR)


# PC
PCLabel = tk.Label(root, text='PC', background="#3c3c3b", foreground="white")
PCLabel.config(font=('helvetica', 16, 'bold'))
canvas1.create_window(1000, 310, window=PCLabel)

PC = tk.Text(root, width=12, height=2, borderwidth=1, relief="solid", highlightbackground="white", font=('helvetica', 12), background="#3c3c3b", foreground="white", cursor="arrow")
PC.pack(padx=10, pady=10)
canvas1.create_window(1000, 350, window=PC)


# DR
DRLabel = tk.Label(root, text='DR', background="#3c3c3b", foreground="white")
DRLabel.config(font=('helvetica', 16, 'bold'))
canvas1.create_window(1065, 400, window=DRLabel)

DR = tk.Text(root, width=12, height=2, borderwidth=1, relief="solid", highlightbackground="white", font=('helvetica', 12), background="#3c3c3b", foreground="white", cursor="arrow")
DR.pack(padx=10, pady=10)
canvas1.create_window(1065, 440, window=DR)

# AC
ACLabel = tk.Label(root, text='AC', background="#3c3c3b", foreground="white")
ACLabel.config(font=('helvetica', 16, 'bold'))
canvas1.create_window(1130, 220, window=ACLabel)

AC = tk.Text(root, width=12, height=2, borderwidth=1, relief="solid", highlightbackground="white", font=('helvetica', 12), background="#3c3c3b", foreground="white", cursor="arrow")
AC.pack(padx=10, pady=10)
canvas1.create_window(1130, 260, window=AC)


# CAR
CARLabel = tk.Label(root, text='CAR', background="#3c3c3b", foreground="white")
CARLabel.config(font=('helvetica', 16, 'bold'))
canvas1.create_window(1130, 310, window=CARLabel)

CAR = tk.Text(root, width=12, height=2, borderwidth=1, relief="solid", highlightbackground="white", font=('helvetica', 12), background="#3c3c3b", foreground="white", cursor="arrow")
CAR.pack(padx=10, pady=10)
canvas1.create_window(1130, 350, window=CAR)



root.mainloop()