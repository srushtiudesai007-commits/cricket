# Cricket Score Calculator

def run_rate(runs, overs):
    return runs / overs

def strike_rate(runs, balls):
    return (runs / balls) * 100

# Example
runs = int(input("Enter runs scored: "))
overs = float(input("Enter overs played: "))
balls = int(input("Enter balls faced: "))

print("Run Rate =", round(run_rate(runs, overs), 2))
print("Strike Rate =", round(strike_rate(runs, balls), 2))