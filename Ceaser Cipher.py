import wx

class CaesarCipherFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Caesar Cipher Tool', size=(750, 650))
        
        self.SetBackgroundColour(wx.Colour(0, 0, 0))
        
        panel = wx.Panel(self)
        panel.SetBackgroundColour(wx.Colour(0, 0, 0))
        
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        
        main_sizer.AddSpacer(20)
        
        
        title = wx.StaticText(panel, label='🔐 Caesar Cipher Tool')
        title_font = wx.Font(36, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        title.SetFont(title_font)
        title.SetForegroundColour(wx.Colour(0, 255, 0))  
        main_sizer.Add(title, 0, wx.CENTER, 0)
        
        main_sizer.AddSpacer(5)
        

        line1 = wx.Panel(panel, size=(700, 3))
        line1.SetBackgroundColour(wx.Colour(0, 255, 0))
        main_sizer.Add(line1, 0, wx.CENTER, 0)
        
        main_sizer.AddSpacer(15)
        
       
        input_box = wx.StaticBox(panel, label='Input', style=wx.BORDER_SIMPLE)
        input_box.SetForegroundColour(wx.Colour(0, 255, 0))
        input_box_font = wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        input_box.SetFont(input_box_font)
        
        input_box_sizer = wx.StaticBoxSizer(input_box, wx.VERTICAL)
        
        self.input_text = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.BORDER_SIMPLE)
        self.input_text.SetBackgroundColour(wx.Colour(0, 0, 0))
        self.input_text.SetForegroundColour(wx.Colour(255, 255, 255))
        input_text_font = wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        self.input_text.SetFont(input_text_font)
        self.input_text.Bind(wx.EVT_TEXT, self.on_text_change)
        input_box_sizer.Add(self.input_text, 1, wx.ALL | wx.EXPAND, 5)
        
        main_sizer.Add(input_box_sizer, 1, wx.LEFT | wx.RIGHT | wx.EXPAND, 20)
        
        main_sizer.AddSpacer(15)
        
        control_sizer = wx.BoxSizer(wx.HORIZONTAL)
        
       
        shift_label = wx.StaticText(panel, label='🔢 Shift:')
        shift_label.SetForegroundColour(wx.Colour(0, 255, 0))
        shift_label_font = wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        shift_label.SetFont(shift_label_font)
        control_sizer.Add(shift_label, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 20)
        
        control_sizer.AddSpacer(10)
        
        self.shift_input = wx.TextCtrl(panel, value='', size=(80, 30), style=wx.TE_CENTER | wx.BORDER_SIMPLE)
        self.shift_input.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.shift_input.SetForegroundColour(wx.Colour(0, 0, 0))
        shift_input_font = wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        self.shift_input.SetFont(shift_input_font)
        self.shift_input.Bind(wx.EVT_TEXT, self.on_text_change)
        control_sizer.Add(self.shift_input, 0, wx.ALIGN_CENTER_VERTICAL)
        
        control_sizer.AddSpacer(40)
        
      
        mode_label = wx.StaticText(panel, label='Mode:')
        mode_label.SetForegroundColour(wx.Colour(0, 255, 0))
        mode_label.SetFont(shift_label_font)
        control_sizer.Add(mode_label, 0, wx.ALIGN_CENTER_VERTICAL)
        
        control_sizer.AddSpacer(15)
        
        self.encode_btn = wx.Button(panel, label='🔒 Encode', size=(110, 35))
        self.encode_btn.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.encode_btn.SetForegroundColour(wx.Colour(0, 0, 0))
        button_font = wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        self.encode_btn.SetFont(button_font)
        self.encode_btn.Bind(wx.EVT_BUTTON, self.on_encode)
        control_sizer.Add(self.encode_btn, 0, wx.ALIGN_CENTER_VERTICAL)
        
        control_sizer.AddSpacer(15)
        
        self.decode_btn = wx.Button(panel, label='🔑 Decode', size=(110, 35))
        self.decode_btn.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.decode_btn.SetForegroundColour(wx.Colour(120, 120, 120))
        self.decode_btn.SetFont(button_font)
        self.decode_btn.Bind(wx.EVT_BUTTON, self.on_decode)
        control_sizer.Add(self.decode_btn, 0, wx.ALIGN_CENTER_VERTICAL)
        

        
        main_sizer.Add(control_sizer, 0, wx.ALL, 5)
        
        main_sizer.AddSpacer(15)
        

        output_box = wx.StaticBox(panel, label='Output', style=wx.BORDER_SIMPLE)
        output_box.SetForegroundColour(wx.Colour(0, 255, 0))
        output_box.SetFont(input_box_font)
        
        output_box_sizer = wx.StaticBoxSizer(output_box, wx.VERTICAL)
        
        self.output_text = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.BORDER_SIMPLE)
        self.output_text.SetBackgroundColour(wx.Colour(0, 0, 0))
        self.output_text.SetForegroundColour(wx.Colour(255, 255, 255))
        self.output_text.SetFont(input_text_font)
        output_box_sizer.Add(self.output_text, 1, wx.ALL | wx.EXPAND, 5)
        
        main_sizer.Add(output_box_sizer, 1, wx.LEFT | wx.RIGHT | wx.EXPAND, 20)
        
        panel.SetSizer(main_sizer)
        
        
        self.mode = 'encode'
        self.update_mode_buttons()
        
        self.Centre()
        self.Show()
    
    def caesar_cipher(self, text, shift, encode=True):
        if not encode:
            shift = -shift
        
        result = []
        for char in text:
            if char.isalpha():
                ascii_offset = ord('A') if char.isupper() else ord('a')
                shifted = (ord(char) - ascii_offset + shift) % 26
                result.append(chr(shifted + ascii_offset))
            else:
                result.append(char)
        
        return ''.join(result)
    
    def on_encode(self, event):
        self.mode = 'encode'
        self.update_mode_buttons()
        self.update_output()
    
    def on_decode(self, event):
        self.mode = 'decode'
        self.update_mode_buttons()
        self.update_output()
    
    def update_mode_buttons(self):
        if self.mode == 'encode':
            self.encode_btn.SetForegroundColour(wx.Colour(0, 0, 0))
            self.decode_btn.SetForegroundColour(wx.Colour(120, 120, 120))
        else:
            self.encode_btn.SetForegroundColour(wx.Colour(120, 120, 120))
            self.decode_btn.SetForegroundColour(wx.Colour(0, 0, 0))
        self.encode_btn.Refresh()
        self.decode_btn.Refresh()
    
    def on_text_change(self, event):
        self.update_output()
    
    def update_output(self):
        input_val = self.input_text.GetValue()
        shift_val = self.shift_input.GetValue()
        
        
        if not shift_val or shift_val.strip() == '':
            self.output_text.SetValue('')
            return
        
        try:
            shift = int(shift_val)
        except ValueError:
            self.output_text.SetValue('Error: Shift must be a number')
            return
        
        encode = (self.mode == 'encode')
        output = self.caesar_cipher(input_val, shift, encode)
        self.output_text.SetValue(output)

if __name__ == '__main__':
    app = wx.App()
    frame = CaesarCipherFrame()
    app.MainLoop()
