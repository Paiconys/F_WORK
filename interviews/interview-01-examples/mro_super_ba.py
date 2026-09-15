"""DRILL: другой граф наследования — ответ уже не B.

Dependencies: none (stdlib)
"""


class A:
    def bar(self):
        print("A")


class B(A):
    def foo(self):
        print("B")


class C:
    def bar(self):
        print("C")


class D(B, C):
    def bar(self):
        super().bar()


obj = D()
obj.bar()  # -> A

print(D.__mro__)
# (D, B, A, C, object) — B без bar, A с bar; до C не доходим
