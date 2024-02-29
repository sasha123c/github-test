str = input("Введіть рядок: ")

dot_index = str.find(';')

before_dot = dot_index
after_dot = len(str) - dot_index - 2

print("Кількість символів до крапки з комою:", before_dot)
print("Кількість символів після крапки з комою:", after_dot)
