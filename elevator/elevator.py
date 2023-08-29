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

    @staticmethod
    def find_closest_floor(current_floor_index, floors_to_visit: list):
        """
        Get the closest floor's index, be it up or down, by looking only at the closest upper and
        lower neighbor around the current floor's index.

        :param current_floor_index: Index of the current floor
        :param floors_to_visit: Sorted List of the unvisited floors, including the current.

        :return: Integer of closest floor's index or
                 None if no other neighbors, floors_to visit is empty, or
                 raise IndexError if index out of range.
        """
        # Index out of range:
        if current_floor_index < 0:
            raise IndexError(f"Index {current_floor_index} is out of range (negative).")
        if len(floors_to_visit) - 1 < current_floor_index:
            raise IndexError(f"Index {current_floor_index} out of range for list length {len(floors_to_visit)}.")
        if len(floors_to_visit) == 1:
            return None
        # No upper floors, so return closest lower floor
        if len(floors_to_visit) - 1 == current_floor_index:
            return current_floor_index - 1
        else:
            closest_upper_neighbor = current_floor_index + 1

        # No lower floors, so return closest upper floor, since eliminated scenario of no down or upper floor.
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
