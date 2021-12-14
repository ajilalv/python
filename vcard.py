def readData(st,en,lines):
    contact=[]
    data = lines[st+1:en]
    for dt in data:
        txt = dt.strip()
        if('FN:' in txt):
            contact.append(txt[3:])
        if('TEL' in txt):
            contact.append(txt.split(':')[-1])
    return contact

lines = []
with open('test.txt') as f:
    lines = f.readlines()

ln = 1
for line in lines:
    if(line.strip() == 'BEGIN:VCARD'):
        start = ln
    if(line.strip() == 'END:VCARD'):
        end = ln
        print(readData(start,end,lines))
    ln+=1
    
print(start,end)
