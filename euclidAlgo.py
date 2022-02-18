def algo(top, bottom):
    if bottom > top:
        temp = bottom
        bottom = top
        top = temp
    sequence = [top, bottom]
    while(sequence[-1] != 0):
        rem = top % bottom
        sequence.append(rem)
        top = bottom
        bottom = rem
    return sequence

if __name__ == "__main__":
    # Ex. 498672943
    firstValue = int(input("input first number: "))
    # Ex. 520221547
    secondValue = int(input("input second number: "))
    sequence = algo(firstValue, secondValue)
    print(sequence)
