class PSResult:
    """ Simple class holding results from power spectrum/2D FFT computation"""

    def __init__(self):
        self.spectra = None
        self.spec_name_list = None
        self.lb = None
        self.ps = None
        self.cov = None

    def store(self, spectra, spec_name_list, lb, ps, cov):
        self.spectra = spectra
        self.spec_name_list = spec_name_list
        self.lb = lb
        self.ps = ps
        self.cov = cov


class PSConfig:
    """ Simple class holding the configuration of the computation"""

    def __init__(self):
        self.lmax = None
        self.method = None
        self.error_method = None
        self.bin_size = None
        self.compute_T_only = None
