# Interview 01 — Codeshare (14 Sep 2026)

Источник: https://codeshare.io/GqboAq  
История восстановлена из `codeHistory` (52 правки). Ниже — **финальные варианты** задач, которые кидал интервьюер.

Формат: «что выведется / какой метод вызовется».

---

## 1. Mutable default argument

Время ~14:34–14:35 UTC

```python
def func(x=[]):
    x.append(1)
    print(x)

func()          # ?
func([1, 2])    # ?
func()          # ?
func([2, 3])    # ?
```

**Ответ (как в паде у интервьюера):**

```text
[1]
[1, 2, 1]
[1, 1]
[2, 3, 1]
```

**Почему:** дефолт `x=[]` создаётся **один раз** при определении функции. Первый `func()` мутирует этот общий список. Когда передаёшь свой список — дефолт не трогается. Третий `func()` снова берёт общий дефолт, в котором уже был `1`.

---

## 2. MRO + `super().bar()` (вариант A)

Время ~14:37 UTC

```python
class A:
    def foo(self):
        print('A')

class B:
    def bar(self):
        print('B')

class C:
    def bar(self):
        print('C')

class D(A, B, C):
    def bar(self):
        super().bar()

obj = D()
obj.bar()
```

**Ответ:** `B`

**Почему:** `D.__mro__` ≈ `(D, A, B, C, object)`.  
`super()` из `D.bar` ищет следующий `bar` после `D`: у `A` нет `bar`, у `B` есть → печатает `B` (не `C`).

---

## 3. MRO + `super().bar()` (вариант B)

Время ~14:39 UTC — тот же вопрос, другой граф наследования

```python
class A:
    def bar(self):
        print('A')

class B(A):
    def foo(self):
        print('B')

class C:
    def bar(self):
        print('C')

class D(B, C):
    def bar(self):
        super().bar()

obj = D()
obj.bar()
```

**Ответ:** `A`

**Почему:** `D.__mro__` ≈ `(D, B, A, C, object)`.  
После `D` идёт `B` (нет `bar`) → `A` (есть `bar`) → `A`. До `C` очередь не доходит.

---

## 4. Late binding в замыкании (lambda в цикле)

Время ~14:41 UTC — последний код в паде

```python
flist = []

for i in range(3):
    flist.append(lambda: print(i))

[f() for f in flist]
```

**Ответ:**

```text
2
2
2
```

**Почему:** lambda захватывает **имя** `i`, а не значение на итерации. К моменту вызова цикл уже закончился, `i == 2`.

**Как починить (если спросят):**

```python
flist.append(lambda i=i: print(i))  # дефолт фиксирует значение
# или
flist.append((lambda i: (lambda: print(i)))(i))
```

---

## Как тренировать

1. Закрой ответы, скажи вслух за 20–40 сек.  
2. Для MRO всегда проговаривай: `Class.__mro__` → «кто следующий с этим методом».  
3. Для дефолтов: «объект дефолта один на функцию».  
4. Для lambda в цикле: «поздняя привязка имени».

Связанные темы в `python-basics.md`: mutable default, MRO/diamond, closures.

---

## Примеры для запуска

```bash
python interviews/interview-01-examples/mutable_default.py
python interviews/interview-01-examples/mro_super_abc.py
python interviews/interview-01-examples/mro_super_ba.py
python interviews/interview-01-examples/lambda_late_binding.py
```
