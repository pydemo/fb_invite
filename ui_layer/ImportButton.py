import wx, sys, time
import copy
from ui.include.Base import Base, reciever
from ui.include.utils import dict2, exception
from pprint import pprint as pp
e=sys.exit


class PopupPanel(wx.Panel, Base):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        #self.SetBackgroundColour("CADET BLUE")
        sizer = wx.BoxSizer(wx.VERTICAL)
        if 1:
            self.b_start=b_start=wx.Button(self, -1, "Start", size=(75,35))
            sizer.Add(b_start, 0, wx.RIGHT|wx.ALIGN_RIGHT)
        pre=[]
        pre.append(dict2(name='Type', value='CLI'))
        pre.append(dict2(name='Url', value='http'))
        pre.append(dict2(name='Pipeline', value='test/test/test'))
        pre.append(dict2(name='Mapping', value='VA_Thermo.Column_Mapping.csv'))
        pre.append(dict2(name='Service', value='VADataTransferMasQC_MTMS'))
        pre.append(dict2(name='Source', value='MAS_LIMS_VA_API_export.csv'))
        
        pre.append(dict2(name='Vendor', value='=="Thermo Fisher "'))
        pre.append(dict2(name='Ratio', value='43/180'))
        
        #bmp = wx.ArtProvider.GetBitmap(wx.ART_INFORMATION, wx.ART_OTHER, (16, 16))
        #titleIco = wx.StaticBitmap(self, wx.ID_ANY, bmp)
        g_sizer = wx.FlexGridSizer(rows=len(pre), cols=2, hgap=3, vgap=3)
        for pr in pre:
            
            
            
            st_name = wx.StaticText(self, -1, '%s:' % pr.name)
            st_value = wx.StaticText(self, -1, pr.value)
            g_sizer.Add(st_name, 0, wx.ALIGN_LEFT)
            g_sizer.Add(st_value, 1, wx.ALL|wx.EXPAND)
            #h_sizer=wx.BoxSizer(wx.HORIZONTAL)
            #h_sizer.Add(st_name, 0,wx.RIGHT|wx.CENTER); h_sizer.Add(st_value, 1,wx.LEFT| wx.CENTER)
        sizer.Add(g_sizer, 1, wx.ALL|wx.EXPAND, 5)
        
        self.Bind(wx.EVT_LEFT_DOWN, self.OnMouseLeftDown)
        self.Bind(wx.EVT_MOTION, self.OnMouseMotion)
        self.Bind(wx.EVT_LEFT_UP, self.OnMouseLeftUp)
        self.Bind(wx.EVT_RIGHT_UP, self.OnRightUp)
        b_start.Bind(wx.EVT_BUTTON, self.OnStart)
        self.SetSize((250,200))
        #self.SetSizer(sizer)
        self.SetAutoLayout(True)
        #self.SetSizeHints(250,300,500,400)
        self.SetSizer(sizer)
        #sizer.Fit(self)
        #sizer.SetSizeHints(self)
        self.Layout()
        
        #self.Layout()
        #self.Fit()
    def OnStart(self,evt):
        self.send('ib_StartImport', ())
        self.Parent.close()
        
    def OnMouseLeftDown(self, evt):
        self.Refresh()
        self.ldPos = evt.GetEventObject().ClientToScreen(evt.GetPosition())
        self.wPos = self.ClientToScreen((0,0))
        self.panel.CaptureMouse()

    def OnMouseMotion(self, evt):
        if evt.Dragging() and evt.LeftIsDown():
            dPos = evt.GetEventObject().ClientToScreen(evt.GetPosition())
            nPos = (self.wPos.x + (dPos.x - self.ldPos.x),
                    self.wPos.y + (dPos.y - self.ldPos.y))
            self.Move(nPos)

    def OnMouseLeftUp(self, evt):
        if self.panel.HasCapture():
            self.panel.ReleaseMouse()

    def OnRightUp(self, evt):
        self.Show(False)
        self.Destroy()


########################################################################
class TestPopup(wx.PopupWindow):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, parent, style):
        """Constructor"""
        wx.PopupWindow.__init__(self, parent, wx.DEFAULT_FRAME_STYLE|wx.FRAME_FLOAT_ON_PARENT)

        panel = PopupPanel(self)
        

        sizer = wx.BoxSizer()
        sizer.Add(panel, 1, wx.ALL|wx.EXPAND)
        self.SetSizer(sizer)
        sz = panel.GetSize()
        
        self.SetSize( (sz.width, sz.height) )        
        #self.SetSize( (sz.width+20, sz.height+20) )
        
        

        #st.Bind(wx.EVT_LEFT_DOWN, self.OnMouseLeftDown)
        #st.Bind(wx.EVT_MOTION, self.OnMouseMotion)
        #st.Bind(wx.EVT_LEFT_UP, self.OnMouseLeftUp)
        #st.Bind(wx.EVT_RIGHT_UP, self.OnRightUp)

        #wx.CallAfter(panel.Fit)    
    def close(self):
        self.Show(False)
        self.Destroy()

def dialog(func):
    def wrapper(*args, **kwargs):
        import ui.dialog.DiaLog as DL
        DL.show('Import started...')
        original_return_val = func(*args, **kwargs)
        return original_return_val
    return wrapper
    
#---------------------------------------------------------------------------
class Controller(object):
    def __init__(self):
        self.sub('ib_StartImport')
    @exception
    @dialog
    def ib_StartImport(self, message, arg2=None, **kwargs):
        print('ib_StartImport')
        for i in range(10):
            self.send('dia_Log', (i))
            time.sleep(1)
def exception(func):
    def wrapper(*args, **kwargs):
        
        try:
            original_return_val = func(*args, **kwargs)
        except:
            ex()
        
        return original_return_val
    return wrapper
    
        
class ImportButton (wx.Button, Base, Controller):
    def __init__(self, parent,*args, **kwargs):
        pp(args)
        Base.__init__(self, parent)
        wx.Button.__init__(self, parent,*args,  **kwargs)

        self.SetBackgroundColour(wx.NullColour) 
        tt = wx.ToolTip('Ortho data import.')
        self.SetToolTip(tt)
        self.sub('ibtn_Refresh')
        self.Bind(wx.EVT_BUTTON, self.OnImport)
        self.Bind(wx.EVT_KILL_FOCUS, self.OnFocusLost)
        self.win=None
        Controller.__init__(self)
    def OnFocusLost(self, evt):
        print('OnFocusLost')
        if self.win:
            self.win.Show(False)
            self.win.Destroy()
        else:
            print('no win')
    def OnImport(self, evt):
        if not self.win:
            self.win=win = TestPopup(self.GetTopLevelParent(), wx.SIMPLE_BORDER)

            btn = evt.GetEventObject()
            pos = btn.ClientToScreen( (0,0) )
            sz =  btn.GetSize()
            x,y=pos
            wsz=self.win.GetSize()
            print(pos, sz, wsz)
            win.Position((x-(wsz[0]-sz[0]),y),(0,sz[1]))

            win.Show(True)
        else:
            self.win.Show(False)
            self.win.Destroy()
    #@reciever
    def ibtn_Refresh(self, message, arg2=None, **kwargs):
        #print('ibtn_Refresh')
        self.SetFocus()
    def _Refresh(self):
        #self.Refresh()
        self.SetFocus()
        #self.send('grid_Refresh', ())



        