import sys

from elevator.closest_floor_elevator import ClosestFloorElevator
from elevator.realistic_elevator import RealisticElevator


def main():
    global an_elevator

    while True:
        invalid_input = True
        while True:
            elevator_choice = input("Choose (0) realistic elevator or (1) closest floor elevator: ")
            if elevator_choice == '0':
                an_elevator = RealisticElevator()
                break
            if elevator_choice == '1':
                an_elevator = ClosestFloorElevator()
                break

        user_input = input("Input the floors to visit as a comma delimited list of integers: ")
        try:
            an_elevator.visit_floors(user_input)
        except ValueError as e:
            sys.exit(f"Exception occurred during elevator execution, quiting. Exception: {e}")

        print(
            f"Floors visited, with total time first and including initial floor: {an_elevator.total_travel_time_sec} "
            f"{', '.join(str(l) for l in an_elevator.floors_visited_inorder)}")


if __name__ == '__main__':
    sys.exit(main())
