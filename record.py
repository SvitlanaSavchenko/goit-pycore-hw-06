from name import Name
from phone import Phone

class Record:
    """Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів."""
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        # Додавання нового телефонного номеру до запису
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)
        else:
            print("Phone number not found.")
            
    def find_phone(self, phone):
        # Пошук телефонного номеру у записі
        for phone in self.phones:
            if phone.value == phone:
                return phone.value
        raise ValueError("Phone number not found in record.")

    def edit_phone(self, old_phone, new_phone):
        # Редагування існуючого телефонного номеру у записі
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                break
        else:
            raise ValueError("Phone number not found in record.")

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(str(phone) for phone in self.phones)}"
