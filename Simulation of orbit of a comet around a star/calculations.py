from math import radians, cos, sin , log2, log
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np
class OrbitalCalculations:
    @staticmethod
    def planet_constants(planet_name:str):
        angular_momentum = {
            'earth': 2.7 * 10 **40,
            'mercury': 9.1 * 10 **38,
            'venus': 1.8 * 10 **40,
            'mars': 3.5 * 10 **39,
            'jupiter': 1.9 * 10 **43,
            'saturn': 7.8 * 10 **42,
            'uranus': 1.7 * 10 **42,
            'neptune': 2.5 * 10 **42,
            'pluto': 3.6 * 10 **38,
            'comet': 1.43* 10**21
            
        }
            
        initial_positions = {
            'mercury': ( -5.67576e+10,-2.73592e+10),
            'venus' : ( 4.28480e+10, 1.00073e+11 ),
            'earth': ( -1.43778e+11,  -4.00067e+10),
            'mars': (-1.14746e+11, -1.96294e+11 ),
            'jupiter': ( -5.66899e+11,  -5.77495e+11),
            'saturn': ( 8.20513e+10,  -1.50241e+12),
            'uranus': ( 2.62506e+12, 1.40273e+12),
            'neptune': (4.30300e+12,  -1.24223e+12),
            'pluto': ( 1.65554e+12, -4.73503e+12 ),
            'comet': (-1.996200094933726E+012,3.649577984151541E+012)
        }
        return [angular_momentum[planet_name], initial_positions[planet_name]]
    @staticmethod
    def solution_based_solver(planet_name:str):
        eccentricity = {
            'earth':0.017 ,
            'mercury': 0.206,
            'venus': 0.007,
            'mars': 0.093,
            'jupiter': 0.048,
            'saturn': 0.056,
            'uranus':0.047,
            'neptune': 0.009,
            'pluto': 0.25,
            'comet':0.97
            }
        r = []
        G = 6.67 * 10 ** (-11)
        M = 1.9 * 10 ** 30
        h = OrbitalCalculations.planet_constants(planet_name)[0]
        e = eccentricity[planet_name]
        for theta in range(0,361):
            r.append(h**2 /(G*M)*(1+e*cos(radians(theta))))
        x_y_vals = [[r*cos(radians(theta)), r*sin(radians(theta))]for r,theta in zip(r,range(360))]
        for val in x_y_vals:
            for ind in [index for index, item in enumerate(val) if item != 0]:
                val[ind] = val[ind]/ 10**22
        major_axis = max([val[0] for val in x_y_vals])
        minor_axis = max([val[1] for val in x_y_vals])
        return major_axis,minor_axis
    @staticmethod
    def rk4_twobody_integrator(planet_name:str):
        G = 6.67 * 10 ** (-11)
        M = 1.9 * 10 ** 30
        angular_momentum, initial_positions = OrbitalCalculations.planet_constants(planet_name)
        f = lambda u : G * M / angular_momentum**2 - u
        u = np.zeros(362, 'float')
        x,y = initial_positions
        u[0] = 1 / ( (x)**2 + (y)**2)**0.5
        du_d0 = np.zeros(362, 'float')
        d0 = 1
        for i in range(361):
            u[i+1] = u[i] + d0*du_d0[i]
            du_d0[i+1] = du_d0[i] + d0*f(u[i])
        r = np.reciprocal(u)
        x_y_vals = [[r*cos(radians(theta)), r*sin(radians(theta))] for r,theta in zip(r,range(360))]
        for val in x_y_vals:
            for ind in [index for index, item in enumerate(val) if item != 0]:
                val[ind] = val[ind]/ 10**11
        return [[val[0], val[1], 0] for val in x_y_vals]

def main():
    vals = OrbitalCalculations.solution_based_solver('comet')
if __name__=='__main__':
    main()
