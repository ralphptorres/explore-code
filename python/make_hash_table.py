class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, string):
        return sum([ord(c) for c in string])

    def add(self, key, value):
        if self.hash(key) not in self.collection:
            self.collection[self.hash(key)] = {}
        self.collection[self.hash(key)][key] = value

    def remove(self, key):
        if self.hash(key) in self.collection:
            if key in self.collection[self.hash(key)]:
                del self.collection[self.hash(key)][key]

    def lookup(self, key):
        if self.hash(key) in self.collection and key in self.collection[self.hash(key)]:
            return self.collection[self.hash(key)][key]
        else:
            return None


h = HashTable()
h.add("golf", "sport")
# h.add('cfc', 'sport')
h.add("fcc", "ball")
print(h.lookup("golf"))
print(h.lookup("cfc"))
