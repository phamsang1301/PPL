# Generated from main/csel/parser/CSEL.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2<")
        buf.write("\u01ef\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\3\2\3\2\3\3\3\3")
        buf.write("\3\4\3\4\3\5\3\5\3\6\3\6\5\6\u009e\n\6\3\7\3\7\3\b\6\b")
        buf.write("\u00a3\n\b\r\b\16\b\u00a4\3\b\3\b\3\t\3\t\3\t\3\t\7\t")
        buf.write("\u00ad\n\t\f\t\16\t\u00b0\13\t\3\t\3\t\3\t\3\t\3\t\3\n")
        buf.write("\3\n\5\n\u00b9\n\n\3\n\3\n\3\n\7\n\u00be\n\n\f\n\16\n")
        buf.write("\u00c1\13\n\3\13\3\13\3\f\3\f\7\f\u00c7\n\f\f\f\16\f\u00ca")
        buf.write("\13\f\3\r\3\r\6\r\u00ce\n\r\r\r\16\r\u00cf\3\16\3\16\5")
        buf.write("\16\u00d4\n\16\3\16\6\16\u00d7\n\16\r\16\16\16\u00d8\3")
        buf.write("\17\5\17\u00dc\n\17\3\17\3\17\5\17\u00e0\n\17\3\17\3\17")
        buf.write("\5\17\u00e4\n\17\5\17\u00e6\n\17\5\17\u00e8\n\17\3\17")
        buf.write("\5\17\u00eb\n\17\3\17\3\17\5\17\u00ef\n\17\3\17\5\17\u00f2")
        buf.write("\n\17\5\17\u00f4\n\17\3\20\3\20\5\20\u00f8\n\20\3\21\3")
        buf.write("\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23\5\23\u0103\n\23")
        buf.write("\3\24\3\24\7\24\u0107\n\24\f\24\16\24\u010a\13\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!")
        buf.write("\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$")
        buf.write("\3$\3$\3$\3%\3%\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3")
        buf.write("&\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3)\3)\3)\3)\3")
        buf.write(")\3)\3)\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60")
        buf.write("\3\60\3\60\3\61\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64")
        buf.write("\3\64\3\65\3\65\3\65\3\66\3\66\3\67\3\67\3\67\38\38\3")
        buf.write("8\39\39\39\3:\3:\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\3")
        buf.write("@\3@\3A\3A\3B\3B\3C\3C\3D\3D\3E\3E\7E\u01ca\nE\fE\16E")
        buf.write("\u01cd\13E\3E\5E\u01d0\nE\3E\3E\3F\3F\7F\u01d6\nF\fF\16")
        buf.write("F\u01d9\13F\3F\3F\3F\3G\3G\3G\3G\5G\u01e2\nG\3H\3H\3H")
        buf.write("\3H\3H\3H\5H\u01ea\nH\3H\3H\3I\3I\3\u00ae\2J\3\2\5\2\7")
        buf.write("\2\t\2\13\2\r\2\17\3\21\4\23\5\25\2\27\2\31\2\33\2\35")
        buf.write("\6\37\7!\2#\2%\2\'\b)\t+\n-\13/\f\61\r\63\16\65\17\67")
        buf.write("\209\21;\22=\23?\24A\25C\26E\27G\30I\31K\32M\33O\34Q\35")
        buf.write("S\36U\37W Y![\"]#_$a%c&e\'g(i)k*m+o,q-s.u/w\60y\61{\62")
        buf.write("}\63\177\64\u0081\65\u0083\66\u0085\67\u00878\u00899\u008b")
        buf.write(":\u008d\2\u008f;\u0091<\3\2\17\3\2\62;\3\2c|\3\2C\\\5")
        buf.write("\2\13\f\16\17\"\"\4\2--//\4\2GGgg\6\2IIKKPPUU\t\2))^^")
        buf.write("ddhhppttvv\7\2\n\f\16\17$$))^^\3\2$$\5\3\n\f\16\17^^\3")
        buf.write("\2))\3\2%%\2\u01fd\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2")
        buf.write("\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2")
        buf.write("\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3")
        buf.write("\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c")
        buf.write("\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2")
        buf.write("m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2")
        buf.write("\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2")
        buf.write("\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2")
        buf.write("\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008f")
        buf.write("\3\2\2\2\2\u0091\3\2\2\2\3\u0093\3\2\2\2\5\u0095\3\2\2")
        buf.write("\2\7\u0097\3\2\2\2\t\u0099\3\2\2\2\13\u009d\3\2\2\2\r")
        buf.write("\u009f\3\2\2\2\17\u00a2\3\2\2\2\21\u00a8\3\2\2\2\23\u00b8")
        buf.write("\3\2\2\2\25\u00c2\3\2\2\2\27\u00c4\3\2\2\2\31\u00cb\3")
        buf.write("\2\2\2\33\u00d1\3\2\2\2\35\u00f3\3\2\2\2\37\u00f7\3\2")
        buf.write("\2\2!\u00f9\3\2\2\2#\u00fc\3\2\2\2%\u0102\3\2\2\2\'\u0104")
        buf.write("\3\2\2\2)\u010e\3\2\2\2+\u0114\3\2\2\2-\u011d\3\2\2\2")
        buf.write("/\u0120\3\2\2\2\61\u0125\3\2\2\2\63\u012a\3\2\2\2\65\u0130")
        buf.write("\3\2\2\2\67\u0134\3\2\2\29\u0137\3\2\2\2;\u013a\3\2\2")
        buf.write("\2=\u0143\3\2\2\2?\u0147\3\2\2\2A\u014c\3\2\2\2C\u0152")
        buf.write("\3\2\2\2E\u0157\3\2\2\2G\u015e\3\2\2\2I\u0165\3\2\2\2")
        buf.write("K\u016d\3\2\2\2M\u0174\3\2\2\2O\u0179\3\2\2\2Q\u017f\3")
        buf.write("\2\2\2S\u0188\3\2\2\2U\u018a\3\2\2\2W\u018c\3\2\2\2Y\u018e")
        buf.write("\3\2\2\2[\u0190\3\2\2\2]\u0192\3\2\2\2_\u0194\3\2\2\2")
        buf.write("a\u0197\3\2\2\2c\u019a\3\2\2\2e\u019c\3\2\2\2g\u019e\3")
        buf.write("\2\2\2i\u01a1\3\2\2\2k\u01a4\3\2\2\2m\u01a6\3\2\2\2o\u01a9")
        buf.write("\3\2\2\2q\u01ac\3\2\2\2s\u01af\3\2\2\2u\u01b3\3\2\2\2")
        buf.write("w\u01b5\3\2\2\2y\u01b7\3\2\2\2{\u01b9\3\2\2\2}\u01bb\3")
        buf.write("\2\2\2\177\u01bd\3\2\2\2\u0081\u01bf\3\2\2\2\u0083\u01c1")
        buf.write("\3\2\2\2\u0085\u01c3\3\2\2\2\u0087\u01c5\3\2\2\2\u0089")
        buf.write("\u01c7\3\2\2\2\u008b\u01d3\3\2\2\2\u008d\u01e1\3\2\2\2")
        buf.write("\u008f\u01e3\3\2\2\2\u0091\u01ed\3\2\2\2\u0093\u0094\7")
        buf.write("&\2\2\u0094\4\3\2\2\2\u0095\u0096\t\2\2\2\u0096\6\3\2")
        buf.write("\2\2\u0097\u0098\t\3\2\2\u0098\b\3\2\2\2\u0099\u009a\t")
        buf.write("\4\2\2\u009a\n\3\2\2\2\u009b\u009e\5\7\4\2\u009c\u009e")
        buf.write("\5\t\5\2\u009d\u009b\3\2\2\2\u009d\u009c\3\2\2\2\u009e")
        buf.write("\f\3\2\2\2\u009f\u00a0\7a\2\2\u00a0\16\3\2\2\2\u00a1\u00a3")
        buf.write("\t\5\2\2\u00a2\u00a1\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4")
        buf.write("\u00a2\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5\u00a6\3\2\2\2")
        buf.write("\u00a6\u00a7\b\b\2\2\u00a7\20\3\2\2\2\u00a8\u00a9\7%\2")
        buf.write("\2\u00a9\u00aa\7%\2\2\u00aa\u00ae\3\2\2\2\u00ab\u00ad")
        buf.write("\13\2\2\2\u00ac\u00ab\3\2\2\2\u00ad\u00b0\3\2\2\2\u00ae")
        buf.write("\u00af\3\2\2\2\u00ae\u00ac\3\2\2\2\u00af\u00b1\3\2\2\2")
        buf.write("\u00b0\u00ae\3\2\2\2\u00b1\u00b2\7%\2\2\u00b2\u00b3\7")
        buf.write("%\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00b5\b\t\2\2\u00b5\22")
        buf.write("\3\2\2\2\u00b6\u00b9\5\3\2\2\u00b7\u00b9\5\7\4\2\u00b8")
        buf.write("\u00b6\3\2\2\2\u00b8\u00b7\3\2\2\2\u00b9\u00bf\3\2\2\2")
        buf.write("\u00ba\u00be\5\13\6\2\u00bb\u00be\5\r\7\2\u00bc\u00be")
        buf.write("\5\5\3\2\u00bd\u00ba\3\2\2\2\u00bd\u00bb\3\2\2\2\u00bd")
        buf.write("\u00bc\3\2\2\2\u00be\u00c1\3\2\2\2\u00bf\u00bd\3\2\2\2")
        buf.write("\u00bf\u00c0\3\2\2\2\u00c0\24\3\2\2\2\u00c1\u00bf\3\2")
        buf.write("\2\2\u00c2\u00c3\t\6\2\2\u00c3\26\3\2\2\2\u00c4\u00c8")
        buf.write("\t\2\2\2\u00c5\u00c7\t\2\2\2\u00c6\u00c5\3\2\2\2\u00c7")
        buf.write("\u00ca\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c8\u00c9\3\2\2\2")
        buf.write("\u00c9\30\3\2\2\2\u00ca\u00c8\3\2\2\2\u00cb\u00cd\7\60")
        buf.write("\2\2\u00cc\u00ce\t\2\2\2\u00cd\u00cc\3\2\2\2\u00ce\u00cf")
        buf.write("\3\2\2\2\u00cf\u00cd\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0")
        buf.write("\32\3\2\2\2\u00d1\u00d3\t\7\2\2\u00d2\u00d4\t\6\2\2\u00d3")
        buf.write("\u00d2\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4\u00d6\3\2\2\2")
        buf.write("\u00d5\u00d7\t\2\2\2\u00d6\u00d5\3\2\2\2\u00d7\u00d8\3")
        buf.write("\2\2\2\u00d8\u00d6\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d9\34")
        buf.write("\3\2\2\2\u00da\u00dc\t\b\2\2\u00db\u00da\3\2\2\2\u00db")
        buf.write("\u00dc\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\u00e7\5\27\f")
        buf.write("\2\u00de\u00e0\7\60\2\2\u00df\u00de\3\2\2\2\u00df\u00e0")
        buf.write("\3\2\2\2\u00e0\u00e8\3\2\2\2\u00e1\u00e3\5\31\r\2\u00e2")
        buf.write("\u00e4\5\33\16\2\u00e3\u00e2\3\2\2\2\u00e3\u00e4\3\2\2")
        buf.write("\2\u00e4\u00e6\3\2\2\2\u00e5\u00e1\3\2\2\2\u00e5\u00e6")
        buf.write("\3\2\2\2\u00e6\u00e8\3\2\2\2\u00e7\u00df\3\2\2\2\u00e7")
        buf.write("\u00e5\3\2\2\2\u00e8\u00f4\3\2\2\2\u00e9\u00eb\t\b\2\2")
        buf.write("\u00ea\u00e9\3\2\2\2\u00ea\u00eb\3\2\2\2\u00eb\u00ec\3")
        buf.write("\2\2\2\u00ec\u00ee\5\27\f\2\u00ed\u00ef\7\60\2\2\u00ee")
        buf.write("\u00ed\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\u00f1\3\2\2\2")
        buf.write("\u00f0\u00f2\5\33\16\2\u00f1\u00f0\3\2\2\2\u00f1\u00f2")
        buf.write("\3\2\2\2\u00f2\u00f4\3\2\2\2\u00f3\u00db\3\2\2\2\u00f3")
        buf.write("\u00ea\3\2\2\2\u00f4\36\3\2\2\2\u00f5\u00f8\5? \2\u00f6")
        buf.write("\u00f8\5A!\2\u00f7\u00f5\3\2\2\2\u00f7\u00f6\3\2\2\2\u00f8")
        buf.write(" \3\2\2\2\u00f9\u00fa\7^\2\2\u00fa\u00fb\t\t\2\2\u00fb")
        buf.write("\"\3\2\2\2\u00fc\u00fd\7)\2\2\u00fd\u00fe\7$\2\2\u00fe")
        buf.write("$\3\2\2\2\u00ff\u0103\n\n\2\2\u0100\u0103\5!\21\2\u0101")
        buf.write("\u0103\5#\22\2\u0102\u00ff\3\2\2\2\u0102\u0100\3\2\2\2")
        buf.write("\u0102\u0101\3\2\2\2\u0103&\3\2\2\2\u0104\u0108\t\13\2")
        buf.write("\2\u0105\u0107\5%\23\2\u0106\u0105\3\2\2\2\u0107\u010a")
        buf.write("\3\2\2\2\u0108\u0106\3\2\2\2\u0108\u0109\3\2\2\2\u0109")
        buf.write("\u010b\3\2\2\2\u010a\u0108\3\2\2\2\u010b\u010c\t\13\2")
        buf.write("\2\u010c\u010d\b\24\3\2\u010d(\3\2\2\2\u010e\u010f\7D")
        buf.write("\2\2\u010f\u0110\7t\2\2\u0110\u0111\7g\2\2\u0111\u0112")
        buf.write("\7c\2\2\u0112\u0113\7m\2\2\u0113*\3\2\2\2\u0114\u0115")
        buf.write("\7E\2\2\u0115\u0116\7q\2\2\u0116\u0117\7p\2\2\u0117\u0118")
        buf.write("\7v\2\2\u0118\u0119\7k\2\2\u0119\u011a\7p\2\2\u011a\u011b")
        buf.write("\7w\2\2\u011b\u011c\7g\2\2\u011c,\3\2\2\2\u011d\u011e")
        buf.write("\7K\2\2\u011e\u011f\7h\2\2\u011f.\3\2\2\2\u0120\u0121")
        buf.write("\7G\2\2\u0121\u0122\7n\2\2\u0122\u0123\7k\2\2\u0123\u0124")
        buf.write("\7h\2\2\u0124\60\3\2\2\2\u0125\u0126\7G\2\2\u0126\u0127")
        buf.write("\7n\2\2\u0127\u0128\7u\2\2\u0128\u0129\7g\2\2\u0129\62")
        buf.write("\3\2\2\2\u012a\u012b\7Y\2\2\u012b\u012c\7j\2\2\u012c\u012d")
        buf.write("\7k\2\2\u012d\u012e\7n\2\2\u012e\u012f\7g\2\2\u012f\64")
        buf.write("\3\2\2\2\u0130\u0131\7H\2\2\u0131\u0132\7q\2\2\u0132\u0133")
        buf.write("\7t\2\2\u0133\66\3\2\2\2\u0134\u0135\7Q\2\2\u0135\u0136")
        buf.write("\7h\2\2\u01368\3\2\2\2\u0137\u0138\7K\2\2\u0138\u0139")
        buf.write("\7p\2\2\u0139:\3\2\2\2\u013a\u013b\7H\2\2\u013b\u013c")
        buf.write("\7w\2\2\u013c\u013d\7p\2\2\u013d\u013e\7e\2\2\u013e\u013f")
        buf.write("\7v\2\2\u013f\u0140\7k\2\2\u0140\u0141\7q\2\2\u0141\u0142")
        buf.write("\7p\2\2\u0142<\3\2\2\2\u0143\u0144\7N\2\2\u0144\u0145")
        buf.write("\7g\2\2\u0145\u0146\7v\2\2\u0146>\3\2\2\2\u0147\u0148")
        buf.write("\7V\2\2\u0148\u0149\7t\2\2\u0149\u014a\7w\2\2\u014a\u014b")
        buf.write("\7g\2\2\u014b@\3\2\2\2\u014c\u014d\7H\2\2\u014d\u014e")
        buf.write("\7c\2\2\u014e\u014f\7n\2\2\u014f\u0150\7u\2\2\u0150\u0151")
        buf.write("\7g\2\2\u0151B\3\2\2\2\u0152\u0153\7E\2\2\u0153\u0154")
        buf.write("\7c\2\2\u0154\u0155\7n\2\2\u0155\u0156\7n\2\2\u0156D\3")
        buf.write("\2\2\2\u0157\u0158\7T\2\2\u0158\u0159\7g\2\2\u0159\u015a")
        buf.write("\7v\2\2\u015a\u015b\7w\2\2\u015b\u015c\7t\2\2\u015c\u015d")
        buf.write("\7p\2\2\u015dF\3\2\2\2\u015e\u015f\7P\2\2\u015f\u0160")
        buf.write("\7w\2\2\u0160\u0161\7o\2\2\u0161\u0162\7d\2\2\u0162\u0163")
        buf.write("\7g\2\2\u0163\u0164\7t\2\2\u0164H\3\2\2\2\u0165\u0166")
        buf.write("\7D\2\2\u0166\u0167\7q\2\2\u0167\u0168\7q\2\2\u0168\u0169")
        buf.write("\7n\2\2\u0169\u016a\7g\2\2\u016a\u016b\7c\2\2\u016b\u016c")
        buf.write("\7p\2\2\u016cJ\3\2\2\2\u016d\u016e\7U\2\2\u016e\u016f")
        buf.write("\7v\2\2\u016f\u0170\7t\2\2\u0170\u0171\7k\2\2\u0171\u0172")
        buf.write("\7p\2\2\u0172\u0173\7i\2\2\u0173L\3\2\2\2\u0174\u0175")
        buf.write("\7L\2\2\u0175\u0176\7U\2\2\u0176\u0177\7Q\2\2\u0177\u0178")
        buf.write("\7P\2\2\u0178N\3\2\2\2\u0179\u017a\7C\2\2\u017a\u017b")
        buf.write("\7t\2\2\u017b\u017c\7t\2\2\u017c\u017d\7c\2\2\u017d\u017e")
        buf.write("\7{\2\2\u017eP\3\2\2\2\u017f\u0180\7E\2\2\u0180\u0181")
        buf.write("\7q\2\2\u0181\u0182\7p\2\2\u0182\u0183\7u\2\2\u0183\u0184")
        buf.write("\7v\2\2\u0184\u0185\7c\2\2\u0185\u0186\7p\2\2\u0186\u0187")
        buf.write("\7v\2\2\u0187R\3\2\2\2\u0188\u0189\7-\2\2\u0189T\3\2\2")
        buf.write("\2\u018a\u018b\7/\2\2\u018bV\3\2\2\2\u018c\u018d\7\61")
        buf.write("\2\2\u018dX\3\2\2\2\u018e\u018f\7\'\2\2\u018fZ\3\2\2\2")
        buf.write("\u0190\u0191\7,\2\2\u0191\\\3\2\2\2\u0192\u0193\7?\2\2")
        buf.write("\u0193^\3\2\2\2\u0194\u0195\7?\2\2\u0195\u0196\7?\2\2")
        buf.write("\u0196`\3\2\2\2\u0197\u0198\7#\2\2\u0198\u0199\7?\2\2")
        buf.write("\u0199b\3\2\2\2\u019a\u019b\7>\2\2\u019bd\3\2\2\2\u019c")
        buf.write("\u019d\7@\2\2\u019df\3\2\2\2\u019e\u019f\7>\2\2\u019f")
        buf.write("\u01a0\7?\2\2\u01a0h\3\2\2\2\u01a1\u01a2\7@\2\2\u01a2")
        buf.write("\u01a3\7?\2\2\u01a3j\3\2\2\2\u01a4\u01a5\7#\2\2\u01a5")
        buf.write("l\3\2\2\2\u01a6\u01a7\7(\2\2\u01a7\u01a8\7(\2\2\u01a8")
        buf.write("n\3\2\2\2\u01a9\u01aa\7~\2\2\u01aa\u01ab\7~\2\2\u01ab")
        buf.write("p\3\2\2\2\u01ac\u01ad\7-\2\2\u01ad\u01ae\7\60\2\2\u01ae")
        buf.write("r\3\2\2\2\u01af\u01b0\7?\2\2\u01b0\u01b1\7?\2\2\u01b1")
        buf.write("\u01b2\7\60\2\2\u01b2t\3\2\2\2\u01b3\u01b4\7*\2\2\u01b4")
        buf.write("v\3\2\2\2\u01b5\u01b6\7+\2\2\u01b6x\3\2\2\2\u01b7\u01b8")
        buf.write("\7}\2\2\u01b8z\3\2\2\2\u01b9\u01ba\7\177\2\2\u01ba|\3")
        buf.write("\2\2\2\u01bb\u01bc\7]\2\2\u01bc~\3\2\2\2\u01bd\u01be\7")
        buf.write("_\2\2\u01be\u0080\3\2\2\2\u01bf\u01c0\7=\2\2\u01c0\u0082")
        buf.write("\3\2\2\2\u01c1\u01c2\7.\2\2\u01c2\u0084\3\2\2\2\u01c3")
        buf.write("\u01c4\7<\2\2\u01c4\u0086\3\2\2\2\u01c5\u01c6\7\60\2\2")
        buf.write("\u01c6\u0088\3\2\2\2\u01c7\u01cb\7$\2\2\u01c8\u01ca\5")
        buf.write("%\23\2\u01c9\u01c8\3\2\2\2\u01ca\u01cd\3\2\2\2\u01cb\u01c9")
        buf.write("\3\2\2\2\u01cb\u01cc\3\2\2\2\u01cc\u01cf\3\2\2\2\u01cd")
        buf.write("\u01cb\3\2\2\2\u01ce\u01d0\t\f\2\2\u01cf\u01ce\3\2\2\2")
        buf.write("\u01d0\u01d1\3\2\2\2\u01d1\u01d2\bE\4\2\u01d2\u008a\3")
        buf.write("\2\2\2\u01d3\u01d7\7$\2\2\u01d4\u01d6\5%\23\2\u01d5\u01d4")
        buf.write("\3\2\2\2\u01d6\u01d9\3\2\2\2\u01d7\u01d5\3\2\2\2\u01d7")
        buf.write("\u01d8\3\2\2\2\u01d8\u01da\3\2\2\2\u01d9\u01d7\3\2\2\2")
        buf.write("\u01da\u01db\5\u008dG\2\u01db\u01dc\bF\5\2\u01dc\u008c")
        buf.write("\3\2\2\2\u01dd\u01de\7^\2\2\u01de\u01e2\n\t\2\2\u01df")
        buf.write("\u01e0\t\r\2\2\u01e0\u01e2\n\13\2\2\u01e1\u01dd\3\2\2")
        buf.write("\2\u01e1\u01df\3\2\2\2\u01e2\u008e\3\2\2\2\u01e3\u01e4")
        buf.write("\7%\2\2\u01e4\u01e5\7%\2\2\u01e5\u01e9\3\2\2\2\u01e6\u01ea")
        buf.write("\n\16\2\2\u01e7\u01e8\7%\2\2\u01e8\u01ea\n\16\2\2\u01e9")
        buf.write("\u01e6\3\2\2\2\u01e9\u01e7\3\2\2\2\u01e9\u01ea\3\2\2\2")
        buf.write("\u01ea\u01eb\3\2\2\2\u01eb\u01ec\bH\6\2\u01ec\u0090\3")
        buf.write("\2\2\2\u01ed\u01ee\13\2\2\2\u01ee\u0092\3\2\2\2\36\2\u009d")
        buf.write("\u00a4\u00ae\u00b8\u00bd\u00bf\u00c8\u00cf\u00d3\u00d8")
        buf.write("\u00db\u00df\u00e3\u00e5\u00e7\u00ea\u00ee\u00f1\u00f3")
        buf.write("\u00f7\u0102\u0108\u01cb\u01cf\u01d7\u01e1\u01e9\7\b\2")
        buf.write("\2\3\24\2\3E\3\3F\4\3H\5")
        return buf.getvalue()


class CSELLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    WS = 1
    COMMENT = 2
    ID = 3
    NUMBER_LITERAL = 4
    BOOLEAN_LITERAL = 5
    STRING_LITERAL = 6
    BREAK = 7
    CONTINUE = 8
    IF = 9
    ELIF = 10
    ELSE = 11
    WHILE = 12
    FOR = 13
    OF = 14
    IN = 15
    FUNCTION = 16
    LET = 17
    TRUE = 18
    FALSE = 19
    CALL = 20
    RETURN = 21
    NUMBER = 22
    BOOLEAN = 23
    STRING = 24
    JSON = 25
    ARRAY = 26
    CONSTANT = 27
    ADD = 28
    SUB = 29
    DIV = 30
    MOD = 31
    MUL = 32
    ASSIGN = 33
    EQ = 34
    NOT_EQ = 35
    LESS_T = 36
    GREAT_T = 37
    LESS_E = 38
    GREAT_E = 39
    NOT = 40
    AND = 41
    OR = 42
    ADD_STR = 43
    COMPARE_STR = 44
    LP = 45
    RP = 46
    LCB = 47
    RCB = 48
    LSB = 49
    RSB = 50
    SM = 51
    CM = 52
    CL = 53
    DOT = 54
    UNCLOSE_STRING = 55
    ILLEGAL_ESCAPE = 56
    UNTERMINATED_COMMENT = 57
    ERROR_CHAR = 58

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Break'", "'Continue'", "'If'", "'Elif'", "'Else'", "'While'", 
            "'For'", "'Of'", "'In'", "'Function'", "'Let'", "'True'", "'False'", 
            "'Call'", "'Return'", "'Number'", "'Boolean'", "'String'", "'JSON'", 
            "'Array'", "'Constant'", "'+'", "'-'", "'/'", "'%'", "'*'", 
            "'='", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'!'", 
            "'&&'", "'||'", "'+.'", "'==.'", "'('", "')'", "'{'", "'}'", 
            "'['", "']'", "';'", "','", "':'", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "COMMENT", "ID", "NUMBER_LITERAL", "BOOLEAN_LITERAL", 
            "STRING_LITERAL", "BREAK", "CONTINUE", "IF", "ELIF", "ELSE", 
            "WHILE", "FOR", "OF", "IN", "FUNCTION", "LET", "TRUE", "FALSE", 
            "CALL", "RETURN", "NUMBER", "BOOLEAN", "STRING", "JSON", "ARRAY", 
            "CONSTANT", "ADD", "SUB", "DIV", "MOD", "MUL", "ASSIGN", "EQ", 
            "NOT_EQ", "LESS_T", "GREAT_T", "LESS_E", "GREAT_E", "NOT", "AND", 
            "OR", "ADD_STR", "COMPARE_STR", "LP", "RP", "LCB", "RCB", "LSB", 
            "RSB", "SM", "CM", "CL", "DOT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "UNTERMINATED_COMMENT", "ERROR_CHAR" ]

    ruleNames = [ "DOLLAR", "DIGIT", "LOWCASE", "UPCASE", "LETTER", "UNDERSCORE", 
                  "WS", "COMMENT", "ID", "SIGN", "INT_PART", "DEC_PART", 
                  "EXPONENT_PART", "NUMBER_LITERAL", "BOOLEAN_LITERAL", 
                  "ESC", "DOUBLE_QUOTE", "CHARACTER", "STRING_LITERAL", 
                  "BREAK", "CONTINUE", "IF", "ELIF", "ELSE", "WHILE", "FOR", 
                  "OF", "IN", "FUNCTION", "LET", "TRUE", "FALSE", "CALL", 
                  "RETURN", "NUMBER", "BOOLEAN", "STRING", "JSON", "ARRAY", 
                  "CONSTANT", "ADD", "SUB", "DIV", "MOD", "MUL", "ASSIGN", 
                  "EQ", "NOT_EQ", "LESS_T", "GREAT_T", "LESS_E", "GREAT_E", 
                  "NOT", "AND", "OR", "ADD_STR", "COMPARE_STR", "LP", "RP", 
                  "LCB", "RCB", "LSB", "RSB", "SM", "CM", "CL", "DOT", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "ESC_ILLEGAL", "UNTERMINATED_COMMENT", 
                  "ERROR_CHAR" ]

    grammarFileName = "CSEL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:       
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        else:
            return result;


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[18] = self.STRING_LITERAL_action 
            actions[67] = self.UNCLOSE_STRING_action 
            actions[68] = self.ILLEGAL_ESCAPE_action 
            actions[70] = self.UNTERMINATED_COMMENT_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                temp = str(self.text)
                self.text = temp[1:-1]

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                legalescape = ['\b', '\t', '\n', '\f', '\r', '\\', "\'"]
                tempstr = str(self.text)
                if tempstr[-1] in legalescape:
                    raise UncloseString(tempstr[1:-1])
                else :
                    raise UncloseString(tempstr[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            		y = str(self.text)
            		raise IllegalEscape(y[1:])
            	
     

    def UNTERMINATED_COMMENT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            		raise UnterminatedComment()
            	
     


