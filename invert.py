def invert(lst: list):
    emptlist = []
    if lst == []:
        return []
    if lst == [0]:
        return [0]
    for numbers in lst:
        if numbers > 0:
            new = -numbers
            emptlist.append(new)
# We utilize an empty list to append each updated (inverted) value which then returns once the loop ends. 
# The loop ends once it reaches the end of the list.
        elif numbers < 0:
            new = -numbers
            emptlist.append(new)
    return emptlist
