from task import Task

class Section:
    tasks = []

    def __init__(self, name) -> None:
        self.name = name

    def add_task(self, new_task: Task):
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"
        else:
            return f"Task is already in the section {self.name}"
        
    def complete_task(self, task_name):
        for i in self.tasks:
            if task_name == i.name:
                i.completed = True
                return f"Completed task {task_name}"
            else:
                return f"Could not find task with the name {task_name}"
            
            
    def clean_section(self):
        cleaned = 0
        for i in self.tasks:
            if i.completed == True:
                cleaned += 1
                self.tasks.remove(i)
        return f"Cleared {cleaned} tasks."

    def view_section(self):
        result = f"Section {self.name}:\n"

        for task in self.tasks:
            result += f"{task.details()}\n"
        return result
    

