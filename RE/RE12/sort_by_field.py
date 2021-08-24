def sort_by_field(filename, field):
    with open(filename, "r") as file:
        order = {}
        counter = 0
        lines = file.readlines()
        result = lines[0]
        first = result[:-1].split(",")
        lines = lines[1:]
        lines[-1] += "\n"
        
        for element in first:
            order[element] = counter
            counter += 1        

        def sorting_rule(line):
            line = line.split(",")
                          
            return line[order[field]]
            
        result_list = sorted(lines, key = sorting_rule) 

        for line in result_list:
            print(result)
            result += line 
            
        return result 
        