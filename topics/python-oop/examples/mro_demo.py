"""MRO / diamond — учебный пример к теории.

Dependencies: none (stdlib)
"""


class A:
    def f(self):
        return "A"


class B(A):
    def f(self):
        return "B+" + super().f()


class C(A):
    def f(self):
        return "C+" + super().f()


class D(B, C):
    pass


print(D().f())      # B+C+A  (C3)
print(D.__mro__)
