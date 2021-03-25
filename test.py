import wx
from notificationbar import NotificationBar, NOTIFY_SHORT, NOTIFY_LONG
import threading


class TestFrame(wx.Frame):

    def __init__(self):
        super().__init__(parent=None, id=-1, title="Test Notification")

        pnl = wx.Panel(self, -1)
        btn = wx.Button(pnl, -1, "Open Notification")
        btn.Bind(wx.EVT_BUTTON, self._on_notify_btn, btn)
        gs = wx.GridSizer(cols=1, rows=1, vgap=0, hgap=0)
        gs.Add(btn, 0, wx.ALIGN_CENTER, 0)
        pnl.SetSizer(gs)
        gs = wx.GridSizer(cols=1, rows=1, vgap=0, hgap=0)
        gs.Add(pnl, 1, wx.EXPAND|wx.ALL, 0)
        self.SetSizer(gs)
        self.SetSize(200, 200)
    
    def _on_notify_btn(self, evt):
        def _notify():
            wx.CallAfter(NotificationBar, self, -1, "",
                         "This is an exmaple text\nto be displayed on\nthe Screen at any onetime",
                         timeout=NOTIFY_SHORT)
        threading.Thread(target=_notify).start()


if __name__ == '__main__':
    app = wx.App()
    TestFrame().Show()
    app.MainLoop()
