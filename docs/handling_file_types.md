# Handling Different File Types

## Introduction

We are going to learn how to handle different file types in Python. We will learn how to read and write to different file types such as text files, CSV files, TSV files, Parquet files and JSON files.

## Text Files

Text files are simple files that contain text data. You can read and write to text files using Python.

### Reading Text Files

You can read text files using the `open()` function. The `open()` function takes two arguments: the file path and the mode. The mode is set to `r` for reading text files.

```python
file_path = 'data.txt'
with open(file_path, 'r') as file:
    data = file.read()
    print(data)
```

### Writing to Text Files

You can write to text files using the `open()` function. The mode is set to `w` for writing text files.

```python
file_path = 'data.txt'
data = 'Hello, World!'
with open(file_path, 'w') as file:
    file.write(data)
```

### Reading Text Files Line by Line

You can read text files line by line using the `readline()` function.

```python
file_path = 'data.txt'
with open(file_path, 'r') as file:
    for line in file:
        print(line)
```

Of course, you can store each line in a list or dictionary as required!

---

## CSV Files

CSV files are files that contain comma-separated values. You can read and write to CSV files using Python.

### Reading CSV Files

You can read CSV files using the `csv` module. The `csv` module provides a `reader` object that allows you to read CSV files.

```python
import csv

file_path = 'data.csv'

with open(file_path, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

### Writing to CSV Files

You can write to CSV files using the `csv` module. The `csv` module provides a `writer` object that allows you to write to CSV files.

```python
import csv

file_path = 'data.csv'

data = [
    ['Name', 'Age'],
    ['Alice', 25],
    ['Bob', 30]
]

with open(file_path, 'w') as file:
    writer = csv.writer(file)
    writer.writerows(data)
```

---

## TSV Files

TSV files are files that contain tab-separated values. You can read and write to TSV files using Python.

### Reading TSV Files

You can read TSV files using the `csv` module. The `csv` module provides a `reader` object that allows you to read TSV files.

```python
import csv

file_path = 'data.tsv'

with open(file_path, 'r') as file:
    reader = csv.reader(file, delimiter='\t')
    for row in reader:
        print(row)
```

### Writing to TSV Files

You can write to TSV files using the `csv` module. The `csv` module provides a `writer` object that allows you to write to TSV files.

```python
import csv

file_path = 'data.tsv'

data = [
    ['Name', 'Age'],
    ['Alice', 25],
    ['Bob', 30]
]

with open(file_path, 'w') as file:
    writer = csv.writer(file, delimiter='\t')
    writer.writerows(data)
```

---

## JSON Files

JSON files are files that contain JSON data. You can read and write to JSON files using Python.

### Reading JSON Files

You can read JSON files using the `json` module. The `json` module provides a `load()` function that allows you to read JSON files.

```python
import json

file_path = 'data.json'

with open(file_path, 'r') as file:
    data = json.load(file)
    print(data)
```

### Writing to JSON Files

You can write to JSON files using the `json` module. The `json` module provides a `dump()` function that allows you to write to JSON files.

```python
import json

file_path = 'data.json'

data = {
    'Name': 'Alice',
    'Age': 25
}

with open(file_path, 'w') as file:
    json.dump(data, file)
```

---

## Parquet Files

Parquet files are columnar storage files that are optimized for reading and writing data. You can read and write to Parquet files using Python.

### Reading Parquet Files

You can read Parquet files using the `pandas` library. The `pandas` library provides a `read_parquet()` function that allows you to read Parquet files.

```python
import pandas as pd

file_path = 'data.parquet'

data = pd.read_parquet(file_path)

print(data)
```

### Writing to Parquet Files

You can write to Parquet files using the `pandas` library. The `pandas` library provides a `to_parquet()` function that allows you to write to Parquet files.

```python
import pandas as pd

file_path = 'data.parquet'

data = pd.DataFrame({
    'Name': ['Alice', 'Bob'],
    'Age': [25, 30]
})

data.to_parquet(file_path)
```

---

## Can `pandas` be used for the other file types?

Yes, `pandas` can be used to read and write to CSV, TSV and JSON files as well. The `pandas` library provides functions such as `read_csv()`, `read_table()` and `read_json()` to read CSV, TSV and JSON files respectively. Similarly, the `pandas` library provides functions such as `to_csv()`, `to_csv()` and `to_json()` to write to CSV, TSV and JSON files respectively.

```python
import pandas as pd

# Reading CSV files
data = pd.read_csv('data.csv')

# Writing to CSV files
data.to_csv('data.csv')

# Reading TSV files
data = pd.read_table('data.tsv')

# Writing to TSV files
data.to_csv('data.tsv', sep='\t')

# Reading JSON files
data = pd.read_json('data.json')

# Writing to JSON files
data.to_json('data.json')
```

Pandas is a powerful library that can be used to read and write to different file types. It is recommended to use `pandas` for reading and writing to CSV, TSV, JSON and Parquet files.  We can also use `pandas` in the ***TRANSFORM*** step of the ETL process, so much more to come on that!

---
