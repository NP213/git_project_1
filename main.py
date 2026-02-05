from add import add
from subtract import subtract
from multiply import multiply
from divide import divide
def calculator():
    a = float(input("첫 번째 숫자: "))
    b = float(input("두 번째 숫자: "))
    op = input("연산자 (+, -, *, /): ")
    operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
    }
    if op in operations:
       try:
           result = operations[op](a, b)
           print("result:", result)
       except Exception as e:
           print("error:", e)
       else:
           print("Invalid operator")
if __name__ == "__main__":
    calculator()
