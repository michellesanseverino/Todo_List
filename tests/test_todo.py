import pytest
from src.todo import add_task, view_tasks, mark_task_completed, remove_task

def test_add_task():
    tasks = []
    result = add_task(tasks, "Test Task")
    assert result is True
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Test Task"
    
def test_add_task_empty_title():
    tasks = []
    result = add_task(tasks, "   ")
    assert result is False
    assert len(tasks) == 0
    
def test_complete_task():
    tasks = [{"title": "Test Task", "completed": False}]
    result = mark_task_completed(tasks, 0)
    assert result is True
    assert tasks[0]["completed"] is True
    
def test_complete_task_invalid_index():
    tasks = [{"title": "Test Task", "completed": False}]
    result = mark_task_completed(tasks, 99)  # Invalid index
    assert result is False
    assert tasks[0]["completed"] is False
    
def test_remove_task():
    tasks = [{"title": "Test Task", "completed": False},
             {"title": "Another Task", "completed": False}]
    removed_task = remove_task(tasks, 0)
    assert removed_task == {"title": "Test Task", "completed": False}
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Another Task"