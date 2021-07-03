from linear_regression import linearRegression
from exponential_regression import exponentialRegression
from polynomial_regression import polynomialRegression
from input import readPoints

xList,yList=readPoints("data.txt")

polynomialRegression(xList,yList,3)

# print(linearRegression([0.698132,0.959931,1.134464,1.570796,1.919862],[0.188224,0.209138,0.230052,0.250965,0.313707]))
# print(linearRegression([0,0.183,0.36,0.5324,0.702,0.867,1.0244,1.1774,1.329,1.479,1.5,1.56],[0,306,612,917,1223,1529,1835,2140,2446,2752,2767,2896],origin=True))
# print(exponentialRegression([0,1,3,5,7,9],[1.000,0.891,0.708,0.562,0.447,0.355]))
# print(polynomialRegression([80,40,-40,-120,-200,-280,-340],[0.00000647,0.00000624,0.00000572,0.00000509,0.00000430,0.00000333,0.00000245],2))