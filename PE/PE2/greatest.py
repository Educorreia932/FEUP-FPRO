def greatest(num):
    result = ""
    list = []
    
    for digit in str(num):
        list.append(digit)
        
    list = sorted(list, reverse = True)
    
    for number in list:
        result += str(number)
    
    return int(result)