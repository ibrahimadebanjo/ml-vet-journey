1. Machine learning processes 

![](./images/DPV1.jpg)


![](./images/DPV2.jpg)


2. Pandas coding

 Imports 
 
![Pandas imports](./images/pandas_01_imports.jpg)



![pandas imports](./images/pandas_02_imports_results.jpg)


---

# Pandas Data Structures & Operations Notes

## Primary Data Structures

```
          [Primary Data Structure]
             /                \
     Series (1D)          DataFrame (2D)

```

> **NB:** `df.shape()` doesn't work because **Shape is not a function, it's a property/attribute**.
> * **Correct:** `df.shape`
> * *Note:* No need to print `df.info()` and `df.describe()`, they are already printed.
> 
> 

---

### 1. Series (1D)

* **Definition:** Data structures are collections of data types that provide the best way of organizing items (values) in terms of memory usage.
* **Characteristics:**
* 1-Dimensional Data structure.
* Homogeneous array (i.e., homogeneous data type).
* It is **size immutable**.



#### **Example Series Representation:**

| Index | Price |
| --- | --- |
| 0 | 200 |
| 1 | 300 |
| 2 | 400 |
| 3 | 450 |
| 4 | 500 |

---

### 2. DataFrame (2D)

* **Definition:** 2D Data structure.
* **Characteristics:** Heterogeneous, **size mutable** (i.e., with different data types).

---

## Joins & Merges

### Methods:

We have **left, right, outer, and inner** joins.

---

### Joins Visualized (Venn Diagrams)

#### **① Left Join**

```
      [A]          [B]
   (#######)     (     )
  (#########)---(       )
   (#######)     (     )
      
      [A] is returned (the rest will be ignored)

```

#### **② Right Join**

```
      [A]          [B]
   (     )     (#######)
  (       )---(#########)
   (     )     (#######)
      
      [B] is returned

```

#### **③ Outer Join**

```
      [A]          [B]
   (#######)     (#######)
  (#########)---(#########)
   (#######)     (#######)
      
      Everything will be returned

```

#### **④ Inner Join**

```
      [A]          [B]
   (     )  ###  (     )
  (       )(###)(       )
   (     )  ###  (     )
      
      Only returns features that are common to both tables

```

---

### Merge (Based on Columns)

```
     ( A )-----( B )
        \     /
         (   )   <-- Merged based on Common Column

```

> **Rule:** Whatever property/properties both **A** & **B** have will be visible in the merged dataset.

---

---

## Using Concat() Method & Merge() Application

### 1. Lambda and Apply

* **Lambda:** It is a quick, small, "one-line" function. No need to add `def`.

#### **Comparison:**

```
  [Standard Function]               [Lambda equivalent]
  def Square(x):            ===>     Lambda x: x**2
      return x**2

```

---

### 2. Apply() Method

`Apply()` means go to each row or each column, and run this function on it.

#### **Syntax & Alignment Map:**

```
                  ┌──────────────────────┐
                  │ df['Column'].apply() │  <-- Used for 1 Column
                  └──────────┬───────────┘
                             │
            ┌────────────────┴────────────────┐
            ▼                                 ▼
┌───────────────────────────┐     ┌───────────────────────────┐
│  df.apply(function,       │     │  df.apply(function,       │
│           axis = 1)       │     │           axis = 0)       │
└───────────┬───────────────┘     └───────────┬───────────────┘
            │                                 │
            ▼                                 ▼
    [Used for EACH ROW]             [Used for EACH COLUMN]
                                        (Default)

```

---

### Application Examples

#### **① Apply lambda to one column:**

```python
df['Salary'] = df['Salary'].apply(lambda x: x**2)

```

#### **② Clean data (Handling negative values):**

> If some values are negative, make them 0.

```python
df['Alcohol'] = df['Alcohol'].apply(lambda x: 0 if x < 0 else x)

```