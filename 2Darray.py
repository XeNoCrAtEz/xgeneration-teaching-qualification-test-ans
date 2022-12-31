# This function performs matrix additioin
# e.g mat1=[[1, 2, 3], [3, 4, 2]]
# mat2=[[4, 2, 3], [1, 3, 7]]
# Output:
# 5 4 6
# 4 7 9
def add_matrix(mat1, mat2):
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        raise ValueError("Cannot add matrices, both dimensions are different!")

    return [[mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]

    # more readable format
    # result_mat = []
    # for i in range(len(mat1)):
    #     row = []
    #     for j in range(len(mat1[0])):
    #         row.append(mat1[i][j] + mat2[i][j])
    #     result_mat.append(row)
    # return result_mat

mat1=[[3, 2, 3], [1, 4, 2]]
mat2=[[4, 2, 3], [1, 3, 7]]
print(add_matrix(mat1, mat2))