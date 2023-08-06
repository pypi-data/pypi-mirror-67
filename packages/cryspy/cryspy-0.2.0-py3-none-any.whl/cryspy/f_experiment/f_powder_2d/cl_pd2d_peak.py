"""
define class Pd2dPeak
"""
__author__ = 'ikibalin'
__version__ = "2019_09_10"
import os
import numpy


from pycifstar import Global


class Pd2dPeak(object):
    """
    This section contains peak information extracted from the
    measured or, if present, the processed diffractogram. 

    Example:

    loop_
    _pd2d_peak_index_h
    _pd2d_peak_index_k
    _pd2d_peak_index_l
    _pd2d_peak_index_mult
    _pd2d_peak_2theta
    _pd2d_peak_f_nucl_sq
    _pd2d_peak_f_m_p_sin_sq
    _pd2d_peak_f_m_p_cos_sq
    _pd2d_peak_cross_sin
    _pd2d_peak_width_2theta
    """
    def __init__(self, h=[], k=[], l=[], mult=[], ttheta=[], f_nucl_sq=[], f_m_p_sin_sq=[], f_m_p_cos_sq=[], cross_sin=[], width_2theta=[]):
        super(Pd2dPeak, self).__init__()
        self.__pd2d_peak_index_h = None
        self.__pd2d_peak_index_k = None
        self.__pd2d_peak_index_l = None
        self.__pd2d_peak_index_mult = None
        self.__pd2d_peak_2theta = None
        self.__pd2d_peak_f_nucl_sq = None
        self.__pd2d_peak_f_m_p_sin_sq = None
        self.__pd2d_peak_f_m_p_cos_sq = None
        self.__pd2d_peak_cross_sin = None
        self.__pd2d_peak_width_2theta = None

        self.h = h
        self.k = k
        self.l = l
        self.mult = mult
        self.ttheta = ttheta
        self.f_nucl_sq = f_nucl_sq
        self.f_m_p_sin_sq = f_m_p_sin_sq
        self.f_m_p_cos_sq = f_m_p_cos_sq
        self.cross_sin = cross_sin
        self.width_2theta = width_2theta

    @property
    def h(self):
        return self.__pd2d_peak_index_h
    @h.setter
    def h(self, l_x):
        l_x_in = []
        for x in l_x:
            if isinstance(x, float):
                x_in = x
            else:
                x_in = int(round(x))
            l_x_in.append(x_in)
        np_x_in = numpy.array(l_x_in, dtype=int)
        self.__pd2d_peak_index_h = np_x_in

    @property
    def k(self):
        return self.__pd2d_peak_index_k
    @k.setter
    def k(self, l_x):
        l_x_in = []
        for x in l_x:
            if isinstance(x, float):
                x_in = x
            else:
                x_in = int(round(x))
            l_x_in.append(x_in)
        np_x_in = numpy.array(l_x_in, dtype=int)
        self.__pd2d_peak_index_k = np_x_in

    @property
    def l(self):
        return self.__pd2d_peak_index_l
    @l.setter
    def l(self, l_x):
        l_x_in = []
        for x in l_x:
            if isinstance(x, float):
                x_in = x
            else:
                x_in = int(round(x))
            l_x_in.append(x_in)
        np_x_in = numpy.array(l_x_in, dtype=int)
        self.__pd2d_peak_index_l = np_x_in

    @property
    def mult(self):
        return self.__pd2d_peak_index_mult
    @mult.setter
    def mult(self, l_x):
        l_x_in = []
        for x in l_x:
            if isinstance(x, float):
                x_in = x
            else:
                x_in = int(round(x))
            l_x_in.append(x_in)
        np_x_in = numpy.array(l_x_in, dtype=int)
        self.__pd2d_peak_index_mult = np_x_in

    @property
    def ttheta(self):
        return self.__pd2d_peak_2theta
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
        self.__pd2d_peak_2theta = np_x_in

    @property
    def f_nucl_sq(self):
        return self.__pd2d_peak_f_nucl_sq
    @f_nucl_sq.setter
    def f_nucl_sq(self, l_x):
        l_x_in = []
        for x in l_x:
            if isinstance(x, float):
                x_in = x
            else:
                x_in = float(x)
            l_x_in.append(x_in)
        np_x_in = numpy.array(l_x_in, dtype=float)
        self.__pd2d_peak_f_nucl_sq = np_x_in

    @property
    def f_m_p_sin_sq(self):
        return self.__pd2d_peak_f_m_p_sin_sq
    @f_m_p_sin_sq.setter
    def f_m_p_sin_sq(self, l_x):
        l_x_in = []
        for x in l_x:
            if isinstance(x, float):
                x_in = x
            else:
                x_in = float(x)
            l_x_in.append(x_in)
        np_x_in = numpy.array(l_x_in, dtype=float)
        self.__pd2d_peak_f_m_p_sin_sq = np_x_in

    @property
    def f_m_p_cos_sq(self):
        return self.__pd2d_peak_f_m_p_cos_sq
    @f_m_p_cos_sq.setter
    def f_m_p_cos_sq(self, l_x):
        l_x_in = []
        for x in l_x:
            if isinstance(x, float):
                x_in = x
            else:
                x_in = float(x)
            l_x_in.append(x_in)
        np_x_in = numpy.array(l_x_in, dtype=float)
        self.__pd2d_peak_f_m_p_cos_sq = np_x_in

    @property
    def cross_sin(self):
        return self.__pd2d_peak_cross_sin
    @cross_sin.setter
    def cross_sin(self, l_x):
        l_x_in = []
        for x in l_x:
            if isinstance(x, float):
                x_in = x
            else:
                x_in = float(x)
            l_x_in.append(x_in)
        np_x_in = numpy.array(l_x_in, dtype=float)
        self.__pd2d_peak_cross_sin = np_x_in

    @property
    def width_2theta(self):
        return self.__pd2d_peak_width_2theta
    @width_2theta.setter
    def width_2theta(self, l_x):
        l_x_in = []
        for x in l_x:
            if isinstance(x, float):
                x_in = x
            else:
                x_in = float(x)
            l_x_in.append(x_in)
        np_x_in = numpy.array(l_x_in, dtype=float)
        self.__pd2d_peak_width_2theta = np_x_in

    def __repr__(self):
        ls_out = ["Pd2dPeak:"]
        ls_out.append("    h     k     l  mult    ttheta    f_nucl_sq f_m_p_sin_sq f_m_p_cos_sq    cross_sin width_2theta")
        for _1, _2, _3, _4, _5, _6, _7, _8, _9, _10 in zip(self.h, self.k, self.l, self.mult, self.ttheta, self.f_nucl_sq, self.f_m_p_sin_sq, self.f_m_p_cos_sq, self.cross_sin, self.width_2theta):
            ls_out.append("{:5} {:5} {:5} {:5} {:9.2f} {:12.5f} {:12.5f} {:12.5f} {:12.5f} {:12.5f}".format(_1, _2, _3, _4, _5, _6, _7, _8, _9, _10))
        return "\n".join(ls_out)

    @property
    def to_cif(self):
        ls_out = []
        if self.is_defined:
            ls_out.append("loop_")
            ls_out.append("_pd2d_peak_index_h")
            ls_out.append("_pd2d_peak_index_k")
            ls_out.append("_pd2d_peak_index_l")
            ls_out.append("_pd2d_peak_mult")
            ls_out.append("_pd2d_peak_2theta")
            ls_out.append("_pd2d_peak_f_nucl_sq")
            ls_out.append("_pd2d_peak_f_m_p_sin_sq")
            ls_out.append("_pd2d_peak_f_m_p_cos_sq")
            ls_out.append("_pd2d_peak_cross_sin")
            ls_out.append("_pd2d_peak_width_2theta")
            for _1, _2, _3, _4, _5, _6, _7, _8, _9, _10 in zip(self.h, self.k, self.l, self.mult, self.ttheta, self.f_nucl_sq, self.f_m_p_sin_sq, self.f_m_p_cos_sq, self.cross_sin, self.width_2theta):
                ls_out.append("{:} {:} {:} {:} {:.2f} {:.5f} {:.5f} {:.5f} {:.5f} {:.5f}".format(_1, _2, _3, _4, _5, _6, _7, _8, _9, _10))
        return "\n".join(ls_out)

    def from_cif(self, string: str):
        cif_global = Global()
        flag = cif_global.take_from_string(string)
        if not flag:
            return False
        flag = False
        flag = cif_global.is_prefix("_pd2d_peak")
        if flag:
            cif_loop = cif_global["_pd2d_peak"]
            l_name = cif_loop.names
            if "_pd2d_peak_index_h" in l_name:
                self.h = [int(_1) for _1 in cif_loop["_pd2d_peak_index_h"]]
            if "_pd2d_peak_index_k" in l_name:
                self.k = [int(_1) for _1 in cif_loop["_pd2d_peak_index_k"]]
            if "_pd2d_peak_index_l" in l_name:
                self.l = [int(_1) for _1 in cif_loop["_pd2d_peak_index_l"]]
            if "_pd2d_peak_index_mult" in l_name:
                self.mult = [int(_1) for _1 in cif_loop["_pd2d_peak_index_mult"]]
            if "_pd2d_peak_2theta" in l_name:
                self.ttheta = [float(_1) for _1 in cif_loop["_pd2d_peak_2theta"]]
            if "_pd2d_peak_f_nucl_sq" in l_name:
                self.f_nucl_sq = [float(_1) for _1 in cif_loop["_pd2d_peak_f_nucl_sq"]]
            if "_pd2d_peak_f_m_p_sin_sq" in l_name:
                self.f_m_p_sin_sq = [float(_1) for _1 in cif_loop["_pd2d_peak_f_m_p_sin_sq"]]
            if "_pd2d_peak_f_m_p_cos_sq" in l_name:
                self.f_m_p_cos_sq = [float(_1) for _1 in cif_loop["_pd2d_peak_f_m_p_cos_sq"]]
            if "_pd2d_peak_cross_sin" in l_name:
                self.cross_sin = [float(_1) for _1 in cif_loop["_pd2d_peak_cross_sin"]]
            if "_pd2d_peak_width_2theta" in l_name:
                self.width_2theta = [float(_1) for _1 in cif_loop["_pd2d_peak_width_2theta"]]
        else:
            self.h, self.k, self.l, self.mult, self.ttheta, self.f_nucl_sq, self.f_m_p_sin_sq, self.f_m_p_cos_sq, self.cross_sin, self.width_2theta = [], [], [], [], [], [], [], []
        return True

    @property
    def is_defined(self):
        cond = all([self.h is not None, self.k is not None, self.l is not None, self.mult is not None, 
                    self.ttheta is not None, self.f_nucl_sq is not None, self.f_m_p_sin_sq is not None,
                    self.f_m_p_cos_sq is not None, self.cross_sin is not None, self.width_2theta is not None])
        return cond

    @property
    def is_variable(self):
        return False
    
    def get_variables(self):
        return []

    def _show_message(self, s_out: str):
        print("***  Error ***")
        print(s_out)
