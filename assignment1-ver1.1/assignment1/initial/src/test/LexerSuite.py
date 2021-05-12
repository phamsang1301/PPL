
import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    """ Empty file """
    def test_101(self):
            input = " "
            expect = r"""<EOF>"""
            self.assertTrue(TestLexer.checkLexeme(input, expect, 101))
    
    """ White-space """

    def test_102(self):
        input = r""" "\t \f \r \n" """
        expect = r"""\t \f \r \n,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 102))


    """ Comment"""
    def test_103(self):
        input = r""" ## Single-line comment ## """
        expect = r"""<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 103))

    def test_104(self):
        input = r""" ## Multiple-line
                    #  Comment
                    ##"""
        expect = r"""<EOF>"""
    
    def test_105(self):
        input = r""" ## Unterminated Comment """
        expect = r"""Unterminated Comment"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 105))
    
    def test_106(self):
        input = r"""#### empty comment"""
        expect = r"""empty,comment,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 106))
    
    def test_107(self):
        input = r""" ## comment ## not a comment"""
        expect = r"""not,a,comment,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 107))

    def test_108(self):
        input = r""" ## comment ## not a comment## """
        expect = r"""not,a,comment,Unterminated Comment"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 108))

    def test_109(self):
        input = r""" ## comment ## not a comment ## comment ##"""
        expect = r"""not,a,comment,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 109))


    def test_112(self):
        input = r""" ### ##"""
        expect = r"""<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 110))
        
    def test_comment(self):
        self.assertTrue(TestLexer.checkLexeme(""" #### ""","<EOF>",111))
        
    def test_comment_multi1(self):
        self.assertTrue(TestLexer.checkLexeme(""" ##em khong la nang tho
                                                    #anh cung khong con la nhac si mong mo
                                                    #tinh nay nhe nhu gio ## ""","<EOF>",112)) 


    """Keyword"""

    def test_113(self):
        input = r""" Let """
        expect = r"""Let,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 113))
    
    def test_114(self):
        input = r"""Break"""
        expect = r"""Break,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 114))

    def test_115(self):
        input = r"""Continue"""
        expect = r"""Continue,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 115))
    
    def test_116(self):
        input = r"""If"""
        expect = r"""If,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 116))
    
    def test_117(self):
        input = r"""Elif"""
        expect = r"""Elif,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 117))

    def test_118(self):
        input = r"""Else"""
        expect = r"""Else,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 118))
    
    def test_119(self):
        input = r"""While"""
        expect = r"""While,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 119))

    def test_120(self):
        input = r"""For"""
        expect = r"""For,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 120))
    
    def test_121(self):
        input = r"""Of"""
        expect = r"""Of,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 121))

    def test_122(self):
        input = r"""In"""
        expect = r"""In,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 122))

    def test_123(self):
        input = r"""Function"""
        expect = r"""Function,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 123))

    def test_124(self):
        input = r"""Let"""
        expect = r"""Let,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 124))
    
    def test_125(self):
        input = r"""True"""
        expect = r"""True,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 125))

    def test_126(self):
        input = r"""False"""
        expect = r"""False,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 126))

    def test_127(self):
        input = r"""Call"""
        expect = r"""Call,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 127))
    
    def test_128(self):
        input = r"""Return"""
        expect = r"""Return,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 128))

    def test_129(self):
        input = r"""Number"""
        expect = r"""Number,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 129))

    def test_130(self):
        input = r"""Boolean"""
        expect = r"""Boolean,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 130))
    
    def test_131(self):
        input = r"""String"""
        expect = r"""String,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 131))

    def test_132(self):
        input = r"""Json"""
        expect = r"""Json,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 132))

    def test_133(self):
        input = r"""Array"""
        expect = r"""Array,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 133))

        
        """ Operator """

    def test_134(self):
        input = r"""+-*/%"""
        expect = r"""+,-,*,/,%,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 134))

    def test_134(self):
        input = r"""+-*/%"""
        expect = r"""+,-,*,/,%,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 134))
    
    def test_135(self):
        input = r"""!&&||"""
        expect = r"""!,&&,||,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 135))
    
    def test_136(self):
        input = r"""==!="""
        expect = r"""==,!=,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 136))
    
    def test_137(self):
        input = r"""><=>>="""
        expect = r""">,<=,>,>=,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 137))
    
    def test_138(self):
        input = r"""+.==."""
        expect = r"""+.,==.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 138))
    
    def test_139(self):
        input = r"""="""
        expect = r"""=,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 139))
       
       
        """ Seperator """
    def test_140(self):
        input = r"""()[]:.,;{}"""
        expect = r"""(,),[,],:,.,,,;,{,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 140))

    """ Identifier """

    def test_141(self):
        input = r"""a b c d e f g h i j k l m n o p q r s t u v w x y z"""
        expect = r"""a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 141))
    
    def test_142(self):
        input = r""" a_0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ """
        expect = r"""a_0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 142))
    

    def test_145(self):
        input = r""" _abcd """
        expect = r"""Error Token _"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 145))


    def test_144(self):
        input = r"""$A1234abcd"""
        expect = r"""$A1234abcd,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 144))


    def test_143(self):
        input = r""" 1234abcd ABCDdefg """
        expect = r"""1234,abcd,Error Token A"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 143))


    def test_146(self):
        input = r""" Abcd """
        expect = r"""Error Token A"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 146))

    def test_147(self):
        input = r""" Bsadsd """
        expect = r"""Error Token B"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 147))

    def test_148(self):
        input = r""" 1 2 3 4 5 6 7 8 9 """
        expect = r"""1,2,3,4,5,6,7,8,9,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 148))

    def test_149(self):
        input = r""" 1 2 3 4 5 6 7 8 9 """
        expect = r"""1,2,3,4,5,6,7,8,9,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 149))

    def test_150(self):
        input = r"""
aa
bb 222222222 $c
444444444 555555555 666666666
Ba 888888888 999999999
"""
        expect = r"""aa,bb,222222222,$c,444444444,555555555,666666666,Error Token B"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 150))

    def test_151(self):
        input = r""" 000"""
        expect = r"""000,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 151))
        
    def test_152(self):
        input = r""" 1"""
        expect = r"""1,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 152))
    def test_153(self):
        input = r""" 123A """
        expect = r"""123,Error Token A"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 153))

    def test_154(self):
        input = r""" 123abc """
        expect = r"""123,abc,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 154))
    

    def test_155(self):
        input = r""" 123A """
        expect = r"""123,Error Token A"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 155))
    def test_156(self):
        input = r""" +4567"""
        expect = r"""+,4567,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 156))
    def test_157(self):
        input = r""" -4567"""
        expect = r"""-,4567,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 157))

    def test_158(self):
        input = r""" 23Aa"""
        expect = r"""23,Error Token A"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 158))

    def test_ID_underscore(self):
        self.assertTrue(TestLexer.checkLexeme("em_ kh_ong l_a n_ang tTTT_ho","em_,kh_ong,l_a,n_ang,tTTT_ho,<EOF>",159))
    
    def test_1560(self):
        input = r""" 8+ 9"""
        expect = r"""8,+,9,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 160))
    

    def test_161(self):
        input = r""" 12.3E3 12.3e3"""
        expect = r"""12.3E3,12.3e3,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 161))
   
    def test_162(self):
        input = r""" 12.3E3 12.3e3 12.3e-3 12.3e-30 """
        expect = r"""12.3E3,12.3e3,12.3e-3,12.3e-30,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 162))
   
    def test_160(self):
        input = r""" 1E1 1E+1 1E-1 1e1 1e+1 1e-1  """
        expect = r"""1E1,1E+1,1E-1,1e1,1e+1,1e-1,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 163))
    def test_1561(self):
        input = r""" 12."""
        expect = r"""12.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 164))
    def test_1511(self):
        input = r""" 0 """
        expect = r"""0,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 165))

    def test_ID(self):
        self.assertTrue(TestLexer.checkLexeme("em khong la nang tho","em,khong,la,nang,tho,<EOF>",166))
        
    """String"""
    def test_normal_string(self):
        self.assertTrue(TestLexer.checkLexeme(""" "mothaiba"  ""","""mothaiba,<EOF>""",167))
    def test_multi_string(self):
        self.assertTrue(TestLexer.checkLexeme(""" "mothaiba" "haibabon" ""","""mothaiba,haibabon,<EOF>""",168))
    def test_illegal_string(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\em\khong\la\\nang tho" ""","""Illegal Escape In String: \e""",169))
    def test_illegal_string(self):
        self.assertTrue(TestLexer.checkLexeme(""" "em khong la nang'" tho" ""","""em khong la nang'" tho,<EOF>""",170))
    def test_unclose_string(self):
        self.assertTrue(TestLexer.checkLexeme(""" "em khong la nang tho ""","Unclosed String: em khong la nang tho ",171))
    def test_normal_string_with_escape(self):
        self.assertTrue(TestLexer.checkLexeme(""" "ab'"c\\n def"  ""","""ab'"c\\n def,<EOF>""",172))   
    def test_normal_string_with_doublequote(self):
        self.assertTrue(TestLexer.checkLexeme(""" "day la cau '"ksks'"kdmckmc" ""","""day la cau '"ksks'"kdmckmc,<EOF>""",173))
    def test_normal_string_with_doublequote2(self):
        self.assertTrue(TestLexer.checkLexeme(""" "day la cau'" lll'" ""","""Unclosed String: day la cau'" lll'" """,174))
    def test_normal_string_with_escape(self):
        """test normal string with escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "ab'"c\\n def"  ""","""ab'"c\\n def,<EOF>""",175))

    """ String literal """
    def test_176(self):
        input = """
"0123456789"
"abcdefghijklmnopqrstuvwxyz"
"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
"!#$%&()*+,-./:;<=>?@[]^_`{|}~"
" "
"""
        expect = "0123456789,abcdefghijklmnopqrstuvwxyz,ABCDEFGHIJKLMNOPQRSTUVWXYZ,!#$%&()*+,-./:;<=>?@[]^_`{|}~, ,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 176))

    def test_177(self):
        input = r""" "\b\f\r\n\t\'\\" """
        expect = r"""\b\f\r\n\t\'\\,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 177))
    def test_178(self):
        input = r""" "str'"" """
        expect = r"""str'",<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 178))
    def test_179(self):
        input = r""" "Next line:\n'"str'"" """
        expect = r"""Next line:\n'"str'",<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 179))


    def test_180(self):
        input = r""" "str\'" """
        expect = r"""str\',<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 180))

    """ Array literals"""
    def test_181(self):
        input = r""" [1] """
        expect = r"""[,1,],<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 181))
    def test_182(self):
        input = r""" [1,2] """
        expect = r"""[,1,,,2,],<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 182))
    def test_183(self):
        input = r""" [1,2,3,4] """
        expect = r"""[,1,,,2,,,3,,,4,],<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 183))
    def test_184(self):
        input = r""" [[1,2]] """
        expect = r"""[,[,1,,,2,],],<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 184))
    def test_185(self):
        input = r""" [[1,2],[3,4]] """
        expect = r"""[,[,1,,,2,],,,[,3,,,4,],],<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 185))
    
    """ Illegal escape """

    def test_186(self):
        input = r""" "it's a dog" """
        expect = r"""Illegal Escape In String: it's"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 186))
    def test_187(self):
        input = r""" "it''s a dog" """
        expect = r"""Illegal Escape In String: it''"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 187))
    def test_188(self):
        input = r""" "it'\" """
        expect = "Illegal Escape In String: it'\\"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 188))
    def test_189(self):
        input = r""" "it' " """
        expect = r"""Illegal Escape In String: it' """
        self.assertTrue(TestLexer.checkLexeme(input, expect, 189))
    def test_190(self):
        input = r""" "str\1str" """
        expect = r"""Illegal Escape In String: str\1"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 190))
    def test_191(self):
        input = r""" "str\zstr" """
        expect = r"""Illegal Escape In String: str\z"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 191))
    def test_192(self):
        input = r""" "str\"str" """
        expect = "Illegal Escape In String: str\\\""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 192))
    def test_193(self):
        input = r""" "str\ str" """
        expect = r"""Illegal Escape In String: str\ """
        self.assertTrue(TestLexer.checkLexeme(input, expect, 193))

    """ Unclosed string """
    def test_194(self):
        input = r""""str"""
        expect = r"""Unclosed String: str"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 194))
    def test_195(self):
        input = r""" "
"""
        expect = r"""Unclosed String: """
        self.assertTrue(TestLexer.checkLexeme(input, expect, 195))   
    def test_196(self):
        input = " \""
        expect = r"""Unclosed String: """
        self.assertTrue(TestLexer.checkLexeme(input, expect, 196))
    def test_197(self):
        input = " \"str'\""
        expect = "Unclosed String: str'\""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 197))
    
    
    """ Error token """
    def test_198(self):
        input = r""" abcd? """
        expect = r"""abcd,Error Token ?"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 198))
    def test_199(self):
        input = r""" 1 / 2 """
        expect = r"""1,/,2,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 1990))

    def test_let(self):
        input =  r"""Let a;"""
        expect = r"""Let,a,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 1991))
    def test_let_2(self):
        input =  r"""Let a = 2;"""
        expect = r"""Let,a,=,2,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 1992))
    def test_let_3(self):
        input =  r"""Let a = 2, b;"""
        expect = r"""Let,a,=,2,,,b,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 1993))
    def test_Let_4(self):
        input =  r"""a = 2;"""
        expect = r"""a,=,2,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 1994))
 
    
    """Json"""
    def test_Json(self):
        input = r""" {name:  "Yanxi",address:"Chinese"} """
        expect = r"""{,name,:,Yanxi,,,address,:,Chinese,},<EOF> """
        
 