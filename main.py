from Queue import Queue

queue = Queue(10)
for i in range(10):
    number = int(input("Podaj Liczbe"))
    queue.add(number)



for i in range(10):
    print(queue.remove())

