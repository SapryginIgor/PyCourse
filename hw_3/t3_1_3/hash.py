import numpy as np
from matrix1 import Matrix


class Hash:
    def __hash__(self):
        res = 0
        for row in self.mtx:
            for el in row:
                res ^= hash(el)
        return res
    
    def __eq__(self, other):
        return self.mtx == other.mtx

class HashableMatrix(Matrix, Hash):

    def __init__(self, mtx):
        super().__init__(mtx)
        self._cache = dict()

    def __matmul__(self, other):
        if (hash(self),hash(other)) not in self._cache:
            self._cache[(hash(self),hash(other))] = HashableMatrix((super().__matmul__(other)).mtx)
        else:
            print("I used cache!!")
        return self._cache[(hash(self),hash(other))]
    
    def write_to_file(self,file):
        file.write(str(self)+'\n')

if __name__ == "__main__":
    np.random.seed(0)
    B = np.random.randint(0, 10, (10, 10))
    B = HashableMatrix(B.tolist())
    D = B

    A = np.eye(10)
    C = -np.eye(10)
    A = HashableMatrix(A.tolist())
    C = HashableMatrix(C.tolist())


    assert((hash(A) == hash(C)) and (A != C) and (B == D) and (A @ B != C @ D))
    assert((hash(A) == hash(C)) and (A != C) and (B == D) and (A @ B != C @ D)) # to test cache

    Afile = open("t3_1_3/3/A.txt", 'w')
    Bfile = open("t3_1_3/3/B.txt", 'w')
    Cfile = open("t3_1_3/3/C.txt", 'w')
    Dfile = open("t3_1_3/3/D.txt", 'w')
    ABfile = open("t3_1_3/3/AB.txt", 'w')
    CDfile = open("t3_1_3/3/CD.txt", 'w')
    hashfile = open("t3_1_3/3/hash.txt", 'w')

    A.write_to_file(Afile)
    B.write_to_file(Bfile)
    C.write_to_file(Cfile)
    D.write_to_file(Dfile)
    (A @ B).write_to_file(ABfile)
    (C @ D).write_to_file(CDfile)


    
    hashfile.write("AB hash: " + str(hash(A@B)) + '\n')
    hashfile.write("CD hash: " + str(hash(C@D)) + '\n')
    
    





    

