from elevator.elevator import Elevator


an_elevator = Elevator()
user_input = input("Input the floors to visit as a comma delimited list of integers: ")
an_elevator.visit_floors(user_input)
print(f"Completed: {an_elevator.floors_visited_inorder}")
print(f"Floors visited, with total time first and including initial floor: {an_elevator.total_travel_time_sec} {', '.join(str(l) for l in an_elevator.floors_visited_inorder)}")
