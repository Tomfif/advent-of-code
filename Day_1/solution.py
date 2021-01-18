
with open("./advent-of-code/Day_1/input.txt") as f:
    inputs = [
        int(line)
        for line in f.read().splitlines()
    ]



def two_entries(numbers):
    for i in numbers:
        for j in numbers:
            if i + j == 2020:
                return i * j


def three_entries(numbers):
    for i in numbers:
        for j in numbers:
            for k in numbers:
                if i + j + k == 2020:
                    return i * j * k



print(two_entries(inputs))
print(three_entries(inputs))