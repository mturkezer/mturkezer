import numpy as np


# TODO --- Terzaghi's 1D Consolidation Settlement Formulation

# inputs --> H, Cc, Sig_0, Sig_f
# output --> s (mm)

class NativeSoil():
    def __init__(self, soil_input):
        self.elevation = (soil_input['top_elevation'],
                          soil_input['top_elevation'] - self.depth
                          )
        self.depth = soil_input['depth']
        self.gamma_sat = soil_input['gamma_sat']
        self.gamma_dry = soil_input['gamma_dry']

    def vertical_stress(self, gwt_elv):
        top_elv = self.elevation[0]
        bottom_elv = self.elevation[1]

        if gwt_elv >= top_elv:  # Fully saturated layer.
            ver_str = self.gamma_sat * self.depth

        elif gwt_elv <= bottom_elv:
            ver_str = self.gamma_dry * self.depth  # Completely dry layer.

        elif gwt_elv in np.linspace(top_elv, bottom_elv, 201):  # GWT in the middle. 5 cm interval
            ver_str = self.gamma_dry * (top_elv - gwt_elv) + self.gamma_sat * (gwt_elv - bottom_elv)

        return ver_str


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











def vertical_stress():









def main():
    clay_1_prop = {'gamma_sat': 19,
                   'depth': 40,
                   'Cc': 0.30,
                   'Cr': 1.15,
                   'e0': 1.15,
                   'OCR': 1,
                   'K': 0.0001,
                   'Kr': 0.0005,
                   'top_elevation': 0
                   }

    preload_prop = {'gamma_sat': 19,
                    'height': 5,
                    'gamma_dry': 18,
                    'base_width': 200
                    }

    cl1 = CompressibleSoil(clay_1_prop)
    preload = Embankment(preload_prop)

    print(f"CLAY-1 height: {cl1.height}, Preload unit weight: {preload.gamma_sat}")






print(f"__name__ value: {__name__}")
if __name__ == '__main__':
    main()

#
# H = 5
# gamma_soil = 19
# gamma_fill = 20
# height_fill = 10
# Cc = 0.30
# p_0 = gamma * (H/2)
# pload = gamma_fill * height_fill


# TODO --- Time Rate of Consolidation


# TODO --- Radial Consolidation and Preloading
