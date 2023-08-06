import pytest
import math
import numpy
from cryspy.common.cl_fitable import Fitable

from cryspy.pd2dcif_like.cl_pd2d_instr_reflex_asymmetry import Pd2dInstrReflexAsymmetry

STR_FROM_CIF_1 = """
 _pd2d_instr_reflex_asymmetry_p1 0.01
 _pd2d_instr_reflex_asymmetry_p2 0.02
 _pd2d_instr_reflex_asymmetry_p3 0.03
 _pd2d_instr_reflex_asymmetry_p4 0.04
    """

def test_init():
    try:
        _object = Pd2dInstrReflexAsymmetry()
        flag = True
    except:
        flag = False
    assert flag

def test_to_cif():
    try:
        _object = Pd2dInstrReflexAsymmetry()
        _str = _object.to_cif
        flag = True
    except:
        flag = False
    assert flag


def test_from_cif():
    rel_tol, abs_tol =0.001, 0.001
    _obj = Pd2dInstrReflexAsymmetry.from_cif(STR_FROM_CIF_1)

    assert math.isclose(float(_obj.p1), 0.01, rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(float(_obj.p2), 0.02, rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(float(_obj.p3), 0.03, rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(float(_obj.p4), 0.04, rel_tol=rel_tol, abs_tol=abs_tol)
    assert _obj.is_defined
    
