count_inventory()
TEAM X

def count_inventory(fruit_list:list[str])->dict[str,int]:
  freq = {}
  for i in fruit_list:
    freq[i] = freq.get(i,0)+1
  return freq
fruit_list = input().split()
print(count_inventory(fruit_list))
