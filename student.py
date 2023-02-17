class Student:
    def __init__(self, name):
        self.name = name
        self.test_scores = []

    def add_test(self, score):
        self.test_scores.append(score)