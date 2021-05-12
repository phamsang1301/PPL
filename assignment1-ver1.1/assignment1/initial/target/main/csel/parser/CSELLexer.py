# Generated from main/csel/parser/CSEL.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2?")
        buf.write("\u01f5\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\3\2\3\2\5\2\u008c\n\2\3\2\7\2\u008f\n\2\f\2\16")
        buf.write("\2\u0092\13\2\3\3\3\3\7\3\u0096\n\3\f\3\16\3\u0099\13")
        buf.write("\3\3\4\3\4\5\4\u009d\n\4\3\4\7\4\u00a0\n\4\f\4\16\4\u00a3")
        buf.write("\13\4\3\5\3\5\5\5\u00a7\n\5\3\5\7\5\u00aa\n\5\f\5\16\5")
        buf.write("\u00ad\13\5\3\5\6\5\u00b0\n\5\r\5\16\5\u00b1\3\5\5\5\u00b5")
        buf.write("\n\5\3\5\3\5\7\5\u00b9\n\5\f\5\16\5\u00bc\13\5\3\5\7\5")
        buf.write("\u00bf\n\5\f\5\16\5\u00c2\13\5\3\5\3\5\6\5\u00c6\n\5\r")
        buf.write("\5\16\5\u00c7\3\5\5\5\u00cb\n\5\3\5\6\5\u00ce\n\5\r\5")
        buf.write("\16\5\u00cf\3\5\3\5\5\5\u00d4\n\5\3\6\3\6\3\6\3\6\7\6")
        buf.write("\u00da\n\6\f\6\16\6\u00dd\13\6\3\6\3\6\3\6\3\6\3\6\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\34\3\34\5\34\u0160\n\34\3")
        buf.write("\34\6\34\u0163\n\34\r\34\16\34\u0164\3\35\3\35\3\36\3")
        buf.write("\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3$\3%\3")
        buf.write("%\3%\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3*\3*\3+\3+\3+\3")
        buf.write(",\3,\3,\3-\3-\3-\3-\3.\3.\3.\3/\3/\3\60\3\60\3\61\3\61")
        buf.write("\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67")
        buf.write("\3\67\38\38\39\39\3:\6:\u01ab\n:\r:\16:\u01ac\3:\3:\3")
        buf.write(";\3;\3<\3<\3=\3=\3>\3>\3>\3>\3>\3>\7>\u01bd\n>\f>\16>")
        buf.write("\u01c0\13>\3>\3>\3>\3?\3?\3?\3?\3?\3?\7?\u01cb\n?\f?\16")
        buf.write("?\u01ce\13?\3?\5?\u01d1\n?\3?\3?\3@\3@\3@\3@\3@\3@\7@")
        buf.write("\u01db\n@\f@\16@\u01de\13@\3@\3@\3@\3A\3A\3A\3A\5A\u01e7")
        buf.write("\nA\3B\3B\5B\u01eb\nB\3C\3C\7C\u01ef\nC\fC\16C\u01f2\13")
        buf.write("C\3D\3D\3\u00db\2E\3\3\5\4\7\2\t\5\13\6\r\7\17\b\21\t")
        buf.write("\23\n\25\13\27\f\31\r\33\16\35\17\37\20!\21#\22%\23\'")
        buf.write("\24)\25+\26-\27/\30\61\31\63\32\65\33\67\29\34;\35=\36")
        buf.write("?\37A C!E\"G#I$K%M&O\'Q(S)U*W+Y,[-]._/a\60c\61e\62g\63")
        buf.write("i\64k\65m\66o\67q8s9u\2w\2y\2{:};\177<\u0081\2\u0083=")
        buf.write("\u0085>\u0087?\3\2\16\3\2c|\6\2\62;C\\aac|\4\2GGgg\4\2")
        buf.write("--//\5\2\13\f\17\17\"\"\3\2\62;\3\2\63;\3\2$$\7\2\n\f")
        buf.write("\16\17$$))^^\t\2))^^ddhhppttvv\5\3\n\f\16\17^^\3\2))\2")
        buf.write("\u0210\2\3\3\2\2\2\2\5\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write("\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2")
        buf.write("\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2")
        buf.write("\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2")
        buf.write("\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3")
        buf.write("\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\29\3\2\2")
        buf.write("\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2")
        buf.write("\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3")
        buf.write("\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W")
        buf.write("\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2")
        buf.write("a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2")
        buf.write("\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2")
        buf.write("\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0083\3\2\2\2")
        buf.write("\2\u0085\3\2\2\2\2\u0087\3\2\2\2\3\u008b\3\2\2\2\5\u0093")
        buf.write("\3\2\2\2\7\u009c\3\2\2\2\t\u00d3\3\2\2\2\13\u00d5\3\2")
        buf.write("\2\2\r\u00e3\3\2\2\2\17\u00e9\3\2\2\2\21\u00f2\3\2\2\2")
        buf.write("\23\u00f5\3\2\2\2\25\u00fa\3\2\2\2\27\u00ff\3\2\2\2\31")
        buf.write("\u0105\3\2\2\2\33\u0109\3\2\2\2\35\u010c\3\2\2\2\37\u010f")
        buf.write("\3\2\2\2!\u0118\3\2\2\2#\u011c\3\2\2\2%\u0121\3\2\2\2")
        buf.write("\'\u0127\3\2\2\2)\u012c\3\2\2\2+\u0133\3\2\2\2-\u013a")
        buf.write("\3\2\2\2/\u0142\3\2\2\2\61\u0149\3\2\2\2\63\u014e\3\2")
        buf.write("\2\2\65\u0154\3\2\2\2\67\u015d\3\2\2\29\u0166\3\2\2\2")
        buf.write(";\u0168\3\2\2\2=\u016a\3\2\2\2?\u016c\3\2\2\2A\u016e\3")
        buf.write("\2\2\2C\u0170\3\2\2\2E\u0172\3\2\2\2G\u0174\3\2\2\2I\u0177")
        buf.write("\3\2\2\2K\u017a\3\2\2\2M\u017c\3\2\2\2O\u017f\3\2\2\2")
        buf.write("Q\u0182\3\2\2\2S\u0184\3\2\2\2U\u0186\3\2\2\2W\u0189\3")
        buf.write("\2\2\2Y\u018c\3\2\2\2[\u0190\3\2\2\2]\u0193\3\2\2\2_\u0195")
        buf.write("\3\2\2\2a\u0197\3\2\2\2c\u0199\3\2\2\2e\u019b\3\2\2\2")
        buf.write("g\u019d\3\2\2\2i\u019f\3\2\2\2k\u01a1\3\2\2\2m\u01a3\3")
        buf.write("\2\2\2o\u01a5\3\2\2\2q\u01a7\3\2\2\2s\u01aa\3\2\2\2u\u01b0")
        buf.write("\3\2\2\2w\u01b2\3\2\2\2y\u01b4\3\2\2\2{\u01b6\3\2\2\2")
        buf.write("}\u01c4\3\2\2\2\177\u01d4\3\2\2\2\u0081\u01e6\3\2\2\2")
        buf.write("\u0083\u01e8\3\2\2\2\u0085\u01ec\3\2\2\2\u0087\u01f3\3")
        buf.write("\2\2\2\u0089\u008c\5q9\2\u008a\u008c\t\2\2\2\u008b\u0089")
        buf.write("\3\2\2\2\u008b\u008a\3\2\2\2\u008c\u0090\3\2\2\2\u008d")
        buf.write("\u008f\t\3\2\2\u008e\u008d\3\2\2\2\u008f\u0092\3\2\2\2")
        buf.write("\u0090\u008e\3\2\2\2\u0090\u0091\3\2\2\2\u0091\4\3\2\2")
        buf.write("\2\u0092\u0090\3\2\2\2\u0093\u0097\t\2\2\2\u0094\u0096")
        buf.write("\t\3\2\2\u0095\u0094\3\2\2\2\u0096\u0099\3\2\2\2\u0097")
        buf.write("\u0095\3\2\2\2\u0097\u0098\3\2\2\2\u0098\6\3\2\2\2\u0099")
        buf.write("\u0097\3\2\2\2\u009a\u009d\7\62\2\2\u009b\u009d\5w<\2")
        buf.write("\u009c\u009a\3\2\2\2\u009c\u009b\3\2\2\2\u009d\u00a1\3")
        buf.write("\2\2\2\u009e\u00a0\5u;\2\u009f\u009e\3\2\2\2\u00a0\u00a3")
        buf.write("\3\2\2\2\u00a1\u009f\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2")
        buf.write("\b\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a4\u00a7\7\62\2\2\u00a5")
        buf.write("\u00a7\5w<\2\u00a6\u00a4\3\2\2\2\u00a6\u00a5\3\2\2\2\u00a7")
        buf.write("\u00ab\3\2\2\2\u00a8\u00aa\5u;\2\u00a9\u00a8\3\2\2\2\u00aa")
        buf.write("\u00ad\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ab\u00ac\3\2\2\2")
        buf.write("\u00ac\u00d4\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ae\u00b0\5")
        buf.write("\7\4\2\u00af\u00ae\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00af")
        buf.write("\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b4\3\2\2\2\u00b3")
        buf.write("\u00b5\5k\66\2\u00b4\u00b3\3\2\2\2\u00b4\u00b5\3\2\2\2")
        buf.write("\u00b5\u00ba\3\2\2\2\u00b6\u00b9\5u;\2\u00b7\u00b9\5\67")
        buf.write("\34\2\u00b8\u00b6\3\2\2\2\u00b8\u00b7\3\2\2\2\u00b9\u00bc")
        buf.write("\3\2\2\2\u00ba\u00b8\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb")
        buf.write("\u00d4\3\2\2\2\u00bc\u00ba\3\2\2\2\u00bd\u00bf\5\7\4\2")
        buf.write("\u00be\u00bd\3\2\2\2\u00bf\u00c2\3\2\2\2\u00c0\u00be\3")
        buf.write("\2\2\2\u00c0\u00c1\3\2\2\2\u00c1\u00c3\3\2\2\2\u00c2\u00c0")
        buf.write("\3\2\2\2\u00c3\u00c5\5k\66\2\u00c4\u00c6\5u;\2\u00c5\u00c4")
        buf.write("\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c7")
        buf.write("\u00c8\3\2\2\2\u00c8\u00ca\3\2\2\2\u00c9\u00cb\5\67\34")
        buf.write("\2\u00ca\u00c9\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb\u00d4")
        buf.write("\3\2\2\2\u00cc\u00ce\5\7\4\2\u00cd\u00cc\3\2\2\2\u00ce")
        buf.write("\u00cf\3\2\2\2\u00cf\u00cd\3\2\2\2\u00cf\u00d0\3\2\2\2")
        buf.write("\u00d0\u00d1\3\2\2\2\u00d1\u00d2\5\67\34\2\u00d2\u00d4")
        buf.write("\3\2\2\2\u00d3\u00a6\3\2\2\2\u00d3\u00af\3\2\2\2\u00d3")
        buf.write("\u00c0\3\2\2\2\u00d3\u00cd\3\2\2\2\u00d4\n\3\2\2\2\u00d5")
        buf.write("\u00d6\7%\2\2\u00d6\u00d7\7%\2\2\u00d7\u00db\3\2\2\2\u00d8")
        buf.write("\u00da\13\2\2\2\u00d9\u00d8\3\2\2\2\u00da\u00dd\3\2\2")
        buf.write("\2\u00db\u00dc\3\2\2\2\u00db\u00d9\3\2\2\2\u00dc\u00de")
        buf.write("\3\2\2\2\u00dd\u00db\3\2\2\2\u00de\u00df\7%\2\2\u00df")
        buf.write("\u00e0\7%\2\2\u00e0\u00e1\3\2\2\2\u00e1\u00e2\b\6\2\2")
        buf.write("\u00e2\f\3\2\2\2\u00e3\u00e4\7D\2\2\u00e4\u00e5\7t\2\2")
        buf.write("\u00e5\u00e6\7g\2\2\u00e6\u00e7\7c\2\2\u00e7\u00e8\7m")
        buf.write("\2\2\u00e8\16\3\2\2\2\u00e9\u00ea\7E\2\2\u00ea\u00eb\7")
        buf.write("q\2\2\u00eb\u00ec\7p\2\2\u00ec\u00ed\7v\2\2\u00ed\u00ee")
        buf.write("\7k\2\2\u00ee\u00ef\7p\2\2\u00ef\u00f0\7w\2\2\u00f0\u00f1")
        buf.write("\7g\2\2\u00f1\20\3\2\2\2\u00f2\u00f3\7K\2\2\u00f3\u00f4")
        buf.write("\7h\2\2\u00f4\22\3\2\2\2\u00f5\u00f6\7G\2\2\u00f6\u00f7")
        buf.write("\7n\2\2\u00f7\u00f8\7k\2\2\u00f8\u00f9\7h\2\2\u00f9\24")
        buf.write("\3\2\2\2\u00fa\u00fb\7G\2\2\u00fb\u00fc\7n\2\2\u00fc\u00fd")
        buf.write("\7u\2\2\u00fd\u00fe\7g\2\2\u00fe\26\3\2\2\2\u00ff\u0100")
        buf.write("\7Y\2\2\u0100\u0101\7j\2\2\u0101\u0102\7k\2\2\u0102\u0103")
        buf.write("\7n\2\2\u0103\u0104\7g\2\2\u0104\30\3\2\2\2\u0105\u0106")
        buf.write("\7H\2\2\u0106\u0107\7q\2\2\u0107\u0108\7t\2\2\u0108\32")
        buf.write("\3\2\2\2\u0109\u010a\7Q\2\2\u010a\u010b\7h\2\2\u010b\34")
        buf.write("\3\2\2\2\u010c\u010d\7K\2\2\u010d\u010e\7p\2\2\u010e\36")
        buf.write("\3\2\2\2\u010f\u0110\7H\2\2\u0110\u0111\7w\2\2\u0111\u0112")
        buf.write("\7p\2\2\u0112\u0113\7e\2\2\u0113\u0114\7v\2\2\u0114\u0115")
        buf.write("\7k\2\2\u0115\u0116\7q\2\2\u0116\u0117\7p\2\2\u0117 \3")
        buf.write("\2\2\2\u0118\u0119\7N\2\2\u0119\u011a\7g\2\2\u011a\u011b")
        buf.write("\7v\2\2\u011b\"\3\2\2\2\u011c\u011d\7V\2\2\u011d\u011e")
        buf.write("\7t\2\2\u011e\u011f\7w\2\2\u011f\u0120\7g\2\2\u0120$\3")
        buf.write("\2\2\2\u0121\u0122\7H\2\2\u0122\u0123\7c\2\2\u0123\u0124")
        buf.write("\7n\2\2\u0124\u0125\7u\2\2\u0125\u0126\7g\2\2\u0126&\3")
        buf.write("\2\2\2\u0127\u0128\7E\2\2\u0128\u0129\7c\2\2\u0129\u012a")
        buf.write("\7n\2\2\u012a\u012b\7n\2\2\u012b(\3\2\2\2\u012c\u012d")
        buf.write("\7T\2\2\u012d\u012e\7g\2\2\u012e\u012f\7v\2\2\u012f\u0130")
        buf.write("\7w\2\2\u0130\u0131\7t\2\2\u0131\u0132\7p\2\2\u0132*\3")
        buf.write("\2\2\2\u0133\u0134\7P\2\2\u0134\u0135\7w\2\2\u0135\u0136")
        buf.write("\7o\2\2\u0136\u0137\7d\2\2\u0137\u0138\7g\2\2\u0138\u0139")
        buf.write("\7t\2\2\u0139,\3\2\2\2\u013a\u013b\7D\2\2\u013b\u013c")
        buf.write("\7q\2\2\u013c\u013d\7q\2\2\u013d\u013e\7n\2\2\u013e\u013f")
        buf.write("\7g\2\2\u013f\u0140\7c\2\2\u0140\u0141\7p\2\2\u0141.\3")
        buf.write("\2\2\2\u0142\u0143\7U\2\2\u0143\u0144\7v\2\2\u0144\u0145")
        buf.write("\7t\2\2\u0145\u0146\7k\2\2\u0146\u0147\7p\2\2\u0147\u0148")
        buf.write("\7i\2\2\u0148\60\3\2\2\2\u0149\u014a\7L\2\2\u014a\u014b")
        buf.write("\7u\2\2\u014b\u014c\7q\2\2\u014c\u014d\7p\2\2\u014d\62")
        buf.write("\3\2\2\2\u014e\u014f\7C\2\2\u014f\u0150\7t\2\2\u0150\u0151")
        buf.write("\7t\2\2\u0151\u0152\7c\2\2\u0152\u0153\7{\2\2\u0153\64")
        buf.write("\3\2\2\2\u0154\u0155\7E\2\2\u0155\u0156\7q\2\2\u0156\u0157")
        buf.write("\7p\2\2\u0157\u0158\7u\2\2\u0158\u0159\7v\2\2\u0159\u015a")
        buf.write("\7c\2\2\u015a\u015b\7p\2\2\u015b\u015c\7v\2\2\u015c\66")
        buf.write("\3\2\2\2\u015d\u015f\t\4\2\2\u015e\u0160\t\5\2\2\u015f")
        buf.write("\u015e\3\2\2\2\u015f\u0160\3\2\2\2\u0160\u0162\3\2\2\2")
        buf.write("\u0161\u0163\5u;\2\u0162\u0161\3\2\2\2\u0163\u0164\3\2")
        buf.write("\2\2\u0164\u0162\3\2\2\2\u0164\u0165\3\2\2\2\u01658\3")
        buf.write("\2\2\2\u0166\u0167\7-\2\2\u0167:\3\2\2\2\u0168\u0169\7")
        buf.write("/\2\2\u0169<\3\2\2\2\u016a\u016b\7,\2\2\u016b>\3\2\2\2")
        buf.write("\u016c\u016d\7\61\2\2\u016d@\3\2\2\2\u016e\u016f\7\'\2")
        buf.write("\2\u016fB\3\2\2\2\u0170\u0171\7#\2\2\u0171D\3\2\2\2\u0172")
        buf.write("\u0173\7(\2\2\u0173F\3\2\2\2\u0174\u0175\7(\2\2\u0175")
        buf.write("\u0176\7(\2\2\u0176H\3\2\2\2\u0177\u0178\7~\2\2\u0178")
        buf.write("\u0179\7~\2\2\u0179J\3\2\2\2\u017a\u017b\7?\2\2\u017b")
        buf.write("L\3\2\2\2\u017c\u017d\7?\2\2\u017d\u017e\7?\2\2\u017e")
        buf.write("N\3\2\2\2\u017f\u0180\7#\2\2\u0180\u0181\7?\2\2\u0181")
        buf.write("P\3\2\2\2\u0182\u0183\7@\2\2\u0183R\3\2\2\2\u0184\u0185")
        buf.write("\7>\2\2\u0185T\3\2\2\2\u0186\u0187\7@\2\2\u0187\u0188")
        buf.write("\7?\2\2\u0188V\3\2\2\2\u0189\u018a\7>\2\2\u018a\u018b")
        buf.write("\7?\2\2\u018bX\3\2\2\2\u018c\u018d\7?\2\2\u018d\u018e")
        buf.write("\7?\2\2\u018e\u018f\7\60\2\2\u018fZ\3\2\2\2\u0190\u0191")
        buf.write("\7-\2\2\u0191\u0192\7\60\2\2\u0192\\\3\2\2\2\u0193\u0194")
        buf.write("\7+\2\2\u0194^\3\2\2\2\u0195\u0196\7*\2\2\u0196`\3\2\2")
        buf.write("\2\u0197\u0198\7_\2\2\u0198b\3\2\2\2\u0199\u019a\7]\2")
        buf.write("\2\u019ad\3\2\2\2\u019b\u019c\7}\2\2\u019cf\3\2\2\2\u019d")
        buf.write("\u019e\7\177\2\2\u019eh\3\2\2\2\u019f\u01a0\7=\2\2\u01a0")
        buf.write("j\3\2\2\2\u01a1\u01a2\7\60\2\2\u01a2l\3\2\2\2\u01a3\u01a4")
        buf.write("\7<\2\2\u01a4n\3\2\2\2\u01a5\u01a6\7.\2\2\u01a6p\3\2\2")
        buf.write("\2\u01a7\u01a8\7&\2\2\u01a8r\3\2\2\2\u01a9\u01ab\t\6\2")
        buf.write("\2\u01aa\u01a9\3\2\2\2\u01ab\u01ac\3\2\2\2\u01ac\u01aa")
        buf.write("\3\2\2\2\u01ac\u01ad\3\2\2\2\u01ad\u01ae\3\2\2\2\u01ae")
        buf.write("\u01af\b:\2\2\u01aft\3\2\2\2\u01b0\u01b1\t\7\2\2\u01b1")
        buf.write("v\3\2\2\2\u01b2\u01b3\t\b\2\2\u01b3x\3\2\2\2\u01b4\u01b5")
        buf.write("\t\5\2\2\u01b5z\3\2\2\2\u01b6\u01be\t\t\2\2\u01b7\u01bd")
        buf.write("\n\n\2\2\u01b8\u01b9\7^\2\2\u01b9\u01bd\t\13\2\2\u01ba")
        buf.write("\u01bb\7)\2\2\u01bb\u01bd\7$\2\2\u01bc\u01b7\3\2\2\2\u01bc")
        buf.write("\u01b8\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bd\u01c0\3\2\2\2")
        buf.write("\u01be\u01bc\3\2\2\2\u01be\u01bf\3\2\2\2\u01bf\u01c1\3")
        buf.write("\2\2\2\u01c0\u01be\3\2\2\2\u01c1\u01c2\t\t\2\2\u01c2\u01c3")
        buf.write("\b>\3\2\u01c3|\3\2\2\2\u01c4\u01cc\7$\2\2\u01c5\u01cb")
        buf.write("\n\n\2\2\u01c6\u01c7\7^\2\2\u01c7\u01cb\t\13\2\2\u01c8")
        buf.write("\u01c9\7)\2\2\u01c9\u01cb\7$\2\2\u01ca\u01c5\3\2\2\2\u01ca")
        buf.write("\u01c6\3\2\2\2\u01ca\u01c8\3\2\2\2\u01cb\u01ce\3\2\2\2")
        buf.write("\u01cc\u01ca\3\2\2\2\u01cc\u01cd\3\2\2\2\u01cd\u01d0\3")
        buf.write("\2\2\2\u01ce\u01cc\3\2\2\2\u01cf\u01d1\t\f\2\2\u01d0\u01cf")
        buf.write("\3\2\2\2\u01d1\u01d2\3\2\2\2\u01d2\u01d3\b?\4\2\u01d3")
        buf.write("~\3\2\2\2\u01d4\u01dc\7$\2\2\u01d5\u01db\n\n\2\2\u01d6")
        buf.write("\u01d7\7^\2\2\u01d7\u01db\t\13\2\2\u01d8\u01d9\7)\2\2")
        buf.write("\u01d9\u01db\7$\2\2\u01da\u01d5\3\2\2\2\u01da\u01d6\3")
        buf.write("\2\2\2\u01da\u01d8\3\2\2\2\u01db\u01de\3\2\2\2\u01dc\u01da")
        buf.write("\3\2\2\2\u01dc\u01dd\3\2\2\2\u01dd\u01df\3\2\2\2\u01de")
        buf.write("\u01dc\3\2\2\2\u01df\u01e0\5\u0081A\2\u01e0\u01e1\b@\5")
        buf.write("\2\u01e1\u0080\3\2\2\2\u01e2\u01e3\7^\2\2\u01e3\u01e7")
        buf.write("\n\13\2\2\u01e4\u01e5\t\r\2\2\u01e5\u01e7\n\t\2\2\u01e6")
        buf.write("\u01e2\3\2\2\2\u01e6\u01e4\3\2\2\2\u01e7\u0082\3\2\2\2")
        buf.write("\u01e8\u01ea\7%\2\2\u01e9\u01eb\13\2\2\2\u01ea\u01e9\3")
        buf.write("\2\2\2\u01ea\u01eb\3\2\2\2\u01eb\u0084\3\2\2\2\u01ec\u01f0")
        buf.write("\t\2\2\2\u01ed\u01ef\t\3\2\2\u01ee\u01ed\3\2\2\2\u01ef")
        buf.write("\u01f2\3\2\2\2\u01f0\u01ee\3\2\2\2\u01f0\u01f1\3\2\2\2")
        buf.write("\u01f1\u0086\3\2\2\2\u01f2\u01f0\3\2\2\2\u01f3\u01f4\13")
        buf.write("\2\2\2\u01f4\u0088\3\2\2\2!\2\u008b\u0090\u0097\u009c")
        buf.write("\u00a1\u00a6\u00ab\u00b1\u00b4\u00b8\u00ba\u00c0\u00c7")
        buf.write("\u00ca\u00cf\u00d3\u00db\u015f\u0164\u01ac\u01bc\u01be")
        buf.write("\u01ca\u01cc\u01d0\u01da\u01dc\u01e6\u01ea\u01f0\6\b\2")
        buf.write("\2\3>\2\3?\3\3@\4")
        return buf.getvalue()


class CSELLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ID_SIGN = 1
    ID_NOT_SIGN = 2
    NUMBER_LIT = 3
    BLOCK_COMMENT = 4
    BREAK = 5
    CONTINUE = 6
    IF = 7
    ELIF = 8
    ELSE = 9
    WHILE = 10
    FOR = 11
    OF = 12
    IN = 13
    FUNCTION = 14
    LET = 15
    TRUE = 16
    FALSE = 17
    CALL = 18
    RETURN = 19
    NUMBER = 20
    BOOLEAN = 21
    STRING = 22
    JSON = 23
    ARRAY = 24
    CONSTANT = 25
    ADD = 26
    SUB = 27
    MUL = 28
    DIV = 29
    MOD = 30
    NOT = 31
    AMP = 32
    AND = 33
    OR = 34
    EQUAL = 35
    ASS = 36
    DIF = 37
    BGT = 38
    LGT = 39
    BGZ = 40
    LGZ = 41
    COM = 42
    CAT = 43
    RCC = 44
    LCC = 45
    RSQ = 46
    LSQ = 47
    LS = 48
    RS = 49
    SM = 50
    DOT = 51
    COLON = 52
    CM = 53
    DOL = 54
    WS = 55
    STRING_LIT = 56
    UNCLOSE_STRING = 57
    ILLEGAL_ESCAPE = 58
    UNTERMINATED_COMMENT = 59
    ID = 60
    ERROR_CHAR = 61

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Break'", "'Continue'", "'If'", "'Elif'", "'Else'", "'While'", 
            "'For'", "'Of'", "'In'", "'Function'", "'Let'", "'True'", "'False'", 
            "'Call'", "'Return'", "'Number'", "'Boolean'", "'String'", "'Json'", 
            "'Array'", "'Constant'", "'+'", "'-'", "'*'", "'/'", "'%'", 
            "'!'", "'&'", "'&&'", "'||'", "'='", "'=='", "'!='", "'>'", 
            "'<'", "'>='", "'<='", "'==.'", "'+.'", "')'", "'('", "']'", 
            "'['", "'{'", "'}'", "';'", "'.'", "':'", "','", "'$'" ]

    symbolicNames = [ "<INVALID>",
            "ID_SIGN", "ID_NOT_SIGN", "NUMBER_LIT", "BLOCK_COMMENT", "BREAK", 
            "CONTINUE", "IF", "ELIF", "ELSE", "WHILE", "FOR", "OF", "IN", 
            "FUNCTION", "LET", "TRUE", "FALSE", "CALL", "RETURN", "NUMBER", 
            "BOOLEAN", "STRING", "JSON", "ARRAY", "CONSTANT", "ADD", "SUB", 
            "MUL", "DIV", "MOD", "NOT", "AMP", "AND", "OR", "EQUAL", "ASS", 
            "DIF", "BGT", "LGT", "BGZ", "LGZ", "COM", "CAT", "RCC", "LCC", 
            "RSQ", "LSQ", "LS", "RS", "SM", "DOT", "COLON", "CM", "DOL", 
            "WS", "STRING_LIT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT", 
            "ID", "ERROR_CHAR" ]

    ruleNames = [ "ID_SIGN", "ID_NOT_SIGN", "INT_L", "NUMBER_LIT", "BLOCK_COMMENT", 
                  "BREAK", "CONTINUE", "IF", "ELIF", "ELSE", "WHILE", "FOR", 
                  "OF", "IN", "FUNCTION", "LET", "TRUE", "FALSE", "CALL", 
                  "RETURN", "NUMBER", "BOOLEAN", "STRING", "JSON", "ARRAY", 
                  "CONSTANT", "EXPONENT", "ADD", "SUB", "MUL", "DIV", "MOD", 
                  "NOT", "AMP", "AND", "OR", "EQUAL", "ASS", "DIF", "BGT", 
                  "LGT", "BGZ", "LGZ", "COM", "CAT", "RCC", "LCC", "RSQ", 
                  "LSQ", "LS", "RS", "SM", "DOT", "COLON", "CM", "DOL", 
                  "WS", "DIGIT", "NDIGIT", "SIGN", "STRING_LIT", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "ESC_ILLEGAL", "UNTERMINATED_COMMENT", 
                  "ID", "ERROR_CHAR" ]

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
            actions[60] = self.STRING_LIT_action 
            actions[61] = self.UNCLOSE_STRING_action 
            actions[62] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
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
            	
     


