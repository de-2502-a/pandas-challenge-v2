import pandas as pd
import pytest
from pandas.testing import assert_frame_equal
from unittest.mock import patch
from extracted.pandas_challenge_extracted import task_1_1, task_1_2, task_1_3, task_1_4

STUDENTS_CSV_PATHS = ["students.csv", "./students.csv"]
STUDENTS_MARKS_CSV_PATHS = ["students_marks.csv", "./students_marks.csv"]


@pytest.fixture
def setup_mock_functions():
    with patch("pandas.read_csv") as mock_read_csv:
        yield [mock_read_csv]


@pytest.fixture
def setup_mock_data():
    # Create some mock DataFrames
    # (based on the first 6 rows of the students.csv file)
    mock_students_df = pd.DataFrame(
        {
            "ID": [1, 2, 3, 4, 5, 6],
            "Year": [5, 7, 7, 5, 5, 6],
            "Class": ["A", "A", "B", "C", "C", "A"],
        }
    )

    mock_students_marks_df = pd.DataFrame(
        {
            "ID": [1, 2, 3, 4, 5, 6],
            "L1": [6, 5, 9, 9, 10, 7],
            "L2": [10, 7, 8, 7, 8, 10],
            "Maths": [10, 9, 6, 7, 7, 9],
            "Philosophy": [5, 6, 10, 5, 7, 8],
        }
    )

    mock_students_df_with_index = mock_students_df.set_index("ID")
    mock_students_marks_df_with_index = mock_students_marks_df.set_index("ID")

    return (
        mock_students_df,
        mock_students_marks_df,
        mock_students_df_with_index,
        mock_students_marks_df_with_index,
    )


def test_task_1_1(setup_mock_functions):
    # Arrange
    mock_csv = setup_mock_functions[0]
    # Act
    task_1_1()
    # Assert
    assert any(
        mock_csv.call_args == ((path,),) for path in STUDENTS_CSV_PATHS
    ), f"mock_csv was not called with any of {STUDENTS_CSV_PATHS}"


def test_task_1_2(setup_mock_functions):
    # Arrange
    mock_csv = setup_mock_functions[0]
    # Act
    task_1_2()
    # Assert
    assert any(
        mock_csv.call_args == ((path,),) for path in STUDENTS_MARKS_CSV_PATHS
    ), f"mock_csv was not called with any of {STUDENTS_MARKS_CSV_PATHS}"


def test_task_1_3(setup_mock_data):
    # Arrange
    mock_students_df, mock_students_marks_df, _, _ = setup_mock_data

    # Act
    result_students_df, result_students_marks_df = task_1_3(
        mock_students_df, mock_students_marks_df
    )

    # Assert
    # Check that the index is set to 'ID' for both DataFrames
    assert (
        result_students_df.index.name == "ID"
    ), "Index for students_df is not set to 'ID'"
    assert (
        result_students_marks_df.index.name == "ID"
    ), "Index for students_marks_df is not set to 'ID'"

    # Check that the 'ID' column no longer exists in either DataFrame
    assert (
        "ID" not in result_students_df.columns
    ), "'ID' column still exists in students_df"
    assert (
        "ID" not in result_students_marks_df.columns
    ), "'ID' column still exists in students_marks_df"


def test_task_1_4(setup_mock_data):
    # Arrange
    mock_students_df, mock_students_marks_df, _, _ = setup_mock_data

    # Expected result of the merge
    expected_df = pd.merge(
        mock_students_df, mock_students_marks_df, how="left", on="ID"
    )

    # Act
    result = task_1_4(mock_students_df, mock_students_marks_df)[0]

    # Assert
    # Check that the resulting DataFrame matches the expected DataFrame
    assert_frame_equal(result, expected_df, check_dtype=False)
