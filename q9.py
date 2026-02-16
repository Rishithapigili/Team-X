generate_threes()
TEAM X
def generate_threes(start:int,end:int)->list[int]:
  list1 = []
  for i in range(start,end,3):
      list1.append(i)
  return list1
start = int(input())
end = int(input())
print(generate_threes(start,end))
