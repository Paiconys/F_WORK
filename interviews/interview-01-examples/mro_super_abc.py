"""DRILL: какой метод вызовет super().bar()?

MRO: всегда смотри Class.__mro__

Dependencies: none (stdlib)
"""


class A:
    def foo(self):
        print("A")


class B:
    def bar(self):
        print("B")


class C:
    def bar(self):
        print("C")


class D(A, B, C):
    def bar(self):
        # super() = следующий класс в MRO после D
        super().bar()


obj = D()
obj.bar()  # -> B

print(D.__mro__)
# (D, A, B, C, object) — у A нет bar, у B есть
