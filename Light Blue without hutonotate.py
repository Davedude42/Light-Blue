#########################
#                       #
#     *Light Blue*      #
#    David Haroldsen    #
# Last Modified 6/27/19 #
#                       #
#########################


from tkinter import *
from time import sleep, time
from math import *
from random import randint

VERSION = '1.0.2'

def opengames():
    global games, gamesn, gamess, filet
    file = open('C:\hutonotate.txt','r')
    filet = file.read()
    filet += '%'
    games = []
    gamesn = []
    gamess = []
    i = 0
    while i < len(filet):
        if filet[i - 13 : i] == 'NEW GAME OF: ' or filet[i - 20 : i] == 'NEW GAME PLAYED BY: ':
            if filet[i - 13 : i] == 'NEW GAME OF: ':
                gamess.append(i - 13)
            else:
                gamess.append(i - 20)
            RET = '';
            while filet[i] != '$':
                RET += filet[i]
                
                i += 1
            gamesn.append(RET)
        if filet[i-3] + filet[i-2] + filet[i-1] == 'CK$':
            games.append([])
            RET = ''
            while filet[i] != '%' and filet[i] + filet[i + 1] != 'NE':
                
                if filet[i] != ' ' and filet[i] != ',' and filet[i] != '$' and filet[i] != '\n' and filet[i] != '/n' and filet[i] != '':
                    RET += filet[i]
                else:
                    if RET != '':
                        games[-1].append(RET)
                        RET = ''
                i += 1
        i += 1
    gamess.append(len(filet) - 1)
    file.close()
    
print('// Hi, I guess.')
COM=int(input('// Play without or with COM? (0/1)'))
while COM!=0 and COM!=1:
    COM=int(input('// Invalide! Play with COM? (0/1)'))
if COM==1:
    COM=int(input('// You White or Black? (1/-1)')) * -1
    DIFF=int(input('// What level? (0/1/2/3/4)'))
    VARIABILITY=float(input('// Variability? (0 < N < 10)'))
"""

fil = open('C:\\version.txt', 'r')
filt = fil.read()
VAL = int(filt[6:])
if VERSION != filt[0:5]:
    filt = VERSION + '0'
else:
    VAL += 1
fil.close()
fil = open('C:\\version.txt', 'w')
fil.write(str(VAL))
fil.close()

VERSION += str(VAL)
fil.close()"""
COL=['Black','','White']
if COM != 2:
    """file = open('C:\hutonotate.txt','a')
    if input('// Notate? (0/1)')=='1':
        if COM == 0:
            name1 = input('// Name of player playing white?')
            while '$' in name1 or 'OF: ' in name1 or '%' in name1 or 'NE' in name1 or 'BY: ' in name1:
                name = input('// Invalide name! Name?')
            name2 = input('// Name of player playing black?')
            while '$' in name2 or 'OF: ' in name2 or '%' in name2 or 'NE' in name2 or 'BY: ' in name2:
                name2 = input('// Invalide name! Name?')
        else:
            if COM == -1:
                name1 = input('// Name of player playing COM?')
                while '$' in name1 or 'OF: ' in name1 or '%' in name1 or 'NE' in name1 or 'BY: ' in name1:
                    name1 = input('// Invalide name! Name?')
                name2 = 'COM v' + VERSION
            else:
                name2 = input('// Name of player playing COM?')
                while '$' in name2 or 'OF: ' in name2 or '%' in name2 or 'NE' in name2 or 'BY: ' in name2:
                    name2 = input('// Invalide name! Name?')
                name1 = 'COM v' + VERSION
        
        file.write('$\n$\nNEW GAME OF: ' + name1 + ' vs ' + name2)
        if COM != 0:
            file.write(' V=' + str(VARIABILITY))
        file.write('$\nWHITE BLACK$\n')"""
        
window = Tk()
window.title('Light Blue v' + VERSION)
window.lift()
PMOVPLACE=[-1,-1]

# C:\Users\david\AppData\Local\Programs\Python\Python37\Chess 1.5\background.png
"""
1 - pawn
2 - knight
3 - bishop
4 - rook
5 - queen
6 - king
"""

lit=[[[-3,-4,-4,-5,-5,-4,-4,-3,-3,-4,-4,-5,-5,-4,-4,-3,-3,-4,-4,-5,-5,-4,-4,-3,-3,-4,-4,-5,-5,-4,-4,-3,-2,-3,-3,-4,-4,-3,-3,-2,-1,-2,-2,-2,-2,-2,-2,-1,2,2,0,0,0,0,2,2,2,1,9,0,0,1,9,2],\
     [-2,-1,-1,-0.5,-0.5,-1,-1,-2,-1,0,0,0,0,0,0,-1,-1,0,0.5,0.5,0.5,0.5,0,-1,-0.5,0,0.5,0.5,0.5,0.5,0,-0.5,0,0,0.5,0.5,0.5,0.5,0,-0.5,-1,0.5,0.5,0.5,0.5,0.5,0,-1,-1,0,0.5,0,0,0,0,-1,-2,-1,-1,-0.5,-0.5,-1,-1,-2],\
     [0,0,0,0,0,0,0,0,0.5,1,1,1,1,1,1,0.5,-0.5,0,0,0,0,0,0,-0.5,-0.5,0,0,0,0,0,0,-0.5,0.5,0,0,0,0,0,0,-0.5,-0.5,0,0,0,0,0,0,-0.5,-0.5,0,0,0,0,0,0,-0.5,0,-3,0,3,0.5,3,-3,0],\
     [-2,-1,-1,-1,-1,-1,-1,-2,-1,0,0,0,0,0,0,-1,-1,0,0.5,1,1,0.5,0,-1,-1,0.5,0.5,1,1,0.5,0.5,-1,-1,0,1,1,1,1,0,-1,-1,1,1,1,1,1,1,-1,-1,0.5,0,0,0,0,0.5,-1,-2.5,-2.5,-2.5,-2.5,-2.5,-2.5,-2.5,-2.5],\
     [-5,-4,-3,-3,-3,-3,-4,-5,-4,-2,0,0,0,0,-2,-4,-3,0,1,1.5,1.5,1,0,-3,-3,0.5,1.5,2,2,1.5,0.5,-3,-3,0,1.5,2,2,1.5,0,-3,-3,0.5,3,1.5,1.5,3,0.5,-3,-4,-2,0,0.5,0.5,0,-2,-4,-5,-4,-3,-3,-3,-3,-4,-5],\
     [0,0,0,0,0,0,0,0,13,13,13,13,13,13,13,13,1,1,2,3,3,2,1,1,0.5,0.5,1,2.5,2.5,1,0.5,0.5,0,0,0,5,5,0,0,0,0.5,-0.5,-1,0,0,-1,-0.5,0.5,0.5,1,1,-2,-2,1,1,0.5,0,0,0,0,0,0,0,0]],\
     
     [[-3,-4,-4,-5,-5,-4,-4,-3,-3,-4,-4,-5,-5,-4,-4,-3,-3,-4,-4,-5,-5,-4,-4,-3,-3,-4,-4,-5,-5,-4,-4,-3,-2,-3,-3,-4,-4,-3,-3,-2,-1,-2,-2,-2,-2,-2,-2,-1,2,2,0,0,0,0,2,2,2,9,1,0,0,9,1,2],\
     [-2,-1,-1,-0.5,-0.5,-1,-1,-2,-1,0,0,0,0,0,0,-1,-1,0,0.5,0.5,0.5,0.5,0,-1,-0.5,0,0.5,0.5,0.5,0.5,0,-0.5,0,0,0.5,0.5,0.5,0.5,0,-0.5,-1,0.5,0.5,0.5,0.5,0.5,0,-1,-1,0,0.5,0,0,0,0,-1,-2,-1,-1,-0.5,-0.5,-1,-1,-2],\
     [0,0,0,0,0,0,0,0,0.5,1,1,1,1,1,1,0.5,-0.5,0,0,0,0,0,0,-0.5,-0.5,0,0,0,0,0,0,-0.5,0.5,0,0,0,0,0,0,-0.5,-0.5,0,0,0,0,0,0,-0.5,-0.5,0,0,0,0,0,0,-0.5,0,-3,3,0.5,3,0,-3,0],\
     [-2,-1,-1,-1,-1,-1,-1,-2,-1,0,0,0,0,0,0,-1,-1,0,0.5,1,1,0.5,0,-1,-1,0.5,0.5,1,1,0.5,0.5,-1,-1,0,1,1,1,1,0,-1,-1,1,1,1,1,1,1,-1,-1,0.5,0,0,0,0,0.5,-1,-2.5,-2.5,-2.5,-2.5,-2.5,-2.5,-2.5,-2.5],\
     [-5,-4,-3,-3,-3,-3,-4,-5,-4,-2,0,0,0,0,-2,-4,-3,0,1,1.5,1.5,1,0,-3,-3,0.5,1.5,2,2,1.5,0.5,-3,-3,0,1.5,2,2,1.5,0,-3,-3,0.5,3,1.5,1.5,3,0.5,-3,-4,-2,0,0.5,0.5,0,-2,-4,-5,-4,-3,-3,-3,-3,-4,-5],\
     [0,0,0,0,0,0,0,0,13,13,13,13,13,13,13,13,1,1,2,3,3,2,1,1,0.5,0.5,1,2.5,2.5,1,0.5,0.5,0,0,0,5,5,0,0,0,0.5,-0.5,-1,0,0,-1,-0.5,0.5,0.5,1,1,-2,-2,1,1,0.5,0,0,0,0,0,0,0,0]]]
BOARD = [[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],\
         [4,2,3,5,6,3,2,4,1,1,1,1,1,1,1,1],\
         [48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63],\
         [1,1,1,1,1,1,1,1,4,2,3,5,6,3,2,4],\
         [0],[0,0,0],[0,0,0],[0],[],[0]]
PM=[-1,-1]
PBS=[]
# bpl bpe wpl wpe points bca wca enpasante notation turn-num
SIDETEXTS = []
BOXES = []
BOXTEXT = []
BOXTEXT3=[]
POINTVALS=[0,10,30,30,50,90,9000]
NAMES = ['','\u2659', '\u2658', '\u2657', '\u2656', '\u2655', '\u2654','\u265A', '\u265B', '\u265C', '\u265D', '\u265E', '\u265F']
NAMESOOO=['None','Pawn','Knight','Bishop','Rook','Queen','King']
temp = [['8','7','6','5','4','3','2','1'],['a','b','c','d','e','f','g','h']]
HW = 420
CS = -1
S = 0
veto2=0
xy=[-1,-1,-1]
TURN=1
if COM!=0:
    SIDE=COM
COLORS = ['white','#ddd','#777','#555']
c = Canvas(window, width=480, height=425, bg=COLORS[2])
c.pack()

NUM=8000
veto=0
# --------------------------------

def gd(o,t,f=0):
    if t!=0 and o!=0:
        if t=='':
            return o//abs(o)
        else:
            if f==0:
                return o/t
            else:
                return o//t
    else:
        return 0
def hasthree(B,PB):
    PBB=deepcopy(PB)
    if B[0:4] in PBB:
        PBB.pop(PBB.index(B[0:4]))
    if B[0:4] in PBB:
        PBB.pop(PBB.index(B[0:4]))
    if B[0:4] in PBB:   
        return True
    return False
    
def deepcopy(li):
    re = []
    for i in range(len(li)):
        re.append(li[i][:])
    return re
PMC=['#FFFA8A','#E6DD3D']
def drawboxes(B):
    c.itemconfig(SCORETEXTW,text='White:'+str(BoardVal(B)))
    c.itemconfig(SCORETEXTB,text='Black:'+str(BoardVal(B)*-1))
    c.itemconfig(SCORETEXTT,text='Turn #'+str(B[9][0]//2))
    if S == 0:
        if COM==0:
            side=TURN
        else:
            side=COM*-1
    else:
        side = S
    for i in range(64):
        if i<8:
            c.itemconfig(SIDETEXTS[i],text=temp[0][abs(7*(side==-1)-i)])
        elif i<16:
            c.itemconfig(SIDETEXTS[i],text=temp[1][abs(7*(side==-1)-(i-8))])
        if i in B[0]:
            c.itemconfig(BOXTEXT[abs((63*(side==-1))-i)],text=NAMES[B[1][B[0].index(i)]*-1],font=('Arial Unicode MS' ,25))
        elif i in B[2]:
            c.itemconfig(BOXTEXT[abs((63*(side==-1))-i)],text=NAMES[B[3][B[2].index(i)]],font=('Arial Unicode MS' ,25))
        else:
            c.itemconfig(BOXTEXT[abs((63*(side==-1))-i)],text='',font=('Arial Unicode MS' ,25))
        if CS==i:
            c.itemconfig(BOXTEXT[abs((63*(side==-1))-i)],font=('Arial Unicode MS' ,35))
        if veto!=0:
            c.itemconfig(BOXTEXT2[abs((63*(side==-1))-i)],text=lit[gd(veto,'')==-1][-abs(veto)][abs((63*(gd(veto,'')==-1))-i)])
        else:
            c.itemconfig(BOXTEXT2[abs((63*(side==-1))-i)],text='')
        c.itemconfig(BOXES[i],fill=COLORS[(i%2*2-1)*(((i//8)%2)*2-1)==-1])
    if PM[0]!=-1:
        c.itemconfig(BOXES[abs((63*(side==-1))-PM[0])],fill=PMC[(PM[0]%2*2-1)*(((PM[0]//8)%2)*2-1)==-1])
        c.itemconfig(BOXES[abs((63*(side==-1))-PM[1])],fill=PMC[(PM[1]%2*2-1)*(((PM[1]//8)%2)*2-1)==-1])
            
    c.update()
def chb(S1,S2,B,S3='no',gg=True):
    if True:
        SB=deepcopy(B)
        SB[8].append(str(temp[1][S1%8])+str(8-S1//8)+','+str(temp[1][S2%8])+str(8-S2//8))
        SB[9][0]+=1
        if S1 in SB[0]:
            ps=SB[1][SB[0].index(S1)]
            #if ps==6 and SB[9][0]<5:
            #    SB[4][0]+=3
            #SB[4][0]+=lit[1][6-ps][63-S1]
            #SB[4][0]-=lit[1][6-ps][63-S2]
            P=ps
            if P==6:
                SB[5][1]=1
            if P==4 and S1%8==0:
                SB[5][0]=1
            if P==4 and S1%8==7:
                SB[5][2]=1
            if P==6 and S1%8==4 and S2%8==6 and 7 in SB[0]:
                SB[0][SB[0].index(7)]=5
                SB[5][1]=2
            if P==6 and S1%8==4 and S2%8==2 and 0 in SB[0]:
                SB[0][SB[0].index(0)]=3
                SB[5][1]=2
            SB[0][SB[0].index(S1)]=S2
            if S2 in SB[2]:
                #SB[4][0]-=POINTVALS[SB[3][SB[2].index(S2)]]+lit[1][-SB[3][SB[2].index(S2)]][63-S2]
                SB[3].pop(SB[2].index(S2))
                SB[2].pop(SB[2].index(S2))
            elif P==1 and S2//8==5 and S2%8==abs(SB[7][0]) and gd(SB[7][0],'')==1:
                #SB[4][0]-=POINTVALS[1]+lit[1][-1][63-(S2-8)]
                SB[3].pop(SB[2].index(S2-8))
                SB[2].pop(SB[2].index(S2-8))
            if S3!='no':
                #SB[4][0]+=POINTVALS[P]+lit[1][-P][63-S2]
                #SB[4][0]-=lit[1][-S3][63-S2]+POINTVALS[S3]
                SB[1][SB[0].index(S2)]=S3
            if P==1 and S1//8==1 and S2//8==3:
                SB[7][0]=(S1%8)*-1
            else:
                SB[7][0]=0
        elif S1 in SB[2]:
            ps=SB[3][SB[2].index(S1)]
            if ps==6 and SB[9][0]<5:
                SB[4][0]-=3
            #SB[4][0]-=(lit[0][6-ps][S1])
            #SB[4][0]+=(lit[0][6-ps][S2])
            P=ps
            if P==6:
                SB[6][1]=1
            if P==4 and S1%8==0:
                SB[6][0]=1
            if P==4 and S1%8==7:
                SB[6][2]=1
            if P==6 and S1%8==4 and S2%8==6 and 63 in SB[2]:
                SB[2][SB[2].index(63)]=61
                SB[6][1]=2
            if P==6 and S1%8==4 and S2%8==2 and 56 in SB[2]:
                SB[2][SB[2].index(56)]=59
                SB[6][1]=2
            SB[2][SB[2].index(S1)]=S2
            if S2 in SB[0]:
                #SB[4][0]+=POINTVALS[SB[1][SB[0].index(S2)]]+lit[0][-SB[1][SB[0].index(S2)]][S2]
                SB[1].pop(SB[0].index(S2))
                SB[0].pop(SB[0].index(S2))
            elif P==1 and S2//8==2 and S2%8==abs(SB[7][0]) and gd(SB[7][0],'')==-1:
                #SB[4][0]+=POINTVALS[SB[1][SB[0].index(S2+8)]]+lit[0][-SB[1][SB[0].index(S2+8)]][(S2+8)]
                SB[1].pop(SB[0].index(S2+8))
                SB[0].pop(SB[0].index(S2+8))
            if S3!='no':
                #SB[4][0]-=POINTVALS[P]+lit[0][-P][S2]
                SB[4][0]+=lit[0][-S3][S2]+POINTVALS[S3]
                SB[3][SB[2].index(S2)]=S3
            if P==1 and S1//8==6 and S2//8==4:
                SB[7][0]=S1%8
            else:
                SB[7][0]=0
        return SB
        

def kic(C,B,gg=True):
    if 6 in B[2+C]:
        KP=B[1+C][B[2+C].index(6)]
        for i in B[1-C]:
            if KP in pmoves(i,B,gg):
                return True
    return False
def kicm(C,B,gg=True,ch=True):
    if len(cmoves(C,B,gg))==0:
        if (not(ch) or kic(C,B,gg)):
            return True
    else:
        return False
def kid(B,ch=True):
    WP=B[3].copy()
    BP=B[1].copy()
    WP.sort()
    BP.sort()
    if (len(cmoves(1,B))==0 and (not(ch) or not(kic(1,B)))) or (len(cmoves(-1,B))==0 and (not(ch) or not(kic(-1,B))))\
       or ((WP==[6] or WP==[2,6]) and (BP==[6] or BP==[2,6])) or hasthree(B,PBS):
        return True
    else:
        return False
def motion(event):
    global xy
    xy[0]=event.x-2
    xy[1]=event.y-2
    x=(xy[0]-22)//50
    y=(xy[1]-2)//50
    if not(x==8 or y==8 or x==-1 or y==-1):
        #xy[2]=(x+(y*8))
        xy[2]=abs((63*(TURN==-1))-(x+(y*8)))
    else:
        xy[2]=-1

def press(event):
    
    global PMOVEPLACE
    global CS
    global BOARD
    global TURN
    global TURNNUM
    global PBS
    global PM
    if TURN!=0:
        if TURN!=COM:
            #print(BOARD)
            if xy[2] in BOARD[1+TURN]:
                CS=xy[2]
            elif CS!=-1 and xy[2] in pmoves(CS,BOARD):
                OB = deepcopy(BOARD)
                BOARD = deepcopy(chb(CS,xy[2],BOARD))
                drawboxes(BOARD)
                PBS.append(deepcopy(BOARD[0:4]))
                if hasthree(BOARD, PBS):
                    ggg = input('// WARNING!! If you do this it will be a tie! Still do it? (y/n)')
                    if ggg != 'y' and ggg != 'Y':
                        BOARD = deepcopy(OB)
                        drawboxes(BOARD)
                        return

                PM=[CS,xy[2]]
                #file.write(BOARD[8][len(BOARD[8])-1])
                if BOARD[2+TURN][BOARD[1+TURN].index(xy[2])]==1 and xy[2]//8==3.5-3.5*TURN:
                    drawboxes(BOARD)
                    np=input('// What piece will it become?\n2 - Knight\n3 - Bishop\n4 - Rook\n5 - Queen\n')
                    print(np)
                    while np!='2' and np!='3' and np!='4'and np!='5':
                        np=input('// Invalide!!\nWhat piece will it become?\n2 - Knight\n3 - Bishop\n4 - Rook\n5 - Queen\n')
                    BOARD[2+TURN][BOARD[1+TURN].index(xy[2])]=int(np)
                    #BOARD[4]+=TURN*((POINTVALS[int(np)])-1)
                    #file.write(','+str(np))
                """if TURN==-1:
                    #file.write('$\n')
                else:
                    #file.write('  ')"""
                CS=-1
                drawboxes(BOARD)
                if kic(TURN*-1,BOARD):
                    print('// Check!')
                if COM==0:
                    sleep(0.5)
                else:
                    sleep(0.1)
                TURN*=-1
                TURNNUM+=1
                
                drawboxes(BOARD)
                if kicm(TURN,BOARD):
                    print('// Checkmate!')
                    #file.close()
                    TURN=0
                    return
                if kid(BOARD):
                    print('// It\'s a tie!')
                    #file.close()
                    TURN=0
                    return
                if TURN==COM:
                    OT=time()
                    print('// BEGIN')
                    PBS.append(deepcopy(BOARD[0:4]))
                    BOARD=deepcopy(whatTHEcom(TURN,BOARD,DIFF))
                    for i in range(len(BOARD[1+TURN])):
                        if BOARD[1+TURN][i] != PBS[-1][1+TURN][i]:
                            PM=[PBS[-1][1+TURN][i],BOARD[1+TURN][i]]
                    #file.write(BOARD[8][len(BOARD[8])-1])
                    """if TURN==-1:
                       # file.write('$\n')
                    else:
                        #file.write('  ')"""
                    if kic(TURN*-1,BOARD):
                        print('// Check!')
                    TURN*=-1
                    TURNNUM+=1
                    print('// END Checked',NUM,'nodes. Took',floor((time()- OT) * 100) / 100,'seconds.'\
                          ,(floor(((time()-OT)/NUM)*100000))/100,'ms per node. ES:',GG,BOARD[8][-1])
                    drawboxes(BOARD)
                    if kicm(TURN,BOARD):
                        print('// Checkmate!')
                        #file.close()
                        TURN=0
                        return
                    if kid(BOARD):
                        print('// It\'s a tie!')
                        #file.close()
                        TURN=0
                        return
                    PBS.append(BOARD)
                    
                    
            elif CS!=-1:
                if randint(0,5)==3:
                    print('// Nice try, bud!')
                else:
                    print('// Illegal move!')
            drawboxes(BOARD)

        
        
def pmoves(S1,B,gg3=True):
    ans=[]
    if S1 in B[0]:
        C=-1
    else:
        C=1
    P=B[2+C][B[1+C].index(S1)]
    if P==1:
        if not(S1-8*C in B[0] or S1-8*C in B[2]):
            ans.append(S1-8*C)
            if not(S1-16*C in B[0] or S1-16*C in B[2]) and S1//8==3.5+C*2.5:
                ans.append(S1-16*C)
        if (S1-7*C in B[1-C] or (B[7][0]==-1*C*((S1%8)+1*C)) and S1//8==3.5-(0.5*C)) and S1%8!=3.5+3.5*C:
            ans.append(S1-7*C)
        if (S1-9*C in B[1-C] or (B[7][0]==-1*C*((S1%8)-1*C)) and S1//8==3.5-(0.5*C)) and S1%8!=3.5-3.5*C:
            ans.append(S1-9*C)
    if P==2:
        if abs(S1%8-(S1-6)%8)==2 and abs(S1//8-(S1-6)//8)==1 and not(S1-6 in B[1+C]) and S1-6>=0:
            ans.append(S1-6)
        if abs(S1%8-(S1-10)%8)==2 and abs(S1//8-(S1-10)//8)==1 and not(S1-10 in B[1+C]) and S1-10>=0:
            ans.append(S1-10)
        if abs(S1%8-(S1+6)%8)==2 and abs(S1//8-(S1+6)//8)==1 and not(S1+6 in B[1+C]) and S1+6<64:
            ans.append(S1+6)
        if abs(S1%8-(S1+10)%8)==2 and abs(S1//8-(S1+10)//8)==1 and not(S1+10 in B[1+C]) and S1+10<64:
            ans.append(S1+10)
            
        if abs(S1%8-(S1+15)%8)==1 and abs(S1//8-(S1+15)//8)==2 and not(S1+15 in B[1+C]) and S1+15<64:
            ans.append(S1+15)
        if abs(S1%8-(S1+17)%8)==1 and abs(S1//8-(S1+17)//8)==2 and not(S1+17 in B[1+C]) and S1+17<64:
            ans.append(S1+17)
        if abs(S1%8-(S1-15)%8)==1 and abs(S1//8-(S1-15)//8)==2 and not(S1-15 in B[1+C]) and S1-15>=0:
            ans.append(S1-15)
        if abs(S1%8-(S1-17)%8)==1 and abs(S1//8-(S1-17)//8)==2 and not(S1-17 in B[1+C]) and S1-17>=0:
            ans.append(S1-17)
    if P==3 or P==5:
        i=S1-7
        while i>=0 and i<64:
            if abs((i%8)-(S1%8))!=abs((i//8)-(S1//8)) or i in B[1+C]:
                break
            if i in B[1-C]:
                ans.append(i)
                break
            ans.append(i)
            i-=7
        i=S1-9
        while i>=0 and i<64:
            if abs((i%8)-(S1%8))!=abs((i//8)-(S1//8)) or i in B[1+C]:
                break
            if i in B[1-C]:
                ans.append(i)
                break
            ans.append(i)
            i-=9
        i=S1+7
        while i>=0 and i<64:
            if abs((i%8)-(S1%8))!=abs((i//8)-(S1//8)) or i in B[1+C]:
                break
            if i in B[1-C]:
                ans.append(i)
                break
            ans.append(i)
            i+=7
        i=S1+9
        while i>=0 and i<64:
            if abs((i%8)-(S1%8))!=abs((i//8)-(S1//8)) or i in B[1+C]:
                break
            if i in B[1-C]:
                ans.append(i)
                break
            ans.append(i)
            i+=9
    if P==4 or P==5:
        i=S1-8
        while i>=0 and i<64:
            if i in B[1+C] or i%8!=S1%8:
                break
            if i in B[1-C]:
                ans.append(i)
                break
            ans.append(i)
            i-=8
        i=S1-1
        while i>=0 and i<64:
            if i in B[1+C] or i//8!=S1//8:
                break
            if i in B[1-C]:
                ans.append(i)
                break
            ans.append(i)
            i-=1
        i=S1+8
        while i>=0 and i<64:
            if i in B[1+C] or i%8!=S1%8:
                break
            if i in B[1-C]:
                ans.append(i)
                break
            ans.append(i)
            i+=8
        i=S1+1
        while i>=0 and i<64:
            if i in B[1+C] or i//8!=S1//8:
                break
            if i in B[1-C]:
                ans.append(i)
                break
            ans.append(i)
            i+=1
    if P==6:
        if not(S1+1 in B[1+C]) and S1%8!=7 and S1+1<=63:
            ans.append(S1+1)
        if not(S1-1 in B[1+C]) and S1%8!=0 and S1-1>=0:
            ans.append(S1-1)
        if not(S1+8 in B[1+C]) and S1//8!=7 and S1+8<=63:
            ans.append(S1+8)
        if not(S1-8 in B[1+C]) and S1//8!=0 and S1-8>=0:
            ans.append(S1-8)
        if not(S1+7 in B[1+C]) and abs(S1%8-(S1+7)%8)==abs(S1//8-(S1+7)//8) and S1+7<=63:
            ans.append(S1+7)
        if not(S1-7 in B[1+C]) and abs(S1%8-(S1-7)%8)==abs(S1//8-(S1-7)//8) and S1-7>=0:
            ans.append(S1-7)
        if not(S1+9 in B[1+C]) and abs(S1%8-(S1+9)%8)==abs(S1//8-(S1+9)//8) and S1+9<=63:
            ans.append(S1+9)
        if not(S1-9 in B[1+C]) and abs(S1%8-(S1-9)%8)==abs(S1//8-(S1-9)//8) and S1-9>=0:
            ans.append(S1-9)
        if gg3==True:
            if not(kic(C,B,False)):
                if B[round(5.5+C*0.5)][0]==0 and B[round(5.5+C*0.5)][1]==0 and not(S1-1 in B[0])\
                   and not(S1-1 in B[2]) and not(S1-2 in B[0]) and not(S1-2 in B[2]) and not(S1-3 in B[0]) and not(S1-3 in B[2]) and not(kic(C,chb(S1,S1-1,B))):
                    ans.append(S1-2)
                if B[round(5.5+C*0.5)][2]==0 and B[round(5.5+C*0.5)][1]==0 and not(S1+1 in B[0])\
                   and not(S1+1 in B[2]) and not(S1+2 in B[0]) and not(S1+2 in B[2]) and not(kic(C,chb(S1,S1+1,B))):
                    ans.append(S1+2)
        
    
    if gg3==True:
        for i in range(len(ans)-1,-1,-1):
            if kic(C,chb(S1,ans[i],B),False):
                ans.pop(i)
    return ans
def cmoves(C,B,gg2=True):
    ans=[]
    for i in B[1+C]:
        ans2=pmoves(i,B,gg2)
        for j in ans2:
            if B[2+C][B[1+C].index(i)]==1 and j//8==3.5-3.5*C:
                ans.append([i,j,5])
            else:
                ans.append([i,j,B[2+C][B[1+C].index(i)]])
    return ans
def d2al(L,F):
    NL=[]
    for i in range(len(L)):
        NL.append(eval(F.replace('\i',str(i)).replace('\v',str(L[i]))))
    return NL
# ------------------------------------------------

def OpeningBook(B):
    if B[9][0] == 0:
        if randint(1,4) >= 2:
            return [52, 36]
        else:
            return [51, 35]
    elif B[9][0] == 1:
        if 35 in B[3] and B[2][B[3].index(35)] == 1:
            return [11, 27]
        if not(45 in B[3] and B[2][B[3].index(45)] == 2):
            return [12, 28]
    elif B[9][0] == 3:
        if 36 in B[2] and 28 in B[0] and 45 in B[2]:
            return [1, 18]
        
    return [-1, -1]
def BoardVal(B):
    RET=0
    for i in range(len(B[0])):
        RET -= POINTVALS[B[1][i]]+lit[1][6-B[1][i]][63-B[0][i]]*(7*(1/(B[9][0] + 7)))
    for i in range(len(B[2])):
        RET += POINTVALS[B[3][i]]+lit[0][6-B[3][i]][B[2][i]]*(7*(1/(B[9][0] + 7)))
    """
    if B[1] == [6]:
        ATSPOTS = cmoves(1, B)
        for i in range(len(ATSPOTS)):
            ATSPOTS[i] = ATSPOTS[i][1]
        SPOTS = [B[0]]
        N = 0
        while len(SPOTS) != 0:
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if SPOTS[0] + x + y * 8 not in SPOTS and SPOTS[0] + x + y * 8 not in ATSPOTS and not(x == 0 and y == 0):
                        
                        SPOTS.append(SPOTS[0] + x + y * 8)
            SPOTS.pop(0)
            N += 1
            
        RET -= N * 0.5
    elif B[3] == [6]:
        ATSPOTS = cmoves(-1, B)
        for i in range(len(ATSPOTS)):
            ATSPOTS[i] = ATSPOTS[i][1]
        SPOTS = [B[0][0]]
        PSPOTS = []
        N = 0
        while len(SPOTS) != 0:
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if SPOTS[0] + x + y * 8 not in PSPOTS and SPOTS[0] + x + y * 8 not in ATSPOTS and not(x == 0 and y == 0):
                        SPOTS.append(SPOTS[0] + x + y * 8)
            PSPOTS.append(SPOTS[0])
            SPOTS.pop(0)
            N += 1
        RET += N * 0.5
    """
    if B[5][1] == 1:
        RET += (1 / ((B[9][0] // 2) + 5)) * 36
    if B[6][1] == 1:
        RET -= (1 / ((B[9][0] // 2) + 5)) * 36
    if 5 in B[1] and B[0][B[1].index(5)] != 3:
        RET += (1 / ((B[9][0] // 2) + 1)) * 4
    if 5 in B[3] and 63 - B[2][B[3].index(5)] != 4:
        RET -= (1 / ((B[9][0] // 2) + 1)) * 4
    """if kid(B):
        RET=0
    if kicm(1,B):
        RET=-1000
    if kicm(-1,B):
        RET=1000"""
    
    return floor(RET*100)/100
TURNNUM=0
def whowon(B):
    KIC = 0
    C = 1
    KP=B[1+C][B[2+C].index(6)]
    CMW=[]
    CMB=[]
    for i in B[2]:
        CMW.extend(pmoves(i,B))
    for i in B[0]:
        CMB.extend(pmoves(i,B))
    if len(CMW)==0 or len(CMB)==0:
        for i in B[1-C]:
            if KP in pmoves(i,B):
                KIC = 1
        C = -1
        for i in B[1-C]:
            if KP in pmoves(i,B):
                KIC = -1
        
        if KIC == 1:
            return -9999
        if KIC == -1:
            return 9999
        if KIC == 0:
            return 0
        
    WP=B[3].copy()
    BP=B[1].copy()
    WP.sort()
    BP.sort()  
    if ((WP==[6] or WP==[2,6]) and (BP==[6] or BP==[2,6])) or hasthree(B,PBS):
        return 0
    return 'nothin'
def srt(e):
    return BoardVal(e)
BRD=0
GG=0
def minmax(B,D,C,A,E,OD=True):
    #drawboxes(B)
    global NUM
    NUM+=1
    KIC=0
    """RET=whowon(B)
    if RET != 'nothin':
        return RET"""
    if (5 not in B[1] and 4 not in B[1] and 3 not in B[1] and 2 not in B[1] and len(cmoves(-1,B)) == 0)\
       or (5 not in B[3] and 4 not in B[3] and 3 not in B[3] and 2 not in B[3] and len(cmoves(1,B)) == 0)\
       or hasthree(B,PBS):
        return 0
    if D == 0:
        return BoardVal(B) * C
    global GG
    values=[]
    a=A
    b=E
    childrenm=cmoves(C,B)
    children=[]
    for i in range(len(childrenm)):
        children.append(chb(childrenm[i][0],childrenm[i][1],B,childrenm[i][2]))
    if C==1:
        children.sort(reverse=True,key=srt)
    else:
        children.sort(reverse=False,key=srt)
    for child in children:
        if child==children[0]:
            score = -(minmax(child, D - 1, -C, -b, -a, False))
        else:
            score = -(minmax(child, D - 1, -C, -a - 1, -a, False))
            if a < score < b:
                score = -(minmax(child, D - 1, -C, -b, -score, False))
        values.append(score)
        a = max(a, score)
        if a >= b:
            break
    if OD:
        RET=[]
        for i in range(len(values)):
            RET.append([values[i],children[i]])
        return RET
    else:
        return a
    
    
    """
    global NUM
    global BRD
    global GG
    NUM+=1
    a=A
    b=E
    if TURNNUM==1 and ordepth==D and COM==-1 and 36 in B[2]:
        return chb(12,28,B)
    elif TURNNUM==1 and ordepth==D and COM==-1 and 35 in B[2]:
        return chb(11,27,B)
    else:
        if D==0:
            if kicm(C,B):
                return inf*-C
            return B[4][0]
        else:
            value=(-inf)*C
            children=cmoves(C,B)
            for i in range(len(children)):
                children[i]=chb(children[i][0],children[i][1],B,children[i][2])
            #children.sort(reverse=(c==1),key=srt)
            value2=[]
            for j in children:
                drawboxes(j)
                if ordepth==D:
                    minnn=minmax(j,D-1,-C,a,b)
                    if value==minnn:
                        value2.append(j)
                    if value*C<minnn*C:
                        value=minnn
                        value2=[j]
                else:
                    value=max(value*C,(minmax(j,D-1,-C,a,b))*C)*C
                if C==1:
                    a=max(a,value)
                elif C==-1:
                    b=min(b,value)
                if a>=b:
                    break
                sleep(0.01)
            if ordepth==D:
                GG=value
                return value2.pop(randint(0,len(value2)-1))
            else:
                return value
    """

        
ordepth=0      
def sorBY(e):
  return e[3]
def whatTHEcom(C,B,L):
    global ordepth
    global NUM
    global GG
    NUM=0
    if L==0:
        NUM=1
        ans=cmoves(C,B)
        ans=ans.pop(randint(0,len(ans)-1))
        return chb(ans[0],ans[1],B,ans[2])
    if L>=1:
        ordepth=L
        if L >= 3:
            OB=[-1, -1]
            if B[9][0]<=3 and B[9][0]!=2:
                OB = OpeningBook(B)
            if OB[0] != -1:
                NUM=1
                return chb(OB[0], OB[1], B)
        if L>=3:
            minn=minmax(B,L,C,-999,999)
            minn2=minmax(B,2,C,-999,999)
            maxx=[-99999,[]]
            for i in range(len(minn)):
                if minn[i][0]+minn2[i][0] > maxx[0]:
                    maxx[0]=minn[i][0]*2+minn2[i][0]
                    maxx[1]=[]
                    maxx[1].append(minn[i][1])
                if abs((minn[i][0]+minn2[i][0]) - maxx[0]) <= VARIABILITY:
                    maxx[1].append(minn[i][1])
        else:
            minn=minmax(B,L,C,-999,999)
            maxx=[-99999,[]]
            for i in range(len(minn)):
                if minn[i][0] > maxx[0]:
                    maxx[0]=minn[i][0]
                    maxx[1]=[]
                    maxx[1].append(minn[i][1])
                if abs((minn[i][0]) - maxx[0]) <= VARIABILITY:
                    maxx[1].append(minn[i][1])
        GG = floor(maxx[0] * 100) / 100  
        return maxx[1].pop(randint(0, len(maxx[1])-1))

    print('It did not work very well.')
    return B

# ------------------------------------------------
"""def debug(event):
    global COM
    global DIFF
    global TURN
    global BOARD
    global TURNNUM
    print('// Got it.')
    if xy[0]>100:
        COM=1
    else:
        COM=-1
    if xy[2]<100:
        DIFF=2
    else:
        DIFF=3
    PBS.append(deepcopy(BOARD[0:4]))
    BOARD=deepcopy(whatTHEcom(TURN,BOARD,DIFF))
    if kic(TURN*-1,BOARD):
        print('// Check!')
    TURN*=-1
    TURNNUM+=1
    drawboxes(BOARD)
    if kicm(TURN,BOARD):
        print('// Checkmate!')
        TURN=0
    if kid(BOARD):
        print('// It\'s a tie!')
        TURN=0
    drawboxes(BOARD)"""
def debuger(event):
    global veto
    global veto2
    if xy[2] in BOARD[0]:
        veto=-BOARD[1][BOARD[0].index(xy[2])]
    elif xy[2] in BOARD[2]:
        veto=BOARD[3][BOARD[2].index(xy[2])]
    else:
        veto=0
    drawboxes(BOARD)
    print(xy[2])
BOXTEXT2=[]
for i in range(64):
    if i<8:
        SIDETEXTS.append(c.create_text(10, 25+(i*50), fill='white', text=temp[0][i%8]))
    elif i<16:
        SIDETEXTS.append(c.create_text(45+((i-8)*50), 410, fill='white', text=temp[1][i%8]))
    new_box = c.create_polygon(22+(i%8*50), 2+((i//8)*50), 22+(i%8*50), 52+((i//8)*50), 72+(i%8*50), 52+((i//8)*50), 72+(i%8*50), 2+((i//8)*50),\
                               fill=COLORS[(i%2*2-1)*(((i//8)%2)*2-1)==-1])
    new_text = c.create_text(47+(i%8*50), 24+((i//8)*50), fill='black', font=('Arial Unicode MS' ,25), text='SOMETHINGISWRONGHERE'[i%20])
    new_text2 = c.create_text(65+(i%8*50), 7+((i//8)*50), fill='black', font=('Arial Unicode MS' ,5), text='')
    BOXES.append(new_box)
    BOXTEXT.append(new_text)
    BOXTEXT2.append(new_text2)

#BACKIMG = PhotoImage(file='C:\Chess\gackground.png')
#BACK = c.create_image(260, 212, image=BACKIMG)
SCORETEXTW=c.create_text(448,30,text='White:0',font=('Arial Unicode MS' ,8),fill='black')
SCORETEXTB=c.create_text(448,60,text='Black:0',font=('Arial Unicode MS' ,8),fill='black')
SCORETEXTT=c.create_text(448,90,text='Turn #0',font=('Arial Unicode MS' ,8),fill='black')
if COM==2:
    opengames()
    for i in range(len(gamesn)):
        print('// ' + str(i + 1) + ' - ' + gamesn[i])
    WG = int(input('// Which game?')) - 1
    if WG < -1:
        WG = abs(WG + 1) - 1
        nfilet=filet[ : gamess[WG]] + filet[gamess[WG + 1] : ]
        file = open('C:\hutonotate.txt', 'w')
        file.write(nfilet)
        file.close()
        print('Successfuly deleted game #' + str(WG + 1) + ';', gamesn[WG + 1])
        TURN = 0
    else:
        PBS = [deepcopy(BOARD)]
        i = 0
        while i < len(games[WG]):
            if i < len(games[WG]) - 2 and len(games[WG][i + 2]) == 1:
                PBS.append(deepcopy(chb((temp[1].index(games[WG][i][0])) + 8 * (8 - int(games[WG][i][1])),\
                                    (temp[1].index(games[WG][i + 1][0])) + 8 * (8 - int(games[WG][i + 1][1])), PBS[-1], int(games[WG][i + 2]))))
                games[WG].pop(i + 2)
            else:
                PBS.append(deepcopy(chb((temp[1].index(games[WG][i][0])) + 8 * (8 - int(games[WG][i][1])),\
                                    (temp[1].index(games[WG][i + 1][0])) + 8 * (8 - int(games[WG][i + 1][1])), PBS[-1])))
            i += 2
        SPOT = 0
        S = 1
drawboxes(BOARD)
DDATA=c.create_text(200,100,font=('Arial Unicode MS',15),fill='red')
def chbt(B):
    CB=[[],[],[],[],[0],[0,0,0],[0,0,0],[0],[]]
    for i in range(len(B)):
        for j in range(len(B[i])):
            if B[i][j]!=0:
                CB[2+gd(B[i][j],'')].append(abs(B[i][j]))
                CB[1+gd(B[i][j],'')].append(i+j*8)
    return CB

    
if COM==1:
    sleep(2)
    PBS.append(deepcopy(BOARD[0:4]))
    BOARD=deepcopy(whatTHEcom(TURN,BOARD,DIFF))
    for i in range(len(BOARD[1+TURN])):
        if BOARD[1+TURN][i] != PBS[-1][1+TURN][i]:
            PM=[PBS[-1][1+TURN][i],BOARD[1+TURN][i]]
    #file.write(BOARD[8][len(BOARD[8])-1])
    """if TURN==-1:
        #file.write('$\n')
    else:
        #file.write('  ')"""
    if kic(TURN*-1,BOARD):
        print('// Check!')
    TURN*=-1
    drawboxes(BOARD)
    if kicm(TURN,BOARD):
        print('// Checkmate!')
        file.close()
        TURN=0
def closefle(event):
    global BOARD
    global SPOT
    global PM
    global TURN, S
    if COM == 2:
        if event.keysym == 'Right' and SPOT != len(PBS) - 1:
            SPOT += 1
            BOARD = deepcopy(PBS[SPOT])
            PM = [(temp[1].index(games[WG][SPOT * 2 - 2][0])) + 8 * (8 - int(games[WG][SPOT * 2 - 2][1])),\
                                (temp[1].index(games[WG][SPOT * 2 - 1][0])) + 8 * (8 - int(games[WG][SPOT * 2 - 1][1]))]
        if event.keysym == 'Left' and SPOT != 0:
            SPOT -= 1
            BOARD = deepcopy(PBS[SPOT])
            if SPOT != 0:
                PM = [(temp[1].index(games[WG][SPOT * 2 - 2][0])) + 8 * (8 - int(games[WG][SPOT * 2 - 2][1])),\
                                (temp[1].index(games[WG][SPOT * 2 - 1][0])) + 8 * (8 - int(games[WG][SPOT * 2 - 1][1]))]
            else:
                PM = [-1,-1]
        if event.keysym == 'f':
            S *= -1
        drawboxes(BOARD)
    else:
        
        if event.keysym=='b':
            #file.close()
            print('// Game ended.')
            TURN = 0
        if event.keysym=='p':
            BOARD=chbt(eval(input('board\n')))
        if event.keysym=='q':
            print(BOARD)
        drawboxes(BOARD)
c.bind_all('<Motion>', motion)
if COM != 2:
    c.bind_all('<Button-1>', press)
c.bind_all('<Button-2>', debuger)
c.bind_all('<KeyPress>', closefle)


