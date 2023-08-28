import sys
from elevator.elevator import Elevator


an_elevator = Elevator()
user_input = input("Input the floors to visit as a comma delimited list of integers: ")
try:
    an_elevator.visit_floors(user_input)
except ValueError as e:
    sys.exit(f"Exception occurred during elevator execution, quiting. Exception: {e}")

print(
    f"Floors visited, with total time first and including initial floor: {an_elevator.total_travel_time_sec} "
    f"{', '.join(str(l) for l in an_elevator.floors_visited_inorder)}")

