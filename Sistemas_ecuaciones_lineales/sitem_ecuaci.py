from pulp import *
prob =LpProblem("sistema", LpMinimize)

x = LpVariable("x")
y= LpVariable("y")
z = LpVariable("z")

prob+=0

prob += 2*x+4*y+6*z == 18
prob += 4*x+5*y+6*z == 24
prob += 2*x+7*y+12*z == 30

prob.solve()

print("Valor x =", value(x))
print("Valor y = ", value(y))
print("Valor z = ", value(z))
print(LpStatus)