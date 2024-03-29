set1 = {1, 2, 3}
set2 = {3, 4, 5, 6}
union = set1.union(set2)
# print(new_set)

intersection = set1.intersection(set2)
# print(intersection)

my_set = {"apple", "banana", "orange", "banana", "kiwi"}
# print(len(my_set))


def common(input1, input2):
    return input1.intersection(input2)


# print(common(set1, set2))

vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
word = {"h", "e", "l", "l", "o"}
print(common(vowels, word))
