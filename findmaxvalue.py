numbers = [1,2,-3,-5,6,7,0,-4,9,10]


def sort_numbers(numbers):
    lenth = len(numbers)
    lenth = int(len(numbers))
    for i in range(0, lenth - 1):
        for j in  range(i+1,lenth):
            if numbers[i] > numbers[j]:
                tmp = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = tmp
        
    return numbers

print("Mảng trước khi sắp xếp")
print(numbers)
 
print("Mảng sau khi sắp xếp")
print(sort_numbers(numbers))

a = sort_numbers(numbers)[-2]
b = sort_numbers(numbers)[-1]
print("Hai số lớn nhất trong list là: ", a ,",", b)