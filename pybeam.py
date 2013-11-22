'''
D. Melgar 11/2013

Some random tools for looking at multibeam diagnostics and data
'''



def bistanalysis():
    import numpy as np
    import glob,re
    
    #Wheres the data
    path='/Users/dmelgarm/Documents/Cruises/RR1319/bist/'
    #List allt ests
    bistlist=glob.glob(path+'*.bist')
    #Initalize
    chnoise1=np.zeros((len(bistlist),32)) #Channel noise board 1
    chnoise2=np.zeros((len(bistlist),32)) #Channel noise board 2
    for i in range(len(bistlist)):
        #Read BIST
        f=open(bistlist[i])
        while True:
            line=f.readline()
            if not line: break #EOF
            if 'RX NOISE LEVEL' in line:  #Found board noise level
                print bistlist[i]
                f.readline();f.readline();f.readline()
                for k in range(0,10):
                    line=f.readline()
                    m=re.match(" (\d*):        (\d*.\d*)       (\d*.\d*)",line)
                    chn=m.groups()
                    chnoise1[i,k]=chn[1]
                    chnoise2[i,k]=chn[2]
                for k in range(10,32):
                    line=f.readline()
                    m=re.match("(\d*):        (\d*.\d*)       (\d*.\d*)",line)             
                    chn=m.groups()
                    chnoise1[i,k]=chn[1]
                    chnoise2[i,k]=chn[2]