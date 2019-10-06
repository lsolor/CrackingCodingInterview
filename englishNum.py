
def english_int(num):
    negative_num = False
    if num == 0:
        return "zero"
    if num < 0:
        negative_num = True
        num *= -1

    phone = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    first19 = ["one", "two", "three", "four", "five", "six", "seven", "eight",
               "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
               "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    mag = ["", "thousand", "million", "billion", "trillion"]
    index = 0
    english_num = ""

    while num // 1000 != 0 or num % 1000 != 0:

        if num % 1000 != 0:
            # start of function
            temp = num % 1000

            s = ""
            if temp // 100 >= 1:
                s += phone[(temp // 100) - 1]
                s += " "
                s += "hundred"
                s += " "
                temp = temp % 100

            if temp // 20 >= 1:

                s += tens[(temp // 10) - 2]
                s += " "
                temp = temp % 10

            if 1 <= temp < 20:
                s += first19[(temp % 100) - 1]
                s += " "

            s += mag[index]
            if index != 0:
                s += ","
            s += " "
            english_num = s + english_num
            index += 1
            num //= 1000

        else:

            index += 1
            num //= 1000

    if negative_num:
        english_num = "negative " + english_num
    return english_num


if __name__ == "__main__":
    x = english_int(-129934)
    print(x)
