## Titanic 4 (2 POINTS)

Implement the following functions:

1. A function that identifies passengers with a lucky ticket and calculates among them the proportion of those who drowned. We'll call a ticket "lucky" if it meets the following requirements:
    - is a natural number (without letters and other symbols);
    - consists of an even number of digits;
    - the sum of the digits of the first half of the number is equal to the sum of the digits of the second half.
Implement a helper function ```is_lucky``` which determines whether a ticket is lucky or not by its number and apply to the dataframe the ```apply``` method, calling this function.
