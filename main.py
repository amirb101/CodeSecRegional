import tkinter as tk
from tkinter import ttk

from sympy import false

WEIGHT = 70
HEIGHT = 170
AGE = 21
#RESTINGBPM = 0
WIDTH = 960
HEIGHT = 480

def GetBMI(WEIGHT, HEIGHT):
  BMI = WEIGHT/(HEIGHT**2)
  return BMI

def GetDistance(Distance, unit):
  if unit.lower() == "km":
    return Distance
  elif unit.lower() == "m":
    return Distance/1000
  elif unit.lower() == "cm":
    return Distance/100000
  elif unit.lower() == "mil" or unit.lower() == "miles":
    return Distance*1.61
  

def CaloriesCalculate(Time, Weight, Distance): #minutes, kg, Kilometres
  Speed = Distance/(Time/60)#input time as minutes, convert to hours
  Mph = Speed/1.61 #converts to miles for calculator
  MET = (Mph*1.8)-2 #approximation using online MET values for different speeds
  Calories = ((Time*MET)*(3.5*Weight))/200 #formula for calories burnt

  return Calories

#print(CaloriesCalculate(30, 80, 10000)) #<-- for testing

def LoadData():
  FileHandle = "save.txt"

def BuildWindow():
  window = tk.Tk()
  window.title('Healthy Steps')

  ScreenWidth = window.winfo_screenwidth()
  ScreenHeight = window.winfo_screenheight()

  CenterX = int(ScreenWidth/2 - WIDTH / 2)
  CenterY = int(ScreenHeight/2 - HEIGHT / 2)

  window.resizable(False, False)

  exit_button = ttk.Button(window, text='EXIT', command=lambda: window.quit())
  exit_button.pack()

  window.geometry('{}x{}+{}+{}'.format(WIDTH, HEIGHT, CenterX, CenterY))

  window.mainloop()

def MainLoop():
  #Build GUI Structure
  BuildWindow()
  #Take user inputs for constants named above

  #Save constants to text file

  #If constants are saved to text file they should not be changed

  

  #Call functions
  BMI = GetBMI(WEIGHT, HEIGHT)

if __name__ == "__main__":
  MainLoop()
