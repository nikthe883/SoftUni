class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = (photos_count + 3) // 4  # Calculate the required number of pages
        return cls(pages)

    def add_photo(self, label):
        for page_number, page in enumerate(self.photos, start=1):
            if len(page) < 4:
                page.append(label)
                slot_number = len(page)
                return f"{label} photo added successfully on page {page_number} slot {slot_number}"

        return "No more free slots"

    def display(self):
        photos = ["-" * 11]

        for row in self.photos:
            photos.append(("[] " * len(row)).rstrip())
            photos.append("-" * 11)

        return '\n'.join(photos)


# Test the PhotoAlbum class
import unittest

class TestsPhotoAlbum(unittest.TestCase):
    def test_init_creates_all_attributes(self):
        album = PhotoAlbum(2)
        self.assertEqual(album.pages, 2)
        self.assertEqual(album.photos, [[], []])

    def test_from_photos_should_create_instance(self):
        album = PhotoAlbum.from_photos_count(12)
        self.assertEqual(album.pages, 3)
        self.assertEqual(album.photos, [[], [], []])

    def test_add_photo_with_no_free_spots(self):
        album = PhotoAlbum(1)
        album.add_photo("baby")
        album.add_photo("first grade")
        album.add_photo("eight grade")
        album.add_photo("party with friends")
        result = album.add_photo("prom")
        self.assertEqual(result, "No more free slots")

    def test_add_photo_with_free_spots(self):
        album = PhotoAlbum(1)
        album.add_photo("baby")
        album.add_photo("first grade")
        album.add_photo("eight grade")
        album.add_photo("party with friends")
        self.assertEqual(album.photos, [['baby', 'first grade', 'eight grade', 'party with friends']])

    def test_display_with_one_page(self):
        album = PhotoAlbum(1)
        album.add_photo("baby")
        album.add_photo("first grade")
        album.add_photo("eight grade")
        album.add_photo("party with friends")
        result = album.display().strip()
        self.assertEqual(result, "-----------\n[baby] [first grade] [eight grade] [party with friends]\n-----------")

    def test_display_with_three_pages(self):
        album = PhotoAlbum(3)
        for _ in range(8):
            album.add_photo("asdf")
        result = album.display().strip()
        self.assertEqual(result, "-----------\n[asdf] [asdf] [asdf] [asdf]\n-----------\n[asdf] [asdf] [asdf] [asdf]\n-----------\n\n-----------")

if __name__ == "__main__":
    unittest.main()
