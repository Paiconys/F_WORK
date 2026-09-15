"""super() идёт по MRO, не «всегда к прямому родителю по имени».

Dependencies: none (stdlib)
"""


class A:
    def f(self):
        return "A"


class B(A):
    def f(self):
        return "B+" + super().f()


print(B().f())  # B+A
