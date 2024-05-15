from field import Field

class Phone(Field):
    """Клас для зберігання номера телефону. Має валідацію формату (10 цифр)."""
    def __init__(self, value):
        super().__init__(value)
        if not self.validate_phone():
            raise ValueError("Invalid phone number format.")

    def validate_phone(self):
        """Перевірка правильності формату номера телефону."""

        if len(self.value) != 10:
            raise ValueError("The phone number must contain 10 digits")

        if not self.value.isdigit():
            raise ValueError("The phone number must contain only numbers")

        return True

    def __eq__(self, other):
        """Магічний метод для порівняння об'єктів класу Phone за їхнім значенням."""
        if isinstance(other, Phone):
            return self.value == other.value
        return False
