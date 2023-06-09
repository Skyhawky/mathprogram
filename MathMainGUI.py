import wx
from lib.MathIndices import *
from lib.Statistics import *
from lib.MathShapes import *

class MyFrame(wx.Frame):   
    value = "" 
    def __init__(self):        
        super().__init__(parent=None, title='math fun :)')       
        self.panel = wx.Panel(self)
        #img_file = "Logo.png"
        #img = wx.Image(img_file,wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        #self.bitmap1 = wx.StaticBitmap(self,-1,img,(0,0))
        self.my_sizer = wx.BoxSizer(wx.VERTICAL)        
        lst = ["indices","shapes and area","statistics","quit"]        
        self.combo = wx.ComboBox(self.panel, choices=lst)        
        self.my_sizer.Add(self.combo, 0, wx.ALL | wx.EXPAND, 5)        
        my_btn = wx.Button(self.panel, label='select an option')       
        self.combo.Bind(wx.EVT_COMBOBOX, self.on_selection)        
        my_btn.Bind(wx.EVT_BUTTON, self.on_press)        
        self.my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)        
        self.panel.SetSizer(self.my_sizer)

        
        self.Show()
        
    def on_press(self, event):        
        if self.value == "quit":
            exit(0)
        elif self.value == "indices":
            wx.MessageBox(indices(), "Learn about indices", wx.OK | wx.ICON_NONE)
        elif self.value == "shapes and area":
            pass
        elif self.value == "statistics":
            #wx.MessageBox("Testing...","I am testing",wx.Button())
            btn = wx.Button(self.panel,label = "hi")
            self.my_sizer.Add(btn,5, wx.ALL | wx.CENTER, 10)
            self.panel.SetSizer(self.my_sizer)
            

    def on_selection(self, event):
        self.value = self.combo.GetValue()
        



if __name__ == '__main__':    
    app = wx.App()   
    frame = MyFrame()
    #p = Panel(frame,-1)
    #icon = wx.EmptyIcon() 
    #icon.CopyFromBitmap(wx.Bitmap("icon.ico", wx.BITMAP_TYPE_ANY))
    #frame.SetIcon(wx.Icon("icon.ico")) 
    app.MainLoop()