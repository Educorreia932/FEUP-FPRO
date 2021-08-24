def raise_exception(alist, value):
    result = []
    
    for number in alist:
        if number <= value:
            result.append(ValueError(str(number) + " is not greater than " + str(value)))
            
    return result
    