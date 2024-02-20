from task import Task

class Section:
    tasks = []

    def __init__(self, name) -> None:
        self.name = name

    def add_task(self, new_task: Task):
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section "
        else:
            return f"Task is already in the section {self.name}"
        
    def complet_task(self, task_name):
        for i in self.tasks:
            if task_name == i.name:
                
            

    def clean_section(self):
        pass

    def view_section(self):
        pass