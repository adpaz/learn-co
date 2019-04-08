import copy
import collections

class School():
    
    def __init__(self, name):
        self.name = name
        self._roster = {}
    
    def roster(self):
        return self._roster
    
    def add_student(self, name, level):
        if level in self._roster:
            self._roster[level].append(name)
        else:
            self._roster[level] = [name]
        return self._roster
    def grade(self, grade):
        return self._roster[grade]
    def sort_roster(self):
        sorting = collections.OrderedDict(sorted(self._roster.items()))
        return sorting
    
        