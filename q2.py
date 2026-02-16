  TEAM X
def convert_seconds(total_seconds):
    minutes = total_seconds//60
    seconds = total_seconds%60
    return f"\"{minutes}m {seconds}s\""
total_seconds = int(input())
print(convert_seconds(total_seconds))
