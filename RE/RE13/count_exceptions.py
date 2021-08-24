def count_exceptions(f, n1, n2):
    result = 0
    
    for n in range(n1, n2 + 1):
        try:
            f(n)
            
        except Exception:
            result +=1
                        
    return result     