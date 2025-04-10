TASKS = [
    {
        "task": "task_1",
        "dataframes": ["students_df", "students_marks_df", "students_data_df"],
        "subtasks": [
            {
                "task_marker": "### Task 1.1",
                "args": "",
                "return": ["students_df"],
            },
            {
                "task_marker": "### Task 1.2",
                "args": "",
                "return": ["students_marks_df"],
            },
            {
                "task_marker": "### Task 1.3",
                "args": ["students_df", "students_marks_df"],
                "return": ["students_df", "students_marks_df"],
            },
            {
                "task_marker": "### Task 1.4",
                "args": ["students_df", "students_marks_df"],
                "return": ["students_data_df"],
            },
        ],
    },
    {
        "task": "task_2",
        "dataframes": [
            "student_data_df",
            "new_students_df",
            "all_students_data_df",
        ],
        "subtasks": [
            {
                "task_marker": "### Task 2.1",
                "args": ["new_students_df"],
                "return": ["new_students_df"],
            },
            {
                "task_marker": "### Task 2.2",
                "args": ["students_data_df", "new_students_df"],
                "return": ["all_students_data_df"],
            },
        ],
    },
    {
        "task": "task_3",
        "dataframes": ["all_students_data_df"],
        "subtasks": [
            {
                "task_marker": "### Task 3.1",
                "args": ["all_students_data_df"],
                "return": ["all_students_data_df"],
            },
            {
                "task_marker": "### Task 3.2",
                "args": ["all_students_data_df"],
                "return": ["all_students_data_df"],
            },
            {
                "task_marker": "### Task 3.3",
                "args": ["all_students_data_df"],
                "return": ["all_students_data_df"],
            },
        ],
    },
    {
        "task": "task_4",
        "dataframes": [
            "all_students_data_df",
            "num_of_students_in_each_class",
            "grading_change",
            "grading_change=task_4_2()",
        ],
        "subtasks": [
            {
                "task_marker": "### Task 4.1",
                "args": ["all_students_data_df"],
                "return": ["num_of_students_in_each_class"],
            },
            {
                "task_marker": "### Task 4.2",
                "args": [],
                "return": ["grading_change"],
            },
            {
                "task_marker": "### Task 4.3",
                "args": ["all_students_data_df", "grading_change=task_4_2()"],
                "return": ["all_students_data"],
            },
        ],
    },
    {
        "task": "task_5",
        "dataframes": ["all_students_data", "math_a_students"],
        "subtasks": [
            {
                "task_marker": "### Task 5.1",
                "args": ["all_students_data"],
                "return": ["math_a_students"],
            },
            {
                "task_marker": "### Task 5.2",
                "args": ["math_a_students"],
                "return": ["math_a_students"],
            },
            {
                "task_marker": "### Task 5.3",
                "args": ["math_a_students"],
                "return": ["math_a_students"],
            },
        ],
    },
]

IPYNB_PATH = "pandas_challenge.ipynb"

# Define the extracted file names
EXTRACTED_PATH = "extracted/pandas_challenge_extracted.py"

DEF_STATEMENT = "def func_name(args):"

INDENT = "    "

NEW_LINE = "\n"
