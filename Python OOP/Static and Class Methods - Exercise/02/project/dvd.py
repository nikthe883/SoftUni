from calendar import month_name

class DVD:
    def __init__(self, name , id, creation_year, creation_month, age_restriction) -> None:
          self.name = name
          self.id = id
          self.creation_year = creation_year
          self.creation_month = creation_month
          self.age_restriction = age_restriction
          self.is_rented = False

    def get_dvd(self):
        return self.name, self.id, self.age_restriction, self.is_rented

    @classmethod
    def from_date(cls,id,name, date,age_restriction):
        day, month, year = [int(x) for x in date.split('.')]
        return cls(name,id,year, month_name[month] ,age_restriction)
    
    def __repr__(self) -> str:
        status = 'not rented'
        if self.is_rented:
            status = "rented"
        
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: {status}"
    
