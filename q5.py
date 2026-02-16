Claculate()
TEAM X

def calculate(expression: str) -> float:
    expression = expression.replace(" ", "")
    
    total = 0
    last_number = 0
    num = 0
    sign = '+'
    
    for i in range(len(expression)):
        ch = expression[i]
        
        if ch.isdigit():
            num = num * 10 + int(ch)
        
        if ch in "+-*/" or i == len(expression) - 1:
            
            if sign == '+':
                total += last_number
                last_number = num
            
            elif sign == '-':
                total += last_number
                last_number = -num
            
            elif sign == '*':
                last_number = last_number * num
            
            elif sign == '/':
                last_number = last_number / num
            
            sign = ch
            num = 0
    
    total += last_number
    
    return round(total, 2)
expression=input()
print(calculate(expression))
