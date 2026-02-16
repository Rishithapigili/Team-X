sanitize_email()
TEAM X

def sanitize_email(raw_input:str)->str:
  raw_input = raw_input.strip().lower()
  if raw_input.count("@") == 1:
    return raw_input
  else:
    return "Invalid Email"
raw_input = input()
print(sanitize_email(raw_input))
