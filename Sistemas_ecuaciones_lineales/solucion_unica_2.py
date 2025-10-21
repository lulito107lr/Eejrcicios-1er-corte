from pulp import *
prob =LpProblem("sistema", LpMinimize)

x = LpVariable("x")
y= LpVariable("y")
z = LpVariable("z")

prob+=0

prob += x+y+z == 6
prob += 2*x-y+z == 3
prob += x+2*y-z == 4

prob.solve()

print("Valor x =", value(x))
print("Valor y = ", value(y))
print("Valor z = ", value(z))
print(LpStatus)
