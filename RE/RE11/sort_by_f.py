def sort_by_f(l):
  return sorted(l, key = lambda a: 5 - a if a >= 5 else a)
  