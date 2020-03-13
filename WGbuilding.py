# This function is design for the user to chose the line type to direct the SWG blocks in a waveguide  
"""
Created on Thu Feb 20 15:49:24 2020

@author: edison.luan
"""
import numpy as np
import math

class curveclass:
    
    def __init__(self,resolution=0.001):
        self.resolution = resolution 
    
    def curve_func(self, eqn_key, params): # eqn_key is the number of function-type, params are the input parameters
        switcher={
                'Line': "2,%s*%s", ## y = a*x: first input = a, second input = x
                'Circle': "2,math.sqrt(%s**2-(%s)**2)", ## y^2=r^2-x^2: first input = radius, second input = x
                'Sigmoid': "3,%s/(1+math.exp(-%s*%s))", ## y = a/(1+e^(-b*x)): first input = a, second input = b, third input = x
                'Lorentzian': "3,%s/(1+%s*(%s)**2)" ## y = a/(1+b*x^2): first input = a, second input = b, third input = x
                }
        self.nparams, self.eqn = switcher[eqn_key].split(',')
        self.nparams = int(self.nparams)
        
        if(len(params)== self.nparams):
            self.ans = eval(self.eqn%tuple(params))
            return(self.ans)
        else:
            print('Incorrect number of variables, %d required'%(self.nparams))
    
    
    def step_func(self, xo, xn, pitch, width, eqn_key, params):
        

        xarray = list(np.arange(xo,xn+pitch,self.resolution)) # get all x points from xo to (xn + 1*pitch) with default resolution, the last point will be deleted later
        #xhigh = list(np.arange(xo,xn+pitch,self.resolution))
        xhigh = list(np.arange(xo,xn,self.resolution))
        
        yarray=[]
        for i in range(0,len(xarray)):
            params.append(xarray[i]) # add x value into the params list
            yarray.append(self.curve_func(eqn_key,params)) #run the curve_func to calculate y value
            del params[int((len(params)-1))] # remove the added x value in order to add next x value    
        yhigh = []           
        for i in range(0,len(xhigh)):
            params.append(xhigh[i]) # add x value into the params list
            yhigh.append(self.curve_func(eqn_key,params)) #run the curve_func to calculate y value
            del params[int((len(params)-1))] # remove the added x value in order to add next x value

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
        thigh = []
        for j in range(0,(len(xhigh)-1)):
            thigh.append(math.atan((yhigh[j+1]-yhigh[j])/(xhigh[j+1]-xhigh[j])))
        
        del xarray[-1] # remove the last point from x, y arrays, to make a constant index of x, y and angle arrays
        del yarray[-1]
        del xhigh[-1]
        del yhigh[-1]
        
        xcore = []
        ycore = []
        for ii in range(0,len(xhigh)):
            xcore.append(xhigh[ii]-math.sin(thigh[ii])*(width/2))
            ycore.append(yhigh[ii]+math.cos(thigh[ii])*(width/2))
            #xcore.append(xhigh[ii])
            #ycore.append(yhigh[ii]+w/2)
            
        for ii in range(1,len(xhigh)-1):
            xcore.append(xhigh[-ii]+math.sin(thigh[-ii])*(width/2))
            ycore.append(yhigh[-ii]-math.cos(thigh[-ii])*(width/2))       
            #xcore.append(xhigh[-ii])
            #ycore.append(yhigh[-ii]-w/2)
        
        return xarray, yarray, theta, xcore, ycore
