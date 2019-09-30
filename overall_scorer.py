def isReliable(*args):

    diff = abs(args[0] - args[1])

    if diff <= 10:
        comment = "Highly Reliable"
    elif 10 <= diff < 20:
        comment = "Less Reliable"
    else:
        comment = "Unreliable"

    return comment

def scorer(*args):

    avg = (args[0] + args[1]) // 2

    if avg < -5:
        return "Terrible"
    elif -5 <= avg < 5:
        return "Think once again"
    elif 5 <= avg < 10:
        return "Sounds good"
    else:
        return "Go for it!"