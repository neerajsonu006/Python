num = int(input("Enter the range number: "))
i = 0
f_val = 0
s_val = 1

while i < num:
    if i <= 1:
        next = i
    else:
        next = f_val + s_val
        f_val = s_val
        s_val = next
    print(next)
    i += 1
