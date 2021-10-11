import numpy as np

grades = np.array([[87, 96, 70], [100, 87, 90], [94, 77, 90], [100, 81, 82]])

student1 = grades[1]

student0_test1 = grades[0,1]
student5 =grades[0,0]

all_students_test0 = grades[:, 0]

all_students_test1_2 = grades[:,1:3]

all_students_test0and2 = grades[:,[0,2]]



grades1 = np.array(np.random.randint(60, 101,12,).rehape(3,4))

print(grades1.mean(axis=0))
print(grades1.mean(axis=1))
numbers_copy = numbers.copy()

               9

numbers[1] *= 10


print()