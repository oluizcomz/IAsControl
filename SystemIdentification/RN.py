from telnetlib import FORWARD_X
import this
from PalntaTeste import *
import random
from matplotlib import pyplot as plt
from math import e

class First_Order():
    alpha = 0.01
    weight = np.random.rand(2)
    bies =  random.uniform(-1,1)
    def __init__(self) -> None:
        pass
    def learn(self,Y_wanted,input):
        ##FORWARD
        Y0 = e**(input * self.weight[0])
        Y_cal = (Y0*self.weight[1])+ self.bies
        #BACKPROPAGCION
        delta_s = Y_wanted - Y_cal ##ERROR
        delta_o = delta_s * self.weight[1] ##ERROR HIDDEN
        #W1 = w1 + (ERROR *FAT'(out) * in *alpha)
        #W1 = w1 + (ERROR *1*Y0)
        self.weight[1] = self.weight[1] + (delta_s * self.alpha*Y0)
        #W0 = w0 + ERROR *FAT'(out) * in * alpha
        #W0 = w0 + ((ERROR_Hideen)*(E**Y0)*T*alpha)
        self.weight[0] = self.weight[0] + (delta_o*(e**Y0)*input*self.alpha)
        self.bies = delta_o 
        print(delta_s)

if __name__=="__main__":
    a = np.random.rand(2)
    print(a)
    RN = First_Order()

    for i in range(10):
        RN.learn(1,1)


Y_ruido = np.array([])
Y,T = model()
alpha = 0.01
weight = np.random.rand(1,2)
bies =  random.uniform(-1,1)


for y,t in zip(Y,T):
    Y_ruido = np.append(Y_ruido,[ y + random.uniform(-0.1,0.1)], axis=0)
    

legend = []

plt.figure()
plt.plot(T, Y_ruido, 'o', color='red',markersize=1)
legend.append("G_r(s)")
plt.plot(T,Y,color='blue', lw=2)
legend.append("G(s)")
plt.legend(legend)

plt.xlabel('Tempo (s)')
plt.ylabel('y')
plt.grid()
plt.show()