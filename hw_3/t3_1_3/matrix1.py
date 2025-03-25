import numpy as np

class Matrix:
    def __init__(self, mtx):

        self.mtx = mtx
        self._H = len(mtx)
        self._W = len(mtx[0]) 
        for row in mtx:
            if len(row) != self.W:
                raise ValueError("not a matrix")
    @property
    def H(self):
        return self._H
    
    @property
    def W(self):
        return self._W
    
    @property
    def mtx(self):
        return self._mtx
    
    def is_matrix(self, mtx):
        W = len(mtx[0])
        for row in mtx:
            if len(row) != W:
                return False
        return True
    
    @mtx.setter
    def mtx(self, new_mtx):
        W = len(new_mtx[0])
        if not self.is_matrix(new_mtx):
                raise ValueError("not a matrix")
        self._mtx = new_mtx
    
    def __add__(self,other):
        if self.H != other.H or self.W != other.W:
            raise ValueError("matrices can't be added: got ({},{}) and ({},{}) shapes".format(self.H,self.W,other.H,other.W))
        result = [row[:] for row in self.mtx]
        for i in range(self.H):
            for j in range(self.W):
                result[i][j] += other.mtx[i][j]
        return Matrix(result)

        
    def __mul__(self, other):
        if self.H != other.H or self.W != other.W:
            raise ValueError("matrices can't be multiplied (element-wise): got ({},{}) and ({},{}) shapes".format(self.H,self.W,other.H,other.W))
        result = [row[:] for row in self.mtx]
        for i in range(self.H):
            for j in range(self.W):
                result[i][j] *= other.mtx[i][j]    
        return Matrix(result)

    def __matmul__(self,other):
        if self.W != other.H:
            raise ValueError("matrices can't be multiplied: got ({},{}) and ({},{}) shapes".format(self.H,self.W,other.H,other.W))
        result = [[0 for j in range(other.W)] for i in range(self.H)]
        for i in range(self.H):
            for j in range(other.W):
                tmp_sum = 0
                for k in range(other.H):
                    tmp_sum += self.mtx[i][k]*other.mtx[k][j]
                result[i][j] = tmp_sum
        return Matrix(result)
    
    def __str__(self):
        res = ''
        for row in self.mtx:
            res += str(row)
            res += '\n'
        return res

def write_result(file, A, B, result):
    file.write("A: \n")
    file.write(str(A))
    file.write("B: \n")
    file.write(str(B))
    file.write("result: \n")  
    file.write(str(result))  


if __name__ == "__main__":
    np.random.seed(0)
    A = np.random.randint(0, 10, (10, 10))
    B = np.random.randint(0, 10, (10, 10))
    mtxA = Matrix(A.tolist())
    mtxB = Matrix(B.tolist())
    assert ((mtxA + mtxB).mtx == (A+B)).all()
    assert ((mtxA * mtxB).mtx == (A*B)).all()
    assert ((mtxA @ mtxB).mtx == (A@B)).all()
    file1 = open("t3_1_3/1/matrix+.txt", 'w')
    file2 = open("t3_1_3/1/matrix*.txt", 'w')
    file3 = open("t3_1_3/1/matrix@.txt", 'w')
    write_result(file1, mtxA, mtxB, mtxA+mtxB)
    write_result(file2, mtxA, mtxB, mtxA*mtxB)
    write_result(file3, mtxA, mtxB, mtxA@mtxB)
