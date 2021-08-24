def exception_str(f):
    try:
        f()
    
    except Exception as ex:
        return(str(ex))
        
    else:
        return("No exception was raised")