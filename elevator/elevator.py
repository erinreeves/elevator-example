import sys

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

        current_floor = floors_to_visit[0]
        floors_to_visit = set(floors_to_visit)

        # Account for starting at a floor and add it to visited set.
        floors_to_visit.remove(current_floor)
        self.floors_visited_inorder.append(current_floor)

        # Iterate through the floors not yet visited by finding the closest next floor to visit
        while len(floors_to_visit) > 0:
            next_floor = self.find_closest_floor(current_floor, floors_to_visit)

            # Remove this visited floor and put it onto the visited set.
            floors_to_visit.remove(next_floor)
            self.floors_visited_inorder.append(next_floor)
            self.total_travel_time_sec += abs(next_floor - current_floor) * self.FLOOR_DELTA_TIME_SEC
            current_floor = next_floor

    @staticmethod
    def find_closest_floor(current_floor, set_unvisited_floors: set):
        """
        Get the closest floor, be it up or down.

        :param current_floor: Integer of the current floor
        :param set_unvisited_floors: Set of the unvisited floors

        :return: Integer of closest floor or None if unvisited floors empty.
        """
        if len(set_unvisited_floors) == 0:
            return None

        closest_floor = None
        for next_floor in set_unvisited_floors:
            if closest_floor is None or abs(next_floor - current_floor) < abs(closest_floor - current_floor):
                closest_floor = next_floor

        return closest_floor

    @staticmethod
    def sanitize_and_convert_input(input_str):
        """
        Sanitize and convert comma delimited string into a list of positive or negative integers.
        If any of the entries are not integers the program exits.

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
                sys.exit(f"Invalid input, not numeric, for the item '{x}' from split of input string '{input_str}'")

            # Convert original string to int, since should be safe to do so.
            int_x = int(x)
            list_int.append(int_x)

        return list_int
