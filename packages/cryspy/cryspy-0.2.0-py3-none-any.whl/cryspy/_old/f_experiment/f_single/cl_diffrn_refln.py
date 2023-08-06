"""
define classe DiffrnRefln which describes the single diffraction experiment
"""
__author__ = 'ikibalin'
__version__ = "2019_09_10"
import os
import numpy


from pycifstar import Global
from cryspy.f_common.cl_fitable import Fitable


class DiffrnRefln(object):
    """
    Data items in the DIFFRN_REFLN category record details about
    the intensities measured in the diffraction experiment.

    The DIFFRN_REFLN data items refer to individual intensity
    measurements and must be included in looped lists.

    Example:

    loop_
    _diffrn_refln_index_h
    _diffrn_refln_index_k
    _diffrn_refln_index_l
    _diffrn_refln_fr
    _diffrn_refln_fr_sigma
        0    0    8   0.64545   0.01329 
        2    0    6   1.75682   0.0454  
    
    reference: https://www.iucr.org/__data/iucr/cifdic_html/1/cif_core.dic/Cdiffrn_refln.html
    """
    def __init__(self, h=[], k=[], l=[], fr=[], fr_sigma=[]
                 ):
        super(DiffrnRefln, self).__init__()
        self.__diffrn_refln_index_h = None
        self.__diffrn_refln_index_k = None
        self.__diffrn_refln_index_l = None
        self.__diffrn_refln_fr = None
        self.__diffrn_refln_fr_sigma = None
        self.h = h
        self.k = k
        self.l = l
        self.fr = fr
        self.fr_sigma = fr_sigma

        self.__diffrn_refln_fr_calc = None
        self.__diffrn_refln_intensity_up_calc = None
        self.__diffrn_refln_intensity_down_calc = None

    @property
    def h(self):
        return self.__diffrn_refln_index_h
    @h.setter
    def h(self, l_x):
        l_x_in = []
        for x in l_x:
            if isinstance(x, int):
                x_in = x
            else:
                x_in = int(round(x))
            l_x_in.append(x_in)
        np_x_in = numpy.array(l_x_in, dtype=int)
        self.__diffrn_refln_index_h = np_x_in

    @property
    def k(self):
        return self.__diffrn_refln_index_k
    @k.setter
    def k(self, l_x):
        l_x_in = []
        for x in l_x:
            if isinstance(x, int):
                x_in = x
            else:
                x_in = int(round(x))
            l_x_in.append(x_in)
        np_x_in = numpy.array(l_x_in, dtype=int)
        self.__diffrn_refln_index_k = np_x_in

    @property
    def l(self):
        return self.__diffrn_refln_index_l
    @l.setter
    def l(self, l_x):
        l_x_in = []
        for x in l_x:
            if isinstance(x, int):
                x_in = x
            else:
                x_in = int(round(x))
            l_x_in.append(x_in)
        np_x_in = numpy.array(l_x_in, dtype=int)
        self.__diffrn_refln_index_l = np_x_in

    @property
    def fr(self):
        return self.__diffrn_refln_fr
    @fr.setter
    def fr(self, l_x):
        l_x_in = []
        for x in l_x:
            if isinstance(x, float):
                x_in = x
            else:
                x_in = float(x)
            l_x_in.append(x_in)
        np_x_in = numpy.array(l_x_in, dtype=float)
        self.__diffrn_refln_fr = np_x_in


    @property
    def fr_sigma(self):
        return self.__diffrn_refln_fr_sigma
    @fr_sigma.setter
    def fr_sigma(self, l_x):
        l_x_in = []
        for x in l_x:
            if isinstance(x, float):
                x_in = x
            else:
                x_in = float(x)
            l_x_in.append(x_in)
        np_x_in = numpy.array(l_x_in, dtype=float)
        self.__diffrn_refln_fr_sigma = np_x_in


    @property
    def fr_calc(self):
        return self.__diffrn_refln_fr_calc
    @fr_calc.setter
    def fr_calc(self, l_x):
        l_x_in = []
        for x in l_x:
            if isinstance(x, float):
                x_in = x
            else:
                x_in = float(x)
            l_x_in.append(x_in)
        np_x_in = numpy.array(l_x_in, dtype=float)
        if np_x_in.size != self.h.size:
            np_x_in = None
            self._show_message("Size of  fr_calc is different from size of hkl")
        self.__diffrn_refln_fr_calc = np_x_in

    @property
    def intensity_up_calc(self):
        return self.__diffrn_refln_intensity_up_calc
    @intensity_up_calc.setter
    def intensity_up_calc(self, l_x):
        l_x_in = []
        for x in l_x:
            if isinstance(x, float):
                x_in = x
            else:
                x_in = float(x)
            l_x_in.append(x_in)
        np_x_in = numpy.array(l_x_in, dtype=float)
        if np_x_in.size != self.h.size:
            np_x_in = None
            self._show_message("Size of  intensity_up_calc is different from size of hkl")
        self.__diffrn_refln_intensity_up_calc = np_x_in

    @property
    def intensity_down_calc(self):
        return self.__diffrn_refln_intensity_down_calc
    @intensity_down_calc.setter
    def intensity_down_calc(self, l_x):
        l_x_in = []
        for x in l_x:
            if isinstance(x, float):
                x_in = x
            else:
                x_in = float(x)
            l_x_in.append(x_in)
        np_x_in = numpy.array(l_x_in, dtype=float)
        if np_x_in.size != self.h.size:
            np_x_in = None
            self._show_message("Size of  intensity_down_calc is different from size of hkl")
        self.__diffrn_refln_intensity_down_calc = np_x_in
            
    def __repr__(self):
        ls_out = ["DiffrnRefln"]
        ls_out.append(str(self))
        return "\n".join(ls_out)

    def __str__(self):
        ls_out = []
        ls_out.append(" number of reflections: {:}".format(self.fr.size))
        ls_out.append("     min  max\n h  {:4} {:4}\n k  {:4} {:4}\n l  {:4} {:4}".format(
            self.h.min(), self.h.max(), self.k.min(), self.k.max(), self.l.min(), self.l.max()
        ))
        flag_fr_calc = self.fr_calc is not None
        if flag_fr_calc:
            ls_out.append("     h     k     l        fr  fr_sigma   fr_calc")
            for _1, _2, _3, _4, _5, _6 in zip(self.h, self.k, self.l, self.fr, self.fr_sigma, self.fr_calc):
                ls_out.append(" {:5} {:5} {:5} {:9.5} {:9.5} {:9.5}".format(_1, _2, _3, _4, _5, _6))
        else:
            ls_out.append("     h     k     l        fr  fr_sigma")
            for _1, _2, _3, _4, _5 in zip(self.h, self.k, self.l, self.fr, self.fr_sigma):
                ls_out.append(" {:5} {:5} {:5} {:9.5} {:9.5}".format(_1, _2, _3, _4, _5))

        return "\n".join(ls_out)

    @property
    def to_cif(self):
        ls_out = []
        flag_fr_calc = self.fr_calc is not None
        if self.is_defined:
            ls_out.append("loop_")
            ls_out.append("_diffrn_refln_index_h")
            ls_out.append("_diffrn_refln_index_k")
            ls_out.append("_diffrn_refln_index_l")
            ls_out.append("_diffrn_refln_fr")
            ls_out.append("_diffrn_refln_fr_sigma")
            if flag_fr_calc:
                ls_out.append("_diffrn_refln_fr_calc")
                for _1, _2, _3, _4, _5, _6 in zip(self.h, self.k, self.l, self.fr, self.fr_sigma, self.fr_calc):
                    ls_out.append("{:} {:} {:} {:} {:} {:}".format(_1, _2, _3, _4, _5, _6))
            else:
                for _1, _2, _3, _4, _5 in zip(self.h, self.k, self.l, self.fr, self.fr_sigma):
                    ls_out.append("{:} {:} {:} {:} {:}".format(_1, _2, _3, _4, _5))

        return "\n".join(ls_out)

    def from_cif(self, string: str):
        cif_global = Global()
        flag = cif_global.take_from_string(string)
        if not flag:
            return False
        flag = False
        flag = cif_global.is_prefix("_diffrn_refln")
        if flag:
            cif_loop = cif_global["_diffrn_refln"]
            l_name = cif_loop.names
            if "_diffrn_refln_index_h" in l_name:
                self.h = [int(_1) for _1 in cif_loop["_diffrn_refln_index_h"]]
            if "_diffrn_refln_index_k" in l_name:
                self.k = [int(_1) for _1 in cif_loop["_diffrn_refln_index_k"]]
            if "_diffrn_refln_index_l" in l_name:
                self.l = [int(_1) for _1 in cif_loop["_diffrn_refln_index_l"]]
            if "_diffrn_refln_fr" in l_name:
                self.fr = [float(_1) for _1 in cif_loop["_diffrn_refln_fr"]]
            if "_diffrn_refln_fr_sigma" in l_name:
                self.fr_sigma = [float(_1) for _1 in cif_loop["_diffrn_refln_fr_sigma"]]
        else:
            self.h, self.k, self.l, self.fr, self.fr_sigma = [], [], [], [], []
        return True

    @property
    def is_defined(self):
        cond = all([self.h is not None, self.k is not None, self.l is not None, self.fr is not None, self.fr_sigma is not None])
        return cond

    @property
    def is_variable(self):
        return False
    
    def get_variables(self):
        return []

    def _show_message(self, s_out: str):
        print("***  Error ***")
        print(s_out)
    def print_agreement_factor_exp(self):
        l_chi_sq_exp, l_ag_f_exp = [], []
        l_hkl = [(int(_1), int(_2), int(_3))for _1, _2, _3 in zip(self.h, self.k, self.l)]
        for _hkl, _fr_1, _fr_sigma_1 in zip(l_hkl, self.fr, self.fr_sigma):
            _mhkl = (-1*_hkl[0], -1*_hkl[1], -1*_hkl[2])
            if _mhkl in l_hkl:
                ind_mhkl = l_hkl.index(_mhkl)
                _fr_2, _fr_sigma_2 = self.fr[ind_mhkl], self.fr_sigma[ind_mhkl]
                _fr_sigma = 1./(_fr_sigma_1**(-2)+_fr_sigma_2**(-2))**0.5
                _fr_average = (_fr_1*_fr_sigma_1**(-2)+_fr_2*_fr_sigma_2**(-2))*_fr_sigma**2
                delta_fr = abs(_fr_1-_fr_average)
                chi_sq_exp = (delta_fr/_fr_sigma_1)**2
                l_chi_sq_exp.append(chi_sq_exp)
                ag_f_exp = abs((_fr_1-_fr_average)/(_fr_1-1.))
                l_ag_f_exp.append(ag_f_exp)
                #print("hkl: {:4} {:4} {:4}".format(_hkl[0], _hkl[1], _hkl[2]))
                #print("chi_sq_exp: {:.3f} ".format(chi_sq_exp))
                #print("ag_f_exp: {:.3f} ".format(ag_f_exp))
        ls_out = []
        n_friedel = len(l_chi_sq_exp)
        ls_out.append("number of Friedel reflections is {:}".format(n_friedel))
        if n_friedel != 0:
            ls_out.append("agreement factor_exp/n is {:.3f}".format(sum(l_ag_f_exp)/n_friedel))
            ls_out.append("chi_sq_exp/n is {:.3f}".format(sum(l_chi_sq_exp)/n_friedel))
        return "\n".join(ls_out) 

