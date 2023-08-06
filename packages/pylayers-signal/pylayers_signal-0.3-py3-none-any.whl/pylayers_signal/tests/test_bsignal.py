from pylayers_signal.bsignal import *

tb1=TBsignal()
N = 1000
M = 50
fGHz = np.linspace(3,5,N)
data = np.random.rand(M,N)+1j*np.random.rand(M,N)
fu1=FUsignal(x=fGHz,y=data)
