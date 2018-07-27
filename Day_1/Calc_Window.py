import wx


class Calc(wx.Frame):
    numbers = ("")
    def Operations(self, numbers):
        def Addition(a,b):
            sum = a + b
            sum = str(sum)
            self.display.WriteText(sum)

        def Subtraction(a,b):
            difference = a - b
            difference = str(difference)
            self.display.WriteText(difference)

        def Multiplication(a,b):
            c = 0
            count = 0
            while(count < b):
                count += 1
                c += a
            product = c
            product = str(c)
            self.display.WriteText(product)

        def Division(a,b):
            count = 0
            while(a >= b):
                count += 1
                a -= b
            quotient = count
            quotient = str(quotient)
            self.display.WriteText(quotient)


        def Exponent(a,b):
            c = 1
            count = 0
            while(count < b):
                count += 1
                c *= a
            power = c
            power = str(power)
            self.display.WriteText(power)

        def Modulo(a,b):
            count = 0
            while(a >= b):
                count += 1
                a -= b
            remainder = a
            remainder = str(remainder)
            self.display.WriteText(remainder)

        def Bintodec(a):
            b = a.split('.')
            c = 0
            d = 0
            for i in range(len(b)):
                for x in range(len(b[i])):
                    if i == 0:
                        c += int(b[i][x])*(2**(len(b[i])-(x + 1)))
                    else:
                        d += int(b[i][x])*(2**(x-len(b[i])))
            e = str(c + d)
            self.display.WriteText(e)


        def Bintooc(a):
            left = ""
            right = ""
            if "." in a:
                [left, right] = a.split(".")
            else:
                left = a
            output = ""
            output2 = ""


            if len(left) % 3 == 1:
                left = "00" + left
            elif len(left) % 3 == 2:
                left = "0" + left

            if len(right) % 3 == 1:
                right = right + "00"
            elif len(right) % 3 == 2:
                right = right + "0"

            for value in range(0, len(left), 3):
                cur_group = left[value: value + 3]
                if cur_group == "000":
                    output = output + "0"
                elif cur_group == "001":
                    output = output + "1"
                elif cur_group == "010":
                    output = output + "2"
                elif cur_group == "011":
                    output = output + "3"
                elif cur_group == "100":
                    output = output + "4"
                elif cur_group == "101":
                    output = output + "5"
                elif cur_group == "110":
                    output = output + "6"
                elif cur_group == "111":
                    output = output + "7"

            if len(right) == 0:
                output2 = "0"
            else:
                for value in range(0, len(right), 3):
                    cur_group = right[value: value + 3]
                    if cur_group == "000":
                        output2 = output2 + "0"
                    elif cur_group == "001":
                        output2 = output2 + "1"
                    elif cur_group == "010":
                        output2 = output2 + "2"
                    elif cur_group == "011":
                        output2 = output2 + "3"
                    elif cur_group == "100":
                        output2 = output2 + "4"
                    elif cur_group == "101":
                        output2 = output2 + "5"
                    elif cur_group == "110":
                        output2 = output2 + "6"
                    elif cur_group == "111":
                        output2 = output2 + "7"

            if output == "0":
                self.display.WriteText (output)
            else:
                self.display.WriteText(output + "." + output2)

        def Bintohex(a):
            left = ""
            right = ""
            if "." in a:
                [left, right] = a.split(".")
            else:
                left = a
            output = ""
            output2 = ""


            if len(left) % 4 == 1:
                left = "000" + left
            elif len(left) % 4 == 2:
                left = "00" + left
            elif len(left) % 4 == 3:
                left = "0" + left

            if len(right) % 4 == 1:
                right = right + "000"
            elif len(right) % 4 == 2:
                right = right + "00"
            elif len(right) % 4 == 3:
                right = "0" + right

            for value in range(0, len(left), 4):
                cur_group = left[value: value + 4]
                if cur_group == "0000":
                    output = output + "0"
                elif cur_group == "0001":
                    output = output + "1"
                elif cur_group == "0010":
                    output = output + "2"
                elif cur_group == "0011":
                    output = output + "3"
                elif cur_group == "0100":
                    output = output + "4"
                elif cur_group == "0101":
                    output = output + "5"
                elif cur_group == "0110":
                    output = output + "6"
                elif cur_group == "0111":
                    output = output + "7"
                elif cur_group == "1000":
                    output = output + "8"
                elif cur_group == "1001":
                    output = output + "9"
                elif cur_group == "1010":
                    output = output + "A"
                elif cur_group == "1011":
                    output = output + "B"
                elif cur_group == "1100":
                    output = output + "C"
                elif cur_group == "1101":
                    output = output + "D"
                elif cur_group == "1110":
                    output = output + "E"
                elif  cur_group == "1111":
                    output = output + "F"


            if len(right) == 0:
                output2 = "0"
            else:
                for value in range(0, len(right), 4):
                    cur_group = right[value: value + 4]
                    if cur_group == "0000":
                        output2 = output2 + "0"
                    elif cur_group == "0001":
                        output2 = output2 + "1"
                    elif cur_group == "0010":
                        output2 = output2 + "2"
                    elif cur_group == "0011":
                        output2 = output2 + "3"
                    elif cur_group == "0100":
                        output2 = output2 + "4"
                    elif cur_group == "0101":
                        output2 = output2 + "5"
                    elif cur_group == "0110":
                        output2 = output2 + "6"
                    elif cur_group == "0111":
                        output2 = output2 + "7"
                    elif cur_group == "1000":
                        output2 = output2 + "8"
                    elif cur_group == "1001":
                        output2 = output2 + "9"
                    elif cur_group == "1010":
                        output2 = output2 + "A"
                    elif cur_group == "1011":
                        output2 = output2 + "B"
                    elif cur_group == "1100":
                        output2 = output2 + "C"
                    elif cur_group == "1101":
                        output2 = output2 + "D"
                    elif cur_group == "1110":
                        output2 = output2 + "E"
                    elif  cur_group == "1111":
                        output2 = output2 + "F"

            if output == "0":
                self.display.WriteText (output)
            else:
                self.display.WriteText(output + "." + output2)


        if '+' in numbers:
            [a, b] = numbers.split("+")
            Addition(int(a),int(b))
        elif '-' in numbers:
            [a, b] = numbers.split("-")
            Subtraction(int(a), int(b))
        elif '*' in numbers:
            [a, b] = numbers.split("*")
            Multiplication(int(a), int(b))
        elif '/' in numbers:
            [a, b] = numbers.split("/")
            Division(int(a), int(b))
        elif '^' in numbers:
            [a, b] = numbers.split("^")
            Exponent(int(a), int(b))
        elif '%' in numbers:
            [a, b] = numbers.split("%")
            Modulo(int(a), int(b))
        elif 'Binary to Decimal' in numbers:
            [a, b] = numbers.split("Binary to Decimal")
            Bintodec(str(a))
        elif 'Binary to Octal' in numbers:
            [a, b] = numbers.split("Binary to Octal")
            Bintooc(str(a))
        elif 'Binary to Hexadecimal' in numbers:
            [a, b] = numbers.split("Binary to Hexadecimal")
            Bintohex(str(a))

    def __init__(self, parent, title):
        super(Calc, self).__init__(parent, title=title,
            size=(700, 500))

        self.InitUI()
        self.Centre()

    def InitUI(self):

        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

        clear_button = (wx.Button(self, label='C'))
        power_button = (wx.Button(self, label='^'))
        seven_button = (wx.Button(self, label='7'))
        eight_button = (wx.Button(self, label='8'))
        nine_button = (wx.Button(self, label='9'))
        modulo_button = (wx.Button(self, label='%'))
        divide_button = (wx.Button(self, label='/'))
        four_button = (wx.Button(self, label='4'))
        five_button = (wx.Button(self, label='5'))
        six_button = (wx.Button(self, label='6'))
        bin_to_dec_button = (wx.Button(self, label='Binary to Decimal'))
        multiply_button = (wx.Button(self, label='*'))
        one_button = (wx.Button(self, label='1'))
        two_button = (wx.Button(self, label='2'))
        three_button = (wx.Button(self, label='3'))
        bin_to_oc_button = (wx.Button(self, label='Binary to Octal'))
        subtract_button = (wx.Button(self, label='-'))
        decimal_button = (wx.Button(self, label='.'))
        zero_button = (wx.Button(self, label='0'))
        equals_button = (wx.Button(self, label='='))
        bin_to_hex_button = (wx.Button(self, label='Binary to Hex'))
        add_button = (wx.Button(self, label='+'))

        self.Bind(wx.EVT_BUTTON, self.onButton_clear, clear_button)
        self.Bind(wx.EVT_BUTTON, self.onButton_power, power_button)
        self.Bind(wx.EVT_BUTTON, self.onButton_7, seven_button)
        self.Bind(wx.EVT_BUTTON, self.onButton_8, eight_button)
        self.Bind(wx.EVT_BUTTON, self.onButton_9, nine_button)
        self.Bind(wx.EVT_BUTTON, self.onButton_modulo, modulo_button)
        self.Bind(wx.EVT_BUTTON, self.onButton_divide, divide_button)
        self.Bind(wx.EVT_BUTTON, self.onButton_4, four_button)
        self.Bind(wx.EVT_BUTTON, self.onButton_5, five_button)
        self.Bind(wx.EVT_BUTTON, self.onButton_6, six_button)
        self.Bind(wx.EVT_BUTTON, self.onButton_bin_to_dec, bin_to_dec_button)
        self.Bind(wx.EVT_BUTTON, self.onButton_multiply, multiply_button)
        self.Bind(wx.EVT_BUTTON, self.onButton_1, one_button)
        self.Bind(wx.EVT_BUTTON, self.onButton_2, two_button)
        self.Bind(wx.EVT_BUTTON, self.onButton_3, three_button)
        self.Bind(wx.EVT_BUTTON, self.onButton_bin_to_oc, bin_to_oc_button)
        self.Bind(wx.EVT_BUTTON, self.onButton_subtract, subtract_button)
        self.Bind(wx.EVT_BUTTON, self.onButton_decimal, decimal_button)
        self.Bind(wx.EVT_BUTTON, self.onButton_0, zero_button)
        self.Bind(wx.EVT_BUTTON, self.onButton_equals, equals_button)
        self.Bind(wx.EVT_BUTTON, self.onButton_bin_to_hex, bin_to_hex_button)
        self.Bind(wx.EVT_BUTTON, self.onButton_add, add_button)

        vbox = wx.BoxSizer(wx.VERTICAL)
        self.display = wx.TextCtrl(self, style=wx.TE_RIGHT)
        vbox.Add(self.display, flag=wx.EXPAND|wx.TOP|wx.BOTTOM, border=4)
        gs = wx.GridSizer(5, 6, 5, 5)

        gs.AddMany( [(wx.StaticText(self), wx.EXPAND),
            (wx.StaticText(self), wx.EXPAND),
            (wx.StaticText(self), wx.EXPAND),
            (wx.StaticText(self), wx.EXPAND),
            (clear_button, 0, wx.EXPAND),
            (power_button, 0, wx.EXPAND),
            (seven_button, 0, wx.EXPAND),
            (eight_button, 0, wx.EXPAND),
            (nine_button, 0, wx.EXPAND),
            (wx.StaticText(self), wx.EXPAND),
            (modulo_button, 0, wx.EXPAND),
            (divide_button, 0, wx.EXPAND),
            (four_button, 0, wx.EXPAND),
            (five_button, 0, wx.EXPAND),
            (six_button, 0, wx.EXPAND),
            (wx.StaticText(self), wx.EXPAND),
            (bin_to_dec_button, 0, wx.EXPAND),
            (multiply_button, 0, wx.EXPAND),
            (one_button, 0, wx.EXPAND),
            (two_button, 0, wx.EXPAND),
            (three_button, 0, wx.EXPAND),
            (wx.StaticText(self), wx.EXPAND),
            (bin_to_oc_button, 0, wx.EXPAND),
            (subtract_button, 0, wx.EXPAND),
            (decimal_button, 0, wx.EXPAND),
            (zero_button, 0, wx.EXPAND),
            (equals_button, 0, wx.EXPAND),
            (wx.StaticText(self), wx.EXPAND),
            (bin_to_hex_button, 0, wx.EXPAND),
            (add_button, 0, wx.EXPAND) ])

        vbox.Add(gs, proportion=1, flag=wx.EXPAND)
        self.SetSizer(vbox)

    def onButton_clear(self, event):
        self.display.Clear()
        self.numbers = ""
        return

    def onButton_power(self, event):
        self.display.WriteText("^")
        self.numbers += ('^')

    def onButton_7(self, event):
        self.display.WriteText("7")
        self.numbers += ('7')

    def onButton_8(self, event):
        self.display.WriteText("8")
        self.numbers += ('8')

    def onButton_9(self, event):
        self.display.WriteText("9")
        self.numbers += ('9')

    def onButton_modulo(self, event):
        self.display.WriteText("%")
        self.numbers += ('%')

    def onButton_divide(self, event):
        self.display.WriteText("/")
        self.numbers += ('/')

    def onButton_4(self, event):
        self.display.WriteText("4")
        self.numbers += ('4')

    def onButton_5(self, event):
        self.display.WriteText("5")
        self.numbers += ('5')

    def onButton_6(self, event):
        self.display.WriteText("6")
        self.numbers += ('6')

    def onButton_bin_to_dec(self, event):
        self.display.WriteText(" --Binary to Dec-- ")
        self.numbers += ('Binary to Decimal')

    def onButton_multiply(self, event):
        self.display.WriteText("*")
        self.numbers += ('*')

    def onButton_1(self, event):
        self.display.WriteText("1")
        self.numbers += ('1')

    def onButton_2(self, event):
        self.display.WriteText("2")
        self.numbers += ('2')

    def onButton_3(self, event):
        self.display.WriteText("3")
        self.numbers += ('3')

    def onButton_bin_to_oc(self, event):
        self.display.WriteText(" --Binary to Octal-- ")
        self.numbers += ('Binary to Octal')

    def onButton_subtract(self, event):
        self.display.WriteText("-")
        self.numbers += ('-')

    def onButton_decimal(self, event):
        self.display.WriteText(".")
        self.numbers += ('.')

    def onButton_0(self, event):
        self.display.WriteText("0")
        self.numbers += ('0')

    def onButton_equals(self, event):
        self.display.WriteText("=")
        self.Operations(self.numbers)

    def onButton_bin_to_hex(self, event):
        self.display.WriteText(" --Binary to Hexadecimal-- ")
        self.numbers += ('Binary to Hexadecimal')

    def onButton_add(self, event):
        self.display.WriteText("+")
        self.numbers += ('+')


def main():

    app = wx.App()
    ex = Calc(None, title='Calculator')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
