   Team x
def average_passing_grades(grades: list[int])->float:
      avg1 = 0
      for i in grades:
        avg1 += i/len(grades)
      if avg1>=50:
        return avg1
      else:
        return 0.0
grades = [int(x) for x in input().split()]
print(average_passing_grades(grades))
