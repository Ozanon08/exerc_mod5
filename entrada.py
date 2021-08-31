def analise(s):

    if s % 5 == 0 and s % 7 == 0:
        return("fizzbuzz")

    elif s % 5 == 0:
        return("fizz")

    elif s % 7 == 0:
        return("buzz")

    elif s % 5 != 0 and s % 7 != 0:
        return("miss")
