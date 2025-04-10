import pandas as pd
import pytest
from unittest.mock import patch, call
from extracted.pandas_challenge_extracted import task_3_1, task_3_2, task_3_3
from pandas.testing import assert_frame_equal


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
        "Absences": [0, 0, 0, 0],
    }
    df = pd.DataFrame(data).set_index("ID")
    return df


def test_task_3_1(mock_all_students_data):
    # Arrange
    input_df = mock_all_students_data.copy()
    expected_df = input_df.copy()
    expected_df["Absences"] = 0

    # Act
    result = task_3_1(input_df)[0]

    # Assert
    assert_frame_equal(result, expected_df)


def test_task_3_2(mock_all_students_data):
    # Arrange
    input_df = mock_all_students_data.copy()

    # Act & Assert
    with patch.object(pd.DataFrame, "loc", wraps=input_df.loc) as mock_loc:
        task_3_2(input_df)
        mock_loc.__setitem__.assert_called_once_with((3, "Absences"), 2)


def test_task_3_3(mock_all_students_data):
    # Arrange
    input_df = mock_all_students_data.copy()
    expected_calls = [call((1, 7), 1), call((1, -1), 1)]

    # Act & Assert
    with patch.object(pd.DataFrame, "iloc", wraps=input_df.iloc) as mock_iloc:
        task_3_3(input_df)

        calls = mock_iloc.__setitem__.call_args_list

        assert any(
            c in expected_calls for c in calls
        ), f"Expected calls: {expected_calls}, but got: {calls}"
