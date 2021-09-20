my_list1 = [1, 2, 3, 4, 5, 6, 7, 100, 110, 21, 33, 32, 2, 4]
even_numbers = []
odd_numbers = []
outliners = []


for i in range(len(my_list1)):
    if my_list1[i] < 90:
        if my_list1[i] % 2 == 0:
            even_numbers.append(my_list1[i])
        else:
            odd_numbers.append(my_list1[i])
    else:
        outliners.append(my_list1[i])


print(even_numbers)
print(odd_numbers)
print(outliners)


# Cumulative sum

my_list = [1, 2, 3, 4, 5, 6, 7, 100, 110, 21, 33, 32, 2, 4]
cumulative_sum_list = []

for i in range(len(my_list)):

    cumulative_sum_list.append(sum(my_list[:i+1]))

print(cumulative_sum_list)
