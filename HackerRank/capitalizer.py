string = input()
split = string.split()
split = [(split[i]).capitalize() for i in range(len(split))]

i = 0
j = 0
newtext = ''

while i < len(string):
    if string[i] == ' ':
        newtext += ' '
        i += 1
    else:
        newtext += split[j]
        i += len(split[j])
        j += 1

print(newtext)
 