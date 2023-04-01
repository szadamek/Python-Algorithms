import numpy as np

def multiplying_matrix(A, B):
    n = len(A)
    C = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C


if __name__ == '__main__':
    # a = np.array([[1, 2], [3, 4]])
    # b = np.array([[5, 6], [7, 8]])
    # a = np.array([[1, 2, 3, 4], [5, 6, 7, 8],
    #                 [9, 10, 11, 12], [13, 14, 15, 16]])
    # b = np.array([[17, 18, 19, 20], [21, 22, 23, 24],
    #                 [25, 26, 27, 28], [29, 30, 31, 32]])
    a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    b = np.array([[10, 11, 12], [13, 14, 15], [16, 17, 18]])
    print(multiplying_matrix(a, b))
