from elevator.elevator import Elevator


class ClosestFloorElevator(Elevator):

    def visit_floors(self, floors_to_visit: str):
        """
        Visits the specified floors, starting at the first entry.
        Keeps track of the order of visited floors plus the total travel time in seconds (not including the first entry)

        :param floors_to_visit: list of integers, positive or negative, representing the floors to visit
         where the first entry is the starting point.

        """

        floors_to_visit = super().sanitize_and_convert_input(floors_to_visit)

        if len(floors_to_visit) == 0:
            return
        if len(floors_to_visit) == 1:
            self.floors_visited_inorder = list(floors_to_visit)
            return

        next_floor_value = floors_to_visit[0]  # Initial floor, acquire before misordering by setting to a set.

        floors_to_visit = list(set(floors_to_visit))  # Remove duplicate floors
        floors_to_visit.sort()  # Pre sort so easier to find closest neighbor

        # Iterate through the floors not yet visited by finding the closest next floor, above or below, to visit
        while len(floors_to_visit) > 0:
            # Do this first so works for initial loop too. Do after popping from floors var since value's index changes.
            current_floor_index = floors_to_visit.index(next_floor_value)

            next_floor_index = Elevator.find_closest_floor(current_floor_index, floors_to_visit)

            # Remove the current floor, adding to visited floors
            self.floors_visited_inorder.append(floors_to_visit[current_floor_index])

            # If next floor exists calculate stats
            if next_floor_index is not None:
                next_floor_value = floors_to_visit[next_floor_index]
                time = abs(floors_to_visit[next_floor_index] - floors_to_visit[
                    current_floor_index]) * self.FLOOR_DELTA_TIME_SEC
                self.total_travel_time_sec += time

            floors_to_visit.pop(current_floor_index)  # Pop visited floors so don't revisit. Do last so have all values.
