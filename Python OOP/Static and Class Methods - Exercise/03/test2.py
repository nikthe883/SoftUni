from project.category import Category
from project.document import Document
from project.storage import Storage
from project.topic import Topic


c = Category(1, "C")
t = Topic(1, "T", "C:\\user")
d = Document(1, 1, 1, "D")
s = Storage()

doc = Document.from_instances(1, c, t, "Doc")

print(doc.id, 1)
print(doc.category_id, 1)
print(doc.topic_id, 1)
print(doc.file_name, "Doc")
print(doc.tags, [])
