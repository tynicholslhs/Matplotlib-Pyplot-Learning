import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import numpy as np
import math


def graph_parabola(a, b, c, xbounds = (0, 10), ybounds =(0, 10)):
    """
    graphs a parabola from a quadratic equation using a numpy array
    xbounds and ybounds are tuples of (min, max) format
    a, b, and c are the coefficients of the quadratic
    """
    
    #create an array of x-values
    x = np.arange(xbounds[0], xbounds[1], 0.1)
    
    #create y to be the function of x based on a, b, and c
    y = a * x**2 + b * x + c
    
    #plot the points
    plt.plot(x, y)
    
    #set the bounds of the display
    plt.axis([xbounds[0], xbounds[1], ybounds[0], ybounds[1]])
    
    #display the graph
    plt.show
    
def graph_line(m, b, xbounds = (0, 10), ybounds = (0, 10)):
    """
    graphs a line in slope-intercept form
    m is the slope, b is the y-intercept, xbounds and ybounds are tuples of the form (min, max)
    """
    
    #create an array of x-values
    x = np.arange(xbounds[0], xbounds[1], 0.1)
    
    #create y to be the function of x based upon m and b
    y = m * x + b
    
    #plot the points 
    plt.plot(x, y)
    
    #set the bounds of the display
    plt.axis([xbounds[0], xbounds[1], ybounds[0], ybounds[1]])
    
    #show the graph
    plt.show
    
def graph_ellipse(focus1 = (0, 0), focus2 = (0, 0), eccentricity = 0.5, xbounds = (0, 10), ybounds = (0, 10)):
    """
    graph an ellipse from the locations of the two foci and the eccentricity, which must be between 0 and 1
    xbounds and ybounds are tuples of the form (min, max)
    """
    
    #create a figure
    plt.figure()
    
    #get the axes
    ax = plt.gca()
    
    #compute rise of the line connecting the foci
    rise = float(focus1[1] - focus2[1])
    
    #compute the run of the line connecting the foci
    run = float(focus1[0] - focus2[0])
    
    #compute the distance between the foci
    foci_distance = math.sqrt((run)**2 + (rise)**2)
    
    #set the length of the major axis using the distance and eccentricity formulae
    majaxis = foci_distance/eccentricity
    
    #set the length of the minor axis using the major axis and the 
    minaxis = math.sqrt(majaxis**2 - foci_distance**2)
    
    #if the ellipse is not vertically oriented along its major axis
    if run != 0:
        
        #compute the angle of the ellipse in radians using the slope formula and arctangent
        ellipse_angle = math.degrees(math.atan(rise/run))
        
    #if the run is 0, i.e. if the ellipse is vertical
    else:
        
        #set the ellipse angle to be 90 degrees
        ellipse_angle = 90
    
    #create a new ellipse object with the given properties, setting the fill to be false
    ellipse = Ellipse(xy = (0, 0), width = majaxis, height = minaxis, angle = ellipse_angle, fill = False)
    
    #set the bounds of the graph
    ax.set_xlim(xbounds[0], xbounds[1])
    ax.set_ylim(ybounds[0], ybounds[1])
    
    #add the ellipse to the graph
    ax.add_patch(ellipse)