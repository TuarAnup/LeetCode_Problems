#Iterative approach

class anagram:
    def __init__(self,s1,s2):
        self.s1 = s1
        self.s2 = s2
        self.a = ''
    def frequency(self):
        if len(self.s1) == len(self.s2):
            for char in self.s1:
                if char in self.s2:
                    self.a += char
    def check_func(self):
        if self.a == self.s1:
            print('The given strings',self.s1,'and',self.s2 ,'are Anagram')
        else:
            print('no,Not an Anagram')
a = input('Enter the first string')
b = input('Enter the Second String')
obj = anagram(a,b)
obj.frequency()
obj.check_func()
        

# Counter approach

from collections import Counter
def are_anagrams(s1,s2):
    if len(s1) != len(s2):
        return False
    return Counter(s1) == Counter(s2)
are_anagrams('anup','puna')

        


