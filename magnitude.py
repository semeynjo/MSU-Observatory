import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class MagnitudeCalculation():

    def __init__(self):
        self.numC = float(input('Number of comparison stars (up to 3):'))
        if self.numC > 3 or self.numC < 1:
            raise ValueError('Number of comparison stars must be between 1 and 3')
        self.star_name = input('Star name:')
        self.filter = input('input the filter type (R, V, I, or B):')
        self.cname = input('input the first comp star name:')
        self.kname = input('input the second comp star name:')
        self.trans = 'NO'
        self.mtype = 'STD'
        self.group = 'na'
        self.chart = 'na'
        self.notes = 'na'


    def comp_stars(self):

        if self.numC == 1:
            self.C2mag = float(input('Magnitude of the first comparison star:'))
            self.C3mag = 'none'
        elif self.numC == 2:
            self.C2mag = float(input('Magnitude of the first comparison star:'))
            self.C3mag = float(input('Magnitude of the second comparison star:'))
        elif self.numC == 3:
            self.C2mag = float(input('Magnitude of the first comparison star:'))
            self.C3mag = float(input('Magnitude of the second comparison star:'))
            self.C4mag = float(input('Magnitude of the third comparison star:'))

    def read_file(self):

        filename = input('input the filename (csv):')

        data = pd.read_csv(filename)

        self.time = data['J.D.-2400000']
        self.jd = data['JD_UTC']
        self.airmass = data['AIRMASS']
        self.Tcounts = data['Source-Sky_T1']
        self.Terror = data['Source_Error_T1']
        self.C2counts = data['Source-Sky_C2']
        self.C2error = data['Source_Error_C2']
        if self.numC == 2:
            self.C3counts = data['Source-Sky_C3']
            self.C3error = data['Source_Error_C3']
        if self.numC == 3:
            self.C3counts = data['Source-Sky_C3']
            self.C3error = data['Source_Error_C3']
            self.C4counts = data['Source-Sky_C4']
            self.C4error = data['Source_Error_C4']

    def calc_mag(self):

        if self.numC == 1:
            Tmag2 = -2.5*np.log10(self.Tcounts/self.C2counts) + self.C2mag
            Terrmag2 = np.sqrt((2.5*self.Terror/(np.log(10.0)*self.Tcounts))**2 +
            ((2.5*self.C2error/(np.log(10.0)*self.C2counts))**2))
            print(Tmag2[0],Terrmag2[0])
            return Tmag2, Terrmag2

        elif self.numC == 2:
            Tmag2 = -2.5*np.log10(self.Tcounts/self.C2counts) + self.C2mag
            Terrmag2 = np.sqrt((2.5*self.Terror/(np.log(10.0)*self.Tcounts))**2 +
            ((2.5*self.C2error/(np.log(10.0)*self.C2counts))**2))
            print(Tmag2[0],Terrmag2[0])

            Tmag3 = -2.5*np.log10(self.Tcounts/self.C3counts) + self.C3mag
            Terrmag3 = np.sqrt((2.5*self.Terror/(np.log(10.0)*self.Tcounts))**2
            + ((2.5*self.C3error/(np.log(10.0)*self.C3counts))**2))
            print(Tmag3[0],Terrmag3[0])
            return Tmag2, Terrmag2, Tmag3, Terrmag3

        elif self.numC == 3:
            Tmag2 = -2.5*np.log10(self.Tcounts/self.C2counts) + self.C2mag
            Terrmag2 = np.sqrt((2.5*self.Terror/(np.log(10.0)*self.Tcounts))**2 +
            ((2.5*self.C2error/(np.log(10.0)*self.C2counts))**2))
            print(Tmag2[0],Terrmag2[0])

            Tmag3 = -2.5*np.log10(self.Tcounts/self.C3counts) + self.C3mag
            Terrmag3 = np.sqrt((2.5*self.Terror/(np.log(10.0)*self.Tcounts))**2
            + ((2.5*self.C3error/(np.log(10.0)*self.C3counts))**2))
            print(Tmag3[0],Terrmag3[0])

            Tmag4 = -2.5*np.log10(self.Tcounts/self.C4counts) + self.C4mag
            Terrmag4 = np.sqrt((2.5*self.Terror/(np.log(10.0)*self.Tcounts))**2
            + ((2.5*self.C4error/(np.log(10.0)*self.C4counts))**2))
            print(Tmag4[0],Terrmag4[0])
            return Tmag2, Terrmag2, Tmag3, Terrmag3, Tmag4, Terrmag4

def V_var(vvar, vcomp, bvar, bcomp, Vcomp):
    '''
    Calculates the color transformed values for V magnitude

    Parameters:
    vvar: variable star measured V magnitude
    vcomp: comparison star measured V magnitude
    TvBv, Tbv: color transforms
    bvar: variable star measured B magnitude
    bcomp: comparison star measured B magnitude
    Vcomp: published V magnitude of comparison star
    '''

    Tbv = 1.44000005722046
    Tvbv = -0.0579999983310699

    deltav = vvar - vcomp

    deltabv = (bvar-vvar)-(bcomp-vcomp)

    deltaBV = Tbv * deltabv

    return deltav + Tvbv * deltaBV + Vcomp
