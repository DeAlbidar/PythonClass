# Exercise
#

def num_str():
    numbers = input("numbers: ")
    digits_mapping = {
        "1": "One",
        "2": "Two",
        "3": "Three",
        "4": "Four",
        "5": "Five",
        "6": "Six",
        "7": "Seven",
        "8": "Eight",
        "9": "Nine",
        "0": "Zero"
    }
    output = ""
    for i in numbers:
        output += digits_mapping.get(i, "!") + " "
    print(output)


# if __name__ == '__main__':
#     s = input().strip()
#     t = input().strip()
#
#     print(findTheDifference(s, t))
def findTheDifference(s: str, t: str) -> str:
    first = s
    second = t
    res = ''
    for se in second:
        res = se
        if res not in first:
            res = res
    return res


