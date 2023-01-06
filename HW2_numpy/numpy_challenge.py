from operator import matmul
import numpy as np


# принимает 2 матрицы, перемножает их по соответствующим правилам и выдаёт получившуюся матрицу
def matrix_multiplication(matrix1, matrix2):
    return np.matmul(matrix1, matrix2)

# принимает список с матрицами, и выдаёт True, если они могут быть перемножены друг на друга в порядке, 
# в котором они находятся в списке, и False, если их нельзя перемножить.
def multiplication_check(matrixlist):
    if len(matrixlist) == 1 or len(matrixlist)== 0:
        return False
    else:
        for i in range(len(matrixlist) - 1):
           if matrixlist[i].shape[1] != matrixlist[i+1].shape[0]:
            return False
        return True     


# принимает список с матрицами, и выдаёт результат перемножения, если его можно получить, или возвращает
# None, если их нельзя перемножить
def multyply_matrices(matrixlist):
    if multiplication_check(matrixlist):
        
        for i in range(len(matrixlist) - 1):
            pass
    else:
        return None
        



def compute_2d_distance(ar1, ar2):
    return np.linalg.norm(ar2 - ar1)

def compute_multidimensional_distance(ar1, ar2):
    return np.linalg.norm(ar2 - ar1)

def compute_pair_distances(ar1, ar2):
    pass

if __name__=="__main__":
    a = np.full((3, 3), 0)
    b = np.eye(3) + np.arange(stop=21, step = 2)
    c = np.array(((1, 2),
                (3, 4)))
    