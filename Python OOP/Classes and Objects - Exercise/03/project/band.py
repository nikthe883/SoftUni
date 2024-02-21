from album import Album

class Band:
    
    albums = []

    def __init__(self, name) -> None:
        self.name = name

    def add_album(self, album):
        if album not in self.albums:
            self.albums.append(album)
            return f"Band {self.name} has added their newest album {album.name}."
        
        return f"Band {self.name} already has {album.name} in their library."
    
    def remove_album(self,album_name):

        for album in self.albums:
            if album_name == album.name:
                if not album.published:
                    self.albums.remove(album)
                    return f"Album {album_name} has been removed."
                return f"Album has been published. It cannot be removed."
            
        return f"Album {album_name} is not found."

    def details(self):
        result = f"Band {self.name}\n"

        for album in self.albums:
            result += f"{album.details()}\n"

        return result