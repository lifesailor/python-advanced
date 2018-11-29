# logging by print


def sqrt(x, guess=1.0):
    if x < 0:
        print("음수가 입력되었습니다.")
        raise ValueError

    print("Find sqrt of {} starting with guess {}".format(x, guess))
    if good_enough(guess, x):
        return guess
    else:
        print("Guess is not good enough. Improve...")
        new_guess = improve_guess(guess, x)
        return sqrt(x, new_guess)


def good_enough(guess, x):
    print("Check if {} is a good enough guess.".format(guess))
    if abs(guess * guess - x) < 0.1:
        return True
    else:
        return False


def avg(a, b):
    return (a + b) / 2.0


def improve_guess(guess, x):
    new_guess = avg(guess, x/guess)
    print("Improved guess to: {}".format(new_guess))
    return new_guess


sqrt(36)