"""Write a program that takes coefficients of a quadratic equation as input
and solves for the roots. Handle both real and complex roots."""
anum = float(input('Enter the value of a: ')) #anum is value of a
bnum = float(input('Enter the value of b: ')) #bnum is value of b
cnum = float(input('Enter the value of c: ')) #cnum is value of c
dnum = (bnum**2 - 4 *(anum * cnum)) #dnum is the determinant
value1 = (-bnum + dnum**0.5)/2*anum
value2 = (-bnum - dnum**0.5)/2*anum
#value1 and value2 is the soln of the given eqn
print('The soln of the given quadratic eqn is ', value1,'& ', value2)

