"""
define classe Pd2dProc for 1d powder diffraction experiment
"""
__author__ = 'ikibalin'
__version__ = "2019_09_10"
import os
import numpy


from pycifstar import Global


class Pd2dProc(object):
    """
    This section contains the diffraction data set after processing
    and application of correction terms. 

    Example:

    _pd2d_proc_2theta_phi_intensity_up_net
    ;
    ;
    _pd2d_proc_2theta_phi_intensity_down_net
    ;
    ;
    _pd2d_proc_2theta_phi_intensity_up_total
    ;
    ;
    _pd2d_proc_2theta_phi_intensity_down_total
    ;
    ;
    _pd2d_proc_2theta_phi_intensity_bkg_calc
    ;
    ;
    _pd2d_proc_2theta_phi_intensity_up
    ;
    ;
    _pd2d_proc_2theta_phi_intensity_up_sigma
    ;
    ;
    _pd2d_proc_2theta_phi_intensity_down
    ;
    ;
    _pd2d_proc_2theta_phi_intensity_down_sigma
    ;
    ;
    """
    def __init__(self, ttheta=[], phi=[],
                up_net=[[]], down_net=[[]], up_total=[[]], down_total=[[]], bkg_calc=[[]], 
                up=[[]], down=[[]], up_sigma=[[]], down_sigma=[[]]):
        super(Pd2dProc, self).__init__()
        self.__pd2d_proc_2theta = None
        self.__pd2d_proc_phi = None
        self.__pd2d_proc_intensity_up_net = None
        self.__pd2d_proc_intensity_down_net = None
        self.__pd2d_proc_intensity_up_total = None
        self.__pd2d_proc_intensity_down_total = None
        self.__pd2d_proc_intensity_bkg_calc = None
        self.__pd2d_proc_intensity_up = None
        self.__pd2d_proc_intensity_up_sigma = None
        self.__pd2d_proc_intensity_down = None
        self.__pd2d_proc_intensity_down_sigma = None


        self.ttheta = ttheta
        self.phi = phi
        self.up_net = up_net
        self.down_net = down_net
        self.up_total = up_total
        self.down_total = down_total
        self.bkg_calc = bkg_calc
        self.up = up
        self.up_sigma = up_sigma
        self.down = down
        self.down_sigma = down_sigma

    @property
    def ttheta(self):
        return self.__pd2d_proc_2theta
    @ttheta.setter
    def ttheta(self, l_x):
        l_x_in = []
        for x in l_x:
            if isinstance(x, float):
                x_in = x
            else:
                x_in = float(x)
            l_x_in.append(x_in)
        np_x_in = numpy.array(l_x_in, dtype=float)
        self.__pd2d_proc_2theta = np_x_in


    @property
    def phi(self):
        return self.__pd2d_proc_phi
    @phi.setter
    def phi(self, l_x):
        l_x_in = []
        for x in l_x:
            if isinstance(x, float):
                x_in = x
            else:
                x_in = float(x)
            l_x_in.append(x_in)
        np_x_in = numpy.array(l_x_in, dtype=float)
        self.__pd2d_proc_phi = np_x_in


    @property
    def up_net(self):
        return self.__pd2d_proc_intensity_up_net
    @up_net.setter
    def up_net(self, ll_x):
        ll_x_in = []
        for l_x in ll_x:
            l_x_in = []
            for x in l_x:
                if (isinstance(x, float) | (x is None)):
                    x_in = x
                else:
                    x_in = float(x)
                l_x_in.append(x_in)
            ll_x_in.append(l_x_in)
        np_x_in = numpy.array(ll_x_in, dtype=float)
        self.__pd2d_proc_intensity_up_net = np_x_in


    @property
    def down_net(self):
        return self.__pd2d_proc_intensity_down_net
    @down_net.setter
    def down_net(self, ll_x):
        ll_x_in = []
        for l_x in ll_x:
            l_x_in = []
            for x in l_x:
                if (isinstance(x, float) | (x is None)):
                    x_in = x
                else:
                    x_in = float(x)
                l_x_in.append(x_in)
            ll_x_in.append(l_x_in)
        np_x_in = numpy.array(ll_x_in, dtype=float)
        self.__pd2d_proc_intensity_down_net = np_x_in


    @property
    def up_total(self):
        return self.__pd2d_proc_intensity_up_total
    @up_total.setter
    def up_total(self, ll_x):
        ll_x_in = []
        for l_x in ll_x:
            l_x_in = []
            for x in l_x:
                if (isinstance(x, float) | (x is None)):
                    x_in = x
                else:
                    x_in = float(x)
                l_x_in.append(x_in)
            ll_x_in.append(l_x_in)
        np_x_in = numpy.array(ll_x_in, dtype=float)
        self.__pd2d_proc_intensity_up_total = np_x_in


    @property
    def down_total(self):
        return self.__pd2d_proc_intensity_down_total
    @down_total.setter
    def down_total(self, ll_x):
        ll_x_in = []
        for l_x in ll_x:
            l_x_in = []
            for x in l_x:
                if (isinstance(x, float) | (x is None)):
                    x_in = x
                else:
                    x_in = float(x)
                l_x_in.append(x_in)
            ll_x_in.append(l_x_in)
        np_x_in = numpy.array(ll_x_in, dtype=float)
        self.__pd2d_proc_intensity_down_total = np_x_in


    @property
    def bkg_calc(self):
        return self.__pd2d_proc_intensity_bkg_calc
    @bkg_calc.setter
    def bkg_calc(self, ll_x):
        ll_x_in = []
        for l_x in ll_x:
            l_x_in = []
            for x in l_x:
                if (isinstance(x, float) | (x is None)):
                    x_in = x
                else:
                    x_in = float(x)
                l_x_in.append(x_in)
            ll_x_in.append(l_x_in)
        np_x_in = numpy.array(ll_x_in, dtype=float)
        self.__pd2d_proc_intensity_bkg_calc = np_x_in


    @property
    def up(self):
        return self.__pd2d_meas_intensity_up
    @up.setter
    def up(self, ll_x):
        ll_x_in = []
        for l_x in ll_x:
            l_x_in = []
            for x in l_x:
                if (isinstance(x, float) | (x is None)):
                    x_in = x
                else:
                    x_in = float(x)
                l_x_in.append(x_in)
            ll_x_in.append(l_x_in)
        np_x_in = numpy.array(ll_x_in, dtype=float)
        self.__pd2d_meas_intensity_up = np_x_in

    @property
    def up_sigma(self):
        return self.__pd2d_meas_intensity_up_sigma
    @up_sigma.setter
    def up_sigma(self, ll_x):
        ll_x_in = []
        for l_x in ll_x:
            l_x_in = []
            for x in l_x:
                if (isinstance(x, float) | (x is None)):
                    x_in = x
                else:
                    x_in = float(x)
                l_x_in.append(x_in)
            ll_x_in.append(l_x_in)
        np_x_in = numpy.array(ll_x_in, dtype=float)
        self.__pd2d_meas_intensity_up_sigma = np_x_in

    @property
    def down(self):
        return self.__pd2d_meas_intensity_down
    @down.setter
    def down(self, ll_x):
        ll_x_in = []
        for l_x in ll_x:
            l_x_in = []
            for x in l_x:
                if (isinstance(x, float) | (x is None)):
                    x_in = x
                else:
                    x_in = float(x)
                l_x_in.append(x_in)
            ll_x_in.append(l_x_in)
        np_x_in = numpy.array(ll_x_in, dtype=float)
        self.__pd2d_meas_intensity_down = np_x_in

    @property
    def down_sigma(self):
        return self.__pd2d_meas_intensity_down_sigma
    @down_sigma.setter
    def down_sigma(self, ll_x):
        ll_x_in = []
        for l_x in ll_x:
            l_x_in = []
            for x in l_x:
                if (isinstance(x, float) | (x is None)):
                    x_in = x
                else:
                    x_in = float(x)
                l_x_in.append(x_in)
            ll_x_in.append(l_x_in)
        np_x_in = numpy.array(ll_x_in, dtype=float)
        self.__pd2d_meas_intensity_down_sigma = np_x_in


            
    def __repr__(self):
        ls_out = ["Pd2dProc:"]
        ls_out.append("\n ttheta: min - {:}°, max - {:}°, points - {:}".format(self.ttheta.min(), self.ttheta.max(), self.ttheta.size))
        ls_out.append(" phi:    min - {:}°, max - {:}°, points - {:}".format(self.phi.min(), self.phi.max(), self.phi.size))
        ls_out.append(" phi: {:}".format(str(self.phi)))
        ls_out.append("\n up_total")
        ls_out.append(str(self.up_total.transpose()))
        ls_out.append("\n up")
        ls_out.append(str(self.up.transpose()))
        ls_out.append("\n down_total")
        ls_out.append(str(self.down_total.transpose()))
        ls_out.append("\n down")
        ls_out.append(str(self.down.transpose()))
        return "\n".join(ls_out)

    @property
    def to_cif(self):
        ls_out = []
        if self.is_defined:
            ls_out.append("_pd2d_proc_2theta_phi_intensity_up_net")
            ls_out.append(";")
            ls_out.append("{:12} ".format(len(self.phi)) + " ".join(["{:6.2f}      ".format(_) for _ in self.ttheta]))
            for phi, l_intensity in zip(self.phi, self.up_net.transpose()):
                ls_out.append("{:12.2f} ".format(phi) + " ".join(["{:12}".format(_) if _ is not numpy.nan else "        None" for _ in l_intensity]))
            ls_out.append(";")

            ls_out.append("_pd2d_proc_2theta_phi_intensity_down_net")
            ls_out.append(";")
            ls_out.append("{:12} ".format(len(self.phi)) + " ".join(["{:6.2f}      ".format(_) for _ in self.ttheta]))
            for phi, l_intensity in zip(self.phi, self.down_net.transpose()):
                ls_out.append("{:12.2f} ".format(phi) + " ".join(["{:12}".format(_) if _ is not numpy.nan else "        None" for _ in l_intensity]))
            ls_out.append(";")

            ls_out.append("_pd2d_proc_2theta_phi_intensity_up_total")
            ls_out.append(";")
            ls_out.append("{:12} ".format(len(self.phi)) + " ".join(["{:6.2f}      ".format(_) for _ in self.ttheta]))
            for phi, l_intensity in zip(self.phi, self.up_total.transpose()):
                ls_out.append("{:12.2f} ".format(phi) + " ".join(["{:12}".format(_) if _ is not numpy.nan else "        None" for _ in l_intensity]))
            ls_out.append(";")

            ls_out.append("_pd2d_proc_2theta_phi_intensity_down_total")
            ls_out.append(";")
            ls_out.append("{:12} ".format(len(self.phi)) + " ".join(["{:6.2f}      ".format(_) for _ in self.ttheta]))
            for phi, l_intensity in zip(self.phi, self.down_total.transpose()):
                ls_out.append("{:12.2f} ".format(phi) + " ".join(["{:12}".format(_) if _ is not numpy.nan else "        None" for _ in l_intensity]))
            ls_out.append(";")

            ls_out.append("_pd2d_proc_2theta_phi_intensity_bkg_calc")
            ls_out.append(";")
            ls_out.append("{:12} ".format(len(self.phi)) + " ".join(["{:6.2f}      ".format(_) for _ in self.ttheta]))
            for phi, l_intensity in zip(self.phi, self.bkg_calc.transpose()):
                ls_out.append("{:12.2f} ".format(phi) + " ".join(["{:12}".format(_) if _ is not numpy.nan else "        None" for _ in l_intensity]))
            ls_out.append(";")

            ls_out.append("_pd2d_proc_2theta_phi_intensity_up")
            ls_out.append(";")
            ls_out.append("{:12} ".format(len(self.phi)) + " ".join(["{:6.2f}      ".format(_) for _ in self.ttheta]))
            for phi, l_intensity in zip(self.phi, self.up.transpose()):
                ls_out.append("{:12.2f} ".format(phi) + " ".join(["{:12}".format(_) if _ is not numpy.nan else "        None" for _ in l_intensity]))
            ls_out.append(";")

            ls_out.append("_pd2d_proc_2theta_phi_intensity_up_sigma")
            ls_out.append(";")
            ls_out.append("{:12} ".format(len(self.phi)) + " ".join(["{:6.2f}      ".format(_) for _ in self.ttheta]))
            for phi, l_intensity in zip(self.phi, self.up_sigma.transpose()):
                ls_out.append("{:12.2f} ".format(phi) + " ".join(["{:12}".format(_) if _ is not numpy.nan else "        None" for _ in l_intensity]))
            ls_out.append(";")

            ls_out.append("_pd2d_proc_2theta_phi_intensity_down")
            ls_out.append(";")
            ls_out.append("{:12} ".format(len(self.phi)) + " ".join(["{:6.2f}      ".format(_) for _ in self.ttheta]))
            for phi, l_intensity in zip(self.phi, self.down.transpose()):
                ls_out.append("{:12.2f} ".format(phi) + " ".join(["{:12}".format(_) if _ is not numpy.nan else "        None" for _ in l_intensity]))
            ls_out.append(";")

            ls_out.append("_pd2d_proc_2theta_phi_intensity_down_sigma")
            ls_out.append(";")
            ls_out.append("{:12} ".format(len(self.phi)) + " ".join(["{:6.2f}      ".format(_) for _ in self.ttheta]))
            for phi, l_intensity in zip(self.phi, self.down_sigma.transpose()):
                ls_out.append("{:12.2f} ".format(phi) + " ".join(["{:12}".format(_) if _ is not numpy.nan else "        None" for _ in l_intensity]))
            ls_out.append(";")
        return "\n".join(ls_out)

    def from_cif(self, string: str):
        cif_global = Global()
        flag = cif_global.take_from_string(string)
        if not flag:
            return False
        flag = cif_global.is_prefix("_pd2d_proc_2theta_phi_intensity_up_net")
        if flag:
            cif_value = cif_global["_pd2d_proc_2theta_phi_intensity_up_net"]
            string = cif_value.value
            l_1 = string.strip().split("\n")
            l_ttheta = [float(_) for _ in l_1[0].strip().split()[1:]]
            l_phi, ll_intensity = [], []
            for line in l_1[1:]:
                l_1 = line.strip().split()
                l_phi.append(float(l_1[0]))
                ll_intensity.append([float(_) if _ != "None" else None for _ in l_1[1:]])
            ll_intensity = [[ll_intensity[_2][_1] for _2 in range(len(ll_intensity))] for _1 in range(len(ll_intensity[0]))]
            self.phi = l_phi
            self.ttheta = l_ttheta
            self.up_net = ll_intensity

        flag = cif_global.is_prefix("_pd2d_proc_2theta_phi_intensity_down_net")
        if flag:
            cif_value = cif_global["_pd2d_proc_2theta_phi_intensity_down_net"]
            string = cif_value.value
            l_1 = string.strip().split("\n")
            l_ttheta = [float(_) for _ in l_1[0].strip().split()[1:]]
            l_phi, ll_intensity = [], []
            for line in l_1[1:]:
                l_1 = line.strip().split()
                l_phi.append(float(l_1[0]))
                ll_intensity.append([float(_) if _ != "None" else None for _ in l_1[1:]])
            ll_intensity = [[ll_intensity[_2][_1] for _2 in range(len(ll_intensity))] for _1 in range(len(ll_intensity[0]))]
            self.phi = l_phi
            self.ttheta = l_ttheta
            self.down_net = ll_intensity

        flag = cif_global.is_prefix("_pd2d_proc_2theta_phi_intensity_up_total")
        if flag:
            cif_value = cif_global["_pd2d_proc_2theta_phi_intensity_up_total"]
            string = cif_value.value
            l_1 = string.strip().split("\n")
            l_ttheta = [float(_) for _ in l_1[0].strip().split()[1:]]
            l_phi, ll_intensity = [], []
            for line in l_1[1:]:
                l_1 = line.strip().split()
                l_phi.append(float(l_1[0]))
                ll_intensity.append([float(_) if _ != "None" else None for _ in l_1[1:]])
            ll_intensity = [[ll_intensity[_2][_1] for _2 in range(len(ll_intensity))] for _1 in range(len(ll_intensity[0]))]
            self.phi = l_phi
            self.ttheta = l_ttheta
            self.up_total = ll_intensity

        flag = cif_global.is_prefix("_pd2d_proc_2theta_phi_intensity_down_total")
        if flag:
            cif_value = cif_global["_pd2d_proc_2theta_phi_intensity_down_total"]
            string = cif_value.value
            l_1 = string.strip().split("\n")
            l_ttheta = [float(_) for _ in l_1[0].strip().split()[1:]]
            l_phi, ll_intensity = [], []
            for line in l_1[1:]:
                l_1 = line.strip().split()
                l_phi.append(float(l_1[0]))
                ll_intensity.append([float(_) if _ != "None" else None for _ in l_1[1:]])
            ll_intensity = [[ll_intensity[_2][_1] for _2 in range(len(ll_intensity))] for _1 in range(len(ll_intensity[0]))]
            self.phi = l_phi
            self.ttheta = l_ttheta
            self.down_total = ll_intensity


        flag = cif_global.is_prefix("_pd2d_proc_2theta_phi_intensity_bkg_calc")
        if flag:
            cif_value = cif_global["_pd2d_proc_2theta_phi_intensity_bkg_calc"]
            string = cif_value.value
            l_1 = string.strip().split("\n")
            l_ttheta = [float(_) for _ in l_1[0].strip().split()[1:]]
            l_phi, ll_intensity = [], []
            for line in l_1[1:]:
                l_1 = line.strip().split()
                l_phi.append(float(l_1[0]))
                ll_intensity.append([float(_) if _ != "None" else None for _ in l_1[1:]])
            ll_intensity = [[ll_intensity[_2][_1] for _2 in range(len(ll_intensity))] for _1 in range(len(ll_intensity[0]))]
            self.phi = l_phi
            self.ttheta = l_ttheta
            self.bkg_calc = ll_intensity

        flag = cif_global.is_prefix("_pd2d_proc_2theta_phi_intensity_up")
        if flag:
            cif_value = cif_global["_pd2d_proc_2theta_phi_intensity_up"]
            string = cif_value.value
            l_1 = string.strip().split("\n")
            l_ttheta = [float(_) for _ in l_1[0].strip().split()[1:]]
            l_phi, ll_intensity = [], []
            for line in l_1[1:]:
                l_1 = line.strip().split()
                l_phi.append(float(l_1[0]))
                ll_intensity.append([float(_) if _ != "None" else None for _ in l_1[1:]])
            ll_intensity = [[ll_intensity[_2][_1] for _2 in range(len(ll_intensity))] for _1 in range(len(ll_intensity[0]))]
            self.phi = l_phi
            self.ttheta = l_ttheta
            self.up = ll_intensity

        flag = cif_global.is_prefix("_pd2d_proc_2theta_phi_intensity_up_sigma")
        if flag:
            cif_value = cif_global["_pd2d_proc_2theta_phi_intensity_up_sigma"]
            string = cif_value.value
            l_1 = string.strip().split("\n")
            l_ttheta = [float(_) for _ in l_1[0].strip().split()[1:]]
            l_phi, ll_intensity = [], []
            for line in l_1[1:]:
                l_1 = line.strip().split()
                l_phi.append(float(l_1[0]))
                ll_intensity.append([float(_) if _ != "None" else None for _ in l_1[1:]])
            ll_intensity = [[ll_intensity[_2][_1] for _2 in range(len(ll_intensity))] for _1 in range(len(ll_intensity[0]))]
            self.phi = l_phi
            self.ttheta = l_ttheta
            self.up_sigma = ll_intensity

        flag = cif_global.is_prefix("_pd2d_proc_2theta_phi_intensity_down")
        if flag:
            cif_value = cif_global["_pd2d_proc_2theta_phi_intensity_down"]
            string = cif_value.value
            l_1 = string.strip().split("\n")
            l_ttheta = [float(_) for _ in l_1[0].strip().split()[1:]]
            l_phi, ll_intensity = [], []
            for line in l_1[1:]:
                l_1 = line.strip().split()
                l_phi.append(float(l_1[0]))
                ll_intensity.append([float(_) if _ != "None" else None for _ in l_1[1:]])
            ll_intensity = [[ll_intensity[_2][_1] for _2 in range(len(ll_intensity))] for _1 in range(len(ll_intensity[0]))]
            self.phi = l_phi
            self.ttheta = l_ttheta
            self.down = ll_intensity

        flag = cif_global.is_prefix("_pd2d_proc_2theta_phi_intensity_down_sigma")
        if flag:
            cif_value = cif_global["_pd2d_proc_2theta_phi_intensity_down_sigma"]
            string = cif_value.value
            l_1 = string.strip().split("\n")
            l_ttheta = [float(_) for _ in l_1[0].strip().split()[1:]]
            l_phi, ll_intensity = [], []
            for line in l_1[1:]:
                l_1 = line.strip().split()
                l_phi.append(float(l_1[0]))
                ll_intensity.append([float(_) if _ != "None" else None for _ in l_1[1:]])
            ll_intensity = [[ll_intensity[_2][_1] for _2 in range(len(ll_intensity))] for _1 in range(len(ll_intensity[0]))]
            self.phi = l_phi
            self.ttheta = l_ttheta
            self.down_sigma = ll_intensity
        return True

    @property
    def is_defined(self):
        cond = all([self.ttheta is not None, self.phi is not None, 
                    self.up_net is not None, self.down_net is not None, self.up_total is not None, self.down_total is not None,
                    self.bkg_calc is not None,
                    self.up is not None, self.up_sigma is not None, self.down is not None, self.down_sigma is not None])
        return cond

    @property
    def is_variable(self):
        return False
    
    def get_variables(self):
        return []

    def _show_message(self, s_out: str):
        print("***  Error ***")
        print(s_out)
