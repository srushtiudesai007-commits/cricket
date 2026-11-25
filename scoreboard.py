# Cricket Score Calculator

def run_rate(runs, overs):
    return runs / overs

def strike_rate(runs, balls):
    return (runs / balls) * 100

def required_rate(target, current_runs, overs_left):
    runs_needed = target - current_runs
    return runs_needed / overs_left

# Input
runs = int(input("Enter runs scored: "))
overs = float(input("Enter overs played: "))
balls = int(input("Enter balls faced: "))

target = int(input("Enter target score: "))
current_runs = int(input("Enter current score: "))
overs_left = float(input("Enter overs left: "))

# Output
print("\nRun Rate =", round(run_rate(runs, overs), 2))
print("Strike Rate =", round(strike_rate(runs, balls), 2))
print("Required Run Rate =", round(required_rate(target, current_runs, overs_left), 2))
