import unittest

from elevator.elevator import Elevator


class TestElevator(unittest.TestCase):

    def setUp(self):
        self.an_elevator = Elevator()

    def test_happy_input(self):
        # Inputs: [list of floors to visit] (e.g. elevator start=12 floor=2,9,1,32)
        input_floors = [12, 2, 9, 1, 32]
        exp_floors_visited_inorder = {12, 9, 2, 1, 32}
        # Calculate travel time based on expected visit order:
        exp_travel_time = (3 + 7 + 1 + 31) * self.an_elevator.FLOOR_DELTA_TIME_SEC

        # Travel specified floors
        self.an_elevator.visit_floors(input_floors)

        # Outputs: [total travel time, floors visited in order] (e.g. 560 12,2,9,1,32), 420 in this case for time
        assert self.an_elevator.floors_visited_inorder == exp_floors_visited_inorder
        assert self.an_elevator.total_travel_time_sec == exp_travel_time

    def test_input_1_floor(self):
        # Input too little
        input_floors = [13]
        exp_floors_visited_inorder = {13}
        # Time 0 since didn't visit any additional floors, just initial one
        exp_travel_time = 0

        # Travel specified floors
        self.an_elevator.visit_floors(input_floors)

        # Verify output indicates no floors traveled to
        assert self.an_elevator.floors_visited_inorder == exp_floors_visited_inorder
        assert self.an_elevator.total_travel_time_sec == exp_travel_time

    def test_input_empty(self):
        # Input too little
        input_floors = []
        exp_floors_visited_inorder = set()
        # Time 0 since didn't visit any floors
        exp_travel_time = 0

        # Travel specified floors
        self.an_elevator.visit_floors(input_floors)

        # Verify output indicates no floors traveled to
        assert self.an_elevator.floors_visited_inorder == exp_floors_visited_inorder
        assert self.an_elevator.total_travel_time_sec == exp_travel_time

    def test_dup_input(self):
        # Input duplicates, causing 1 travel, no more.
        input_floors = [0, 1, 1]
        exp_floors_visited_inorder = {0, 1}
        # Calculate travel time based on expected visit order:
        exp_travel_time = 1 * self.an_elevator.FLOOR_DELTA_TIME_SEC

        # Travel specified floors
        self.an_elevator.visit_floors(input_floors)

        # Verify output indicates 1 floor traveled to
        assert self.an_elevator.floors_visited_inorder == exp_floors_visited_inorder
        assert self.an_elevator.total_travel_time_sec == exp_travel_time

    def test_find_closest_floor_happy(self):
        # Input
        current_floor = 0
        unvisited_floors = {-3, 10, 15}
        exp_closest_floor = -3

        # Get closest floor
        output = Elevator.find_closest_floor(current_floor, unvisited_floors)

        # Verify output finds closest floor
        assert output == exp_closest_floor

    def test_find_closest_floor_for_empty_set(self):
        # Input
        current_floor = 0
        unvisited_floors = set()
        exp_closest_floor = None

        # Get closes floor
        output = Elevator.find_closest_floor(current_floor, unvisited_floors)

        # Verify output finds closest floor
        assert output == exp_closest_floor
