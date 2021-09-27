import numpy


# TODO --- Terzaghi's 1D Consolidation Settlement Formulation

# inputs --> H, Cc, Sig_0, Sig_f
# output --> s (mm)

soil_1 = {'gamma_sat': 19,
             'height': 40,
             'Cc': 0.30,
             'Cr': 1.15,
             'e0': 1.15,
             'OCR': 1,
             'K': 0.0001,
             'Kr': 0.0005
}


class CompressibleSoil():
    def __init__(self, soil_input):
        self.gamma_sat = soil_input['gamma_sat']
        self.height = soil_input['height']
        self.Cc = soil_input['Cc']
        self.Cr = soil_input['Cr']
        self.e0 = soil_input['e0']
        self.OCR = soil_input['OCR']
        self.K = soil_input['K']
        self.Kr = soil_input['Kr']


class NonCompressibleSoil():
    def __init__(self, soil_input):
        self.gamma_sat = soil_input['gamma_sat']
        self.gamma_dry = soil_input['gamma_dry']


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
        







H = 5
gamma_soil = 19
gamma_fill = 20
height_fill = 10
Cc = 0.30
p_0 = gamma * (H/2)
pload = gamma_fill * height_fill


# TODO --- Time Rate of Consolidation







# TODO --- Radial Consolidation and Preloading





