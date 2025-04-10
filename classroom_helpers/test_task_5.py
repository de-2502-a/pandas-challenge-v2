import pandas as pd
import pytest
from pandas.testing import assert_frame_equal
from unittest.mock import patch
from extracted.pandas_challenge_extracted import task_5_1, task_5_2, task_5_3


@pytest.fixture
def mock_all_students_data():
    data = {
        "ID": [1, 2, 3, 4],
        "Year": [5, 7, 6, 8],
        "Class": ["A", "B", "A", "C"],
        "L1": ["C", "C", "B", "B"],
        "L2": ["A", "B", "B", "C"],
        "Maths": ["A", "B", "B", "C"],
        "Philosophy": ["D", "C", "C", "B"],
        "Absences": [0, 1, 2, 0],
    }
    df = pd.DataFrame(data).set_index("ID")
    return df


def test_task_5_1(mock_all_students_data):
    # Arrange
    input_df = mock_all_students_data.copy()
    expected_data = {
        "ID": [1],
        "Year": [5],
        "Class": ["A"],
        "L1": ["C"],
        "L2": ["A"],
        "Maths": ["A"],
        "Philosophy": ["D"],
        "Absences": [0],
    }
    expected_df = pd.DataFrame(expected_data).set_index("ID")

    # Act
    result = task_5_1(input_df)[0]

    # Assert
    assert_frame_equal(result, expected_df)


def test_task_5_2(mock_all_students_data):
    # Arrange
    input_df = mock_all_students_data.copy()
    math_a_students = input_df[input_df["Maths"] == "A"]

    # Introduce unsorted data
    unsorted_data = math_a_students.copy()
    unsorted_data.loc[1, "L1"] = "B"  # Change L1 to make it unsorted
    unsorted_data.loc[1, "L2"] = "C"  # Change L2 to make it unsorted

    expected_data = {
        "ID": [1],
        "Year": [5],
        "Class": ["A"],
        "L1": ["B"],  # Sorted by L1
        "L2": ["C"],  # Sorted by L2
        "Maths": ["A"],
        "Philosophy": ["D"],
        "Absences": [0],
    }
    expected_df = pd.DataFrame(expected_data).set_index("ID")

    # Act
    result = task_5_2(unsorted_data)[0]

    # Assert
    assert_frame_equal(result, expected_df)


def test_task_5_3(mock_all_students_data):
    # Arrange
    input_df = mock_all_students_data[mock_all_students_data["Maths"] == "A"].copy()

    # Act & Assert
    with patch.object(
        pd.DataFrame, "head", wraps=input_df.head
    ) as mock_head, patch.object(
        pd.DataFrame, "iloc", wraps=input_df.iloc
    ) as mock_iloc, patch.object(
        pd.DataFrame, "loc", wraps=input_df.loc
    ) as mock_loc, patch(
        "pandas.DataFrame.__getitem__", wraps=input_df.__getitem__
    ) as mock_slice, patch(
        "pandas.DataFrame.query", wraps=input_df.query
    ) as mock_query, patch(
        "pandas.DataFrame.take", wraps=input_df.take
    ) as mock_take, patch(
        "pandas.DataFrame.sample", wraps=input_df.sample
    ) as mock_sample, patch(
        "pandas.DataFrame.filter", wraps=input_df.filter
    ) as mock_filter:

        task_5_3(input_df)

        # Assert that at least one of the methods was called
        assert (
            mock_head.called
            or mock_iloc.called
            or mock_loc.called
            or mock_slice.called
            or mock_query.called
            or mock_take.called
            or mock_sample.called
            or mock_filter.called
        ), "None of the expected methods (head, iloc, loc, slice, query, take, sample, filter) were called."
