class utils:
    def reversed(number):
        if not isinstance(number, int):
            raise TypeError("Input must be an integer")

        sign = -1 if number < 0 else 1
        reversed_str = str(abs(number))[::-1]
        return sign * int(reversed_str)

    @staticmethod
    def formatter(number):
        if not isinstance(number, int):
            raise TypeError("Input must be an integer")

        binary = bin(number)
        octal = oct(number)
        return binary, octal