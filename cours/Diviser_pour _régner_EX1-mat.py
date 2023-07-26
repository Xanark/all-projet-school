from sympy import symbols, solve,

# Définir les variables
x = symbols('x')
y = symbols('y')
# Définir l'équation à résoudre
equation = 3*x + 2 - 5*x + 6*x * 9*y + 3*y**2 - 8

# Résoudre l'équation
solution = solve(equation)

# Afficher la solution
print(solution)


