# 🐍 Python Data Types Cheat Sheet

> Essential syntax and methods for **List**, **Tuple**, **Set**, and **Dictionary**.

---

# 📌 List (`[]`)

## Create

```python
numbers = [10, 20, 30]
```

## Access

```python
numbers[0]
numbers[-1]
```

## Update

```python
numbers[1] = 50
```

## Add

```python
numbers.append(40)
numbers.insert(1, 100)
numbers.extend([50, 60])
```

## Delete

```python
numbers.pop()
numbers.pop(1)
numbers.remove(20)
del numbers[0]
numbers.clear()
```

## Search

```python
20 in numbers
numbers.index(30)
numbers.count(20)
```

## Sort

```python
numbers.sort()
numbers.sort(reverse=True)
numbers.reverse()
```

## Copy

```python
copy = numbers.copy()
```

## Length

```python
len(numbers)
```

## Loop

```python
for item in numbers:
    print(item)
```

---

# 📌 Tuple (`()`)

## Create

```python
person = ("Rejo", 20)
```

## Access

```python
person[0]
person[-1]
```

## Count

```python
person.count("Rejo")
```

## Index

```python
person.index(20)
```

## Length

```python
len(person)
```

## Loop

```python
for item in person:
    print(item)
```

## Unpacking

```python
name, age = person
```

```python
first, *rest = (1, 2, 3, 4)
```

> **Note:** Tuple is **immutable**.

* ❌ `append()`
* ❌ `remove()`
* ❌ `update()`

---

# 📌 Set (`{}`)

## Create

```python
nums = {1, 2, 3}
```

## Add

```python
nums.add(4)
nums.update([5, 6])
```

## Delete

```python
nums.remove(2)
nums.discard(3)
nums.pop()
nums.clear()
```

## Search

```python
2 in nums
```

## Length

```python
len(nums)
```

## Loop

```python
for item in nums:
    print(item)
```

## Set Operations

```python
a.union(b)
a.intersection(b)
a.difference(b)
```

---

# 📌 Dictionary (`{key: value}`)

## Create

```python
student = {
    "name": "Rejo",
    "age": 20
}
```

## Access

```python
student["name"]
student.get("name")
```

## Add

```python
student["city"] = "Gopalganj"
```

## Update

```python
student["age"] = 21

student.update({
    "age": 22
})
```

## Delete

```python
student.pop("age")
del student["name"]
student.clear()
```

## Search

```python
"name" in student
```

## Get All

```python
student.keys()
student.values()
student.items()
```

## Copy

```python
copy = student.copy()
```

## Length

```python
len(student)
```

## Loop

### Only Keys

```python
for key in student:
    print(key)
```

### Only Values

```python
for value in student.values():
    print(value)
```

### Key & Value

```python
for key, value in student.items():
    print(key, value)
```

---

# ⭐ Most Used Methods

## List

```text
append()
insert()
extend()
remove()
pop()
sort()
reverse()
index()
count()
copy()
clear()
```

## Tuple

```text
count()
index()
unpacking
```

## Set

```text
add()
update()
remove()
discard()
pop()
union()
intersection()
difference()
clear()
```

## Dictionary

```text
get()
update()
keys()
values()
items()
pop()
copy()
clear()
```

---

# 📋 Quick Comparison

| Feature          | List | Tuple | Set | Dictionary |
| ---------------- | :--: | :---: | :-: | :--------: |
| Ordered          |   ✅  |   ✅   |  ❌  |      ✅     |
| Mutable          |   ✅  |   ❌   |  ✅  |      ✅     |
| Duplicate Values |   ✅  |   ✅   |  ❌  |      ✅     |
| Duplicate Keys   |   —  |   —   |  —  |      ❌     |

---

# 🚀 90% Essential Methods

### List

* `append()`
* `insert()`
* `extend()`
* `remove()`
* `pop()`
* `sort()`
* `reverse()`

### Tuple

* `count()`
* `index()`
* `unpacking`

### Set

* `add()`
* `update()`
* `remove()`
* `discard()`
* `union()`
* `intersection()`

### Dictionary

* `get()`
* `update()`
* `keys()`
* `values()`
* `items()`
* `pop()`
