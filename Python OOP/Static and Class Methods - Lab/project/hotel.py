
class Hotel:

    def __init__(self, name ) -> None:
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars):
        return cls(f"{stars} stars Hotel")
    

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for n in self.rooms:
            if n.number == room_number:
                if n.take_room(people) is None:
                    self.guests += people
                

    def free_room(self, room_number):
        for n in self.rooms:
            if n.number == room_number:
                self.guests -= n.guests 
                n.free_room()
                      

    def status(self):
        return f"Hotel {self.name} has {self.guests} total guests\n"\
        f"Free rooms: {', '.join([str(n.number) for n in self.rooms if not n.is_taken])}\n"\
        f"Taken rooms: {', '.join([str(n.number) for n in self.rooms if n.is_taken])}"
    
