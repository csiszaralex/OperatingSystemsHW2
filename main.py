import sys

class MemoriaKeret:
    def __init__(self, name: str) -> None:
        self.name = name
        self.lap = 0
        self.freeze = 0
        self.used = False
    def setLap(self, lap: int):
        self.lap = lap
        self.freeze = 4
        self.used = False
    def read(self):
        self.freeze = 0
        self.used = True
    def unread(self):
        self.used = False
    def time(self):
        if self.freeze > 0:
            self.freeze -= 1 
    def isFreezed(self) -> bool:
        return self.freeze > 0
    def __str__(self) -> str:
        return '' if self.lap == 0 else self.name+('*' if self.used else '')+(f'({self.freeze})' if self.isFreezed() else '')

def lep():
    for i in mems:
        i.time()

mems: list[MemoriaKeret] = [MemoriaKeret('A'),MemoriaKeret('B'),MemoriaKeret('C')]

inp = ''
if inp == '':
    for line in sys.stdin:
        if len(line.strip()) != 0:
            inp = line

out = ''
errors = 0
sor: list[int] = []
for i in inp.split(','):
    sor.append(abs(int(i)))

def csinal(akt: int)->str:
    #Megnézzük benne van-e egyikben, ha igen akkor .read() és cont
    for mem in mems:
        if mem.lap == akt:
            mem.read()
            return '-'
    
    #Végig megyek a listán, ha találok olyat ahol szabad bearkni, berakom
    restart = True
    while(restart):
        restart = False
        for mem in mems:
            if not mem.isFreezed():
                if not mem.used:
                    mem.setLap(akt)
                    mems.remove(mem)
                    mems.append(mem)
                    return mem.name
                mem.unread()
                mems.remove(mem)
                mems.append(mem)
                restart = True
                break;
                
    return '*'

for i in range(len(sor)):
    akt = sor[i]
    lep()
    most = csinal(akt)
    # print(f'FIFO: {mems[2]} {mems[1]} {mems[0]} -> {most} \t ')
    if most != '-':
        errors+=1;
    out += most
    


    
print(out)
print(errors)





