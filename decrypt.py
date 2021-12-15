from grid import get_coords,get_letter

text = input()
lst = []
for i in range(0,len(text)-1,2):
    lst.append(text[i]+text[i+1])
decrypted = ''
for i in lst:
    if get_coords(i[0])[0] == get_coords(i[1])[0]:
        decrypted += get_letter([  get_coords(i[0])[0] , (get_coords(i[0])[1]+1)%5  ]) + get_letter([  get_coords(i[1])[0] , ( get_coords(i[1])[1] +1 )%5 ])
    elif get_coords(i[0])[1] == get_coords(i[1])[1]:
        decrypted += get_letter([ (get_coords(i[0])[0]-1)%5 , get_coords(i[0])[1] ]) + get_letter([ (get_coords(i[1])[0]-1)%5 ,  get_coords(i[1])[1]  ])
    else:
        decrypted += get_letter([get_coords(i[1])[0],get_coords(i[0])[1]]) + get_letter([get_coords(i[0])[0],get_coords(i[1])[1]])
print(decrypted)