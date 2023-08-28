
class Elevator:
    """
    A class representing an elevator and its basic behavior.
    It keeps track of the total travel time and the visited floors each time you visit_floors.
    To reset these class variables call __init__.

    Attributes
    ----------
        FLOOR_DELTA_TIME_SEC: integer
            Predefined travel time between a single floor in seconds.

        total_travel_time_sec: integer
            Total time in seconds spent visiting floors
        floors_visited_inorder: set
            The floors in order that were visited

    Methods
    ----------
        visit_floors(floors_to_visit)
            Returns the total time in seconds to visit all the specified floors.

    """

    # Program Constants:
    FLOOR_DELTA_TIME_SEC = 10

    def __init__(self):
        self.total_travel_time_sec = 0
        self.floors_visited_inorder = []

    def visit_floors(self, floors_to_visit: str):
        """
        Sanitizes and converts string input to a list of floors to visit, starting at the first entry.
        Keeps track of the order of visited floors plus the total travel time in seconds (not including the first entry)
        Will exit if invalid input string is given.

        :param floors_to_visit: string of comma delimited list floors as integers, positive or negative, to visit.
        """
        floors_to_visit_list = Elevator.sanitize_and_convert_input(floors_to_visit)
        self.visit_list_of_floors(floors_to_visit_list)

    def visit_list_of_floors(self, floors_to_visit: list):
        """
        Visits the specified floors, starting at the first entry.
        Keeps track of the order of visited floors plus the total travel time in seconds (not including the first entry)

        :param floors_to_visit: list of integers, positive or negative, representing the floors to visit
         where the first entry is the starting point.

        """
        if len(floors_to_visit) == 0:
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

    @staticmethod
    def find_closest_floor(current_floor_index, floors_to_visit: list):
        """
        Get the closest floor's index, be it up or down, by looking only at the closest upper and
        lower neighbor around the current floor's index.

        :param current_floor_index: Index of the current floor
        :param floors_to_visit: Sorted List of the unvisited floors, including the current.

        :return: Integer of closest floor's index or
                 None if no other neighbors, floors_to visit is empty, or index out of range.
        """
        # Index out of range:
        if current_floor_index < 0 or len(floors_to_visit) - 1 < current_floor_index:
            return None
        # Empty neighbors, just current floor left.
        if len(floors_to_visit) <= 1:
            return None
        # No upper floors, so return closest lower floor
        if len(floors_to_visit) - 1 == current_floor_index:
            return current_floor_index - 1
        else:
            closest_upper_neighbor = current_floor_index + 1

        # No lower floors, so return closest upper floor, since eliminated scenario of no downn or upper floor.
        if current_floor_index == 0:
            return current_floor_index + 1
        else:
            closest_lower_neighbor = current_floor_index - 1

        if abs(floors_to_visit[closest_upper_neighbor] - floors_to_visit[current_floor_index]) <= \
                abs(floors_to_visit[closest_lower_neighbor] - floors_to_visit[current_floor_index]):
            return closest_upper_neighbor
        else:
            return closest_lower_neighbor

    @staticmethod
    def sanitize_and_convert_input(input_str):
        """
        Sanitize and convert comma delimited string into a list of positive or negative integers.
        If any of the entries are not integers an ValueError Exception is raised.

        :return: list of integers representing original string in order
        """
        list_str = input_str.split(',')
        list_int = []
        for x in list_str:
            x = x.strip()
            pos_x = x
            if x.startswith("-"):
                pos_x = x.replace("-", "", 1)
            if not pos_x.isnumeric():
                raise ValueError(f"Invalid input, not numeric, for the item '{x}'"
                                 f" from input string '{input_str}'")

            # Convert original string to int, since should be safe to do so.
            int_x = int(x)
            list_int.append(int_x)

        return list_int
