def compatible(A, B):
    if len(A[0]) != len(B):
        return AssertionError("A and B cannot be multiplied")
    
    else:
        return "A and B can be multiplied"