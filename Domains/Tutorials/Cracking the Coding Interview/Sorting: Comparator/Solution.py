# Enter your code here. Read input from STDIN. Print output to STDOUT
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __str__(self):
        return str(self.name) + " " + str(self.score)
    def __repr__(self):
        return self
    def comparator(x,y):
        if x.score < y.score:
            return 1
        elif y.score < x.score:
            return -1
        elif x.name < y.name:
            return -1
        elif y.name > x.name:
            return 1
        else:
            return 0
