mul = {"hundred": 100, "thousand": 1000, "million": 1_000_000}
nums = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "nineteen": 19,
    "twenty": 20,
    "thirty": 30,
    "forty": 40,
    "fifty": 50,
    "sixty": 60,
    "seventy": 70,
    "eighty": 80,
    "ninety": 90,
}


def parse_int(string):
    pieces = string.replace("-", " ").split(" ")
    cur = 0
    for piece in pieces:
        if piece in nums:
            cur += nums[piece]
        elif piece in mul:
            cur += mul[piece] * (cur % mul[piece]) - (cur % mul[piece])
    return cur
