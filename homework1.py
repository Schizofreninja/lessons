example = 'Топинамбур' # 1
print(example[:1]) # 2
print(example[-1:]) # 3
print(example[5:]) # 4
# второй вариант решения задачи в п.4 (из интернета, но понравился)
second_half = example[len(example)//2:]
print(second_half)

print(example[::-1]) # 5
print(example[1::2]) # 6
