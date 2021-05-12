import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def testcase_0(self):
        input = """Let x=1;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,200))
    def testcase_1(self):
        input = """Let x;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 201))

    def testcase_2(self):
        input = """Let a, temp, a[2,3], x[10];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 202))

    def testcase_3(self):
        input = """Let a = 0, c, d[2,3], e[2] = [1,2,3];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 203))

    def testcase_4(self):
        input = """Let x = [[1,2,3],[4,5,6]];
        Let temp = "This is a string";
        Let y = 1.0E-3058;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 204))

    def testcase_5(self):
        input = """Let x = [[1,2,3],[4,5,6]];
        ##Another global variable declaration##
        Let $Y = True;
        Let temp = 1.876 + 78541;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 205))

    def testcase_6(self):
        input = """
        Let ;
        Function fact(n)
        {
        }
        """
        expect = "Error on line 2 col 12: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 206))

    def testcase_7(self):
        input = """
        Let x = 0, y = [1,2,3];
        Function main(x,y)
        {
        x = y + 0.0001;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 207))

    def testcase_8(self):
        input = """
        Let x = 0, y = [1,2,3];
        Function main(x,y)
        x = y + 0.0001;
        """
        expect = "Error on line 4 col 8: x"
        self.assertTrue(TestParser.checkParser(input, expect, 208))

    def testcase_9(self):
        input = """
        Let x = 0, y = [1,2,3];
        Function main(x,y)
        {
        x = y + 0.0001;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 209))

    def testcase_10(self):
        input = """
        Let x = 0, y = [1,2,3];
        Function main(x,y)
        {
        x = y + 0.0001;
        x = a[2,3] * 1.1e0001;
        b[2] = a[1] % 10.;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 210))

    def testcase_11(self):
        input = """
        Let x = 0, y = [1,2,3];
        Function main( x,y)
        {
        If ( x == 0 ){
            x = x + 1;
            x = y + 1e3;
            b[2] = a[1] % 10.;
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 211))

    def testcase_12(self):
        input = """
        Let x;
        Function foo( x,y,z)
        {
        If ( x >= 0 ){
            b[2] = a[1] % 10.;
        }
        Elif ( x * x == 0 ){
            b[1] = a[8] || a || c;
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 212))

    def testcase_13(self):
        input = """
        Let x;
        Function foo( x,y,z)
        {
            If ( x >= 0 ){
                b[2] = a[1] % 10.;
            }
            Elif ( x * x == 0 ){
                b[1] = a[8] || a || c;
            }
            Else {
                c = a == (x * y);
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 213))

    def testcase_14(self):
        input = """
        Let x;
        Function foo( x,y,z)
        {
            If ( x >= 0 )
            {
                b[2] = a[1] % 10.;
            }
            Elif ( x * x == 0 )
            {
                b[1] = a[8] || a || c;
            }
            Elif ( x * y - z == 0 )
            {
                b[1] = a[8] && a && c;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 214))

    def testcase_15(self):
        input = """
        Let zzz;
        Function foobalu( x,y,z)
        {
        If ( x >= 0 ){
            b[2] = a[1] % 10.;}
        Elif ( x * x == 0 ){
            b[1] = a[8] || a || c;}
        Elif ( x * y - z == 0 ){
            b[1] = a[8] && a && c;}
        Else 
            {Break;}
        
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 215))

    def testcase_16(self):
        input = """
        Let zzz;
        Function foobalu_undenied( a[2,5])
        {
        If ( abc == (True || False) )
        {
            b = a * 10.e-3;
        }
        ## Another condition statement ##
        Elif (  x * x == 0 )
        {
            c = a[8,10] || a && c;
            }
        Else 
            {Continue;}
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 216))

    def testcase_17(self):
        input = """
        Let zzz;
        ## Comment 1 ##
        Function foobalu_undenied( a[2,5])
        {
        ## Comment 2 ##
        If ( a + b - c == 0){
            x = b + c - a % 2;}
        Else 
            {Continue;}
        
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 217))

    def testcase_18(self):
        input = """
        Function fun( temp, value)
            {
            If (a && b && c == 0){
                x = Call(fun,[temp- 1]) * Call(fun,[temp% 2]);
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 218))

    def testcase_19(self):
        input = """
        Function fun( temp, value)
            {
            }
        Function main( x, y, z)
            {
            If (a == c || xyz ){
                Return;}
            Elif ( b - c == a + 12.e-85){
                Break;
            }    
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 219))

    def testcase_20(self):
        input = """
        Let c = 12.1e-34, b[2,3] = [1,2,3,4];
        ##Start the comment##
        Function main( x, y, z)
            ## Begin the body of function ##
            {
            If ( a == c || xyz ){
                Return;}
            Elif ( b - c == a + 12.1e-85 ){
                Break;
            }    
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 220))

    def testcase_21(self):
        input = """
        Function test( x, y, z)
            {
            For i In [1,2,3]{
                x = a + b + x;
                y = a + 12000.;
                z = b || x && c;
            }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 221))

    def testcase_22(self):
        input = """
            Function test( x, y, z)
                {
                For i In [1,2,3] {
                   Call(printLn,[i]);
                }
                }
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 222))

    def testcase_23(self):
        input = """
            Let temp = "This is a string";
            Function main( abc, xyz)
                {
                For x In [1,2] {
                    If (x == 0 ){
                        x = x == 122. % True;
                        y = False || (a + b);
                    }
                    Break;
                }
                }
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 223))

    def testcase_24(self):
        input = """
            Let x;
            Function main()
                { 
                   Break;
                   Continue;
                   Return 0;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 224))

    def testcase_25(self):
        input = """
        ## Comment start at here ?? ##
            Let par = True;
            Function printArray( a[10])
                {
                For i In [1,2,3]{
                    x = i + 10;
                    Call(print,[x]);
                    If  (x == 0){
                        x = x >= 777 * False;
                        y = False && (a - b);
                    }
                    Break;
                }
                }
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 225))

    def testcase_26(self):
        input = """
            Let parser = 1814002;
            Function foo( count, x, y, z)
                {
                While ( x == 1.08765 * 2.098 || True)  {
                    x = x + 1;
                    y = [1,2,3] * 985475;
                    z = "This is a string" ==. "abcdxzy";
                }
                }
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 226))

    def testcase_27(self):
        input = """
            Let parser = 1814002;
            Function foo( count, x, y, z)
                {
                While ( x== 1.08765 * 2.098 || True  ){
                    x = x + 1;
                    y = [1,2,3] * 985475;
                    z = "This is a string" ==. "abcdxzy";
                }
                }
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 227))

    def testcase_28(self):
        input = """
            Function sum( a, b)
                {
                    Return a + b;
                }
            Function main()
            {
                Let s = 0;
                For i In [0,1,2] {
                    If ( s >= 40 ){ Continue;
                    }
                s = s + Call(sum,[i, i + 1]);
                }
                }
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 228))

    def testcase_29(self):
        input = """
            Let parser = 1814002;
            Function foo( count, x, y, z)
                {
                While ( x == 1.08765 * 2.098 || True) {
                    If ( s >= 40 ){ Continue;}
                    Elif (s >= 10.1e-492) { Break;
                    }
                    ##x = x + y. * z;##
                    y = [1,2,3] * 985475;
                    z = "This is a string" ==. "abcdxzy";
                }
                }
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 229))

    def testcase_30(self):
        input = """
            Let parser = 1814002;
            Let temp = [[1,2,3],[1,2,3]];
            Function foo( x, y, z)
                {
                While ( x % z != 1814002) {
                    If ( s >= 40 ){ Continue;}
                    Elif ( s >= 10.1e-492 ){ Break;}
                    Elif ( temp < 12340. ){ Continue;}
                    Else {i = i + 1;
                    }
                    ## Multiline Comment
                    y = [1,2,3] * 985475;
                    #z = "This is a string" == "abcdxzy";
                    ##
                }
                }
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 230))

    def testcase_31(self):
        input = """
            Let parser = 1814002;
            Let temp = "abcd";
            Function foo( x, y, z)
                {
                    x = x + 1;
                    y = y % 10;
                While (x + y > 10 )
                {
                    a = b;
                }    
                }
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 231))

    def testcase_32(self):
        input = """
            ## *Comment here ##
            Function foo( x, y, z)
                {
                  
                    x = x + 1;
                    y = y % 10;
                    If (x >= 0){ 
                        x = y == z + 1;
                        y = y * z;
                        z = 1.1e0033;}
                    Else {x = x + y + z;
                    }
                While ( x + y > 10){
                  a = b;
                }
                }
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 232))

    def testcase_33(self):
        input = """
            ## Comment here ##
            Function foo( x, y, z)
                {
                    If ( x >= 0){ 
                        For i In [1000,2000] { 
                            i = i % 10;
                            a[2] = a[2] + 2;
                            Call(print,[i]);
                        }
                        x = y == z + 1;
                        y = y * z;
                        z = 1.1e0033;
                        }
                    Else {
                        a = 5;
                    }
                While (x + y > 10){
                  a = 5;
                }
                }
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 233))

    def testcase_34(self):
        input = """
            Function foo( x, y, z)
                {
                    If ( x >= 0 ){ 
                        x = y == z + 1;
                        y = y * z;
                        z = 1.1e0033;
                        }
                    Else {x = x + y + z;
                    }
                    For i In [1000,2000]   {
                            i = i % 10;
                            a[2] = a[2] + 2;
                            Call(print,[i]);
                        }
                While ( x + y <= 1814002){
                  a = 4;
                }
                }
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 234))

    def testcase_35(self):
        input = """
            Function foo( x, y, z)
                {
                If ( x == 10.098 || 0 ){
                    For i In [100,200] { 
                        While (x > 0.00)  { 
                            x = x + 1;
                            Call(print,[x]);
                        }
                        Call(print,[a[2]]);
                    }
                    }
                Else {Continue;
                }
                }
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 235))

    def testcase_36(self):
        input = """
            ##Comment##
            Function foo( x, y, z)
                {
                If ( 10.098 == 0) {
                    For x In [1,2,3]   {
                    ## Comment# ##
                        While ( x > 0.00){
                            x = x + 1;
                            Call(print,[x]);
                            
                        }
                ## Comment* ##
                        Call(print,[a[2]]);
                    }
                }
                Else {Continue;}

                }
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 236))

    def testcase_37(self):
        input = """
            ##Comment##
            Function main( x, y, z)
                {
                    Break;
                    Continue;
                    x = Call(foo,[1]) + Call(foo,[2]) + Call(foo,[3]);
                }
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 237))

    def testcase_38(self):
        input = """
            ##Comment##
            Let c = 5, x, y = [1,2,3];
            Function main_foo( a[2,10])
                {
                    If  (x == 0 ){ 
                        Break;
                        x = x + 1.00837;
                        y = y * 1234;
                    }
                    Elif (q == 0){
                        Continue;
                    }
                    x = Call(foo,[1]) +Call(foo,[2]);
                }
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 238))

    def testcase_39(self):
        input = """
            Let c = 5, x, y = [1,2,3];
            Function main_foo()
                {
                    If ( (x == 0) ){ 
                        Break;}
                    Elif (q == 0){
                        Continue;
                    }
                }
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 239))

    def testcase_40(self):
        input = """
            Let c = "A short string";
            Function main_foo( y)
                {
                    If ( x == 0 ){ 
                        Break;}
                    Elif (q == 0) {
                        Continue;
                    }
                }

            Function sub_foo( x)
                {
                   
                }
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 240))

    def testcase_41(self):
        input = """
        Let x;
        Function main()
        {
            Let r = 10., v, i;
            v = (4 /3) * 3.14 * r * r * r;
            For i In [1,2,3] {
               Call(printLn,[i]);
            }
            Return 0;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 241))

    def testcase_42(self):
        input = """
        Function main()
        {
            Let i = 0;
            While  (i < 5) { 
                a[0] = b + 1.0;
                i = i + 1;
            }
            Return 0;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 242))

    def testcase_43(self):
        input = """
        Let x[3,3 * (4 + Call(f,[2]) - 4)];
        Function main( k)
        {
            Let i = 0;
            While ( i < 5)  {
                a[0] = b + 1.0;
                i = i + 1;
            }
            Return 0;
        }
        """
        expect = "Error on line 2 col 18: *"
        self.assertTrue(TestParser.checkParser(input, expect, 243))

    def testcase_44(self):
        input = """
        Function main(k)
        {
            Let i = 10, k[10,2] = [[], []];

                Break;
            While ( i <= 10 )  {
            Return 0;}
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 244))

    def testcase_45(self):
        input = """
        Function main()
        {
            Let s = 0;
            For i In [1,2,3]   {
                s += i * 2;
            }
            Return 0;
        }
        """
        expect = "Error on line 6 col 18: +"
        self.assertTrue(TestParser.checkParser(input, expect, 245))

    def testcase_46(self):
        input = """
        Let a, b, c = 10 + 2 * 4;
        Function main()
        {
            Let i = 0, arr[10];
            c = arr[0];
            For i In [1,2,3]   {
                If (c < arr[i]){
                    c = arr[i];
                }
            }  
            Return 0;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 246))

    def testcase_47(self):
        input = """
        Let a, b, c = 10;
        Function func()
        {
            Return "Hello World";
        }
        Function main()
        {
            Call(print,[Call(func,[])]);
            Return;  
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 247))

    def testcase_48(self):
        input = """
        Let a, b, c = 2;
        Function func()
        {
            Return "Hello World" 1967;
        }
        Function main()
        {
            Call(print,[func()]);
            Return;  
        }
        """
        expect = "Error on line 5 col 33: 1967"
        self.assertTrue(TestParser.checkParser(input, expect, 248))

    def testcase_49(self):
        input = """
        Function main()
        {
            Let i;
            For i In [1,2,3] {  
                Continue i;
            }  
            Return 0;
        }
        """
        expect = "Error on line 6 col 25: i"
        self.assertTrue(TestParser.checkParser(input, expect, 249))

    def testcase_50(self):
        input = """
        Function main()
        {
            Let i;  
            For i In [1,2,3] {  
                Continue;
            }
            Return 0;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 250))
        
        def test_function_1(self):
            input = r""" 
        Function foo(a[5],b, c, d[1])
        {
            Let i = 5;
        }"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 251))


    def test_index_5(self):
        input = """
        Function main()
            {
                a[3+Call(foo,[2])] =  4;
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,252))
    """While"""
    def test_while(self):
        input = r"""
        Function foo() {
            While (i < 5)
            {
                i = a + 1;
            }
        }
         """
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 253))

    """Break"""
    def test_break(self):
        input = r"""
        Function foo() {
            While (i < 5)
            {
                i = a + 1;
                Break;
            }
        }
         """
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 254))
      
    """Return"""
    def test_return_1(self):
        input = r"""
        Function foo() {
            While (i < 5)
            {
                i = a + 1;
                Return;
            }
        }
         """
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 255))
        
    def test_return_2(self):
        input = r"""
        Function foo() {
            While (i < 5)
            {
                i = a + 1;
                Return 1;
            }
        }
         """
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 256))
    def test_return_3(self):
        input = r"""
        Function foo() {
            While (i < 5)
            {
                i = a + 1;
                Return i;
            }
        }
         """
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 257))
    def test_return_4(self):
        input = r"""
        Function foo() {
            While (i < 5)
            {
                i = a + 1;
                Return (i+1);
            }
        }
         """
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 258))

    """Test Continue"""

    def test_continue(self):
        input = r"""
        Function foo() {
            While (i < 5)
            {
                i = a + 1;
                Continue;            
                
            }
        }
         """
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 259))

    """Test if"""

    def test_if(self):
        input = r"""
        Function foo() {
            While (i < 5)
            {
                i = a + 1;
                If( i > 0)
                {
                    Return (i+1);
                }
            }
        }
         """
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 260))

    def test_if_else(self):
        input = r"""
        Function foo() {
            While (i < 5)
            {
                i = a + 1;
                If( i > 0)
                {
                    Return (i+1);
                }
                Else
                {
                    Return 1;
                }
            }
        }
         """
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 260))

    def test_if__elif_else(self):
        input = r"""
        Function foo() {
            While (i < 5)
            {
                i = a + 1;
                If( i > 0)
                {
                    Return (i+1);
                }
                Elif (i  < 0)
                {
                    Return 0;
                }
                Else
                {
                    Let a = 0;
                    Return 1;
                }
            }
        }
         """
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 261))

    """For In """
    def test_for_in(self):
        input = r"""
        Function foo() {
           For i In [1,2,3,4,5]
           {
               a = a + i;
               Let c = i;
           }
        }
         """
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 262))

    def test_for_in_1(self):
        input = r"""
        Function foo() {
           For i In [[1,2],[3,4],[5,6]]
           {
               a = a + i;
               Let c = i;
           }
        }
         """
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 263))
        
    """For Of"""
    def test_for_of(self):
        input = r"""
        Function foo() {
            Let a = {
                    name: "Yanxi Place",
                    address: "Chinese Forbidden City" 
                    };
            For key Of a
            {

                 Call(printLn, ["Value of " + key + ": " + a[key]]);
            }
        }
         """
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 264))
        
    """Call"""

    def test_call_1(self):
        input = r"""
        Function foo() {
            Call(foo, [2 + x, 4 / y]);
        }
         """
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 265))

    """Test Let bonus"""
    def test_let_with_type(self):
        input = """Let a:Number = 5;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,266))
    
    def test_let_with_float(self):
        input = """Let a:Number = 5.9;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,267))
    def test_let_with_string(self):
        input = """Let a:Number = "mot ha ba bon";"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,268))
    def test_let_with_arr(self):
        input = """
        Let b[2, 3] = [[1, 2, 3], [4, 5, 6]];
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,269))

    """Test Constant"""
    def test_constant(self):
        input = """
        Constant $b[2, 3] = [[1, 2, 3], [4, 5, 6]];
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,270))
    def test_constant_1(self):
        input = """
        Constant $b: String = "tory of Yanxi Place";
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,271))

    """Random Test"""
    def test_random(self):
        input = """
            Let a = 2;
            Constant $c = 1;
            Function foo()
            {
                
                While (a < 0)
                {
                    While ( b > 1)
                    {
                        a  = a % b;
                        Let d;
                        d = a / b;
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,272))

    def test_random_1(self):
        input = """
            Let a = 2;
            Constant $c = 1;
            Function foo()
            {
                
                While (a < 0)
                {
                    While ( b > 1)
                    {
                        a  = a % b;
                        Let d;
                        d = a / b;
                        a = a == b;
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,273))

    def test_random_2(self):
        input = """
            Let a = 2;
            Constant $c = 1;
            Function foo()
            {
                Let v = 2;
                Constant $d = 1;
                a = (3<5) == True && (2>5) || (5>2);

            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,274))

    def test_random_3(self):
        input = """      
            }
        """
        expect = "Error on line 2 col 12: }"
        self.assertTrue(TestParser.checkParser(input,expect,275))
    def test_random_4(self):
        input = """
        Function main()
        {
            Let r = 10., v;
            Let v = (4. / 3.) * 3.14 * r * r * r;
            v = em + la - nang * tho;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,276))

    def test_random_5(self):
        input = """
        Function main()
        {
            em != khong; 
        }"""
        expect = "Error on line 4 col 15: !="
        self.assertTrue(TestParser.checkParser(input,expect,277))
    def test_random_6(self):
        input = """
        Function main(a.b) 
        { 

            While (statement != 3) 
            {
                Let a = 5;
            } 

        }"""
        expect = "Error on line 2 col 23: ."
        self.assertTrue(TestParser.checkParser(input,expect,278))

    def test_exp6(self):
        input = """
        Function main()
        {
            x = em != (khong == la && nang || tho); 
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,279))
    def test_exp8(self):
        input = """
        Function main()
        {
            x = (em != khong) == la >= nang || tho; 
        """
        expect = "Error on line 4 col 36: >="
        self.assertTrue(TestParser.checkParser(input,expect,280))
    def test_exp9(self):
        input = """
        Function main()
        {
            x = (em != khong) == la >= nang || tho; 
        """
        expect = "Error on line 4 col 36: >="
        self.assertTrue(TestParser.checkParser(input,expect,281))

    def random_test_8(self):
        input = r""" 
        Function foo(a[5],b, c, d[1])
        {
            Call(foo,[,]);
        }"""
        expect = r"Error on line 4 col 22: ,"
        self.assertTrue(TestParser.checkParser(input, expect, 282))    

    def test_function_9 (self):
        input = r""" 
        Function foo(a[5],b, c, d[1])
        {
            Call(foo,]);
        }"""
        expect = r"Error on line 4 col 21: ]"
        self.assertTrue(TestParser.checkParser(input, expect, 283)) 
    def test_assign3(self):
        input = r"""
Function foo( a[5], b)

{
    a = [12,3,[1,2]] = Call(foo,[]);
}
"""
        expect = r"Error on line 5 col 21: ="
        self.assertTrue(TestParser.checkParser(input, expect, 284)) 
    def test_assign(self):
        input = r"""
Function foo()

{
    a = b = c ;
}
"""
        expect = r"Error on line 5 col 10: ="
        self.assertTrue(TestParser.checkParser(input, expect, 285))  

    def test_exp6(self):
        input = """
        Function main(A)
        {
            x = em != (khong == la && nang || tho); 
        }"""
        expect = "Error on line 2 col 23: A"        
    def test_arr_declare3(self):
        input = r"""
    Function foo()
    {
        Let a = [1,    3 ,   4] ;
    }
    """
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 286))

    def test_arr_declare4(self):
        input = r"""
        Function foo()
            {
                Let a = [False,    True ,   True] ;
            }
        """
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 287))

    def test_arr_declare5(self):
        input = r"""
            Function foo()
                {
                    Let a = ["ASD", "SD" , "ss"] ;
                }
            """
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 288))

    def test_arr_declare6(self):
        input = r"""
        Function foo()
        {
            Let b: Number;
            Let a:String = "Saf" +.  "Sadf";
        }

                """ 
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 289))

    def test_null_func(self):
        input = r"""
        Function foo()
        {

        }
            """
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 290))

    def test_index_exp(self):
        input = r"""
        Function foo(a[5], b)
        {
            b = a[a[a[a[a[a[a[a]]]]]]] ;
        }
        """
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 291))

    def test_nothing(self):
        input = """ 
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,292))

    def test_index_exp2(self):
        input = r"""
        Function foo(a[5], b)
        {
            b = a[((2%3 * 3.0)==3) && (3==3)];

        }
        """
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 293))
    def test_index_exp3(self):
        input = r"""
        Function foo(a[5], b)
        {
            b = a[((2%3 * 3.0)==3) && (3==3) -21e3];
        }
        """
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 294))

    def test_comment(self):
        input = r"""
        ## Empty program, more likes empty life ##
        """
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 295))

    def test_comment1(self):
        input = r"""
        ## Empty program, more likes empty life
        One mul zero is zero ##
    """
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 296))

    def test_var1(self):
        input = r"""
        Let a = 5;
        Let b[2,3] = [[2,3,4],[4,5,6]];
        Let c, d = 6, e, f;
        Let m, n[10];
        """
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 297))

    def test_sign_expression(self):
        input = r"""
        Function foo (a[5], b)
        {
            b = -3 + -3 --3 ;
        }
        """
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 298))

    def test_sign_expression1(self):
        input = r"""
        Function foo(a[5], b)
        {
            b = -3.0 ;
        }
        """
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 299))

    def test_sign_expression2(self):
        input = r"""
        Function foo(a[5], b)
        {
            b = -----3.0 ;
        }
        """
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 300))

    def test_not_expression(self):
        input = r"""
            Function foo(a[5], b)
            {
                b = !((-3 + -3 --3) == -3);
            }
            """
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 301))

    def test_not_expression1(self):
        input = r"""
            Function foo(a[5], b)
            {
                b = !!!!!((-3 + -3 --3) == -3) ;
            }
            """
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 302))
    def test_random_9(self):
        input =  r""" 
Let a. 5;  """        
        expect = r"Error on line 2 col 5: ."
        self.assertTrue(TestParser.checkParser(input, expect, 303))

    def test_random_10(self):
        input =  r""" 
Let a. 5;  """        
        expect = r"Error on line 2 col 5: ."
        self.assertTrue(TestParser.checkParser(input, expect, 304))

    def test_random_11(self):
        input =  r""" 
Function. foo(a){}

              """        
        expect = r"Error on line 2 col 8: ."
        self.assertTrue(TestParser.checkParser(input, expect, 305))

    def test_random_11(self):
        input =  r""" 
Function foo(.aa){}

              """        
        expect = r"Error on line 2 col 13: ."
        self.assertTrue(TestParser.checkParser(input, expect, 306))

    def test_random_12(self):
        input =  r""" 
Function foo(){
    While(input)
    {
        Let a = 5;
    }

}

              """        
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 307))
    def test_random_13(self):
        input =  r""" 
Function foo(){
    While(input)
    {
        a= b + c - a + 2.3e3;
    }

}

              """        
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 308))

    def testcase81(self):
        input = """Function foo(a[5], b) {
                Let i = 0;
                While (i < 5) {
                a[i] = b + 1;
                Let u: Number = i + 1;
                If (a[u] == 10) {
                Return a[i];
                }
                }
                For a In [1,2,3]{
                    Call(foo,[a[1]]);
                }
                Call(foo, [2 + x, 4 / y]);
                Call(goo, []);
                a[2] = Call(foo, [2]) + Call(foo, [Call(bar, [2, 3])]);
                Return -1;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,309))
    def testcase82(self):
        input = """Function foo(a[5], b) {
                Let i = 0;
                While (i < 5) {
                a[i] = b + 1;
                Let u: Number = i + 1;
                If (a[u] == 10) {
                Return a[i];
                }
                }
                a[2] = Call(foo, [2] + Call(foo, [Call(bar, [2, 3])]);
                Return -1;
                }"""
        expect = "Error on line 10 col 37: +"
        self.assertTrue(TestParser.checkParser(input,expect,310))
    def testcase83(self):
        input = """Function foo(a[5], b) {
                Let i = 12.+e3;
                While (i < 5) {
                a[i] = b + 1;
                Let u: Number = i + 1;
                If (a[u] == 10) {
                Return a[i];
                }
                }
                a[2] = Call(foo, [2]) + Call(foo, [Call(bar, [2, 3])]);
                Return -1;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,311))
    def testcase84(self):
        input = """Function foo(a[5],b) 
        {
                Let i = 0;
                While (i < 5) 
            {
                a[i] = b + 1;
                Let u: Number = i + 1;
                If (a[u] == 10) 
                {
                    If(b==5)
                    {
                        Return a[i];
                    }
                    Elif(b==5)
                    {
                        i=i+1;
                    }
                    Else
                    {
                        Return 0;
                    }
                }
            }
                a[2] = Call(foo, [2]) + Call(foo, [Call(bar, [2, 3])]);
                Return a[2] + Call(foo, [2]) + Call(foo, [Call(bar, [2, 3])]);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,312))
    def testcase85(self):
        input = """Function foo(a[5],b) 
        {
                Let i = 0;
                While (i < 5) 
            {
                a[i] = b + 1;
                Let u: Number = i + 1;
                If (a[u] == 10) 
                {
                    If(b==5)
                    {
                        Return a[i];
                    }
                    Elif(b==5)
                    {
                        i=i+1;
                    }
                    Else
                    {
                        Return 0;
                    }
                }
            }
                a[2] = Call(foo, [2]) + Call(foo, [Call(bar, [2, 3])]);
                Return a[2] + Call(foo, [2]) + Call(foo, [Call(bar, [2, 3])]);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,313))
    def testcase86(self):
        input = """Function foo(a[5],b) 
        {
                Let i = 0;
                While (i < 5) 
            {
                a[i] = b + 1;
                Let u: Number = i + 1;
                If (a[u] == 10) 
                {
                    If(b==5)
                    {
                        Return a[i];
                    }
                    Elif(b==5)
                    {
                        i=i+1;
                    }
                    Else
                    {
                        Return 0;
                    }
                }
            }
                a[2] = Call(foo, [2]) + Call(foo, [Call(bar, [2, 3])]);
                Return a[2] + Call(foo, [2]) + Call(foo, [Call(bar, [2, 3])]);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,314))
    def testcase87(self):
        input = """Function foo(a[5], b) {
                Let i = 0;
                While (i < 5) {
                    While(i){
                    a[i] = b + 1;
                    Let u: Number = i + 1;
                    If (a[u] == 10) {
                    Return a[i];
                    }
                }
                }
                
                Return ;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,315))
    def testcase88(self):
        input = """Function foo(a[5], b) {
                Let i = 0;
                While (i < 5) {
                    While(i){
                    a[i] = b + 1;
                    Let u :: Number = i + 1;
                    If (a[u] == 10) {
                    Return a[i];
                    }
                }
                }
                Return ;
                }"""
        expect = "Error on line 6 col 27: :"
        self.assertTrue(TestParser.checkParser(input,expect,316))
    def testcase89(self):
        input = """Constant $a = 10;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,317))
    def testcase90(self):
        input = """Constant $a = 10;
                Function foo(a[5], b) {
                Constant $b: String = "Story of Yanxi Place";
                Let i = 0;
                While (i < 5) {
                a[i] = (b + 1) * $a;
                Let u: Number = i + 1;
                If (a[u] == 10) {
                Return $b;
                }
                i = i + 1;
                }
                a[2] = a[b["name","first"]] + 4;
                Return $b + ": Done";
                }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,318))
    def testcase91(self):
        input = """Constant $a = 10;
                Function foo(a[5], b) {
                Constant $b: String = "Story of Yanxi Place";
                Let i = 0;
                While (i < 5) {
                a[i] = (b + 1) * $a;
                Let u: Number = i + 1;
                If (a[u] == 10) {
                Return $b;
                }
                i = i + 1;
                }
                a[2] = a[b["name","first"]] + 4;
                Return $b + ": Done";
                }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,319))
    def testcase92(self):
        input = """Constant $a = 10;
                Function foo(a[5], b) {
                Constant $b: String: = "Story of Yanxi Place";
                Let i = 0;
                While (i < 5) {
                a[i] = (b + 1) * $a;
                Let u: Number = i + 1;
                If (a[u] == 10) {
                Return $b;
                }
                i = i + 1;
                }
                a[2] = a[b["name","first"]] + 4;
                Return $b + ": Done";
                }"""
        expect = "Error on line 3 col 35: :"
        self.assertTrue(TestParser.checkParser(input,expect,320))
    def testcase93(self):
        input = """Constant $a = 10;
                Function foo(a[5], b) {
                Constant $b: String = "Story of Yanxi Place";
                Let i = 0;
                While (i < 5) {
                a[i] = (b + 1) * $a;
                Let u: Number = i + 1;
                If (a[u] == 10) {
                Return $b;
                }
                i = i + 1;
                a[2] = a[b["name","first"]] + 4;
                Return $b + ": Done";
                }"""
        expect = "Error on line 14 col 17: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,321))
    def testcase94(self):
        input = """Constant $a = 10;
                Function foo() {
                Constant $b: String = "Story of Yanxi Place";
                Let i = 0;
                While (i < 5) {
                a[i] = (b + 1) * $a;
                Let u: Number = i + 1;
                If (a[u] == 10) {
                Return $b;
                }
                i = i + 1;
                }
                a[2] = a[b["name","first"]] + 4;
                Return $b + ": Done";
                }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,322))
    def testcase95(self):
        input = """
                Function foo(a) {
                    Let b: String = a["name"] + a["address"];
                    a["name"] = "Qianqing Palace";
                }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,323))
    def testcase96(self):
        input = """
                Function foo(a) {
                    Let b: String = a["name"] + a["address"];
                    a+=["name"] = "Qianqing Palace";
                }"""
        expect = "Error on line 4 col 21: +"
        self.assertTrue(TestParser.checkParser(input,expect,324))
    def testcase97(self):
        input = """
                Function foo(a) {
                    Let b: String = a["name"] + a["address"];
                    a["name"] = "Qianqing Palace";
                    b= True;
                    While(b==2){
                    }
                    Return ;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,325))
    def testcase98(self):
        input = """
                Function foo{
                    Let a;
                }
                """
        expect = "Error on line 2 col 28: {"
        self.assertTrue(TestParser.checkParser(input,expect,326))
    def testcase99(self):
        input = """
                Function foo(a,b){
                    Let a;
                    b=[1,"name"];
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,327))
    
 
    def test_random_14(self):
        input =  r""" 
Function foo(){
    While(input)
    {
        Let a = "ss";
        Let b =  "ss";
        c = (a==.b);
        Return c;
    }
}
  """        
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 328))
    def test_random_15(self):
        input =  r""" 
Function foo(){
    While(input)
    {
        Let a = "ss";
        Let b =  "ss";
        c = (a==.b);
        Let d;
        d = a+. b;
    }
}
  """        
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 329))

    def test_index_exp_assign(self):
        input = r"""
            Function foo (a[5], b)
            {
                a[Call(foo,[2])] = a[b["name"]["first"]] + 4;          
            }
            """
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 330))
    def test_index_exp_assign_2(self):
        input = r"""
            Function foo (a[5], b)
            {
                d[Call(foo,[2])] = a[b["name"]["first"]] + 4;          
            }
            """
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 331))

    def test_stmt6(self):
        input = r"""
        Let  m,n[10] ;
        Function main()
        {
            Return Call(hello, [n]);
        }
            """
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 332))
    def test_stmt8(self):
        input = r"""
        Let  m,n[10] ;
        Function main()
        {
            Return Call(hello, [n]);
        }
            """
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 333))
    def test_stmt6(self):
        input = r"""
        Let  m,n[10] ;
        Function main()
        {
            Return Call(hello, [n]);
        }
            """
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 334))
    def test_stmt2(self):
        input = r"""
            Let m,n[10] ;
            Function  main()
            {

                While (expression) { a=3 ;} 
            } 
            """
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 335))

    def test_stmt(self):
        input = r"""
            Let m,n[10];
            Function fact(n)
            {
                If (a) { a=3;} 
                Elif (b){b=4;} 
                Elif (c) {c=5;} 
            } 
            """
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 336))


    def test_func(self):
        input = r"""
        Let m,n[10];
        Function fact()
        {
            If (n == 6)
            {
                Return 1;
            }
            Else 
            {
                Return n * Call(fact, [n - 1]);
            }
        }
        """
        expect = r"successful"
  
        self.assertTrue(TestParser.checkParser(input,expect,337))
  
    
  
        
    def testcase57(self):
        input = """Let x=5,;"""
        expect ="Error on line 1 col 8: ;"
        self.assertTrue(TestParser.checkParser(input,expect,338))
    def testcase58(self):
        input = """Let x==5;"""
        expect ="Error on line 1 col 5: =="
        self.assertTrue(TestParser.checkParser(input,expect,339))
    def testcase59(self):
        input = """Let x+=5;"""
        expect ="Error on line 1 col 5: +"
        self.assertTrue(TestParser.checkParser(input,expect,340))
    def testcase60(self):
        input = """Let x-5;"""
        expect ="Error on line 1 col 5: -"
        self.assertTrue(TestParser.checkParser(input,expect,341))
    ####################################################
   
        self.assertTrue(TestParser.checkParser(input,expect,342))
    def testcase69(self):
        input = """Function foo(a;b){
            Let i = 0;
            Let a[5]=[1,2,3,4,5];
            Constant b="name";
            Return i;
        }"""
        expect = "Error on line 1 col 14: ;"
        self.assertTrue(TestParser.checkParser(input,expect,343))
    def testcase70(self):
        input = """Function foo(a,){
            Let i = 0;
            Let a[5]=[1,2,3,4,5];
            Constant b="name";
            Return i;
        }"""
        expect = "Error on line 1 col 15: )"
        self.assertTrue(TestParser.checkParser(input,expect,344))

    
    def testcase72(self):
        input = """Function foo(a[5], b) {
                Let i = 0;
                While (i < 5) {
                a[i] = b + 1;
                Let u: Number = i + 1;
                If (a[u] == 10) {
                
                }
                }
                Return -1
                }"""
        expect = "Error on line 11 col 16: }"
        self.assertTrue(TestParser.checkParser(input,expect,345))
    def testcase73(self):
        input = """Function foo(a[5], b) {
                Let i = 0;
                While (i < 5) {
                a[i] = b + 1;
                Let u: Number = i + 1;
                If (a[u] == 10) {
                Return a[i];
                }
                }
                For a In [1,2,3]{
                    Call(foo,[a[1]]);
                }
                Return -1;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,346))
    def testcase74(self):
        input = """Function foo(a[5], b) {
                For i In [1, 2, 3] {
                    Call(printLn, [i])
                }

                }"""
        expect = "Error on line 4 col 16: }"
        self.assertTrue(TestParser.checkParser(input,expect,347))
    def testcase75(self):
        input = """Function foo(a[5], b) {
                For i In [1, 2, 3] {
                    Call(printLn, [i]);
                }
                Let a = {
                name: "Yanxi Place",
                address: "Chinese Forbidden City"
                };
                For key In a {
                Call(printLn, ["Value of " + key + ": " + a[key]]);
                }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,348))
    def testcase76(self):
        input = """Function foo(a[5], b) {
                For i In [1; 2, 3] {
                    Call(printLn, [i]);
                }
                Let a = {
                name: "Yanxi Place",
                address: "Chinese Forbidden City"
                };
                For key In a {
                Call(printLn, ["Value of " + key + ": " + a[key]]);
                }
                }"""
        expect = "Error on line 2 col 27: ;"
        self.assertTrue(TestParser.checkParser(input,expect,349))
    def testcase77(self):
        input = """Function foo(a[5], b) {
                For i In [1, 2, 3] {
                    Call(printLn, [i]);
                }
                Let a = {
                name: "Yanxi Place",
                address: "Chinese Forbidden City"
                };
                For key In a {
                Call(printLn, ["Value of " + key + ": " + a[key]]);
                };
                }"""
        expect = "Error on line 11 col 17: ;"
        self.assertTrue(TestParser.checkParser(input,expect,350))
    def testcase78(self):
        input = """Function foo(a[5], b) {
                For i In [1, 2, 3] {
                    Call(printLn, [i]);
                }
                Let a = {
                name: "Yanxi Place",
                address: "Chinese Forbidden City"
                };
                For key In a {
                Call(printLn, ["Value of " + key + ": " + a[key]]);
                }
                Break;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,351))
    def testcase79(self):
        input = """Function foo(a[5], b) {
                For i In [1, 2, 3] {
                    Call(printLn, [i]);
                }
                Let a = {
                name: "Yanxi Place",
                address: "Chinese Forbidden City"
                };
                For key In a {
                Call(printLn, ["Value of " + key + ": " + a[key]]);
                }
                Break
                }"""
        expect = "Error on line 13 col 16: }"
        self.assertTrue(TestParser.checkParser(input,expect,352))
    def testcase80(self):
        input = """Function foo(a[5], b) {
                For i In [1, 2, 3] {
                    Call(printLn, [i]);
                }
                Let a = {
                name: "Yanxi Place",
                address: "Chinese Forbidden City"
                };
                For key In a {
                Call(printLn, ["Value of " + key + ": " + a[key]]);
                }
                Break;
                Continue;
                Return ;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,353))
    def testcase81(self):
        input = """Function foo(a[5], b) {
                Let i = 0;
                While (i < 5) {
                a[i] = b + 1;
                Let u: Number = i + 1;
                If (a[u] == 10) {
                Return a[i];
                }
                }
                For a In [1,2,3]{
                    Call(foo,[a[1]]);
                }
                Call(foo, [2 + x, 4 / y]);
                Call(goo, []);
                a[2] = Call(foo, [2]) + Call(foo, [Call(bar, [2, 3])]);
                Return -1;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,354))
    def testcase82(self):
        input = """Function foo(a[5], b) {
                Let i = 0;
                While (i < 5) {
                a[i] = b + 1;
                Let u: Number = i + 1;
                If (a[u] == 10) {
                Return a[i];
                }
                }
                a[2] = Call(foo, [2] + Call(foo, [Call(bar, [2, 3])]);
                Return -1;
                }"""
        expect = "Error on line 10 col 37: +"
        self.assertTrue(TestParser.checkParser(input,expect,355))
    def testcase83(self):
        input = """Function foo(a[5], b) {
                Let i = 12.+e3;
                While (i < 5) {
                a[i] = b + 1;
                Let u: Number = i + 1;
                If (a[u] == 10) {
                Return a[i];
                }
                }
                a[2] = Call(foo, [2]) + Call(foo, [Call(bar, [2, 3])]);
                Return -1;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,356))
    def testcase84(self):
        input = """Function foo(a[5],b) 
        {
                Let i = 0;
                While (i < 5) 
            {
                a[i] = b + 1;
                Let u: Number = i + 1;
                If (a[u] == 10) 
                {
                    If(b==5)
                    {
                        Return a[i];
                    }
                    Elif(b==5)
                    {
                        i=i+1;
                    }
                    Else
                    {
                        Return 0;
                    }
                }
            }
                a[2] = Call(foo, [2]) + Call(foo, [Call(bar, [2, 3])]);
                Return a[2] + Call(foo, [2]) + Call(foo, [Call(bar, [2, 3])]);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,357))
    def testcase85(self):
        input = """Function foo(a[5],b) 
        {
                Let i = 0;
                While (i < 5) 
            {
                a[i] = b + 1;
                Let u: Number = i + 1;
                If (a[u] == 10) 
                {
                    If(b==5)
                    {
                        Return a[i];
                    }
                    Elif(b==5)
                    {
                        i=i+1;
                    }
                    Else
                    {
                        Return 0;
                    }
                }
            }
                a[2] = Call(foo, [2]) + Call(foo, [Call(bar, [2, 3])]);
                Return a[2] + Call(foo, [2]) + Call(foo, [Call(bar, [2, 3])]);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,358))
    def testcase86(self):
        input = """Function foo(a[5],b) 
        {
                Let i = 0;
                While (i < 5) 
            {
                a[i] = b + 1;
                Let u: Number = i + 1;
                If (a[u] == 10) 
                {
                    If(b==5)
                    {
                        Return a[i];
                    }
                    Elif(b==5)
                    {
                        i=i+1;
                    }
                    Else
                    {
                        Return 0;
                    }
                }
            }
                a[2] = Call(foo, [2]) + Call(foo, [Call(bar, [2, 3])]);
                Return a[2] + Call(foo, [2]) + Call(foo, [Call(bar, [2, 3])]);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,359))
    def testcase87(self):
        input = """Function foo(a[5], b) {
                Let i = 0;
                While (i < 5) {
                    While(i){
                    a[i] = b + 1;
                    Let u: Number = i + 1;
                    If (a[u] == 10) {
                    Return a[i];
                    }
                }
                }
                
                Return ;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,360))
    def testcase88(self):
        input = """Function foo(a[5], b) {
                Let i = 0;
                While (i < 5) {
                    While(i){
                    a[i] = b + 1;
                    Let u :: Number = i + 1;
                    If (a[u] == 10) {
                    Return a[i];
                    }
                }
                }
                Return ;
                }"""
        expect = "Error on line 6 col 27: :"
        self.assertTrue(TestParser.checkParser(input,expect,361))
    def testcase89(self):
        input = """Constant $a = 10;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,362))
    def testcase90(self):
        input = """Constant $a = 10;
                Function foo(a[5], b) {
                Constant $b: String = "Story of Yanxi Place";
                Let i = 0;
                While (i < 5) {
                a[i] = (b + 1) * $a;
                Let u: Number = i + 1;
                If (a[u] == 10) {
                Return $b;
                }
                i = i + 1;
                }
                a[2] = a[b["name","first"]] + 4;
                Return $b + ": Done";
                }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,363))
    def testcase91(self):
        input = """Constant $a = 10;
                Function foo(a[5], b) {
                Constant $b: String = "Story of Yanxi Place";
                Let i = 0;
                While (i < 5) {
                a[i] = (b + 1) * $a;
                Let u: Number = i + 1;
                If (a[u] == 10) {
                Return $b;
                }
                i = i + 1;
                }
                a[2] = a[b["name","first"]] + 4;
                Return $b + ": Done";
                }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,364))
    def testcase92(self):
        input = """Constant $a = 10;
                Function foo(a[5], b) {
                Constant $b: String: = "Story of Yanxi Place";
                Let i = 0;
                While (i < 5) {
                a[i] = (b + 1) * $a;
                Let u: Number = i + 1;
                If (a[u] == 10) {
                Return $b;
                }
                i = i + 1;
                }
                a[2] = a[b["name","first"]] + 4;
                Return $b + ": Done";
                }"""
        expect = "Error on line 3 col 35: :"
        self.assertTrue(TestParser.checkParser(input,expect,365))
    def testcase93(self):
        input = """Constant $a = 10;
                Function foo(a[5], b) {
                Constant $b: String = "Story of Yanxi Place";
                Let i = 0;
                While (i < 5) {
                a[i] = (b + 1) * $a;
                Let u: Number = i + 1;
                If (a[u] == 10) {
                Return $b;
                }
                i = i + 1;
                a[2] = a[b["name","first"]] + 4;
                Return $b + ": Done";
                }"""
        expect = "Error on line 14 col 17: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,366))
    def testcase94(self):
        input = """Constant $a = 10;
                Function foo() {
                Constant $b: String = "Story of Yanxi Place";
                Let i = 0;
                While (i < 5) {
                a[i] = (b + 1) * $a;
                Let u: Number = i + 1;
                If (a[u] == 10) {
                Return $b;
                }
                i = i + 1;
                }
                a[2] = a[b["name","first"]] + 4;
                Return $b + ": Done";
                }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,367))

    def testcase96(self):
        input = """
                Function foo(a) {
                    Let b: String = a["name"] + a["address"];
                    a+=["name"] = "Qianqing Palace";
                }"""
        expect = "Error on line 4 col 21: +"
        self.assertTrue(TestParser.checkParser(input,expect,368))
    def testcase97(self):
        input = """
                Function foo(a) {
                    Let b: String = a["name"] + a["address"];
                    Let c: JSON = {};
                    a["name"] = "Qianqing Palace";
                    b= True;
                    While(b==2){
                    }
                    Return ;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,369))
    def testcase1000(self):
        input = """  
        Function foo(a) {
a[Call(foo, [2])] = a[b["namea"]["first"]] + 4;
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,10000))

    
 