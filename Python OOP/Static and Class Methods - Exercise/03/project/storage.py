class Storage:

    def __init__(self) -> None:
        self.categories = []
        self.topics = []
        self.documents = []

    
    def add_category(self,category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)
    
    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self,category_id,new_name):
        for i in self.categories:
            if i.id == category_id:
                i.edit(new_name)

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        for i in self.topics:
            if i.id == topic_id:
                i.edit(new_topic,new_storage_folder)

    def edit_document(self, document_id, new_file_name):
        for i in self.documents:
            if i.id == document_id:
                i.edit(new_file_name)

    def delete_category(self,category_id):
        for i, v in enumerate(self.categories):
            if v.id == category_id:
                del self.categories[i]

    def delete_topic(self,topic_id):
        for i, v in enumerate(self.topics):
            if v.id == topic_id:
             del self.topics[i]


    def delete_document(self,document_id):
        for i, v in enumerate(self.documents):
            if v.id == document_id:
                del self.documents[i]

    def get_document(self, document_id):
        for i in self.documents:
            if i.id == document_id:
                return repr(i)
            
    def __repr__(self) -> str:
        result = ""
        for i in self.documents:
            result += f"{repr(i)}\n"

        return result