josephus_permutation = [int(num) for num in input().split()]
k = int(input())
new_list = []

while len(josephus_permutation) != 0:
    for index in range(len(josephus_permutation)):
        if index % k == 0 and index != 0:
            new_list.append(josephus_permutation[index - 1])
            josephus_permutation.pop(index - 1)


print(new_list)