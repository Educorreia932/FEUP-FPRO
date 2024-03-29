from functools import reduce

def reduce_map_filter(args):
  if args[0] == "map":
    return list(map(args[1], reduce_map_filter(args[2])))
    
  elif args[0] == "filter":
    return list(filter(args[1], reduce_map_filter(args[2])))     
    
  elif args[0] == "reduce": 
    return int(reduce(args[1], reduce_map_filter(args[2])))
  
  elif type(args) == list:
    return args    