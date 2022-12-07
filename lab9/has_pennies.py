def has_pennies(cents):
    nickelsOnly = (cents % 5 != 0)
    return nickelsOnly