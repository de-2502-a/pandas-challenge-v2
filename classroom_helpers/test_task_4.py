import pandas as pd
import pytest
from pandas.testing import assert_frame_equal
from extracted.pandas_challenge_extracted import task_4_1, task_4_2, task_4_3


@pytest.fixture
def mock_all_students_data():
    data = {
        "ID": [1, 2, 3, 4],
        "Year": [5, 7, 6, 8],
        "Class": ["A", "B", "A", "C"],
        "L1": [6, 7, 8, 9],
        "L2": [10, 9, 8, 7],
        "Maths": [10, 9, 8, 7],
        "Philosophy": [5, 6, 7, 8],
        "Absences": [0, 1, 2, 0],
    }
    df = pd.DataFrame(data).set_index("ID")
    return df


def test_task_4_1(mock_all_students_data):
    # Arrange
    input_df = mock_all_students_data.copy()
    expected_pivot_table = pd.DataFrame(
        {
            "A": {5: 1, 6: 1, 7: 0, 8: 0},
            "B": {5: 0, 6: 0, 7: 1, 8: 0},
            "C": {5: 0, 6: 0, 7: 0, 8: 1},
        }
    )
    expected_pivot_table.index.name = "Year"
    expected_pivot_table.columns.name = "Class"

    # Act
    result = task_4_1(input_df)[0]

    # Assert
    assert_frame_equal(result, expected_pivot_table)


def test_task_4_2():
    # Arrange
    grading_change = task_4_2()[0]

    # Act & Assert
    assert grading_change(10) == "A"  # Test for grade A
    assert grading_change(9) == "B"  # Test for grade B
    assert grading_change(8) == "B"  # Test for grade B
    assert grading_change(7) == "C"  # Test for grade C
    assert grading_change(6) == "C"  # Test for grade C
    assert grading_change(5) == "D"  # Test for grade D
    assert grading_change(0) == "D"  # Test for grade D


def test_task_4_3(mock_all_students_data):
    # Arrange
    input_df = mock_all_students_data.copy()
    expected_data = {
        "ID": [1, 2, 3, 4],
        "Year": [5, 7, 6, 8],
        "Class": ["A", "B", "A", "C"],
        "L1": ["C", "C", "B", "B"],
        "L2": ["A", "B", "B", "C"],
        "Maths": ["A", "B", "B", "C"],
        "Philosophy": ["D", "C", "C", "B"],
        "Absences": [0, 1, 2, 0],
    }
    expected_df = pd.DataFrame(expected_data).set_index("ID")

    # Act
    result = task_4_3(input_df)[0]

    # Assert
    assert_frame_equal(result, expected_df)
