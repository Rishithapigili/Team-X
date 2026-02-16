Convert_temperature()
TEAM X

def convert_temperature(value: float,unit:str)-> float | str:
  if unit == 'C':
    return (value * 9/5)+32
  elif unit == 'F':
    return (value - 32)*5/9
  else:
    return "Invalid unit"
value = int(input())
unit = input()
print(convert_temperature(value,unit))
