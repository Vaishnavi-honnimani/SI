p=float("Enter principle amount")
r=float("Enter rate of interest")
t=int("Enter the time")

SI=(p*r*t)/100
CI=p*((1+r/100)**t)-p
print(f"Simple interest",SI)
print(f"Compound Interest:",CI)