def Max_number(*number):
    max_num = 0
    for i in number:
        if i > max_num:
            max_num = i
    return 'Answer for Q2', max_num


print(Max_number(1, 2, 3, 4, 5, 6, 7))


def Time_number_im_ar(num1, *all_number):
    count = 0
    for i in all_number:
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

def Max_number1(*numbers):
    return 'Answer for Q2', max(numbers)


print(Max_number1(1, 2, 3, 4, 5, 6, 7))
