from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        super().__init__(value)
		

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Ведіть номер у правильному форматі!")
		

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))
        
    
    def remove_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)
        else:
            raise ValueError('Телефон не знайдено!')
    
    def edite_phone(self, old_phone, new_phone):
        self.remove_phone(old_phone)
        self.add_phone(new_phone)
    
    def find_phone(self, phone):
        if phone in self.phones:
            return f'{self.name}:{self.phones}'
        else:
            return 'Телефон не знайдено!'
    
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
	    

    def find_record_by_name(self, name):
        if name in self.data:
            return str(self.data[name])
        else:
            return f"Контакт {name} не знайдено"

    def remove_record_by_name(self, name):
        if name in self.data:
            del self.data[name]
        else:
            return f"Контакт {name} не знайдено"