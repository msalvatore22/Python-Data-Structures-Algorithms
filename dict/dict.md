# Dictionairies
A dictionary is a collection which is unordered, changeable and indexed.
Comprised of key: value pairs

## Memory
* Python uses a hash table under the hood. You store the values in an array, and thwen use a hash function to find the index of the array cell that corresponds to the key-value pair.

## Update/Insert
O(1) time complexity

## Linear Search
O(N)

## Deletion
* pop() -> remove element based on key
* popItem() -> remove a random key, value pair
* clear() -> clears the whole dictionary
* del -> delete key value pair

O(1) best case
O(N) average case

## Other Medthods

* fromkeys(): dictionary.fromkeys([sequence], value)
* get(): dictionary.get(key, value)
* items(): dictionary.items() -> list of tuples (key, value)
* keys(): dictionary.keys() -> list of keys
* setdefault: dictionary.setdefault(key, default_value)
* values: dictionary.values() -> list of values
* update(): dictionary.uppdate(other_dictionaryORlist of tuples)

## Operators/Built Ins
* in operator
    * checks for existence of key in dictionary
    * returns boolen
    * O(1)
* for operator
    * iterate over dictionary
* all()
    * check if all values are true or false
    * all or nothing (all have to be true to be true)
* any()
    * all values true =  true
    * all false = false
    * one true = true
    * one false = true
* len()
* sorted(iterable, reverse=boolean, key)

## Dictionary vs List
| Dictionary | List |
| ---------- | ---- |
| Unordered  | Ordered |
| Acess via keys | Access via index |
| Collection of key value pairs | Collection of elements |
| Preferred when you have unique key values | Preferred when you have ordered data |
| No duplicate keys | Allow duplicate elements |

## Time Complexity
| Operation | Time Complexity | Space Complexity |
| --------- | --------------- | ---------------- |
| Creation   | O(len(dict)) | O(N) |
| Insertion  | O(1), O(N)   | O(1) |
| Traversing | O(N))        | O(1) |
| Accessing  | O(1)         | O(1) |
| Searching  | O(N)         | O(1) |
| Deletion   | O(1)         | O(1) |

