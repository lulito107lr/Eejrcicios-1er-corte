from pulp import *
prob =LpProblem("sistema", LpMinimize)

x = LpVariable("x")
y= LpVariable("y")
z = LpVariable("z")

prob+=0

prob += 2*x+3*z == 4
prob += 2*x-6*y+7*z == 15
prob += x-2*y+5*z == 10

prob.solve()

print("Valor x =", value(x))
print("Valor y = ", value(y))
print("Valor z = ", value(z))
print(LpStatus)
