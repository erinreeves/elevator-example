import unittest

from elevator.closest_floor_elevator import ClosestFloorElevator
from elevator.elevator import Elevator
from elevator.realistic_elevator import RealisticElevator


class TestElevator(unittest.TestCase):

    def test_visit_floors_realistically_happy_input(self):
        # Inputs: [list of floors to visit] (e.g. elevator start=12 floor=2,9,1,32)
        input_floors = "12, 13, 2, 9, 1, -32"
        exp_floors_visited_inorder = [12, 13, 9, 2, 1, -32]
        # Calculate travel time based on expected visit order:
        exp_travel_time = (1 + 4 + 7 + 1 + 33) * Elevator.FLOOR_DELTA_TIME_SEC
        an_elevator = RealisticElevator()

        # Travel specified floors
        an_elevator.visit_floors(input_floors)

        # Outputs: [total travel time, floors visited in order] (e.g. 560 12,2,9,1,32), 420 in this case for time
        assert an_elevator.floors_visited_inorder == exp_floors_visited_inorder
        assert an_elevator.total_travel_time_sec == exp_travel_time

    def test_visit_floors_realistically_floors_above_only(self):
        # Input too little
        input_floors = "1, 10"
        exp_floors_visited_inorder = [1, 10]
        # Time 0 since didn't visit any additional floors, just initial one
        exp_travel_time = 9 * Elevator.FLOOR_DELTA_TIME_SEC
        an_elevator = RealisticElevator()

        # Travel specified floors
        an_elevator.visit_floors(input_floors)

        # Verify output indicates no floors traveled to
        assert an_elevator.floors_visited_inorder == exp_floors_visited_inorder
        assert an_elevator.total_travel_time_sec == exp_travel_time

    def test_visit_floors_realistically_floors_below_only(self):
        # Input too little
        input_floors = "10, 1"
        exp_floors_visited_inorder = [10, 1]
        # Time 0 since didn't visit any additional floors, just initial one
        exp_travel_time = 9 * Elevator.FLOOR_DELTA_TIME_SEC
        an_elevator = RealisticElevator()
        
        # Travel specified floors
        an_elevator.visit_floors(input_floors)

        # Verify output indicates no floors traveled to
        assert an_elevator.floors_visited_inorder == exp_floors_visited_inorder
        assert an_elevator.total_travel_time_sec == exp_travel_time

    def test_visit_floors_realistically_input_1_floor(self):
        # Input too little
        input_floors = "13"
        exp_floors_visited_inorder = [13]
        # Time 0 since didn't visit any additional floors, just initial one
        exp_travel_time = 0
        an_elevator = RealisticElevator()

        # Travel specified floors
        an_elevator.visit_floors(input_floors)

        # Verify output indicates no floors traveled to
        assert an_elevator.floors_visited_inorder == exp_floors_visited_inorder
        assert an_elevator.total_travel_time_sec == exp_travel_time

    def test_visit_floors_realistically_input_empty(self):
        with self.assertRaises(ValueError):

            # Input too little
            input_floors = ""
            exp_floors_visited_inorder = []
            # Time 0 since didn't visit any floors
            exp_travel_time = 0
            an_elevator = RealisticElevator()

            # Travel specified floors
            an_elevator.visit_floors(input_floors)

            # Verify output indicates no floors traveled to
            assert an_elevator.floors_visited_inorder == exp_floors_visited_inorder
            assert an_elevator.total_travel_time_sec == exp_travel_time

    def test_visit_floors_realistically_dup_input(self):
        # Input duplicates, causing 1 travel, no more.
        input_floors = "0, 1, 1"
        exp_floors_visited_inorder = [0, 1]
        # Calculate travel time based on expected visit order:
        exp_travel_time = 1 * Elevator.FLOOR_DELTA_TIME_SEC
        an_elevator = RealisticElevator()

        # Travel specified floors
        an_elevator.visit_floors(input_floors)

        # Verify output indicates 1 floor traveled to
        assert an_elevator.floors_visited_inorder == exp_floors_visited_inorder
        assert an_elevator.total_travel_time_sec == exp_travel_time

    def test_visit_floors_closest_floor_happy_input(self):
        # Inputs: [list of floors to visit] (e.g. elevator start=12 floor=2,9,1,32)
        input_floors = "12, 2, 9, 1, -32"
        exp_floors_visited_inorder = [12, 9, 2, 1, -32]
        # Calculate travel time based on expected visit order:
        exp_travel_time = (3 + 7 + 1 + 33) * Elevator.FLOOR_DELTA_TIME_SEC
        an_elevator = ClosestFloorElevator()

        # Travel specified floors
        an_elevator.visit_floors(input_floors)

        # Outputs: [total travel time, floors visited in order] (e.g. 560 12,2,9,1,32), 420 in this case for time
        assert an_elevator.floors_visited_inorder == exp_floors_visited_inorder
        assert an_elevator.total_travel_time_sec == exp_travel_time

    def test_visit_floors_closest_floor_input_1_floor(self):
        # Input too little
        input_floors = "13"
        exp_floors_visited_inorder = [13]
        # Time 0 since didn't visit any additional floors, just initial one
        exp_travel_time = 0
        an_elevator = ClosestFloorElevator()

        # Travel specified floors
        an_elevator.visit_floors(input_floors)

        # Verify output indicates no floors traveled to
        assert an_elevator.floors_visited_inorder == exp_floors_visited_inorder
        assert an_elevator.total_travel_time_sec == exp_travel_time

    def test_visit_floors_closest_floor_input_empty(self):
        with self.assertRaises(ValueError):
            # Input too little
            input_floors = ""
            exp_floors_visited_inorder = []
            # Time 0 since didn't visit any floors
            exp_travel_time = 0
            an_elevator = ClosestFloorElevator()

            # Travel specified floors
            an_elevator.visit_floors(input_floors)

            # Verify output indicates no floors traveled to
            assert an_elevator.floors_visited_inorder == exp_floors_visited_inorder
            assert an_elevator.total_travel_time_sec == exp_travel_time

    def test_visit_floors_closest_floor_dup_input(self):
        # Input duplicates, causing 1 travel, no more.
        input_floors = "0, 1, 1"
        exp_floors_visited_inorder = [0, 1]
        # Calculate travel time based on expected visit order:
        exp_travel_time = 1 * Elevator.FLOOR_DELTA_TIME_SEC
        an_elevator = ClosestFloorElevator()

        # Travel specified floors
        an_elevator.visit_floors(input_floors)

        # Verify output indicates 1 floor traveled to
        assert an_elevator.floors_visited_inorder == exp_floors_visited_inorder
        assert an_elevator.total_travel_time_sec == exp_travel_time

    def test_find_closest_floor_happy(self):
        # Input
        current_floor_index = 1
        unvisited_floors = [-3, 0, 10, 15]
        exp_closest_floor = -3

        # Get closest floor
        output = Elevator.find_closest_floor(current_floor_index, unvisited_floors)

        # Verify output finds closest floor
        assert unvisited_floors[output] == exp_closest_floor

    def test_find_closest_floor_1_floor(self):
        # Input
        current_floor_index = 0
        unvisited_floors = [13]
        exp_closest_floor = None

        # Get closest floor
        output = Elevator.find_closest_floor(current_floor_index, unvisited_floors)

        # Verify output finds closest floor
        assert output == exp_closest_floor

    def test_find_closest_floor_for_empty_floors(self):
        with self.assertRaises(IndexError):
            # Input
            current_floor = 0
            unvisited_floors = []
            exp_closest_floor = None

            # Get closes floor
            output = Elevator.find_closest_floor(current_floor, unvisited_floors)

            # Verify output finds closest floor
            assert output == exp_closest_floor

    def test_find_closest_floor_no_floors_above(self):
        # Input
        current_floor_index = 1
        unvisited_floors = [-3, 0]
        exp_closest_floor = -3

        # Get closest floor
        output = Elevator.find_closest_floor(current_floor_index, unvisited_floors)

        # Verify output finds closest floor
        assert unvisited_floors[output] == exp_closest_floor

    def test_find_closest_floor_no_floors_below(self):
        # Input
        current_floor_index = 0
        unvisited_floors = [0, 10, 15]
        exp_closest_floor = 10

        # Get closest floor
        output = Elevator.find_closest_floor(current_floor_index, unvisited_floors)

        # Verify output finds closest floor
        assert unvisited_floors[output] == exp_closest_floor

    def test_find_closest_floor_index_negative(self):
        with self.assertRaises(IndexError):
            # Input
            current_floor_index = -1
            unvisited_floors = [-3]
            exp_closest_floor = None

            # Get closest floor
            output = Elevator.find_closest_floor(current_floor_index, unvisited_floors)

            # Verify output finds closest floor
            assert output == exp_closest_floor

    def test_sanitize_convert_input_happy_input(self):
        # Typical input
        user_input = " -3, 1 , -2 "

        output = Elevator.sanitize_and_convert_input(user_input)

        # Verify no failures and outputs what expect
        assert output == [-3, 1, -2]

    def test_sanitize_convert_input_input_non_numeric_raises_exception(self):
        with self.assertRaises(ValueError):
            # Bad input with non numeric value
            user_input = " 1a2 "

            Elevator.sanitize_and_convert_input(user_input)

    def test_sanitize_convert_input_input_extra_negative_signs_raises_exception(self):
        with self.assertRaises(ValueError):
            # Bad input with extra negative sign
            user_input = " --a1 "

            Elevator.sanitize_and_convert_input(user_input)
