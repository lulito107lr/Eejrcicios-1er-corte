from pulp import *
prob =LpProblem("sistema", LpMinimize)

x = LpVariable("x")
y= LpVariable("y")
z = LpVariable("z")

prob+=0

prob += x+y+z == 3
prob += 2*x+2*y+2*z == 6
prob += x-y+z == 1

prob.solve()

print("Valor x =", value(x))
print("Valor y = ", value(y))
print("Valor z = ", value(z))
print(LpStatus)