mx = (('X', 'A', 'B', 'N', 'T', 'T'),
      ('Y', 'T', 'N', 'R', 'I', 'E'),
      ('U', 'P', 'O', 'M', 'D', 'S'),
      ('I', 'O', 'H', 'U', 'O', 'T'),
      ('R', 'T', 'E', 'L', 'Q', 'E'),
      ('I', 'W', 'J', 'K', 'P', 'Z'))

def soup(matrix, word):
  order = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F"}
  
  def find(matrix, i, j, word):
    if matrix[i][j] == word[0]:
      if len(word) == 1:
        return True    
      for (a, b) in [(i - 1, j -1), (i + 1, j + 1), (i - 1, j + 1), (i + 1, j - 1), (i, j + 1), (i, j - 1), (i - 1, j), (i + 1, j)]:
        if a >= 0 and b >= 0 and a <= len(mx[0]) - 1 and b <= len(mx) - 1 and matrix[a][b] == word[1] :
          return True and find(matrix, a, b, word[1:]) 
            
  for i in range(len(matrix)): 
    for j in range(len(matrix)):  
      if find(matrix, i, j, word) == True:
        return order[i] + str(j + 1)
      
print(soup(mx, "TESTE"))
    
