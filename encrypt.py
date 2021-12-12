from grid import get_letter, get_coords

text = input().replace(' ','').lower()
x = None
for i in range(len(text)-1):
    if text[i] == text[i+1] and i%2 == 0:
        text = text[:i+1] + 'x' + text[i+1:]
if len(text)%2 != 0:
    text += 'x'
lst = []
for i in range(0,len(text),2):
    lst.append(text[i]+text[i+1])
encrypted = ''
for i in lst:
    if get_coords(i[0])[0] == get_coords(i[1])[0]:
        encrypted += get_letter([  get_coords(i[0])[0] , (get_coords(i[0])[1]-1)%5  ]) + get_letter([  get_coords(i[1])[0] , ( get_coords(i[1])[1] -1 )%5 ])
    elif get_coords(i[0])[1] == get_coords(i[1])[1]:
        encrypted += get_letter([ (get_coords(i[0])[0]+1)%5 , get_coords(i[0])[1] ]) + get_letter([ (get_coords(i[1])[0]+1)%5 ,  get_coords(i[1])[1]  ])
    else:
        encrypted += get_letter([get_coords(i[1])[0],get_coords(i[0])[1]]) + get_letter([get_coords(i[0])[0],get_coords(i[1])[1]])
print(encrypted)
