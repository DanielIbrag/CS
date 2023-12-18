from sympy import symbols, Eq, solve

# Define the variable
x = symbols('x')

# Define the cubic equation
equation = Eq(4*x**3 + 16*x**2 + 23*x + 11, 0)

# Solve the equation
roots = solve(equation, x)

# Display the roots
print("The roots are:", roots)
