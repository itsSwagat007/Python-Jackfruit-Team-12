import wx

# Caesar cipher logic
def caesar_cipher(text, shift, mode='encode'):
    if mode == 'decode':
        shift = -shift
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base + shift) % 26 + base)
        else:
            result += ch
    return result

app = wx.App(False)

frame = wx.Frame(None, title="Caesar Cipher", size=(520, 390))
panel = wx.Panel(frame)

panel.SetBackgroundColour("yellow")


heading = wx.StaticText(panel, label="🔐 Caesar Cipher Tool", pos=(150, 10))
heading.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT,
                        wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))


input_label = wx.StaticText(panel, label="Input Text:", pos=(30, 50))
input_box = wx.TextCtrl(panel, pos=(30, 70), size=(450, 80), style=wx.TE_MULTILINE)


shift_label = wx.StaticText(panel, label="➡️ Shift:", pos=(30, 170))
shift_box = wx.TextCtrl(panel, pos=(100, 165), size=(50, 25))


encode_btn = wx.Button(panel, label="🔒 Encode", pos=(200, 160), size=(100, 35))
decode_btn = wx.Button(panel, label="🗝️ Decode", pos=(320, 160), size=(100, 35))

output_label = wx.StaticText(panel, label="Output:", pos=(30, 220))
output_box = wx.TextCtrl(panel, pos=(30, 240),
                         size=(450, 80),
                         style=wx.TE_MULTILINE | wx.TE_READONLY)

def on_encode(event):
    text = input_box.GetValue()
    shift = int(shift_box.GetValue())  # direct conversion
    output_box.SetValue(caesar_cipher(text, shift, "encode"))

def on_decode(event):
    text = input_box.GetValue()
    shift = int(shift_box.GetValue())  # direct conversion
    output_box.SetValue(caesar_cipher(text, shift, "decode"))

encode_btn.Bind(wx.EVT_BUTTON, on_encode)
decode_btn.Bind(wx.EVT_BUTTON, on_decode)

frame.Show()
app.MainLoop()
