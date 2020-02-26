# This function is design for the user to chose the line type to direct the SWG blocks in a waveguide  
"""
Created on Thu Feb 20 15:49:24 2020

@author: edison.luan
"""
class curveclass:
    
    import numpy as np
    import math
    
    def __init__(self,resolution=0.01):
        self.resolution = resolution 
    
    def curve_func(self, eqn_key, params): # eqn_key is the number of function-type, params are the input parameters
        switcher={
                'Line': "2,%s*%s", ## y = a*x: first input = a, second input = x
                'Circle': "2,math.sqrt(%s**2-%s**2)", ## y^2=r^2-x^2: first input = radius, second input = x
                'Sigmoid': "3,%s/(1+math.exp(-%s*%s))" ## y = a/(1+e^(-b*x)): first input = a, second input = b, third input = x
                }
        self.nparams, self.eqn = switcher[eqn_key].split(',')
        self.nparams = int(self.nparams)
        
        if(len(params)== self.nparams):
            self.ans = eval(self.eqn%tuple(params))
            return(self.ans)
        else:
            print('Incorrect number of variables, %d required'%(self.nparams))
    
    
    def step_func(self, xo, xn, pitch, eqn_key, params):
        

        xarray = list(np.arange(xo,xn,self.resolution)) # get all x points from xo to xn with default resolution
        yarray=[]
        for i in range(0,len(xarray)):
            params.append(xarray[i]) # add x value into the params list
            yarray.append(self.curve_func(eqn_key,params)) #run the curve_func to calculate y value
            del params[int((len(params)-1))] # remove the added x value in order to add next x value
            
        #x_new=[xo] # add the first x coordinate into the new x_array
        ii = 0
        while ii < (len(xarray)-1):
            dis = math.sqrt((xarray[ii+1]-xarray[ii])**2+(yarray[ii+1]-yarray[ii])**2) # calculate the distance between two adjacent points
            if dis >= pitch:
                #x_new.append(xarray[ii+1]) # put the point into new x_array
                ii=ii+1 # add i to i+1
            else:
                del xarray[ii+1]
                del yarray[ii+1]
                
        # extract the theta information for each point           
        theta = []
        for j in range(0,(len(xarray)-1)):
            theta.append(math.degrees(math.atan((yarray[j+1]-yarray[j])/(xarray[j+1]-xarray[j]))))        
         
        return xarray, yarray, theta
#%% Import (xo, xn, pitch, curve_func) to extract [xc, yc] and theta information for SWG blocks  
import numpy as np
import math
enxiao=curveclass()
   


