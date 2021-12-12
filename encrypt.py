from grid import get_letter, get_coords

text = input().replace(' ','').lower()
x = None
for i in range(len(text)-1):
    if text[i] == text[i+1] and i%2 == 0:
        text = text[:i+1] + 'x' + text[i+1:]
if len(text)%2 != 0:
    text += 'x'