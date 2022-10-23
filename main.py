def intRomanNumeral(number):
    values = [1, 4, 5, 9, 10, 40, 50, 90,100, 400, 500, 900, 1000]
    symbols = ["I", "IV", "V", "IX", "X", "XL","L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12
      
    while number:
        div = number // values[i]
        number %= values[i]
  
        while div:
            print(symbols[i], end = "")
            div -= 1
        i -= 1

number = int(input("Enter a number: "))
intRomanNumeral(number)