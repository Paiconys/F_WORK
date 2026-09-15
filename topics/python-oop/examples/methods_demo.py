"""instance / class / static methods.

Dependencies: none (stdlib)
"""


class A:
    def inst(self):
        return "instance", self

    @classmethod
    def cls(cls):
        return "class", cls

    @staticmethod
    def st():
        return "static"


print(A().inst()[0], A.cls()[0], A.st())
