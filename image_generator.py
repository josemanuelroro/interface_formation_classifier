import numpy as np
import matplotlib.pylab as plt
import os as os
from threading import Thread
import cv2

def altura(A,L):
    suma=0
    for i in range(1,L-1):
        suma=suma+np.sum(A[i,:])
    suma=suma/(L-2)
    return 1*suma

def deposicion(p):
    
    L=50
    T=50
    suelo=np.zeros([L,T])
    factor=0
    tiempo=[]
    alt=[]
    while factor<1000:
        j=np.random.randint(1,L-1)
        for i in range(1,T-1):
            if (i==T-2):
                suelo[T-1,j]=1
#Comment or uncomment to generate image from the different processes            

            #BALLISTIC DEPOSITION NNN
            if(suelo[i+1,j] or suelo[i-1,j] or suelo[i,j+1] or suelo[i,j-1] or suelo[i-1,j-1] or suelo[i+1,j-1])==1:
                suelo[i,j]=1
                text="class_NNN"
                break            
            # BALLISTIC DEPOSITION
            # if(suelo[i+1,j] or suelo[i-1,j] or suelo[i,j+1] or suelo[i,j-1])==1:
                # suelo[i,j]=1
                # text="class_ballistic_deposition"
                # break
                
            # RANDOM DEPOSITION
            # if (suelo[i+1,j]==1):
                # suelo[i,j]=1
                # text="class_random"
                # break

        tiempo.append(factor)
        alt.append(altura(suelo,L))
        factor=factor+1

    if not os.path.exists(f"{text}"):
        os.makedirs(f"{text}")
    cv2.imwrite(f"{text}/{text}{p}.png",255*suelo)
    return suelo

#200 images will be generated
image_number=200
for i in range(image_number):
    plt.figure(figsize=(5,5))
    t=Thread(target=deposicion,args=[i])
    t.start()
    t.join()
    plt.close()
    


    
    