from elevator.elevator import Elevator


class RealisticElevator(Elevator):

    def visit_floors(self, floors_to_visit: str):
        """
        Visit the floors of an elevator realistically.
        i.e. choose the closest floor from initial floor and traverse that direction first,
        then switch to the opposite direction.

        :param floors_to_visit: string of comma delimited list floors as integers, positive or negative, to visit.
         """
        floors_to_visit = super().sanitize_and_convert_input(floors_to_visit)

        if len(floors_to_visit) == 0:
            return
        if len(floors_to_visit) == 1:
            self.floors_visited_inorder = list(floors_to_visit)
            return

        initial_floor_value = floors_to_visit[0]  # Initial floor, acquire before misordering by setting to a set.

        floors_to_visit = list(set(floors_to_visit))  # Remove duplicate floors
        floors_to_visit.sort()  # Pre sort so easier to find closest neighbor
        initial_floor_index = floors_to_visit.index(initial_floor_value)

        self.floors_visited_inorder = [initial_floor_value]
        if initial_floor_index > 0:  # There are floors to the left
            floors_to_left_reversed = floors_to_visit[0:initial_floor_index]
            floors_to_left_reversed.reverse()
            dist_to_left_floor = initial_floor_value - floors_to_left_reversed[0]

            # No floors to the right, therefore visit only floors to left
            if len(floors_to_visit) == initial_floor_index + 1:
                self.floors_visited_inorder += floors_to_left_reversed
            else:  # There are floors to the right and left
                floors_to_right = floors_to_visit[initial_floor_index + 1:]
                dist_to_right_floor = floors_to_right[0] - initial_floor_value
                print(f"floors right={floors_to_right} and left={floors_to_left_reversed}"
                      f" dist to right={dist_to_right_floor} dist to left={dist_to_left_floor}")
                if dist_to_right_floor <= dist_to_left_floor:  # Visit floors right then left
                    self.floors_visited_inorder += floors_to_right + floors_to_left_reversed
                else: # Visit floors left then right
                    self.floors_visited_inorder +=  floors_to_left_reversed + floors_to_right
        # Only floors to right
        else:
            floors_to_right = floors_to_visit[initial_floor_index + 1:]
            self.floors_visited_inorder += floors_to_right

        # Calculate the time took
        for index, floor in enumerate(self.floors_visited_inorder):
            if index > 0:
                time = abs(self.floors_visited_inorder[index] - self.floors_visited_inorder[index - 1]) * self.FLOOR_DELTA_TIME_SEC
                self.total_travel_time_sec += time
