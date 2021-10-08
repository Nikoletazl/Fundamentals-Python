string = "".join(input())
new_string = string.split()
numbers = []
list_string = []

for el in string:
    if el.isdigit():
        numbers.append(el)
    else:
        list_string.append(el)

new_numbers = [int(num) for num in numbers]
take_list = []
skip_list = []

for num in range(len(new_numbers)):
    if num % 2 == 0:
        take_list.append(new_numbers[num])
    else:
        skip_list.append(new_numbers[num])

result_string = []

while take_list and skip_list != 0:
    result_string.append(list_string[:take_list[0]])
    del list_string[:skip_list[0]]
    take_list.pop(0)
    skip_list.pop(0)
print(result_string)







