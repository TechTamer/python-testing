def do_repeat(f,n):
    f() * n

corner = "+"
row = "-"
beam = "|"
filler = " "
width=4
num_across=3
num_down=2

print(((corner + (row * width   )) * num_across) + corner)
print(((beam   + (filler * width)) * num_across) + beam)
print(((beam   + (filler * width)) * num_across) + beam)
print(((beam   + (filler * width)) * num_across) + beam)
print(((beam   + (filler * width)) * num_across) + beam)
print(((corner + (row * width   )) * num_across) + corner)
print(((beam   + (filler * width)) * num_across) + beam)
print(((beam   + (filler * width)) * num_across) + beam)
print(((beam   + (filler * width)) * num_across) + beam)
print(((beam   + (filler * width)) * num_across) + beam)
print(((corner + (row * width   )) * num_across) + corner)

def print_beams(box_width):
    print(((beam   + (filler * box_width)) * num_across) + beam)

#do_repeat(print_beams,width)



