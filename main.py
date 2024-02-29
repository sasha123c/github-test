def find_largest_abs(matrix):
  n = len(matrix)
  max_val = abs(matrix[0][0])
  max_row = max_col = 0

  for i in range(n):
      for j in range(n):
          if abs(matrix[i][j]) > max_val:
              max_val = abs(matrix[i][j])
              max_row = i
              max_col = j

  return max_val, max_row, max_col

def remove_row_and_col(matrix, row, col):
  return [row[:col] + row[col+1:] for row in (matrix[:row]+matrix[row+1:])]

def main():
  n = int(input("Введіть розмірність квадратної матриці: "))
  if n <= 0:
      print("Некоректний розмір матриці.")
      return

  print("Введіть елементи матриці:")
  matrix = [[float(input()) for _ in range(n)] for _ in range(n)]

  max_val, max_row, max_col = find_largest_abs(matrix)
  print("Найбільший за модулем елемент:", max_val)

  new_matrix = remove_row_and_col(matrix, max_row, max_col)

  print("Матриця без рядка", max_row + 1, "та стовпця", max_col + 1, ":")
  for row in new_matrix:
      print('\t'.join(map(str, row)))

if __name__ == "__main__":
  main()
