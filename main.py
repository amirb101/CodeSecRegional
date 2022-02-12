from sqlite3 import Time
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

  def GetHeightAgeWeight():
    Age = AgeBox.get("1.0", "end")
    Height = HeightBox.get("1.0", "end")
    Weight = WeightBox.get("1.0", "end")

    print(Age, Height, Weight)

  HeightBox = tk.Text(window, height=1)
  HeightBox.insert("1.0", "Enter Height (m)")
  HeightBox.pack()

  AgeBox = tk.Text(window, height=1)
  AgeBox.insert("1.0", "Enter Age (yrs)")
  AgeBox.pack()

  WeightBox = tk.Text(window, height=1)
  WeightBox.insert("1.0", "Enter Weight (kg)")
  WeightBox.pack()

  SubmitButton1 = tk.Button(window, height=1, width = 10, text = "Submit Height, Age, Weight.", command = GetHeightAgeWeight())
  SubmitButton1.pack()

  def GetDayDistanceTime():
    Day = DayBox.get("1.0", "end")
    Distance = DistanceBox.get("1.0", "end")
    Time = TimeBox.get("1.0", "end")

    print(Day, Distance, Time)


  DayBox = tk.Text(window, height=1)
  DayBox.insert("1.0", "Enter day (mon, tues, wed..)")
  DayBox.pack()

  DistanceBox = tk.Text(window, height=1)
  DistanceBox.insert("1.0", "Enter Distance (km)")
  DistanceBox.pack()

  TimeBox = tk.Text(window, height=1)
  TimeBox.insert("1.0", "Enter time taken for walk")
  TimeBox.pack()

  SubmitButton2 = tk.Button(window, height=1, width = 10, text = "Submit Day, Distance, Time.", command = GetDayDistanceTime())
  SubmitButton2.pack()

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
