Q1.
import numpy as np

arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

print("1D Array:")
print(arr1)
print("Shape:", arr1.shape)
print("Data Type:", arr1.dtype)

print("\n2D Array:")
print(arr2)
print("Shape:", arr2.shape)
print("Data Type:", arr2.dtype)



Q2.
import numpy as np

a = np.zeros(8)
b = np.ones((4, 4))
c = np.zeros((3, 3))

print("1D Array of 8 zeros:")
print(a)

print("\n4x4 Array of ones:")
print(b)

print("\n3x3 Matrix of zeros:")
print(c)



Q3.
import numpy as np

a = np.arange(0, 21, 1)
b = np.arange(10, 51, 2)
c = np.arange(5, 101, 5)

print("0 to 20:")
print(a)

print("\nEven numbers from 10 to 50:")
print(b)

print("\n5 to 100 (step 5):")
print(c)




Q4.
import numpy as np

a = np.linspace(0, 5, 10)
b = np.linspace(-10, 10, 15)

print("10 equally spaced numbers:")
print(a)
print("Length:", len(a))

print("\n15 equally spaced numbers:")
print(b)
print("Length:", len(b))



Q5.
import numpy as np

a = np.random.rand(10)
b = np.random.randn(3, 3)
c = np.random.randint(10, 51, (4, 5))

print("Random numbers (0 to 1):")
print(a)

print("\n3x3 Standard Normal Matrix:")
print(b)

print("\n4x5 Random Integers (10 to 50):")
print(c)




Q6.
import numpy as np

v1 = np.array([2, 4, 6, 8])
v2 = np.array([1, 3, 5, 7])

print("Addition:")
print(v1 + v2)

print("\nSubtraction:")
print(v1 - v2)

print("\nElement-wise Multiplication:")
print(v1 * v2)

print("\nDot Product:")
print(np.dot(v1, v2))



Q7.
import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

B = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

print("Matrix Addition:")
print(A + B)

print("\nMatrix Multiplication:")
print(np.dot(A, B))

print("\nElement-wise Multiplication:")
print(A * B)



Q8.
import numpy as np

arr = np.random.randint(1, 101, (4, 4))

print("4x4 Matrix:")
print(arr)

print("\nShape:", arr.shape)
print("Dimension (ndim):", arr.ndim)
print("Total Elements (size):", arr.size)
print("Data Type:", arr.dtype)
print("Minimum Value:", arr.min())
print("Maximum Value:", arr.max())



Q9.
import numpy as np

arr = np.random.randint(1, 51, 20)

print("1D Array:")
print(arr)

matrix = arr.reshape(4, 5)

print("\n4x5 Matrix:")
print(matrix)

print("\nSum:", matrix.sum())
print("Mean:", matrix.mean())
print("Standard Deviation:", matrix.std())

print("\nMaximum Value in Each Row:")
print(matrix.max(axis=1))




Q10.
import numpy as np

try:
    n = int(input("Enter how many random numbers to generate: "))

    arr = np.random.randint(10, 101, n)

    print("\nArray:")
    print(arr)

    print("\nMean:", np.mean(arr))
    print("Median:", np.median(arr))
    print("Standard Deviation:", np.std(arr))
    print("Minimum:", np.min(arr))
    print("Maximum:", np.max(arr))

    if n % 2 == 0:
        matrix = arr.reshape(2, n // 2)
        print("\nReshaped 2D Array:")
        print(matrix)

        print("\nRow-wise Sum:")
        print(np.sum(matrix, axis=1))
    else:
        print("\nCannot reshape into a 2D array because the number of elements is odd.")

except ValueError:
    print("Please enter a valid integer.")
