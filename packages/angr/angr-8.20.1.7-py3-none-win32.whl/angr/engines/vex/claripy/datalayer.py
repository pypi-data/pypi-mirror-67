import claripy
import pyvex
import logging

from ..light import VEXMixin
from .... import errors
from .... import sim_options as o

l = logging.getLogger(__name__)
zero = claripy.BVV(0, 32)

def value(ty, val):
    if ty == 'Ity_F32':
        return claripy.FPV(float(val), claripy.FSORT_FLOAT)
    elif ty == 'Ity_F64':
        return claripy.FPV(float(val), claripy.FSORT_DOUBLE)
    else:
        return claripy.BVV(int(val), pyvex.get_type_size(ty))

def symbol(ty, name):
    if ty == 'Ity_F32':
        return claripy.FPS(name, claripy.FSORT_FLOAT)
    elif ty == 'Ity_F64':
        return claripy.FPS(name, claripy.FSORT_DOUBLE)
    else:
        return claripy.BVS(name, pyvex.get_type_size(ty))

class ClaripyDataMixin(VEXMixin):
    # consts

    def _handle_vex_const(self, const):
        return value(const.type, const.value)

    # is this right? do I care?
    def _handle_vex_expr_GSPTR(self, expr):
        return zero

    def _handle_vex_expr_VECRET(self, expr):
        return zero

    def _handle_vex_expr_Binder(self, expr):
        return zero

    # simple wrappers to implement the fp/bv data casting

    def _perform_vex_expr_Get(self, offset, ty, **kwargs):
        res = super()._perform_vex_expr_Get(offset, ty, **kwargs)
        if ty.startswith('Ity_F'):
            return res.raw_to_fp()
        else:
            return res

    def _perform_vex_expr_Load(self, addr, ty, endness, **kwargs):
        res = super()._perform_vex_expr_Load(addr, ty, endness, **kwargs)
        if ty.startswith('Ity_F'):
            return res.raw_to_fp()
        else:
            return res

    def _perform_vex_stmt_Put(self, offset, data, **kwargs):
        super()._perform_vex_stmt_Put(offset, data.raw_to_bv(), **kwargs)

    def _perform_vex_stmt_Store(self, addr, data, endness, **kwargs):
        super()._perform_vex_stmt_Store(addr, data.raw_to_bv(), endness, **kwargs)

    # op support

    def _perform_vex_expr_ITE(self, cond, ifTrue, ifFalse):
        return claripy.If(cond != 0, ifTrue, ifFalse)

    def _perform_vex_expr_Op(self, op, args):
        # TODO: get rid of these hacks (i.e. state options and modes) and move these switches into the engine initializer
        options = getattr(self.state, 'options', {o.SUPPORT_FLOATING_POINT})
        simop = irop.vexop_to_simop(op, extended=o.EXTENDED_IROP_SUPPORT in options, fp=o.SUPPORT_FLOATING_POINT in options)
        return simop.calculate(*args)

    # ccall support

    def _perform_vex_expr_CCall(self, func_name, ty, args, func=None):
        if func is None:
            try:
                func = getattr(ccall, func_name)
            except AttributeError as e:
                raise errors.UnsupportedCCallError("Unsupported ccall %s" % func_name) from e

        return func(self.state, *args)

from . import irop
from . import ccall
