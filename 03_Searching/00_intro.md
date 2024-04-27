# Searcning

## Binary Search
What is Binary Search?

Binary Search is one of the most fundamental and useful algorithms in Computer Science. It describes the process of searching for a specific value in an ordered collection.

Terminology used in Binary Search:

Target - the value that you are searching for
Index - the current location that you are searching
Left, Right - the indicies from which we use to maintain our search Space
Mid - the index that we use to apply a condition to determine if we should search left or right

## 3 Parts of a Successful Binary Search

- Pre-processing - Sort if collection is unsorted.

- Binary Search - Using a loop or recursion to divide search space in half after each comparison.

- Post-processing - Determine viable candidates in the remaining space.

## Templates
When we first learned Binary Search, we might struggle. We might study hundreds of Binary Search problems online and each time we looked at a developer's code, it seemed to be implemented slightly differently. Although each implementation divided the problem space in 1/2 at each step, one had numerous questions:

Why was it implemented slightly differently?

What was the developer thinking?

Which way was easier?

Which way is better?

After many failed attempts and lots of hair-pulling, we found 3 main templates for Binary Search. To prevent hair-pulling and to make it easier for new developers to learn and understand, we have provided them in the next chapter.