a = [['p','l','a','y','f'],['i','r','e','x','m'],['b','c','d','g','h']]
chars = {'p':[0,4],'l':[1,4],'a':[2,4],'y':[3,4],'f':[4,4],'i':[0,3],'j':[0,3],'r':[1,3],'e':[2,3],'x':[3,3],'m':[4,3],'b':[0,2],'c':[1,2],'d':[2,2],'g':[3,2],'h':[4,2],'k':[0,1],'n':[1,1],'o':[2,1],'q':[3,1],'s':[4,1],'t':[0,0],'u':[1,0],'v':[2,0],'w':[3,0],'z':[4,0]}

def get_coords(s):
    return chars[s]

def get_letter(s):
    return list(chars.keys())[list(chars.values()).index(s)]
#print(get_letter(list(map(int,input().split()))))