import numpy as np
tableau = np.array([1, 2, 3], dtype=np.float32)
print(tableau)
print("Type :", tableau.dtype)
tableau_int = tableau.astype(np.int32)
print(tableau_int)
print("Nouveau type :", tableau_int.dtype)
print("Mémoire float32 :", tableau.nbytes, "octets")
print("Mémoire int32 :", tableau_int.nbytes, "octets")
identite = np.eye(4)
print(identite)
constant = np.full((2, 2), 7)
print(constant)
tableau_range = np.arange(12).reshape((4, 3))
print(tableau_range)
matrice = np.array([[1, 2], [3, 4]])
vecteur = np.array([1, 4, 9, 16])
print(matrice * 10)
print(np.sqrt(vecteur))


tableau_1d = np.array([1, 2, 3, 4, 5])
print("Tableau 1D :", tableau_1d)
tableau_2d = np.array([[1, 2, 3],
                       [4, 5, 6]])
print("Tableau 2D :\n", tableau_2d)
zeros = np.zeros((2, 3))
print("Zeros :\n", zeros)
ones = np.ones((3, 2))
print("Ones :\n", ones)
progression = np.arange(0, 10, 2)  
print("np.arange :", progression)
linspace = np.linspace(0, 1, 5)  
print("np.linspace :", linspace)

tableau = np.array([1, 2, 3])
print("dtype :", tableau.dtype)  # type des éléments (int64, float64…)
print("ndim  :", tableau.ndim)   # nombre de dimensions
print("shape :", tableau.shape)  # tuple de dimensions
print("size  :", tableau.size)   # nombre total d'éléments

vecteur = np.arange(1, 10)  
print("Vecteur :", vecteur)
matrice = vecteur.reshape((3, 3))
print("Matrice 3x3 :\n", matrice)
print("Shape :", matrice.shape)
print("Size  :", matrice.size)
matrice_auto = vecteur.reshape((3, -1))  
print("Shape auto :", matrice_auto.shape)
