from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    categories = []
    topics = []
    documents = []

    @staticmethod
    def return_param(id_received, params):
        return [param for param in params if param.id == id_received][0]

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        current_category = self.return_param(category_id, self.categories)
        current_category.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        current_topic = self.return_param(topic_id, self.topics)
        current_topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        current_document = self.return_param(document_id, self.documents)
        current_document.edit(new_file_name)

    def delete_category(self, category_id: int):
        current_category = self.return_param(category_id, self.categories)
        if current_category in self.categories:
            self.categories.remove(current_category)

    def delete_topic(self, topic_id: int):
        current_topic = self.return_param(topic_id, self.topics)
        if current_topic in self.topics:
            self.topics.remove(current_topic)

    def delete_document(self, document_id: int):
        current_document = self.return_param(document_id, self.documents)
        if current_document in self.documents:
            self.documents.remove(current_document)

    def get_document(self, document_id: int):
        return self.return_param(document_id, self.documents)

    def __repr__(self):
        result = ""
        for document in self.documents:
            result += f"{document.__repr__()}\n"

        return result


c1 = Category(1, "work")
t1 = Topic(1, "daily tasks", "C:\\work_documents")
d1 = Document(1, 1, 1, "finilize project")

d1.add_tag("urgent")
d1.add_tag("work")

storage = Storage()
storage.add_category(c1)
storage.add_topic(t1)
storage.add_document(d1)

print(c1)
print(t1)
print(storage.get_document(1))
print(storage)
