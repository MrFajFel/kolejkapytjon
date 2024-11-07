from webbrowser import Error


class Queue:
    def __init__(self,n):
        self.tab = []
        self.n = n

    def add(self,elem):
        if len(self.tab) < self.n:
            self.tab.append(elem)
        else:
            raise Exception("Queue is full")


    def remove(self):
        if len(self.tab) == 0:
            raise Exception("Queue is empty")
        else:
            return self.tab.pop(0)
