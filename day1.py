from aocd import data

input_list = [int(n) for n in data.splitlines()]


##### Star 1 ####
increase = 0
i = 1
while i < len(input_list):
    if input_list[i-1] < input_list[i]:
        increase = increase + 1
    i = i+1
print(increase)


#### Star 2 ####
