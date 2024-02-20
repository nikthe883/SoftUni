
class Task():
    comments = []
    completed = False

    def __init__(self,name, due_date) -> None:
        self.name = name
        self.due_date = due_date

    def change_name(self, new_name):
        if new_name != self.name:
            self.name = new_name
            return self.name
        else:
            return "Name cannot be the same."
    
    def change_due_date(self, new_date):
        if new_date != self.due_date:
            self.due_date = new_date
            return self.due_date
        else:
            return "Date cannot be the same."
        
    def add_comment(self, comment):
        self.comments.append(comment)
    
    def edit_comment(self, comment_number, new_comment):
        if 0 <= comment_number < len(self.comments):
           self.comments[comment_number] = new_comment
           return ', '.join(self.comments)
        else:
           return "Cannot find comment."
       
    def details(self):
        return f"Name: {self.name} - Due Date: {self.due_date}"
    
