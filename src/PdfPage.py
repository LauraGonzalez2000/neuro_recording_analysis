import matplotlib.pylab as plt

class PdfPage:

    def __init__(self, 
                 structure_dict={},
                 debug=False):
        
        # figure in A0 format
        if debug:
            self.fig = plt.figure(figsize=(8.41/1.3,11.90/1.3))
        else:
            self.fig = plt.figure(figsize=(8.41,11.90))

        # default start and width for axes
        X0, DX = 0.12, 0.85 # x coords

        # dictionary of axes
        self.AXs = {}

        # build the axes one by one
        Y0, DY = 0.05, 0.2
        self.AXs['Notes'] = self.create_panel([X0, Y0, DX, DY], 'Notes')
        self.AXs['Notes'].axis('off')

        Y0 += 0.04
        DY = 0.04
        self.AXs['DAC0'] = self.create_panel([X0, Y0, DX, DY], 'DAC0')

        Y0 += 0.08
        DY = 0.04
        self.AXs['DAC1'] = self.create_panel([X0, Y0, DX, DY], 'DAC1')

        Y0 += DY+0.04
        DY = 0.10
        self.AXs['FullResp'] = self.create_panel([X0, Y0, DX, DY], 'Full Response')

        Y0 += DY+0.04
        DY = 0.25
        self.AXs['MemTest'] = self.create_panel([X0, Y0, 0.35, DY], 'Membrane Characteristics')

        DY = 0.06
        self.AXs['Id'] = self.create_panel([0.60, Y0, 0.37, DY])

        Y0 += 0.06
        self.AXs['Rm'] = self.create_panel([0.60, Y0, 0.37, DY])

        Y0 += 0.06
        self.AXs['Ra'] = self.create_panel([0.60, Y0, 0.37, DY])

        Y0 += 0.06
        self.AXs['Cm'] = self.create_panel([0.60, Y0, 0.37, DY])

        Y0 += 0.1
        DY = 0.3
        self.AXs['RespAnalyzed'] = self.create_panel([X0, Y0, DX, DY], 'Response')


    def create_panel(self, coords, title=None):
        """ 
        coords: (x0, y0, dx, dy)
                from left to right
                from top to bottom (unlike matplotlib)
        """
        coords[1] = 1-coords[1]-coords[3]
        ax = self.fig.add_axes(rect=coords)

        if title:
            ax.set_title(title, loc='left', pad=2, fontsize=10)
        return ax

    def save(self, filename):
        """ 
        """
        self.fig.savefig(filename)

        

if __name__=='__main__':
    
    page = PdfPage()
    page.save('nm03Jun2024c0_001_NMDA.pdf')
    plt.show()
