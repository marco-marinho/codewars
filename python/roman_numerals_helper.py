class RomanNumerals:

    @staticmethod
    def to_roman(val : int) -> str:
        if val >= 1000:
            return "M" + RomanNumerals.to_roman(val - 1000)
        if val >= 900:
            return "CM" + RomanNumerals.to_roman(val - 900)
        if val >= 500:
            return "D" + RomanNumerals.to_roman(val - 500)
        if val >= 400:
            return "CD" + RomanNumerals.to_roman(val - 400)
        if val >= 100: 
            return "C" + RomanNumerals.to_roman(val - 100)
        if val >= 90:
            return "XC" + RomanNumerals.to_roman(val - 90)
        if val >= 50:  
            return "L" + RomanNumerals.to_roman(val - 50)
        if val >= 40:
            return "XL" + RomanNumerals.to_roman(val - 40)
        if val >= 10:
            return "X" + RomanNumerals.to_roman(val - 10)
        if val >= 9:
            return "IX" + RomanNumerals.to_roman(val - 9)
        if val >= 5:
            return "V" + RomanNumerals.to_roman(val - 5)
        if val >= 4:
            return "IV" + RomanNumerals.to_roman(val - 4)
        if val >= 1:
            return "I" + RomanNumerals.to_roman(val - 1)
        return ""

    @staticmethod
    def from_roman(roman_num : str) -> int:
        def aux(roman_num : str, idx : int) -> int:
            lookup = [("M", 1000), ("CM", 900), ("D", 500), ("CD", 400), ("C", 100), ("XC", 90), 
                  ("L", 50), ("XL", 40), ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1)]
            if idx == len(roman_num):
                return 0
            for key, val in lookup:
                if roman_num.startswith(key, idx):
                    return val + aux(roman_num, idx + len(key))
            raise ValueError("Invalid roman numeral")
        return aux(roman_num, 0)