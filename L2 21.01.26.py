import numpy as np
# Слияние и разбиение массивов

# Одномерные
x = np.array([1,2,3])
y = np.array([4,5])
z = np.array([6])

xyz = np.concatenate([x,y,z])
print(xyz)

# Двумерные массивы
x = np.array([[1,2,3],[4,5,6]])
y = np.array([[7,8,9],[10,11,12]])

# Склеиваем dертикально (3 способа) - кубики
xy1 = np.concatenate([x,y])
print(xy1)

xy2 = np.concatenate([x,y], axis=0)
print(xy2)

print(np.vstack([x,y]))

# Склеиваем горизонтально
xy3 = np.concatenate([x,y], axis=1)
print(xy3)

print(np.hstack([x,y]))

# Склеиваем по глубине
print(np.dstack([x,y]))

# количество скобок = количество измерений (0,1,2)

# Разбиение массивов
xy = np.vstack([x,y])
print(xy)

print(np.split(xy, [1], axis=1))
print(np.vsplit(xy, [2]))
print(np.hsplit(xy, [2]))

z = np.dstack([x,y])
print(z)

print(np.dsplit(z,[1]))

import timeit
# Универсальные функции - для ускорения работы с векторами
x = np.arange(1,10)
print(x)
def f(x):
  out = np.empty(len(x))
  for i in range(len(x)):
    out[i] = 1.0 /x[i]
  return out
print(f(x))
print(1.0 / x)
print(timeit.timeit(stmt="f(x)", globals=globals()))
print(timeit.timeit(stmt="1.0/x", globals=globals()))
# *универсальная примерно в 10 раз быстрее!

# УФ. Арифметические функции

x = np.arange(5)
print(x)

print(x+1) # add
print(np.add(x,1))

print(x-1) # substarct
print(x * 2)
print(x / 2)
print(x // 2)

print(-x)
print(x ** 2) # power
print(x % 2)

print(x * 2 - 2)

x = np.arange(-5,5)
print(x)

print(abs(x))
print(np.abs(x))
print(np.absolute(x))

x = np.array([3 + 4j, 4 - 3j])
print(abs(x))
print(np.abs(x))

# УФ. тринометрические
# sin, cos, tan, arcsin, arccos, arctan

# УФ. показательные и логарифмы
# exp, power, log, log2, log10

x =[0, 0.0001, 0.001, 0.01, 0.1]
print("exp=", np.exp(x))
# для повышения точности exp -1
print("exp -1 =", np.expm1(x))

print("log(x) = ", np.log(x))
print("log(1+x) = ", np.log1p(x))

# УФ

x = np.arange(5)
print(x)
y = x * 10
print(y)

y = np.multiply(x, 10)
print(y)

z = np.empty(len(x))
np.multiply(x, 10, out=z)
print(z)

x = np.arange(5)
z = np.zeros(10)
print(x)
print(z)
z[::2] = x*10
# 0 0 10 0 20 0 30 40 0
print(z)

z = np.zeros(10)
np.multiply(x, 10, out=z[::2])
print(z)

# Сводные показатели
x = np.arange(1, 5)
print(x)
print(np.add.reduce(x))
print(np.add.accumulate(x))

x = np.arange(1, 10)
print(np.add.outer(x, x))

print(np.multiply.outer(x, x))

# Агрегирование

np.random.seed(1)
s = np.random.random(100)
print(sum(s))
print(np.sum(s))

a = np.array([[1,2,3,4,5], [6, 7, 8, 9, 10]])
print(sum(a))
print(np.sum(a))
print(np.sum(a, axis=0))

print(type(a))
print(a.sum())
print(a.sum(0))
print(a.sum(1))

print(sum(a,2))

# Минимум и максимум
np.random.seed(1)
s = np.random.random(100)

print(min(s))
print(np.min(s))

print(max(s))
print(np.max(s))

# mean, std, var, median, argmin, argmax, percentitle, any, all (на будещее)
# nan*
# Nor a number - NaN

# Транслирование (broadcasting)

a = np.array([1,2,3])
b = np.array([5,5,5])
print(a+b)
# Правила транслирования
# 1. Если размеры массивов разные, к меньшему дописываем слева 1
# 2. Если в каком-то измерении размеры не совпадают и в каком-то массиве измерение = 1, то 1 превращаем в 3.
# 3. Если размеры не совпадают и нет 1, пишем ошибку
