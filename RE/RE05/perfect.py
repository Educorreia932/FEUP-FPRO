def is_perfect(n):
    result = 0
    
    if n == 1: 
        return True
    
    else:
        for i in range(1, n + 1):
            if n % i == 0:
                result = result + i
    
    if result == n:
        return True
    
    else:
        return False
  
print(is_perfect(0))
      
