def rec_exceptions(l):
    result = []
    
    for function in l:
        try:
            function()
            
        except Exception as ex:
            result.append(ex)
            
        else:
            result += rec_exceptions(function())
        
    return result
