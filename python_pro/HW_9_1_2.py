class User:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    def __setattr__(self, name, value):
        if name == "first_name" or name == "last_name":
            raise AttributeError("Direct modification of first_name and last_name is not allowed.")
        else:
            super().__setattr__(name, value)

    def __getattr__(self, name):
        if name == "first_name" or name == "last_name":
            raise AttributeError(f"Property '{name}' does not exist.")
        else:
            raise AttributeError(f"Property '{name}' does not exist.")


# Приклад використання

user = User("John", "Doe")

print(user.first_name)  # Виводиться значення first_name

user.first_name = "Jane"  # Викликає AttributeError: Direct modification of first_name is not allowed.

print(user.unknown_property)  # Викликає AttributeError: Property 'unknown_property' does not exist.
