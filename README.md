# 📘 Python String Slicing – Complete Practice Program

## 📌 Project Overview

This project demonstrates all types of string slicing operations in Python using:

```python
Name = "Harshal Warke"
```

It covers:

- Positive Indexing
- Negative Indexing
- Positive + Positive slicing
- Negative + Negative slicing
- Positive + Negative slicing
- Negative + Positive slicing
- Positive step size
- Negative step size

---

## 🔹 Index Structure

### Positive Index

```
 H  a  r  s  h  a  l     W  a  r  k  e
 0  1  2  3  4  5  6  7  8  9 10 11 12
```

### Negative Index

```
 H   a   r   s   h   a   l      W   a   r   k   e
-13 -12 -11 -10  -9  -8  -7  -6  -5  -4  -3  -2  -1
```

---

# 🧩 Types of Slicing Covered

## 1️⃣ Positive + Positive Index

Example:
```python
Name[0:7]
```
Output:
```
Harshal
```

---

## 2️⃣ Negative + Negative Index

Example:
```python
Name[-13:-6]
```
Output:
```
Harshal
```

---

## 3️⃣ Positive + Negative Index

Example:
```python
Name[0:-6]
```
Output:
```
Harshal
```

---

## 4️⃣ Negative + Positive Index

Example:
```python
Name[-13:7]
```
Output:
```
Harshal
```

---

## 5️⃣ Positive Index with Negative Step

Reverse full string:

```python
Name[::-1]
```

Output:
```
ekraW lahsraH
```

Other examples included:
- Reverse with step 2
- Reverse specific range

---

## 6️⃣ Positive Index with Positive Step

Skip characters example:

```python
Name[::2]
```

Output:
```
HrhlWre
```

Other examples included:
- Step = 1 (normal copy)
- Step = 2 (skip 1 character)
- Step = 3 (skip 2 characters)

---

# 🎯 What You Learn

- How slicing works in Python
- Start index is included
- Stop index is excluded
- How negative indexing works
- How step size controls skipping
- How to reverse a string using slicing

---

# 🚀 How to Run

1. Install Python
2. Save file as:

```
string_slicing.py
```

3. Run:

```
python string_slicing.py
```

---

# 👨‍💻 Author

Harshal Warke  
Python Practice Project
