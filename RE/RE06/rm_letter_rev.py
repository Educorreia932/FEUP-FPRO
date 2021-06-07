def rm_letter_rev(l, astr):
    result = astr.replace(l, "")[::-1]
    return result

print(rm_letter_rev("s", "A Style Guide is about consistency"))

    
      