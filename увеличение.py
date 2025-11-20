class Counter:
    count = 0

    def increment():
        Counter.count += 1

    def decrement():
        Counter.count -= 1

    def get_count():
        return Counter.count


Counter.increment()
Counter.increment()
print(Counter.get_count())

Counter.decrement()
print(Counter.get_count())