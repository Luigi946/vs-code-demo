import cvxpy as cp
from numpy import integer
# Create two scalar variables
x=cp.Variable()
y=cp.Variable()
Constraints=[x+y==1, x-y>=1]
obj=cp.Minimize((x-y)**2)
prob=cp.Problem(obj,Constraints)
prob.solve()
print("status",prob.status)
print("optimal value",prob.value)
print("optimal var",x.value,y.value)
z=cp.Variable(1,boolean=True)
a=1
b=1
c=2