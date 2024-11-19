import numpy as np
import matplotlib.pyplot as plt

# Функція для перевірки закону Бенфорда
def check_benford(numbers):
    # Визначення кількості цифр, що починаються з 1-9
    first_digits = [int(str(num)[0]) for num in numbers if num > 0]
    counts = [first_digits.count(i) for i in range(1, 10)]
    total = sum(counts)
    frequencies = [count / total for count in counts]
    return frequencies

# Генерація чисел за розподілом Бернуллі
bernoulli_numbers = np.random.binomial(n=1, p=0.5, size=10000)
bernoulli_numbers = np.where(bernoulli_numbers == 1, 
                             np.random.randint(100000, 1000000, size=10000), 
                             0)

# Генерація чисел за розподілом Пуассона
poisson_numbers = np.random.poisson(lam=3, size=10000)
poisson_numbers = poisson_numbers / np.max(poisson_numbers) * 899999 + 100000
poisson_numbers = poisson_numbers.astype(int)

# Перевірка закону Бенфорда для обох розподілів
bernoulli_frequencies = check_benford(bernoulli_numbers)
poisson_frequencies = check_benford(poisson_numbers)

# Частоти за законом Бенфорда
benford_frequencies = [np.log10(1 + 1 / i) for i in range(1, 10)]

# Візуалізація результатів
fig, ax = plt.subplots()
index = np.arange(1, 10)
bar_width = 0.25
opacity = 0.8

rects1 = ax.bar(index, bernoulli_frequencies, bar_width,
                alpha=opacity, color='b', label='Bernoulli')

rects2 = ax.bar(index + bar_width, poisson_frequencies, bar_width,
                alpha=opacity, color='r', label='Poisson')

rects3 = ax.bar(index + 2*bar_width, benford_frequencies, bar_width,
                alpha=opacity, color='g', label='Benford\'s Law')

ax.set_xlabel('Digits')
ax.set_ylabel('Frequency')
ax.set_title('Benford\'s Law Verification')
ax.set_xticks(index + bar_width)
ax.set_xticklabels(range(1, 10))
ax.legend()

plt.show()
