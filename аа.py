digit, count, sp = str(int(input())), 0, []
if (len(digit)) <= 3:
    print(digit)
else:
    digit = digit[::-1]
    for i in digit:
        sp.append(i)
        count += 1
        if count == 3:
            sp.append(',')
            count = 0
    if len(digit) > 5 and len(digit) % 3 == 0:
        if len(digit) % 2 == 0:
            print(''.join(sp[len(digit)::-1]))
        else:
            print(''.join(sp[len(digit) + 1::-1]))
    else:
        print(''.join(sp[::-1]))
