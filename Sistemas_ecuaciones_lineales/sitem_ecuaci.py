from pulp import *
prob =LpProblem("sistema", LpMinimize)

x = LpVariable("x")
y= LpVariable("y")
z = LpVariable("z")

prob+=0

prob += 2*x+4*y+6*z == 18
prob += 4*x+5*y+6*z == 24
prob += 3*x+y-2*z == 4

prob.solve()

print("Valor x =", value(x))
print("Valor y = ", value(y))
print("Valor z = ", value(z))
print(LpStatus)