get_ticket_price()
TEAM X
def get_ticket_price(age:int,is_student:bool) -> int:
  if age<12 and not is_student :
    return 8
  elif age>=65:
    return 10
  else :
    if is_student:
      return 12
    else:
      return 15
age = int(input())
is_student = input()
if is_student == "True":
  is_student = True
else:
  is_student = False
print(get_ticket_price(age,is_student))
