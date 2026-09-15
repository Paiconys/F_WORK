"""N+1 vs select_related (Django ORM).

Dependencies:
  pip install Django
"""

import os
import django
from django.conf import settings
from django.db import connection, models


if not settings.configured:
    settings.configure(
        DEBUG=True,
        SECRET_KEY="dev",
        INSTALLED_APPS=["__main__"],
        DATABASES={"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}},
        USE_TZ=False,
    )
    django.setup()


class Author(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        app_label = "demo"


class Comment(models.Model):
    body = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        app_label = "demo"


def setup() -> None:
    with connection.schema_editor() as se:
        se.create_model(Author)
        se.create_model(Comment)
    a = Author.objects.create(name="Ada")
    Comment.objects.create(body="hi", author=a)
    Comment.objects.create(body="yo", author=a)


def bad() -> int:
    connection.queries_log.clear()
    for c in Comment.objects.all():
        _ = c.author.name  # N+1
    return len(connection.queries)


def good() -> int:
    connection.queries_log.clear()
    for c in Comment.objects.select_related("author"):
        _ = c.author.name
    return len(connection.queries)


if __name__ == "__main__":
    setup()
    print("queries bad:", bad())
    print("queries good:", good())
