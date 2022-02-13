from ast import expr_context
import tkinter as tk
from math import floor
from sympy import false

WIDTH = 960
HEIGHT = 480

def GetBMI(WEIGHT, HEIGHT):
  BMI = WEIGHT/(HEIGHT**2)
  return BMI

def CaloriesCalculate(Time, Weight, Distance): #minutes, kg, Kilometres
  Speed = Distance/(Time/60)#input time as minutes, convert to hours
  Mph = Speed/1.61 #converts to miles for calculator
  MET = (Mph*1.8)-2 #approximation using online MET values for different speeds
  Calories = ((Time*MET)*(3.5*Weight))/200 #formula for calories burnt

  return Calories

global Inputs
Inputs = [0,0,0,0,0,0,0,0]


def BuildWindow():
  window = tk.Tk()
  window.title('Healthy Steps')

  ScreenWidth = window.winfo_screenwidth()
  ScreenHeight = window.winfo_screenheight()

  CenterX = int(ScreenWidth/2 - WIDTH / 2)
  CenterY = int(ScreenHeight/2 - HEIGHT / 2)

  window.resizable(False, False)


  def GetHeightAgeWeight():
    Age = AgeBox.get("1.0", "end").strip()
    Height = HeightBox.get("1.0", "end").strip()
    Weight = WeightBox.get("1.0", "end").strip()

    # print(Age, Height, Weight)
    Inputs[0]= Age
    Inputs[1]= Height
    Inputs[2]= Weight

    Inputs[6] = True

  HeightBox = tk.Text(window, height=1)
  HeightBox.insert("1.0", "Enter Height (m)")
  HeightBox.pack()

  AgeBox = tk.Text(window, height=1)
  AgeBox.insert("1.0", "Enter Age (yrs)")
  AgeBox.pack()

  WeightBox = tk.Text(window, height=1)
  WeightBox.insert("1.0", "Enter Weight (kg)")
  WeightBox.pack()

  SubmitButton1 = tk.Button(window, height=1, width = 30, text = "Submit Height, Age, Weight.", command = GetHeightAgeWeight)
  SubmitButton1.pack()


  def GetDayDistanceTime():
    Day = DayBox.get("1.0", "end").strip()
    Distance = DistanceBox.get("1.0", "end").strip()
    Time = TimeBox.get("1.0", "end").strip()

    # print(Day, Distance, Time)
    Inputs[3] = Day.lower()
    Inputs[4] = Distance    
    Inputs[5] = Time

    Inputs[7] = True

  DayBox = tk.Text(window, height=1)
  DayBox.insert("1.0", "Enter day (mon, tues, wed..)")
  DayBox.pack()

  DistanceBox = tk.Text(window, height=1)
  DistanceBox.insert("1.0", "Enter Distance (km)")
  DistanceBox.pack()

  TimeBox = tk.Text(window, height=1)
  TimeBox.insert("1.0", "Enter time taken for walk (mins)")
  TimeBox.pack()

  SubmitButton2 = tk.Button(window, height=1, width = 30, text = "Submit Day, Distance, Time.", command = GetDayDistanceTime)
  SubmitButton2.pack()

  # if Inputs[6] and Inputs[7]:

  window.geometry('{}x{}+{}+{}'.format(WIDTH, HEIGHT, CenterX, CenterY))

  while 1:
    window.update_idletasks()
    window.update()
    if Inputs[6] and Inputs[7]:
      try:
        Calories = floor(CaloriesCalculate(int(Inputs[5]), int(Inputs[2]), int(Inputs[4])))
      except:
        Calories = 0
      CaloriesBox = tk.Label(window, height=1, text="You have burnt {} calories during the inputted session".format(str(Calories)))
      CaloriesBox.pack()
      try:
        BMI = floor(GetBMI(int(Inputs[2]), int(Inputs[1])))
      except:
        BMI = 0
      BMIBOX = tk.Label(window, height=1, text= "Your BMI is {}".format(str(BMI)))
      BMIBOX.pack()
      for i in range(len(Inputs)):
        Inputs[i] = '0'


if __name__ == "__main__":
  BuildWindow()
