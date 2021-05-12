# Generated from main/csel/parser/CSEL.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CSELParser import CSELParser
else:
    from CSELParser import CSELParser

# This class defines a complete generic visitor for a parse tree produced by CSELParser.

class CSELVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CSELParser#program.
    def visitProgram(self, ctx:CSELParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#decllist.
    def visitDecllist(self, ctx:CSELParser.DecllistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#var_decl.
    def visitVar_decl(self, ctx:CSELParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#var_glo_decl.
    def visitVar_glo_decl(self, ctx:CSELParser.Var_glo_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#var_loc_decl.
    def visitVar_loc_decl(self, ctx:CSELParser.Var_loc_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#glo_constant_decl.
    def visitGlo_constant_decl(self, ctx:CSELParser.Glo_constant_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#loc_constant_decl.
    def visitLoc_constant_decl(self, ctx:CSELParser.Loc_constant_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#list_var.
    def visitList_var(self, ctx:CSELParser.List_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#list_index.
    def visitList_index(self, ctx:CSELParser.List_indexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#func_decl.
    def visitFunc_decl(self, ctx:CSELParser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#list_parameters.
    def visitList_parameters(self, ctx:CSELParser.List_parametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#parameter.
    def visitParameter(self, ctx:CSELParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#body.
    def visitBody(self, ctx:CSELParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#bodystmt.
    def visitBodystmt(self, ctx:CSELParser.BodystmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#stmtList.
    def visitStmtList(self, ctx:CSELParser.StmtListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#stmt.
    def visitStmt(self, ctx:CSELParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#if_stmt.
    def visitIf_stmt(self, ctx:CSELParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#list_elif.
    def visitList_elif(self, ctx:CSELParser.List_elifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#else_stmt.
    def visitElse_stmt(self, ctx:CSELParser.Else_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#assign_stmt.
    def visitAssign_stmt(self, ctx:CSELParser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#forIn_stmt.
    def visitForIn_stmt(self, ctx:CSELParser.ForIn_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#forOf_stmt.
    def visitForOf_stmt(self, ctx:CSELParser.ForOf_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#while_stmt.
    def visitWhile_stmt(self, ctx:CSELParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#break_stmt.
    def visitBreak_stmt(self, ctx:CSELParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#continue_stmt.
    def visitContinue_stmt(self, ctx:CSELParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#call_stmt.
    def visitCall_stmt(self, ctx:CSELParser.Call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#list_exp.
    def visitList_exp(self, ctx:CSELParser.List_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#return_stmt.
    def visitReturn_stmt(self, ctx:CSELParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#lhs.
    def visitLhs(self, ctx:CSELParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#exp.
    def visitExp(self, ctx:CSELParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#exp1.
    def visitExp1(self, ctx:CSELParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#exp2.
    def visitExp2(self, ctx:CSELParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#exp3.
    def visitExp3(self, ctx:CSELParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#exp4.
    def visitExp4(self, ctx:CSELParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#exp5.
    def visitExp5(self, ctx:CSELParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#index_exp.
    def visitIndex_exp(self, ctx:CSELParser.Index_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#key.
    def visitKey(self, ctx:CSELParser.KeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#list_key.
    def visitList_key(self, ctx:CSELParser.List_keyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#exp7.
    def visitExp7(self, ctx:CSELParser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#operands.
    def visitOperands(self, ctx:CSELParser.OperandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#func_call.
    def visitFunc_call(self, ctx:CSELParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#literal.
    def visitLiteral(self, ctx:CSELParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#array_literal.
    def visitArray_literal(self, ctx:CSELParser.Array_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#element.
    def visitElement(self, ctx:CSELParser.ElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#list_elements.
    def visitList_elements(self, ctx:CSELParser.List_elementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#json_literal.
    def visitJson_literal(self, ctx:CSELParser.Json_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#primitive_types.
    def visitPrimitive_types(self, ctx:CSELParser.Primitive_typesContext):
        return self.visitChildren(ctx)



del CSELParser