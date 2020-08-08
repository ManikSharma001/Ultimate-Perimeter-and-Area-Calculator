#Perimeter and Area Formulas for Popular Shapes
#'per' indicates perimeter and 'ar' indicates area

import math
import tkinter as tk
from tkinter import messagebox

while True:    
    def perTriangle():
        tk.Label(window, text = "Enter in the Numbers: ", background = "white").place(x = 1115, y = 100)
        tk.Label(window, text = "Side 1: ", background = "white").place(x = 1115, y = 130)
        global entry1
        entry1 = tk.Entry(window)
        entry1.place(x = 1155, y = 130)
        tk.Label(window, text = "Side 2: ", background = "white").place(x = 1115, y = 160)
        global entry2
        entry2 = tk.Entry(window)
        entry2.place(x = 1155, y = 160)
        tk.Label(window, text = "Side 3: ", background = "white").place(x = 1115, y = 190)
        global entry3
        entry3 = tk.Entry(window)
        entry3.place(x = 1155, y = 190)
        check1 = tk.IntVar()
        cButton = tk.Checkbutton(window, text = "Enter: ", variable = check1, command = calPerTriangle)
        cButton.place(x = 1115, y = 220)

    def calPerTriangle():
        btnACommand()
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        num3 = float(entry3.get())
        ans = num1 + num2 + num3
        messagebox.showinfo("Answer:", str(ans))
        window.destroy()

    def arTriangle():
        tk.Label(window, text = "Enter in the Numbers: ", background = "white").place(x = 1115, y = 100)
        tk.Label(window, text = "Base: ", background = "white").place(x = 1115, y = 130)
        global entry1
        entry1 = tk.Entry(window)
        entry1.place(x = 1155, y = 130)
        tk.Label(window, text = "Height: ", background = "white").place(x = 1110, y = 160)
        global entry2
        entry2 = tk.Entry(window)
        entry2.place(x = 1155, y = 160)
        check1 = tk.IntVar()
        cButton = tk.Checkbutton(window, text = "Enter: ", variable = check1, command = calArTriangle)
        cButton.place(x = 1115, y = 190)

    def calArTriangle():
        btnACommand()
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        ans = (num1 * num2) / 2 
        messagebox.showinfo("Answer:", str(ans))
        window.destroy()

    def perSquare():
        tk.Label(window, text = "Enter in the Number: ", background = "white").place(x = 1115, y = 100)
        tk.Label(window, text = "Length: ", background = "white").place(x = 1110, y = 130)
        global entry1
        entry1 = tk.Entry(window)
        entry1.place(x = 1155, y = 130)
        check1 = tk.IntVar()
        cButton = tk.Checkbutton(window, text = "Enter: ", variable = check1, command = calPerSquare)
        cButton.place(x = 1115, y = 160)

    def calPerSquare():
        btnACommand()
        num1 = float(entry1.get())
        ans = num1 * 4 
        messagebox.showinfo("Answer:", str(ans))
        window.destroy()

    def arSquare():
        tk.Label(window, text = "Enter in the Number: ", background = "white").place(x = 1115, y = 100)
        tk.Label(window, text = "Length: ", background = "white").place(x = 1110, y = 130)
        global entry1
        entry1 = tk.Entry(window)
        entry1.place(x = 1155, y = 130)
        check1 = tk.IntVar()
        cButton = tk.Checkbutton(window, text = "Enter: ", variable = check1, command = calArSquare)
        cButton.place(x = 1115, y = 160)

    def calArSquare():
        btnACommand()
        num1 = float(entry1.get())
        ans = num1 ** 2
        messagebox.showinfo("Answer:", str(ans))
        window.destroy()

    def perRectangle():
        tk.Label(window, text = "Enter in the Numbers: ", background = "white").place(x = 1115, y = 100)
        tk.Label(window, text = "Length: ", background = "white").place(x = 1110, y = 130)
        global entry1
        entry1 = tk.Entry(window)
        entry1.place(x = 1155, y = 130)
        tk.Label(window, text = "Width: ", background = "white").place(x = 1110, y = 160)
        global entry2
        entry2 = tk.Entry(window)
        entry2.place(x = 1155, y = 160)
        check1 = tk.IntVar()
        cButton = tk.Checkbutton(window, text = "Enter: ", variable = check1, command = calPerRectangle)
        cButton.place(x = 1115, y = 190)

    def calPerRectangle():
        btnACommand()
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        ans = 2 * (num1 + num2)
        messagebox.showinfo("Answer:", str(ans))
        window.destroy()
        
    def arRectangle():
        tk.Label(window, text = "Enter in the Numbers: ", background = "white").place(x = 1115, y = 100)
        tk.Label(window, text = "Length:  ", background = "white").place(x = 1110, y = 130)
        global entry1
        entry1 = tk.Entry(window)
        entry1.place(x = 1155, y = 130)
        tk.Label(window, text = "Width: ", background = "white").place(x = 1110, y = 160)
        global entry2
        entry2 = tk.Entry(window)
        entry2.place(x = 1155, y = 160)
        check1 = tk.IntVar()
        cButton = tk.Checkbutton(window, text = "Enter: ", variable = check1, command = calArRectangle)
        cButton.place(x = 1115, y = 190)

    def calArRectangle():
        btnACommand()
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        ans = num1 * num2
        messagebox.showinfo("Answer:", str(ans))
        window.destroy()

    def perRhombus():
        tk.Label(window, text = "Enter in the Number: ", background = "white").place(x = 1115, y = 100)
        tk.Label(window, text = "Side 1: ", background = "white").place(x = 1115, y = 130)
        global entry1
        entry1 = tk.Entry(window)
        entry1.place(x = 1155, y = 130)
        check1 = tk.IntVar()
        cButton = tk.Checkbutton(window, text = "Enter: ", variable = check1, command = calPerRhombus)
        cButton.place(x = 1115, y = 160)

    def calPerRhombus():
        btnACommand()
        num1 = float(entry1.get())
        ans = num1 * 4 
        messagebox.showinfo("Answer:", str(ans))
        window.destory()

    def arRhombus():
        tk.Label(window, text = "Enter in the Numbers for the Diagonals: ", background = "white").place(x = 1115, y = 100)
        tk.Label(window, text = "Diagonal 1: ", background = "white").place(x = 1085, y = 130)
        global entry1
        entry1 = tk.Entry(window)
        entry1.place(x = 1155, y = 130)
        tk.Label(window, text = "Diagonal 2: ", background = "white").place(x = 1085, y = 160)
        global entry2
        entry2 = tk.Entry(window)
        entry2.place(x = 1155, y = 160)
        check1 = tk.IntVar()
        cButton = tk.Checkbutton(window, text = "Enter: ", variable = check1, command = calArRhombus)
        cButton.place(x = 1115, y = 190)

    def calArRhombus():
        btnACommand()
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        ans = (num1 * num2) / 2
        messagebox.showinfo("Answer:", str(ans))
        window.destroy()
         
    def perParallelogram():
        tk.Label(window, text = "Enter in the Numbers: ", background = "white").place(x = 1115, y = 100)
        tk.Label(window, text = "Length: ", background = "white").place(x = 1110, y = 130)
        global entry1
        entry1 = tk.Entry(window)
        entry1.place(x = 1155, y = 130)
        tk.Label(window, text = "Width: ", background = "white").place(x = 1110, y = 160)
        global entry2
        entry2 = tk.Entry(window)
        entry2.place(x = 1155, y = 160)
        check1 = tk.IntVar()
        cButton = tk.Checkbutton(window, text = "Enter: ", variable = check1, command = calPerParallelogram)
        cButton.place(x = 1115, y = 190)

    def calPerParallelogram():
        btnACommand()
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        ans = 2 * (num1 + num2)
        messagebox.showinfo("Answer:", str(ans))
        window.destroy()

    def arParallelogram():
        tk.Label(window, text = "Enter in the Numbers: ", background = "white").place(x = 1115, y = 100)
        tk.Label(window, text = "Length: ", background = "white").place(x = 1110, y = 130)
        global entry1
        entry1 = tk.Entry(window)
        entry1.place(x = 1155, y = 130)
        tk.Label(window, text = "Width: ", background = "white").place(x = 1110, y = 160)
        global entry2
        entry2 = tk.Entry(window)
        entry2.place(x = 1155, y = 160)
        check1 = tk.IntVar()
        cButton = tk.Checkbutton(window, text = "Enter: ", variable = check1, command = calArParallelogram)
        cButton.place(x = 1115, y = 190)
        
    def calArParallelogram():
        btnACommand()
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        ans = num1 * num2
        messagebox.showinfo("Answer:", str(ans))
        window.destroy()

    def perTrapezoid():
        tk.Label(window, text = "Enter in the Numbers: ", background = "white").place(x = 1115, y = 100)
        tk.Label(window, text = "Side 1: ", background = "white").place(x = 1115, y = 130)
        global entry1
        entry1 = tk.Entry(window)
        entry1.place(x = 1155, y = 130)
        tk.Label(window, text = "Side 2: ", background = "white").place(x = 1115, y = 160)
        global entry2
        entry2 = tk.Entry(window)
        entry2.place(x = 1155, y = 160)
        tk.Label(window, text = "Side 3: ", background = "white").place(x = 1115, y = 190)
        global entry3
        entry3 = tk.Entry(window)
        entry3.place(x = 1155, y = 190)
        tk.Label(window, text = "Side 4: ", background = "white").place(x = 1115, y = 220)
        global entry4
        entry4 = tk.Entry(window)
        entry4.place(x = 1155, y = 220)
        check1 = tk.IntVar()
        cButton = tk.Checkbutton(window, text = "Enter: ", variable = check1, command = calPerTrapezoid)
        cButton.place(x = 1115, y = 250)

    def calPerTrapezoid():
        btnACommand()
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        num3 = float(entry3.get())
        num4 = float(entry4.get())
        ans = num1 + num2 + num3 + num4
        messagebox.showinfo("Answer:", str(ans))
        window.destroy()
        
    def arTrapezoid():
        tk.Label(window, text = "Enter in the Numbers: ", background = "white").place(x = 1115, y = 100)
        tk.Label(window, text = "Side 1 (Top): ", background = "white").place(x = 1080, y = 130)
        global entry1
        entry1 = tk.Entry(window)
        entry1.place(x = 1155, y = 130)
        tk.Label(window, text = "Side 2 (Bottom): ", background = "white").place(x = 1060, y = 160)
        global entry2
        entry2 = tk.Entry(window)
        entry2.place(x = 1155, y = 160)
        tk.Label(window, text = "Height: ", background = "white").place(x = 1105, y = 190)
        global entry3
        entry3 = tk.Entry(window)
        entry3.place(x = 1155, y = 190)
        check1 = tk.IntVar()
        cButton = tk.Checkbutton(window, text = "Enter: ", variable = check1, command = calArTrapezoid)
        cButton.place(x = 1115, y = 220)

    def calArTrapezoid():
        btnACommand()
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        num3 = float(entry3.get())
        ans = ((num1 + num2) / 2) * num3
        messagebox.showinfo("Answer:", str(ans))
        window.destroy()

    def perKite():
        tk.Label(window, text = "Enter in the Numbers: ", background = "white").place(x = 1115, y = 100)
        tk.Label(window, text = "Side 1: ", background = "white").place(x = 1115, y = 130)
        global entry1
        global entry2
        entry1 = tk.Entry(window)
        entry1.place(x = 1155, y = 130)
        tk.Label(window, text = "Side 2: ", background = "white").place(x = 1115, y = 160)
        entry2 = tk.Entry(window)
        entry2.place(x = 1155, y = 160)
        check1 = tk.IntVar()
        cButton = tk.Checkbutton(window, text = "Enter: ", variable = check1, command = calPerKite)
        cButton.place(x = 1115, y = 190)

    def calPerKite():
        btnACommand()
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        ans = 2 * (num1 + num2)
        messagebox.showinfo("Answer:", str(ans))
        window.destroy()

    def arKite():
        tk.Label(window, text = "Enter in the Numbers for the Diagonals: ", background = "white").place(x = 1115, y = 100)
        tk.Label(window, text = "Diagonal 1: ", background = "white").place(x = 1085, y = 130)
        global entry1
        entry1 = tk.Entry(window)
        entry1.place(x = 1155, y = 130)
        tk.Label(window, text = "Diagonal 2: ", background = "white").place(x = 1085, y = 160)
        global entry2
        entry2 = tk.Entry(window)
        entry2.place(x = 1155, y = 160)
        check1 = tk.IntVar()
        cButton = tk.Checkbutton(window, text = "Enter: ", variable = check1, command = calArKite)
        cButton.place(x = 1115, y = 190)

    def calArKite():
        btnACommand()
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        ans = (num1 * num2)/ 2
        messagebox.showinfo("Answer:", str(ans))
        window.destroy()

    def perTrapezium():
        tk.Label(window, text = "Enter in the Numbers: ", background = "white").place(x = 1115, y = 100)
        tk.Label(window, text = "Side 1: ", background = "white").place(x = 1115, y = 130)
        global entry1
        entry1 = tk.Entry(window)
        entry1.place(x = 1155, y = 130)
        tk.Label(window, text = "Side 2: ", background = "white").place(x = 1115, y = 160)
        global entry2
        entry2 = tk.Entry(window)
        entry2.place(x = 1155, y = 160)
        tk.Label(window, text = "Side 3: ", background = "white").place(x = 1115, y = 190)
        global entry3
        entry3 = tk.Entry(window)
        entry3.place(x = 1155, y = 190)
        tk.Label(window, text = "Side 4: ", background = "white").place(x = 1115, y = 220)
        global entry4
        entry4 = tk.Entry(window)
        entry4.place(x = 1155, y = 220)
        check1 = tk.IntVar()
        cButton = tk.Checkbutton(window, text = "Enter: ", variable = check1, command = calPerTrapezium)
        cButton.place(x = 1115, y = 250)

    def calPerTrapezium():
        btnACommand()
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        num3 = float(entry3.get())
        num4 = float(entry4.get())
        ans = num1 + num2 + num3 + num4
        messagebox.showinfo("Answer:", str(ans))
        window.destroy()

    def arTrapezium():
        tk.Label(window, text = "Enter in the Numbers: ", background = "white").place(x = 1115, y = 100)
        tk.Label(window, text = "Side 1 (Top): ", background = "white").place(x = 1075, y = 130)
        global entry1
        entry1 = tk.Entry(window)
        entry1.place(x = 1155, y = 130)
        tk.Label(window, text = "Side 2 (Bottom): ", background = "white").place(x = 1065, y = 160)
        global entry2
        entry2 = tk.Entry(window)
        entry2.place(x = 1155, y = 160)
        tk.Label(window, text = "Height: ", background = "white").place(x = 1105, y = 190)
        global entry3
        entry3 = tk.Entry(window)
        entry3.place(x = 1155, y = 190)
        check1 = tk.IntVar()
        cButton = tk.Checkbutton(window, text = "Enter: ", variable = check1, command = calArTrapezium)
        cButton.place(x = 1115, y = 220)

    def calArTrapezium():
        btnACommand()
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        num3 = float(entry3.get())
        ans = ((num1 + num2) / 2 ) * num3
        messagebox.showinfo("Answer:", str(ans))
        window.destroy()

    #All following shapes should be assumed as regular.

    def perPentagon():
        tk.Label(window, text = "Enter in the Number: ", background = "white").place(x = 1115, y = 100)
        tk.Label(window, text = "Length: ", background = "white").place(x = 1110, y = 130)
        global entry1
        entry1 = tk.Entry(window)
        entry1.place(x = 1155, y = 130)
        check1 = tk.IntVar()
        cButton = tk.Checkbutton(window, text = "Enter: ", variable = check1, command = calPerPentagon)
        cButton.place(x = 1115, y = 160)

    def calPerPentagon():
        btnACommand()
        num1 = float(entry1.get())
        ans = num1 * 5
        messagebox.showinfo("Answer:", str(ans))
        window.destroy()
        
    def arPentagon():
        tk.Label(window, text = "Enter in the Number: ", background = "white").place(x = 1115, y = 100)
        tk.Label(window, text = "Length: ", background = "white").place(x = 1110, y = 130)
        global entry1
        entry1 = tk.Entry(window)
        entry1.place(x = 1155, y = 130)
        check1 = tk.IntVar()
        cButton = tk.Checkbutton(window, text = "Enter: ", variable = check1, command = calArPentagon)
        cButton.place(x = 1115, y = 160)

    def calArPentagon():
        btnACommand()
        num1 = float(entry1.get())
        ans = 0.25 * math.sqrt(5 * (5 + 2*math.sqrt(5))) * num1 ** 2
        messagebox.showinfo("Answer:", str(ans))
        window.destroy()

    def perHexagon():
        tk.Label(window, text = "Enter in the Number: ", background = "white").place(x = 1115, y = 100)
        tk.Label(window, text = "Length: ", background = "white").place(x = 1110, y = 130)
        global entry1
        entry1 = tk.Entry(window)
        entry1.place(x = 1155, y = 130)
        check1 = tk.IntVar()
        cButton = tk.Checkbutton(window, text = "Enter: ", variable = check1, command = calPerHexagon)
        cButton.place(x = 1115, y = 160)

    def calPerHexagon():
        btnACommand()
        num1 = float(entry1.get())
        ans = num1 * 6 
        messagebox.showinfo("Answer:", str(ans))
        window.destroy()

    def arHexagon():
        tk.Label(window, text = "Enter in the Number:", background = "white").place(x = 1115, y = 100)
        tk.Label(window, text = "Length: ", background = "white").place(x = 1110, y = 130)
        global entry1
        entry1 = tk.Entry(window)
        entry1.place(x = 1155, y = 130)
        check1 = tk.IntVar()
        cButton = tk.Checkbutton(window, text = "Enter: ", variable = check1, command = calArHexagon)
        cButton.place(x = 1115, y = 160)

    def calArHexagon():
        btnACommand()
        num1 = float(entry1.get())
        ans = ((3 * math.sqrt(3)) / 2) * num1 ** 2
        messagebox.showinfo("Answer:", str(ans))
        window.destroy()

    def perHeptagon():
        tk.Label(window, text = "Enter in the Number: ", background = "white").place(x = 1115, y = 100)
        tk.Label(window, text = "Length: ", background = "white").place(x = 1110, y = 130)
        global entry1
        entry1 = tk.Entry(window)
        entry1.place(x = 1155, y = 130)
        check1 = tk.IntVar()
        cButton = tk.Checkbutton(window, text = "Enter: ", variable = check1, command = calPerHeptagon)
        cButton.place(x = 1115, y = 160)

    def calPerHeptagon():
        btnACommand()
        num1 = float(entry1.get())
        ans = num1 * 7
        messagebox.showinfo("Answer:", str(ans))
        window.destroy()

    def arHeptagon():
        tk.Label(window, text = "Enter in the Number: ", background = "white").place(x = 1115, y = 100)
        tk.Label(window, text = "Length: ", background = "white").place(x = 1110, y = 130)
        global entry1
        entry1 = tk.Entry(window)
        entry1.place(x = 1155, y = 130)
        check1 = tk.IntVar()
        cButton = tk.Checkbutton(window, text = "Enter: ", variable = check1, command = calArHeptagon)
        cButton.place(x = 1115, y = 160)

    def calArHeptagon():
        btnACommand()
        num1 = float(entry1.get())
        ans = 7/4 * num1 ** 2 * (1 / math.tan(math.radians(180 / 7 )))
        messagebox.showinfo("Answer:", str(ans))
        window.destroy()

    def perOctogon():
        tk.Label(window, text = "Enter in the Number: ", background = "white").place(x = 1115, y = 100)
        tk.Label(window, text = "Length: ", background = "white").place(x = 1110, y = 130)
        global entry1
        entry1 = tk.Entry(window)
        entry1.place(x = 1155, y = 130)
        check1 = tk.IntVar()
        cButton = tk.Checkbutton(window, text = "Enter: ", variable = check1, command = calPerOctogon)
        cButton.place(x = 1115, y = 160)

    def calPerOctogon():
        btnACommand()
        num1 = float(entry1.get())
        ans = num1 * 8 
        messagebox.showinfo("Answer:", str(ans))
        window.destroy()
        
    def arOctogon():
        tk.Label(window, text = "Enter in the Number: ", background = "white").place(x = 1115, y = 100)
        tk.Label(window, text = "Length: ", background = "white").place(x = 1110, y = 130)
        global entry1
        entry1 = tk.Entry(window)
        entry1.place(x = 1155, y = 130)
        check1 = tk.IntVar()
        cButton = tk.Checkbutton(window, text = "Enter: ", variable = check1, command = calArOctogon)
        cButton.place(x = 1115, y = 160)

    def calArOctogon():
        btnACommand()
        num1 = float(entry1.get())
        ans = 2 * (1 + math.sqrt(2))* num1 ** 2
        messagebox.showinfo("Answer:", str(ans))
        window.destroy()

    def perNonagon():
        tk.Label(window, text = "Enter in the Number: ", background = "white").place(x = 1115, y = 100)
        tk.Label(window, text = "Lenght: ", background = "white").place(x = 1110, y = 130)
        global entry1
        entry1 = tk.Entry(window)
        entry1.place(x = 1155, y = 130)
        check1 = tk.IntVar()
        cButton = tk.Checkbutton(window, text = "Enter: ", variable = check1, command = calPerNonagon)
        cButton.place(x = 1115, y = 160)

    def calPerNonagon():
        btnACommand()
        num1 = float(entry1.get())
        ans = num1 * 9
        messagebox.showinfo("Answer:", str(ans))
        window.destory()
        
    def arNonagon():
        tk.Label(window, text = "Enter in the Number: ", background = "white").place(x = 1115, y = 100)
        tk.Label(window, text = "Length: ", background = "white").place(x = 1110, y = 130)
        global entry1
        entry1 = tk.Entry(window)
        entry1.place(x = 1155, y = 130)
        check1 = tk.IntVar()
        cButton = tk.Checkbutton(window, text = "Enter: ", variable = check1, command = calArNonagon)
        cButton.place(x = 1115, y = 160)

    def calArNonagon():
        btnACommand()
        num1 = float(entry1.get())
        ans = (9/4) * num1 ** 2 * (1 / math.tan(math.radians(180/9)))
        messagebox.showinfo("Answer:", str(ans))
        window.destroy()

    def perDecagon():
        tk.Label(window, text = "Enter in the Number: ", background = "white").place(x = 1115, y = 100)
        tk.Label(window, text = "Length: ", background = "white").place(x = 1110, y = 130)
        global entry1
        entry1 = tk.Entry(window)
        entry1.place(x = 1155, y = 130)
        check1 = tk.IntVar()
        cButton = tk.Checkbutton(window, text = "Enter: ", variable = check1, command = calPerDecagon)
        cButton.place(x = 1115, y = 160)

    def calPerDecagon():
        btnACommand()
        num1 = float(entry1.get())
        ans = num1 * 10
        messagebox.showinfo("Answer:", str(ans))
        window.destroy()

    def arDecagon():
        tk.Label(window, text = "Enter in the Number: ", background = "white").place(x = 1115, y = 100)
        tk.Label(window, text = "Length: ", background = "white").place(x = 1110, y = 130)
        global entry1
        entry1 = tk.Entry(window)
        entry1.place(x = 1155, y = 130)
        check1 = tk.IntVar()
        cButton = tk.Checkbutton(window, text = "Enter: ", variable = check1, command = calArDecagon)
        cButton.place(x = 1115, y = 160)

    def calArDecagon():
        btnACommand()
        num1 = float(entry1.get())
        ans = (5/2) * num1 ** 2 * math.sqrt(5 + 2 * math.sqrt(5))
        messagebox.showinfo("Answer:", str(ans))
        window.destroy()

    def Circumference():
        tk.Label(window, text = "Enter in the Radius: ", background = "white").place(x = 1115, y = 100)
        tk.Label(window, text = "Radius: ", background = "white").place(x = 1112, y = 130)
        global entry1
        entry1 = tk.Entry(window)
        entry1.place(x = 1155, y = 130)
        check1 = tk.IntVar()
        cButton = tk.Checkbutton(window, text = "Enter: ", variable = check1, command = calCircumference)
        cButton.place(x = 1115, y = 160)

    def calCircumference():
        btnACommand()
        num1 = float(entry1.get())
        ans = 2 * 3.14 * num1
        messagebox.showinfo("Answer:", str(ans))
        window.destroy()

    def arCircle():
        tk.Label(window, text = "Enter in the Radius: ", background = "white").place(x = 1115, y = 100)
        tk.Label(window, text = "Radius: ", background = "white").place(x = 1112, y = 130)
        global entry1
        entry1 = tk.Entry(window)
        entry1.place(x = 1155, y = 130)
        check1 = tk.IntVar()
        cButton = tk.Checkbutton(window, text = "Enter: ", variable = check1, command = calArCircle)
        cButton.place(x = 1115, y = 160)

    def calArCircle():
        btnACommand()
        num1 = float(entry1.get())
        ans = 3.14 * num1 ** 2
        messagebox.showinfo("Answer:", str(ans))
        window.destroy()

    def btnACommand():
        btn1.destroy()
        btn2.destroy()
        btn3.destroy()
        btn4.destroy()
        btn5.destroy()
        btn6.destroy()
        btn7.destroy()
        btn8.destroy()
        btn9.destroy()
        btn10.destroy()
        btn11.destroy()
        btn12.destroy()
        btn13.destroy()
        btn14.destroy()
        btn15.destroy()
        btn16.destroy()
        btn17.destroy()
        btn18.destroy()
        btn19.destroy()
        btn20.destroy()
        btn21.destroy()
        btn22.destroy()
        btn23.destroy()
        btn24.destroy()
        btn25.destroy()
        btn26.destroy()
        btn27.destroy()
        btn28.destroy()
        btn29.destroy()
        btn30.destroy()
        label1.place_forget()
        label2.place_forget()
        
    window = tk.Tk()
    window.title("Perimeter and Area Calculator")
    window.configure(background = "white")
    label1 = tk.Label(window, text = "Welcome to the Ultimate Area and Perimeter Calculator!", background = "white", font = ("Helvetica", 16))
    label1.place(x = 65, y = 125)
    label2 = tk.Label(window, text = "Please Choose One of the Options on the Right:", background = "white", font = ("Helvetica", 16))
    label2.place(x = 65, y = 160)

    mainFrame = tk.Frame(window).pack()

    btn1 = tk.Button(mainFrame, text = "Perimeter of Triangle", fg = "red", command = perTriangle)
    btn1.place(x = 625, y = 20) 
    btn2 = tk.Button(mainFrame, text = "Area of Triangle", fg = "red", command = arTriangle)
    btn2.place(x = 625, y = 50)
    btn3 = tk.Button(mainFrame, text = "Perimeter of Square", fg = "orange", command = perSquare)
    btn3.place(x = 625, y = 80)
    btn4 = tk.Button(mainFrame, text = "Area of Square", fg = "orange", command = arSquare)
    btn4.place(x = 625, y = 110)
    btn5 = tk.Button(mainFrame, text = "Perimeter of Rectangle", fg = "green", command = perRectangle)
    btn5.place(x = 625, y = 140)
    btn6 = tk.Button(mainFrame, text = "Area of Rectangle", fg = "green", command = arRectangle)
    btn6.place(x = 625, y = 170)
    btn7 = tk.Button(mainFrame, text = "Perimeter of Rhombus", fg = "brown", command = perRhombus)
    btn7.place(x = 625, y = 200)
    btn8 = tk.Button(mainFrame, text = "Area of Rhombus", fg = "brown", command = arRhombus)
    btn8.place(x = 625, y = 230)
    btn9 = tk.Button(mainFrame, text = "Perimeter of Parallelogram", fg = "blue", command = perParallelogram)
    btn9.place(x = 625, y = 260)
    btn10 = tk.Button(mainFrame, text = "Area of Parallelogram", fg = "blue", command = arParallelogram)
    btn10.place(x = 625, y = 290)
    btn11 = tk.Button(mainFrame, text = "Perimeter of Trapezoid", fg = "red", command = perTrapezoid)
    btn11.place(x = 625, y = 320)
    btn12 = tk.Button(mainFrame, text = "Area of Trapezoid", fg = "red", command = arTrapezoid)
    btn12.place(x = 625, y = 350)
    btn13 = tk.Button(mainFrame, text = "Perimeter of Kite", fg = "orange", command = perKite)
    btn13.place(x = 625, y = 380)
    btn14 = tk.Button(mainFrame, text = "Area of Kite", fg = "orange", command = arKite)
    btn14.place(x = 625, y = 410)
    btn15 = tk.Button(mainFrame, text = "Perimeter of Trapezium", fg = "green", command = perTrapezium)
    btn15.place(x = 625, y = 440)
    btn16 = tk.Button(mainFrame, text = "Area of Trapezium", fg = "green", command = arTrapezium)
    btn16.place(x = 625, y = 470)
    btn17 = tk.Button(mainFrame, text = "Perimeter of Pentagon", fg = "brown", command = perPentagon)
    btn17.place(x = 625, y = 500)
    btn18 = tk.Button(mainFrame, text = "Area of Pentagon", fg = "brown", command = arPentagon)
    btn18.place(x = 625, y = 530)
    btn19 = tk.Button(mainFrame, text = "Perimeter of Hexagon", fg = "blue", command = perHexagon)
    btn19.place(x = 625, y = 560)
    btn20 = tk.Button(mainFrame, text = "Area of Hexagon", fg = "blue", command = arHexagon)
    btn20.place(x = 625, y = 590)
    btn21 = tk.Button(mainFrame, text = "Perimeter of Heptagon", fg = "red", command = perHeptagon)
    btn21.place(x = 625, y = 620)
    btn22 = tk.Button(mainFrame, text = "Area of Heptagon", fg = "red", command = arHeptagon)
    btn22.place(x = 625, y = 650)
    btn23 = tk.Button(mainFrame, text = "Perimeter of Octogon", fg = "orange", command = perOctogon)
    btn23.place(x = 625, y = 680)
    btn24 = tk.Button(mainFrame, text = "Area of Octogon", fg = "orange", command = arOctogon)
    btn24.place(x = 625, y = 710)
    btn25 = tk.Button(mainFrame, text = "Perimeter of Nonagon", fg = "green", command = perNonagon)
    btn25.place(x = 625, y = 740)
    btn26 = tk.Button(mainFrame, text = "Area of Nonagon", fg = "green", command = arNonagon)
    btn26.place(x = 625, y = 770)
    btn27 = tk.Button(mainFrame, text = "Perimeter of Decagon", fg = "brown", command = perDecagon)
    btn27.place(x = 790, y = 20)
    btn28 = tk.Button(mainFrame, text = "Area of Decagon", fg = "brown", command = arDecagon)
    btn28.place(x = 790, y = 50)
    btn29 = tk.Button(mainFrame, text = "Circumference of a Circle", fg = "blue", command = Circumference)
    btn29.place(x = 790, y = 80)
    btn30 = tk.Button(mainFrame, text = "Area of a Circle", fg = "blue", command = arCircle)
    btn30.place(x = 790, y = 110)

    image = tk.PhotoImage(file = "shapes.png")
    placeImage = tk.Label(window, image = image)
    placeImage.place(x = 125, y = 250)

    window.mainloop()

