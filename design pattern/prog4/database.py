class Database:
    def __init__(self, id):
        self.id = id
        self.data = {}

    def add(self, key, value):
        if key in self.data:
            return False, "Key already exists."
        self.data[key] = value
        return True, "Added successfully."

    def update(self, key, value):
        if key not in self.data:
            return False, "Key does not exist."
        self.data[key] = value
        return True, "Updated successfully."

    def remove(self, key):
        if key not in self.data:
            return False, "Key does not exist."
        del self.data[key]
        return True, "Removed successfully."

    def display(self):
        for key, value in self.data.items():
            print(f"{key}| {value}")
        print(" ")
        
        
