import numpy as np

class NumpyMixin:
    def __add__(self,other):
        return self.__class__((np.array(self.mtx)+np.array(other.mtx)).tolist())
    def __mul__(self,other):
        return self.__class__((np.array(self.mtx)*np.array(other.mtx)).tolist())
    def __matmul__(self,other):
        return self.__class__((np.array(self.mtx)@np.array(other.mtx)).tolist())
    def __truediv__(self,other):
        return self.__class__((np.array(self.mtx)/np.array(other.mtx)).tolist())
    def __str__(self):
        return str(np.array(self.mtx))
    def write_to_file(self,file,name=None):
        if name:
            file.write(name + ':\n')
        file.write(str(self)+'\n')
        
    

class GetSet:
    
    @property
    def H(self):
        return self._H

    @property
    def W(self):
        return self._W
    
    def is_matrix(self, mtx):
        W = len(mtx[0])
        for row in mtx:
            if len(row) != W:
                return False
        return True
    
    @property
    def mtx(self):
        return self._mtx
    
    @mtx.setter
    def mtx(self, new_mtx):
        W = len(new_mtx[0])
        if not self.is_matrix(new_mtx):
                raise ValueError("not a matrix")
        self._mtx = new_mtx
    

    


class Matrix(NumpyMixin, GetSet):
    def __init__(self,mtx):
        super().__init__()
        self.mtx = mtx

def write_result(file, A, B, result):
    A.write_to_file(file, 'A')
    B.write_to_file(file, 'B')
    result.write_to_file(file, 'result') 


if __name__ == '__main__':
    np.random.seed(0)
    A = np.random.randint(0, 10, (10, 10))
    B = np.random.randint(0, 10, (10, 10))
    mtxA = Matrix(A.tolist())
    mtxB = Matrix(B.tolist())
    assert ((mtxA + mtxB).mtx == (A+B)).all()
    assert ((mtxA * mtxB).mtx == (A*B)).all()
    assert ((mtxA @ mtxB).mtx == (A@B)).all()
    file1 = open("t3_2/matrix+.txt", 'w')
    file2 = open("t3_2/matrix*.txt", 'w')
    file3 = open("t3_2/matrix@.txt", 'w')
    write_result(file1, mtxA, mtxB, mtxA+mtxB)
    write_result(file2, mtxA, mtxB, mtxA*mtxB)
    write_result(file3, mtxA, mtxB, mtxA@mtxB)
        
    
    