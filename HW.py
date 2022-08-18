def Max_number(*number):
    maxNum = 0
    for i in number:
        if i > maxNum:
            maxNum = i
    return 'Answer for Q2', maxNum


print(Max_number(1, 2, 3, 4, 5, 6, 7))


def Time_number_im_ar(num1, *allnumber):
    count = 0
    for i in allnumber:
        if num1 == i:
            count += 1
    return 'Answer for Q2', count


print(Time_number_im_ar(1, 2, 1, 1, 2,1))


def recursion(num):
      if (num > 0):
        result = num + recursion(num - 1)
        print(result)
      else:
        result = 0
      return result


recursion(2)

def Max_number1(*number):
    return 'Answer for Q2', max(number)


print(Max_number1(1, 2, 3, 4, 5, 6, 7))
