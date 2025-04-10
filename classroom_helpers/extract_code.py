# Define a dictionary of markdown markers
# Cycle through the notebook looking for each of the markers
# Extract the content of any code cells between the markers
# Write the extracted code to a Python function in a separate file
import json
from pathlib import Path
from constants import (
    TASKS,
    IPYNB_PATH,
    EXTRACTED_PATH,
    DEF_STATEMENT,
    NEW_LINE,
    INDENT,
)


def get_path(path):
    current_dir = Path.cwd()
    return current_dir / path


def get_notebook_json():
    with open(get_path(IPYNB_PATH), "r", encoding="utf-8") as f:
        notebook = json.load(f)
    return notebook


def task_marker_in_source(source):
    for task in TASKS:
        for subtask in task["subtasks"]:
            if subtask.get("task_marker") and source.startswith(
                subtask["task_marker"]
            ):
                return True
    return False


def process_markdown_cell(cell, code_cells):
    source_header = cell["source"][0]
    if task_marker_in_source(source_header):
        code_cells.append(create_task_function_line(source_header))
    return source_header


def process_import_code_cell(cell, code_cells):
    stripped_lines = "".join(line.strip() for line in cell["source"])
    code_cells.append(stripped_lines)


def process_regular_code_cell(cell, code_cells):
    if len(cell["source"]) != 0:
        indented_code = "".join(INDENT + line for line in cell["source"])
        code_cells.append(indented_code)


def process_code_and_markdown_transition(
    cell, next_cell, code_cells, source_header
):
    if cell["cell_type"] == "code" and next_cell["cell_type"] == "markdown":
        code_cells.append(function_args(source_header, "return"))


def process_cell(cell, next_cell, code_cells, source_header):
    if not cell["source"]:
        return source_header

    if cell["cell_type"] == "markdown":
        source_header = process_markdown_cell(cell, code_cells)
    elif cell["cell_type"] == "code":
        if isinstance(cell["source"], list) and "".join(
            cell["source"]
        ).startswith("import"):
            process_import_code_cell(cell, code_cells)
        else:
            process_regular_code_cell(cell, code_cells)

    process_code_and_markdown_transition(
        cell, next_cell, code_cells, source_header
    )
    return source_header


def cycle_through_notebook_cells(notebook):
    code_cells = []
    cells = notebook["cells"]
    source_header = None  # Initialize source_header

    for i in range(len(cells) - 1):
        cell = cells[i]
        next_cell = cells[i + 1]
        source_header = process_cell(cell, next_cell, code_cells, source_header)

    return code_cells


def split_code_cells(code_cells):
    return [line for cell in code_cells for line in cell.split(NEW_LINE)]


def write_code_cells_to_file(code_cells):
    code_cells = [code for code in code_cells if code.strip()]
    code_cells[len(code_cells) - 1] = ""
    with open(get_path(EXTRACTED_PATH), "w", encoding="utf-8") as f:
        is_last_line_def = False
        for index, line in enumerate(code_cells):
            if "import" in line:
                f.write(line + NEW_LINE)
            elif is_last_line_def and line.strip().startswith("def "):
                f.write(f"{INDENT}return None{NEW_LINE}")
                f.write(NEW_LINE * 2 + line + NEW_LINE)
            elif line.strip().startswith("def "):
                f.write(NEW_LINE * 2 + line + NEW_LINE)
                is_last_line_def = True
            elif index == len(code_cells) - 1 and is_last_line_def:
                f.write(f"{INDENT}return None{NEW_LINE}")
            else:
                f.write(line + NEW_LINE)
                is_last_line_def = False


def get_code_for_grading():
    notebook_json = get_notebook_json()
    extracted_code = cycle_through_notebook_cells(notebook_json)
    writable_code = split_code_cells(extracted_code)
    write_code_cells_to_file(writable_code)


def return_statement(task, key_to_parse="return"):
    values = task.get(key_to_parse, [])
    if isinstance(values, list) and values:
        return f"{INDENT}return [{', '.join(values)}]"
    return ""


def function_args(source, key_to_parse):
    for task in TASKS:
        for subtask in task["subtasks"]:
            if subtask.get("task_marker") and source.startswith(
                subtask["task_marker"]
            ):
                values = subtask.get(key_to_parse, [])
                if isinstance(values, list):
                    if key_to_parse == "args":
                        return ", ".join(values)
                    elif key_to_parse == "return":
                        return return_statement(subtask, key_to_parse)
    return ""


def create_task_function_line(source):
    function_name = source[4:].replace(" ", "_").replace(".", "_").lower()
    task_line = DEF_STATEMENT.replace("func_name", function_name)
    task_line = task_line.replace(NEW_LINE, "")
    task_line = task_line.replace("args", function_args(source, "args"))
    return f"{NEW_LINE * 2}{task_line}"


get_code_for_grading()
