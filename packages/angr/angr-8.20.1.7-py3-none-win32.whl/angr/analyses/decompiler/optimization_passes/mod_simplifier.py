import logging

from ailment import Expr

from ... import AnalysesHub
from .engine_base import SimplifierAILEngine, SimplifierAILState
from .optimization_pass import OptimizationPass

_l = logging.getLogger(name=__name__)

class ModSimplifierAILEngine(SimplifierAILEngine):

    def _ail_handle_Sub(self, expr):

        operand_0 = self._expr(expr.operands[0])
        operand_1 = self._expr(expr.operands[1])

        if isinstance(operand_1, Expr.BinaryOp) \
            and isinstance(operand_1.operands[1], Expr.Const) \
                and operand_1.op == 'Mul':
            if isinstance(operand_1.operands[0], Expr.BinaryOp) \
                and isinstance(operand_1.operands[0].operands[1], Expr.Const) \
                    and operand_1.operands[0].op in ['Div', 'DivMod']:
                x_0 = operand_1.operands[0].operands[0]
                x_1 = operand_0
                c_0 = operand_1.operands[1]
                c_1 = operand_1.operands[0].operands[1]
            elif isinstance(operand_1.operands[0], Expr.Convert) \
                and isinstance(operand_1.operands[0].operand, Expr.BinaryOp) \
                    and operand_1.operands[0].operand.op in ['Div', 'DivMod']:
                x_0 = operand_1.operands[0].operand.operands[0]
                x_1 = operand_0
                c_0 = operand_1.operands[1]
                c_1 = operand_1.operands[0].operand.operands[1]

            if x_0 == x_1 and c_0.value == c_1.value:
                return Expr.BinaryOp(expr.idx, 'Mod', [x_0, c_0], **expr.tags)
        if (operand_0, operand_1) != (expr.operands[0], expr.operands[1]):
            return Expr.BinaryOp(expr.idx, 'Sub', [operand_0, operand_1], **expr.tags)
        return expr

    def _ail_handle_Mod(self, expr): #pylint: disable=no-self-use
        return expr


class ModSimplifier(OptimizationPass):

    ARCHES = ["X86", "AMD64"]
    PLATFORMS = ["linux", "windows"]

    def __init__(self, func, blocks):

        super().__init__(func, blocks=blocks)

        self.state = SimplifierAILState(self.project.arch)
        self.engine = ModSimplifierAILEngine()

        self.analyze()

    def _check(self):
        return True, None

    def _analyze(self, cache=None):

        for block in self._blocks.values():
            new_block = block
            old_block = None

            while new_block != old_block:
                old_block = new_block
                new_block = self.engine.process(state=self.state.copy(), block=old_block.copy())
                _l.debug("new block: %s", new_block.statements)

            self._update_block(block, new_block)

AnalysesHub.register_default("ModSimplifier", ModSimplifier)
