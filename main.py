with open('input.txt', 'r') as f:
    N = int(f.readline().strip())

# Подсчет количества единиц для каждого числа от 0 до N
results = []
for num in range(0, N + 1):
    count_ones = bin(num).count('1')
    results.append(str(count_ones))

# Запись результата
with open('output.txt', 'w') as f:
    f.write('\n'.join(results))