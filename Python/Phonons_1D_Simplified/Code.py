import numpy as np
import matplotlib.pyplot as plt
import scipy

'''
The goal of this code is to simulate Phonon wave propogation on a mono-atomic lattice only including the quadratic term for the potential
  
The code will take:
  an initial profile/ disturbance
  length of time to simulate
  time step?

The code output a collection of things:
  The time series of the individual atomic displacements from the phonon movement
  Parameters/Fourier Composition of the Phonon Waves
  A video of the phonon wave(s) propogating around
'''

a = 1 #Lattice Constant
L = 10 #Length of the cell we are interested in

#########
#Simulated Inputs
#This will be replaced with code to inserting compands in the begining, or probably an entire new script
########
N = L//a
Integers = np.arange(0, N)
dx0 = np.exp(- (Integers - N//2)**2/10)


#######
#Constructing Lattice
######
#Sanity Check
print('Is $L$ divisable by $a$: ', 0== L % a) 
Equilibrium_Lattice = np.linspace(0, L, L//a)


########
#Potential Terms
#######
kappa_2 = 1 #This is the first order quaderatic term, lowest order necessary for the simulation
kappa_3 = 0 #This will be added in the future code, but for now


######
#Constructing the Basis Matrix
######

#Old Construction
def basis_vector(a,N,p):
  ints = np.arange(1,N)
  term = lambda a, N, p: 1j * (2*np.pi/a) * (ints/N) * p
  basis_p = np.exp( term(a,N,p) ) 
  return(basis_p)

#New Construction
p = (0,N) #Note that p can also be though of as the set of n

term = 1j * (2*np.pi/a) * 1/N * np.outer(p,p)
basis_matrix = np.exp(term) #Non-normalized matrix with orthogonal vectors, Ellen informs me this is not an orthogonal matrix though :-((((((
Coefficients = np.matmul(basis_matrix, dx0)


#########
# Setting Initial Distribution and finding parameters
#########


########
# Evolving the system forward
########

#Next state = forward step of old state, eg RK4 or some shiz, maybe 


#######
#Save all of the location data and Animate the Simulation
#######

