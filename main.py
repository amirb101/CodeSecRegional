WEIGHT = 70
HEIGHT = 170
AGE = 21
#RESTINGBPM = 0


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
  

def CaloriesBurnt(WEIGHT, HEIGHT, AGE, Distance, Time):
  Calories = 0

  return Calories

def MainLoop():
  #Build GUI Structure


  #Take user inputs for constants named above

  #Save constants to text file

  #If constants are saved to text file they should not be changed

  

  #Call functions
  BMI = GetBMI(WEIGHT, HEIGHT)

if __name__ == "__main__":
  MainLoop()