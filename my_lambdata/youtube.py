# ytlink Function Lives here
def ytlink(l, h, m, s):
    ''' This function will take a YouTube link
        ask user to input in hours, minutes and 
        seconds and return link that starts 
        the video at the specified timemark'''
    t = (h*60*60) + (m*60) + s
    # create link components
    first = "https://youtu.be/"
    second = l.split("=")
    second = second[1]
    third = "?t=" + str(t)
    l = first + second + third
    return l    # Return the modified link

l = input("Paste YouTube link here: ")
print()
h = int(input("Enter hour(s) to start: "))
print()
m = int(input("Enter minute(s) to start: "))
print()
s = int(input("Enter second(s) to start: "))

print()
ytlink(l, h, m, s)
print(l)