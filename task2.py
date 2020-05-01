def funnyString(s):
    r = s[::-1]
    for i in range(0, len(s)-1):
        if abs(ord(s[i+1]) - ord(s[i])) != abs(ord(r[i+1]) - ord(r[i])):
            return 'Not Funny'
    return 'Funny'
