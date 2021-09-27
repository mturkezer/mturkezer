import numpy as np


# TODO --- Terzaghi's 1D Consolidation Settlement Formulation

# inputs --> H, Cc, Sig_0, Sig_f
# output --> s (mm)
# TODO - Definition of the Classes
class NativeSoil():
    def __init__(self, soil_input):
        self.depth = soil_input['depth']
        self.elevation = (soil_input['top_elevation'],
                          soil_input['top_elevation'] - self.depth
                          )
        self.gamma_sat = soil_input['gamma_sat']
        self.gamma_dry = soil_input['gamma_dry']

    # Returns the vertical effective stress increase (at the bottom) due to the buoyant weight of the soil layer.
    def buoyant_weight(self, gwt_elv):
        gamma_water = 9.81                              # kN/m^3
        top_elv = self.elevation[0]
        bottom_elv = self.elevation[1]

        if gwt_elv >= top_elv:  # Fully saturated layer.
            buoy_w = (self.gamma_sat - gamma_water) * self.depth

        elif gwt_elv <= bottom_elv:
            buoy_w = self.gamma_dry * self.depth  # Completely dry layer.

        elif gwt_elv in np.linspace(top_elv, bottom_elv, 201):  # GWT in the middle. 5 cm interval
            buoy_w = self.gamma_dry * (top_elv - gwt_elv) + (self.gamma_sat-gamma_water) * (gwt_elv - bottom_elv)

        return buoy_w


class CompressibleSoil(NativeSoil):
    def __init__(self, soil_input):
        super().__init__(soil_input)
        self.Cc = soil_input['Cc']
        self.Cr = soil_input['Cr']
        self.e0 = soil_input['e0']
        self.OCR = soil_input['OCR']
        self.K = soil_input['K']
        self.Kr = soil_input['Kr']


class NonCompressibleSoil(NativeSoil):
    def __init__(self, soil_input):
        super().__init__(soil_input)


class Embankment():
    def __init__(self, soil_input):
        self.gamma_sat = soil_input['gamma_sat']
        self.gamma_dry = soil_input['gamma_dry']
        self.height = soil_input['height']
        self.base_width = soil_input['base_width']


class WickDrain():
    def __init__(self, drain_input):
        if drain_input['type'] == 'circular':
            self.diameter = drain_input['diameter']

        elif drain_input['type'] == 'strip':
            self.width = drain_input['width']
            self.thickness = drain_input['thickness']

        else:
            raise TypeError('Invalid Wick Drain Type!')

        self.spacing = drain_input['spacing']
        self.length = drain_input['length']
        # self.install_stage
        # self.smear_zone
        # self.pattern

def final_settlement(obj):
    h = obj.depth
    e0 = obj.e0
    cc = obj.Cc
    p0 = obj.ver_eff_stress(gwt_elv=-1)


# Sorts the given soil layering according to increasing depth. Returns in a sequenced order of soil layering.
def borehole(layers):
    return sorted(layers, key=lambda x: x.elevation[0], reverse= True)



def main():
    clay1 = {'gamma_sat': 19,
           'gamma_dry':18,
           'depth': 40,
           'Cc': 0.30,
           'Cr': 1.15,
           'e0': 1.15,
           'OCR': 1,
           'K': 0.0001,
           'Kr': 0.0005,
           'top_elevation': -7
             }

    sand1 = {'gamma_sat': 19,
           'gamma_dry':18,
           'depth': 5,
           'top_elevation': 0
             }

    sand2 = {'gamma_sat': 19,
           'gamma_dry':18,
           'depth': 2,
           'top_elevation': -5
             }


    preload_prop = {'gamma_sat': 19,
                    'height': 5,
                    'gamma_dry': 18,
                    'base_width': 200
                    }

    cl1 = CompressibleSoil(clay1)
    preload = Embankment(preload_prop)
    sm1 = NonCompressibleSoil(sand1)
    sm2 = NonCompressibleSoil(sand2)

    borehole1 = [cl1,
                 sm2,
                 sm1
                 ]

    borehole1 = borehole(borehole1)




    print(f"CLAY-1 depth: {cl1.depth}, Preload unit weight: {preload.gamma_sat}\n"
          f"SM-1 vertical effective stress increase: {sm1.buoyant_weight(gwt_elv=-1)}\n"
          f"SM-2 vertical effective stress increase: {sm2.buoyant_weight(gwt_elv=-1)}\n"
          f"Borehole from top to bottom: {borehole1}")


print(f"__name__ value: {__name__}")
if __name__ == '__main__':
    main()

# TODO --- Time Rate of Consolidation


# TODO --- Radial Consolidation and Preloading
