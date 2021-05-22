import wx
from ui_layer.common import * 
from ui_layer.utils import exception


from ui_layer.utils import ex
class StartFrame(wx.Frame):#, Base):
    @exception
    def __init__(self, parent, headless):
        wx.Frame.__init__(self, parent, size = START_SIZE, pos = START_POS)
        self.Show(False)
        
        #self.Freeze()
        
        if not headless:
            from ui_layer.DataLite import DataLite
            self.frame = frame= DataLite(self, 'FB UI')

        #self.Thaw()

