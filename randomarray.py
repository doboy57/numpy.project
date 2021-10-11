import numpy as np
import random


b = np.array(np.random.randint(1, 10, size=(2, 5)))

arr06 = np.arange(5)

arr07 = np.arange(5, 10)

arr08 = np.arange(10, 1, -2)

arr09 = np.linspace(0.0, 1.0, num=5)

arr10 = np.arange(1, 21).reshape(4, 5)

num01 = np.arange(1, 6)

num02 = num01 * 2

num03 = num01 ** 3


num01 += 10

grades = np.array([[87, 96, 70], [100, 87, 90], [94, 77, 90], [100, 81, 82]])

print(grades.sum())
print(grades.mean())
print(grades.std())
print(grades.var())

grades_by_exam = grades.mean(axis=0)
grades_by_student = grades.mean(axis=1)

num07 = np.array([1, 4, 9, 16, 25, 36])
num08 = np.sqrt(num07)
num09 = np.array([10, 20, 30, 40, 50, 60])
num10 = np.add(num07, num09)
# multiplying by a scalar value is broadcasting will be on midterm
num11 = np.multiply(num09, 5)
num12 = num09.reshape(2, 3)
num13 = np.array([2, 4, 6])
num14 = np.multiply(num12, num13)

print()
