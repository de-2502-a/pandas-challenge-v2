import pandas as pd
import pytest
from pandas.testing import assert_frame_equal
from extracted.pandas_challenge_extracted import (
    task_2_1,
    task_2_2,
)


@pytest.fixture
def expected_new_students_df():
    data = [
        {
            "ID": 201,
            "Year": 7,
            "Class": "A",
            "L1": 8,
            "L2": 6,
            "Maths": 8,
            "Philosophy": 7,
        },
        {
            "ID": 202,
            "Year": 5,
            "Class": "A",
            "L1": 8,
            "L2": 6,
            "Maths": 10,
            "Philosophy": 9,
        },
        {
            "ID": 203,
            "Year": 5,
            "Class": "B",
            "L1": 8,
            "L2": 5,
            "Maths": 10,
            "Philosophy": 5,
        },
    ]
    df = pd.DataFrame(data)
    df.set_index("ID", inplace=True)
    return df


@pytest.fixture
def mock_student_data():
    student_data = [
        {
            "ID": 1,
            "Year": 5,
            "Class": "A",
            "L1": 6,
            "L2": 10,
            "Maths": 10,
            "Philosophy": 5,
        },
        {
            "ID": 2,
            "Year": 7,
            "Class": "A",
            "L1": 5,
            "L2": 7,
            "Maths": 9,
            "Philosophy": 6,
        },
    ]
    students_data_df = pd.DataFrame(student_data).set_index("ID")
    return students_data_df


@pytest.fixture
def mock_new_students_data():
    new_students_data = [
        {
            "ID": 201,
            "Year": 7,
            "Class": "A",
            "L1": 8,
            "L2": 6,
            "Maths": 8,
            "Philosophy": 7,
        },
        {
            "ID": 202,
            "Year": 5,
            "Class": "A",
            "L1": 8,
            "L2": 6,
            "Maths": 10,
            "Philosophy": 9,
        },
    ]
    new_students_df = pd.DataFrame(new_students_data).set_index("ID")
    return new_students_df


def test_task_2_1(expected_new_students_df):
    # Act
    # Call the function and get the resulting DataFrame
    result = task_2_1(None)[0]

    # Assert
    # Check that the resulting DataFrame matches the expected DataFrame
    assert_frame_equal(result, expected_new_students_df, check_dtype=False)

    # Additional checks (optional)
    assert result.index.name == "ID", "Index is not set to 'ID'"
    assert list(result.columns) == [
        "Year",
        "Class",
        "L1",
        "L2",
        "Maths",
        "Philosophy",
    ], "Columns do not match expected structure"


def test_task_2_2(mock_student_data, mock_new_students_data):
    # Arrange
    students_data_df = mock_student_data
    new_students_df = mock_new_students_data

    # Expected result of combining the two DataFrames
    expected_df = pd.concat([students_data_df, new_students_df], axis=0)

    # Act
    result = task_2_2(students_data_df, new_students_df)[0]

    # Assert
    # Check that the resulting DataFrame matches the expected DataFrame
    assert_frame_equal(result, expected_df, check_dtype=False)
