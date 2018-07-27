import os
import wx

class PhotoCtrl(wx.Frame):
    def __init__(self,parent,title):
        super(PhotoCtrl,self).__init__(parent,title = title,
        size = (1050,750))

        self.panel = wx.Panel(self)
        self.InitUI()
        self.createWidgets()
        self.Centre()

    def InitUI(self):

        distros = ['Brighten', 'Darken', 'Invert', 'Posterize', 'Solar']
        cb = wx.ComboBox(self.panel, choices=distros,pos=(300,3000),style=wx.CB_READONLY)

        self.st = wx.StaticText(self.panel, label='',)

        sizer = wx.GridBagSizer(4,4)
        self.browseBtn = wx.Button(self.panel, label='Browse')
        sizer.Add(self.browseBtn, pos=(1,3), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=5)
        cb.Bind(wx.EVT_COMBOBOX, self.OnSelect)

        self.panel.SetSizer(sizer)
        cb.SetSize((400, 30))
        cb.Centre()
        cb.Show(True)

    def OnSelect(self, e):
        i = e.GetString()
        self.st.SetLabel(i)

    def createWidgets(self):
        instructions = 'Browse for an image'
        img = wx.Image(240,240)
        self.imageCtrl = wx.StaticBitmap(self.panel, wx.ID_ANY,
                                         wx.Bitmap(img))

        instructLbl = wx.StaticText(self.panel, label=instructions)
        self.photoTxt = wx.TextCtrl(self.panel, size=(400,-1))
        self.browseBtn.Bind(wx.EVT_BUTTON, self.onBrowse)

        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.mainSizer.Add(wx.StaticLine(self.panel, wx.ID_ANY),
                           0, wx.ALL|wx.EXPAND, 5)
        self.mainSizer.Add(instructLbl, 0, wx.ALL, 5)
        self.mainSizer.Add(self.imageCtrl, 0, wx.ALL, 5)
        self.sizer.Add(self.photoTxt, 0, wx.ALL, 5)
        self.sizer.Add(self.browseBtn, 0, wx.ALL, 5)
        self.mainSizer.Add(self.sizer, 0, wx.ALL, 5)

        self.panel.SetSizer(self.mainSizer)
        self.mainSizer.Fit(self.panel)

        self.panel.Layout()

    def onBrowse(self, event):
        """
        Browse for file
        """
        wildcard = "JPEG files (*.jpg)|*.jpg"
        dialog = wx.FileDialog(None, "Choose a file",
                               wildcard=wildcard,
                               style=wx.FD_OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            self.photoTxt.SetValue(dialog.GetPath())
        dialog.Destroy()
        self.onView()

    def onView(self):
        filepath = self.photoTxt.GetValue()
        img = wx.Image(filepath, wx.BITMAP_TYPE_ANY)
        W = img.GetWidth()
        H = img.GetHeight()
        if W > H:
            NewW = self.PhotoMaxSize
            NewH = self.PhotoMaxSize * H / W
        else:
            NewH = self.PhotoMaxSize
            NewW = self.PhotoMaxSize * W / H
        img = img.Scale(NewW,NewH)

        self.imageCtrl.SetBitmap(wx.Bitmap(img))
        self.panel.Refresh()


def main():
    app = wx.App()
    frame = PhotoCtrl(None,title = 'Photoshop')
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
