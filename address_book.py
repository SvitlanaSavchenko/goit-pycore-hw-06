from collections import UserDict
from record import Record

class AddressBook(UserDict):
    """Клас для зберігання та управління записами."""
    def __init__(self):
        self.data = {}
        
    def add_record(self, record):
         # Додавання запису до адресної книги
        self.data[record.name.value] = record

    def search_record_by_name(self, name):
        if name in self.data:
            return self.data[name]
        else:
            return None

    def delete_record_by_name(self, name):
        if name in self.data:
            del self.data[name]
        else:
            print("Contact not found.")
            
    def __str__(self):
        return '\n'.join(str(record) for record in self.data.values())
