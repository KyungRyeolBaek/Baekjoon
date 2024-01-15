alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
text = input()
count = 0

for a in alpha:
    if a in text:
        count += 1
        text = text.replace(a, ' ')

print(len(text))