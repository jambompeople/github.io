alpha = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
def convert(num, base=2):
    assert base <= len(alpha), f"Unable to convert to base {base}"
    converted = ""
    while num > 0:
        converted += alpha[num % base]
        num //= base

    if len(converted) == 0:
        return "0"
    return converted[::-1]

num = int(input("Please enter a number:"))
base = int(input("Please enter the base:"))
print(convert(num, base))
