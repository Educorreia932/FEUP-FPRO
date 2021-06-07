def formal(name):
    name = name.split()

    last_name = name[-1]  

    result = last_name + ", " 

    for word in name[0: -1]:
        if word[0].upper() == word[0]:
            result += word[0] + ". "    

    return result
