import re

def pow(number, pwr):
    if pwr == 1:
        return number
    return number * pow(number, pwr - 1)


def factorial(number):
    if number <= 1:
        return 1

    return number * factorial(number - 1)


def max_items(items):
    if len(items) == 2:
        return items[0] if items[0] > items[1] else items[1]

    other_items_max = max_items(items[1:])
    return other_items_max if other_items_max > items[0] else items[0]


def find_primes(number):
    result = []
    for i in range(2, number + 1):
        if all(i % d > 0 for d in range(2, i)):
            result.append(i)
    return result

# print(find_primes(20))
# print(pow(2, 4))
# print(factorial(100))

# print(max_items([1,2,3,6,20,10, 56, 100, 7]))

def is_palindrome(value):
    striped_value = re.sub(r'\W+', '', value.lower())
    return striped_value[::-1] == striped_value


print(is_palindrome('level'))
