from threading import Thread


class Person(Thread):
    
    def learningPython(self):
        for i in range(21):
            print("Learning python")
            print(i)

    def run(self):
        for i in range(501):
            print("running")


class Cat(Thread):
    def catchRat(self):
        print("catchiing rat")

    def run(self):
        for i in range(501):
            print("running with 4 legs")


person = Person()
person.start()

cat = Cat()
cat.catchRat()
cat.run()