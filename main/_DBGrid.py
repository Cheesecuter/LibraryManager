import wx
import wx.grid
import csv
import _FrozenDir
import _Database
import _lang


class GridControl(wx.Frame):

    def __init__(self, superior, lang):

        self._lang_ = lang
        #self._lang_ = _lang._Language()
        self.srcPath = _FrozenDir.app_path()+r'\\src'
        wx.Frame.__init__(self, parent=superior,
                          style=wx.DEFAULT_FRAME_STYLE ^ (wx.RESIZE_BORDER | wx.MAXIMIZE_BOX | wx.MINIMIZE_BOX))
        self.SetTitle(self._lang_._dbgrid_FrameTitle)
        iconPath = self.srcPath+r'\\icon.png'
        self.SetIcon(wx.Icon(iconPath))
        self.SetSize((800, 600))
        self.Center()
        self.panelGrid = wx.Panel(
            self, -1, pos=(0, 0), size=(800, 600))
        self.panelGrid.SetBackgroundColour("#eeeeee")

        self.grid = wx.grid.Grid(self.panelGrid, -1, pos=(0, 0),
                                 size=(780, 560), style=wx.WANTS_CHARS, name=self._lang_._dbgrid_GridTitle)
        self.grid.CreateGrid(100, 6, selmode=wx.grid.Grid.SelectCells)
        self.grid.EnableEditing(False)

        self.grid.SetColLabelValue(0, self._lang_._dbgrid_gridCOL_Book_Number)
        self.grid.SetColSize(0, 100)
        self.grid.SetColLabelValue(1, self._lang_._dbgrid_gridCOL_Book_Name)
        self.grid.SetColSize(1, 100)
        self.grid.SetColLabelValue(2, self._lang_._dbgrid_gridCOL_Author)
        self.grid.SetColSize(2, 100)
        self.grid.SetColLabelValue(3, self._lang_._dbgrid_gridCOL_Publish_Date)
        self.grid.SetColSize(3, 130)
        self.grid.SetColLabelValue(4, self._lang_._dbgrid_gridCOL_Publisher)
        self.grid.SetColSize(4, 100)
        self.grid.SetColLabelValue(5, self._lang_._dbgrid_gridCOL_Price)
        self.grid.SetColSize(5, 100)

        csvPath = self.srcPath+r'\\books.csv'
        with open(csvPath, encoding='UTF-8-SIG') as f:
            rowNo = 0
            colNo = 0
            bookNo = 1
            self.grid.SetCellValue(0, 0, self._lang_._dbgrid_GridTitle)
            for row in csv.reader(f, skipinitialspace=True):
                if(row == []):
                    continue
                self.grid.SetCellValue(rowNo, 0, str('%06d' % bookNo))
                self.grid.SetCellValue(rowNo, 1, row[0])
                self.grid.SetCellValue(rowNo, 2, row[1])
                self.grid.SetCellValue(rowNo, 3, row[2])
                self.grid.SetCellValue(rowNo, 4, row[3])
                self.grid.SetCellValue(rowNo, 5, row[4])
                rowNo += 1
                bookNo += 1
                pass
        self._DB = _Database.Database()
