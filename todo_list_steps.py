from behave import given, when, then
from main import ToDoList, Task  # Adjust import path based on your project structure

@given('the to-do list is empty')
def step_given_empty_todo_list(context):
    context.todo_list = ToDoList()
    context.todo_list.clear_tasks()

@then('the to-do list is empty')
def step_then_empty_todo_list(context):
    context.todo_list = ToDoList()
    context.todo_list.clear_tasks()

@when('the user adds a task "{title}" "{description}"')
def step_when_user_adds_task(context, title, description):
    context.todo_list.add_task(title, description)

@then('the to-do list should contain {count} tasks in total')
def step_then_todo_list_should_contain_n_tasks(context, count):
    assert len(context.todo_list.tasks) == int(count)

@then('the to-do list should contain')
def step_then_todo_list_should_contain(context):
    for row in context.table:
        found = False
        for task in context.todo_list.tasks:
            if task.title == row['Title']:
                found = True
                assert task.description == row['Description'], \
                    f"Expected description '{row['Description']}', got '{task.description}'"
                expected_status = row['Status'].strip().lower() == 'true'
                assert task.is_done == expected_status, \
                    f"Expected status {expected_status}, got {task.is_done}"
                break
        assert found, f"Task '{row['Title']}' not found in the list"

@given('the to-do list contains')
def step_given_todo_list_contains(context):
    context.todo_list = ToDoList()
    context.todo_list.clear_tasks()
    for row in context.table:
        title = row['Title']
        description = row['Description']
        status = row['Status'].strip().lower() == 'true'
        task = Task(title, description)
        if status:
            task.complete()
        context.todo_list.tasks.append(task)
    context.todo_list.save()

@when('the user lists all tasks')
def step_when_user_lists_all_tasks(context):
    # Capture printed output as a list of task strings
    from io import StringIO
    import sys

    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()

    context.todo_list.list_tasks()

    sys.stdout = old_stdout
    context.output_list = mystdout.getvalue().strip().split('\n')

@when('the user marks the task {task_id} as completed')
def step_when_user_marks_task_as_completed(context, task_id):
    context.todo_list.complete_task(int(task_id))

@when('the user marks the task {task_id} as not completed')
def step_when_user_marks_task_as_not_completed(context, task_id):
    context.todo_list.undo_task(int(task_id))

@when('the user updates the task {task_id} to "{title}" "{description}"')
def step_when_user_updates_task(context, task_id, title, description):
    context.todo_list.update_task(int(task_id), title, description)

@when('the user clears the to-do list')
def step_when_user_clears_todo_list(context):
    context.todo_list.clear_tasks()
