def parse(filename):
    with open(filename) as file:
        lines = file.readlines()
        result = ""

        for i in range(len(lines)): 
            while " " in lines[i]:
                lines[i]=lines[i].strip(" ")
            lines[i]=lines[i].strip("\n")
        
        for line in lines:
            if line == "(":                
                result += line
                
            else:
                result += line + ","
                
        result = "(" + result + ")"   
        
        return eval(result)
    
print(parse("tuple4.txt"))
