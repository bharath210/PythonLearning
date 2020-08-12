from numpy import  *

num1 = array([
                        [1,2,3,4,5,6],
                        [1,2,3,4,5,6]
                    ])

mx1 = matrix(num1)
print(mx1)

mx2 = matrix('1 2 3 ; 4 5 6 ; 7 8 9')
print(mx2)
mx3 = matrix('1 4 3 ; 7 5 6 ; 1 3 9')
print(diagonal(mx2))

mx4 = mx2 * mx3
print(mx4)