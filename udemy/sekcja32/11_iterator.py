# Wzorzec projektowy Iterator jest używany do sekwencyjnego dostępu do elementów kolekcji
# bez konieczności ujawniania jej wewnętrznej reprezentacji.

# Zalety:
# 1. Umożliwia dostęp do zawartości kolekcji bez ujawniania jej wewnętrznej struktury.
# 2. Wspiera różne sposoby przeglądania kolekcji.
# 3. Upraszcza interfejsy kolekcji.

# Wady:
# 1. Może być niepotrzebnie skomplikowany, jeśli kolekcja jest prosta.
# 2. Dodatkowe obiekty iteratorów mogą zwiększyć zużycie pamięci.

class EmployeeNames:
    def __init__(self, names):
        self._names = names

    def __iter__(self):
        return EmployeeIterator(self._names)

class EmployeeIterator:
    def __init__(self, names):
        self._names = names
        self._index = 0

    def __next__(self):
        if self._index < len(self._names):
            name = self._names[self._index]
            self._index += 1
            return name
        raise StopIteration

# Użycie wzorca Iterator
employee_names = EmployeeNames(["Anna", "John", "Marie", "Mark"])
for name in employee_names:
    print(name)
