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


    # Visit a parse tree produced by CSELParser#iden.
    def visitIden(self, ctx:CSELParser.IdenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#vardecl.
    def visitVardecl(self, ctx:CSELParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#elem.
    def visitElem(self, ctx:CSELParser.ElemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#array_decl.
    def visitArray_decl(self, ctx:CSELParser.Array_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#id_array.
    def visitId_array(self, ctx:CSELParser.Id_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#json_decl.
    def visitJson_decl(self, ctx:CSELParser.Json_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#functiondecl.
    def visitFunctiondecl(self, ctx:CSELParser.FunctiondeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#parameters.
    def visitParameters(self, ctx:CSELParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#parameter.
    def visitParameter(self, ctx:CSELParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#body.
    def visitBody(self, ctx:CSELParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#stmt.
    def visitStmt(self, ctx:CSELParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#assign_stmt.
    def visitAssign_stmt(self, ctx:CSELParser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#if_stmt.
    def visitIf_stmt(self, ctx:CSELParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#condi.
    def visitCondi(self, ctx:CSELParser.CondiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#stmt_list.
    def visitStmt_list(self, ctx:CSELParser.Stmt_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#for_stmt.
    def visitFor_stmt(self, ctx:CSELParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#for_in.
    def visitFor_in(self, ctx:CSELParser.For_inContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#for_of.
    def visitFor_of(self, ctx:CSELParser.For_ofContext):
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


    # Visit a parse tree produced by CSELParser#return_stmt.
    def visitReturn_stmt(self, ctx:CSELParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#array_boolean.
    def visitArray_boolean(self, ctx:CSELParser.Array_booleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#array_num.
    def visitArray_num(self, ctx:CSELParser.Array_numContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#array_str.
    def visitArray_str(self, ctx:CSELParser.Array_strContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#array_json.
    def visitArray_json(self, ctx:CSELParser.Array_jsonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#array_arr.
    def visitArray_arr(self, ctx:CSELParser.Array_arrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#new_val.
    def visitNew_val(self, ctx:CSELParser.New_valContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#constantdecl.
    def visitConstantdecl(self, ctx:CSELParser.ConstantdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#booleanexp.
    def visitBooleanexp(self, ctx:CSELParser.BooleanexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#stringexp.
    def visitStringexp(self, ctx:CSELParser.StringexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#numexp.
    def visitNumexp(self, ctx:CSELParser.NumexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#function_call.
    def visitFunction_call(self, ctx:CSELParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#function_call_el.
    def visitFunction_call_el(self, ctx:CSELParser.Function_call_elContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#expression.
    def visitExpression(self, ctx:CSELParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#expression9.
    def visitExpression9(self, ctx:CSELParser.Expression9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#expression1.
    def visitExpression1(self, ctx:CSELParser.Expression1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#expression2.
    def visitExpression2(self, ctx:CSELParser.Expression2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#expression3.
    def visitExpression3(self, ctx:CSELParser.Expression3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#expression4.
    def visitExpression4(self, ctx:CSELParser.Expression4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#expression5.
    def visitExpression5(self, ctx:CSELParser.Expression5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#expression6.
    def visitExpression6(self, ctx:CSELParser.Expression6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#expression7.
    def visitExpression7(self, ctx:CSELParser.Expression7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#expression8.
    def visitExpression8(self, ctx:CSELParser.Expression8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#literals.
    def visitLiterals(self, ctx:CSELParser.LiteralsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#boolean_lit.
    def visitBoolean_lit(self, ctx:CSELParser.Boolean_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#json_lit.
    def visitJson_lit(self, ctx:CSELParser.Json_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#elem_json.
    def visitElem_json(self, ctx:CSELParser.Elem_jsonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#array_lit.
    def visitArray_lit(self, ctx:CSELParser.Array_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#type_arr.
    def visitType_arr(self, ctx:CSELParser.Type_arrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#adding.
    def visitAdding(self, ctx:CSELParser.AddingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#multiplying.
    def visitMultiplying(self, ctx:CSELParser.MultiplyingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#logical.
    def visitLogical(self, ctx:CSELParser.LogicalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#relational.
    def visitRelational(self, ctx:CSELParser.RelationalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#stri.
    def visitStri(self, ctx:CSELParser.StriContext):
        return self.visitChildren(ctx)



del CSELParser