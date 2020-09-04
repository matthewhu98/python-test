#!/usr/bin/env python3

class Test:
    hello = 'hello'
    world = 'world'
    def greeting(self):
        print(self.hello, self.world)

def main():
    test = Test()
    test.greeting()

if __name__ == '__main__': main()
    