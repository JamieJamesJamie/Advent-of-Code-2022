"""Tests for Day5 Solution class."""

# pylint: disable=arguments-differ


import pytest

from advent_of_code.year_2022.day_06.day_06 import Day6
from tests.year_2022.abstract_test_day_2022 import AbstractTestDay2022


class TestDay(AbstractTestDay2022):
    """Test class for testing day 6."""

    @staticmethod
    def day() -> int:
        """Returns the day that is being tested.

        :return: The day that is being tested.
        """
        return 6

    @staticmethod
    def solver() -> type[Day6]:
        """Returns the Solver class that is being tested.

        :return: The solver class that is being tested.
        """
        return Day6

    @pytest.mark.parametrize(
        "example, parsed",
        (
            (1, "mjqjpqmgbljsphdztnvjfqwrcgsmlb"),
            (2, "bvwbjplbgvbhsrlpgdmjqwftvncz"),
            (3, "nppdvjthqldpwncqszvftbrmjlhg"),
            (4, "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"),
            (5, "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"),
        ),
        indirect=["example"],
    )
    def test_parse_example(self, example, parsed):
        """Test that example input is parsed correctly.

        :param example: The actual parsed input from example file.
        :param parsed: The expected parsed input from example file.
        """
        assert example == parsed

    @pytest.mark.parametrize(
        "example, result",
        ((1, 7), (2, 5), (3, 6), (4, 10), (5, 11)),
        indirect=["example"],
    )
    def test_part1_example(self, example, result):
        """Test part 1 on example input.

        :param example: Parsed input from example file.
        :param result: The expected result.
        """
        assert self.solver().part1(example) == result

    @pytest.mark.parametrize(
        "example, result",
        ((1, 19), (2, 23), (3, 23), (4, 29), (5, 26)),
        indirect=["example"],
    )
    def test_part2_example(self, example, result):
        """Test part 2 on example input.

        :param example: Parsed input from example file.
        :param result: The expected result.
        """
        assert self.solver().part2(example) == result
