paras = ['twinkle twinkle little star',
         'how i wonder what you are',
         'up above the world so high',
         'like a diamond in the sky']
poem = " ".join(paras)
print(poem)

poem = ",".join(paras)
print(poem)

poem = "\n".join(paras)
print(poem)

name = ' apple banana '
print(name,len(name))

name_cleaned = name.strip()
print(name_cleaned,len(name_cleaned))

name_cl_left = name.lstrip()
print(name_cl_left,len(name_cl_left))

name_cl_right = name.rstrip()
print(name_cl_right,len(name_cl_right))