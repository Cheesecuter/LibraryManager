import wx
import wx.grid
import time
import csv
import _InfoFrame
import _Craw
import _Database
import _DBGrid
import _FrozenDir
import _lang


class MainFrame(wx.Frame):
    def __init__(self, superior):
        self._lang_ = _lang._Language()
        wx.Frame.__init__(self, parent=superior,
                          style=wx.DEFAULT_FRAME_STYLE ^ (wx.RESIZE_BORDER | wx.MAXIMIZE_BOX | wx.MINIMIZE_BOX))
        self.SetTitle(self._lang_._mframe_FrameTitle)
        self.srcPath = _FrozenDir.app_path()+r'\\src'
        iconPath = self.srcPath+r'\\icon.png'
        self.SetIcon(wx.Icon(iconPath))
        self.SetSize((730, 400))
        self.Center()
        self.SetOwnBackgroundColour("#b3b3b3")
        # panel
        self.panelMainFrame = wx.Panel(
            self, -1, pos=(0, 0), size=(730, 400))
        self.panelMainFrame.SetBackgroundColour("#eeeeee")

        self._initOperators()
        self._initGrid()

        self._DB = _Database.Database()
        self._menuBar()
        pass

    def _menuBar(self):
        self.menuBar = wx.MenuBar()

        self.fileMenu = wx.Menu()
        self.menuBar.Append(self.fileMenu, self._lang_._mframe_menu_file)
        self._inittablessM = self.fileMenu.Append(
            -1, self._lang_._mframe_menu_file_initTables)
        self.Bind(wx.EVT_MENU, self._initTables_f, self._inittablessM)
        self._initdatasM = self.fileMenu.Append(-1,
                                                self._lang_._mframe_menu_file_initDatas)
        self.Bind(wx.EVT_MENU, self._initDatas_f, self._initdatasM)
        self.fileMenu.AppendSeparator()
        self._exitM = self.fileMenu.Append(-1,
                                           self._lang_._mframe_menu_file_exit)
        self.Bind(wx.EVT_MENU, self._exit_f, self._exitM)

        self.viewMenu = wx.Menu()
        self.menuBar.Append(self.viewMenu, self._lang_._mframe_menu_view)
        self._booksgrid_M = self.viewMenu.Append(
            -1, self._lang_._mframe_menu_view_bookGrid)
        self.Bind(wx.EVT_MENU, self._booksGrid_f, self._booksgrid_M)

        self.toolsMenu = wx.Menu()
        self.menuBar.Append(self.toolsMenu, self._lang_._mframe_menu_tools)
        self._languageM = self.toolsMenu.Append(-1,
                                                self._lang_._mframe_menu_tools_language)
        self.Bind(wx.EVT_MENU, self._language_f, self._languageM)

        self.helpMenu = wx.Menu()
        self.menuBar.Append(self.helpMenu, self._lang_._mframe_menu_help)
        self._aboutM = self.helpMenu.Append(-1,
                                            self._lang_._mframe_menu_help_about)
        self.Bind(wx.EVT_MENU, self._about_f, self._aboutM)

        self.SetMenuBar(self.menuBar)

    def _initTables_f(self, event):
        print(self._lang_._mframe_emsg__initTables_f_is_running)
        self._DB._InitTB_Books()
        print(self._lang_._mframe_emsg_Database_initiated)
        print(self._lang_._mframe_emsg__initTables_f_is_done)
        pass

    def _initDatas_f(self, event):
        print(self._lang_._mframe_emsg__initDatas_f_is_running)
        csvPath = self.srcPath+r'\\books.csv'
        f = open(csvPath, mode="w")
        f.write("")
        craw = _Craw.Craw(self._DB)
        craw._craw()
        print(self._lang_._mframe_emsg_Craw_data_initiated)
        print(self._lang_._mframe_emsg__initDatas_f_is_done)
        pass

    def _exit_f(self, event):
        print(self._lang_._mframe_emsg__exit_f_is_running)
        self.Close(True)
        wx.Exit()

    def _booksGrid_f(self, event):
        print(self._lang_._mframe_emsg__booksGrid_f_is_running)
        self.bookGrid = _DBGrid.GridControl(None,self._lang_)
        self.bookGrid.Show()
        print(self._lang_._mframe_emsg__booksGrid_f_is_done)
        pass

    def _language_f(self, event):
        print(self._lang_._mframe_emsg__language_f_is_running)
        path = self.srcPath+r'\\langType.txt'
        f = open(path,
                 mode="r", encoding="UTF-8")
        langType = f.readline()
        if(langType == 'en_US'):
            f = open(path,
                     mode="w", encoding="UTF-8")
            f.write('zh_CN')
            print(langType+" => zh_CN")
            print(self._lang_._mframe_emsg_Language_Changed_Successfully_1n)
            f.close()
        if(langType == 'zh_CN'):
            f = open(path,
                     mode="w", encoding="UTF-8")
            f.write('en_US')
            print(langType+" => en_US")
            print(self._lang_._mframe_emsg_Language_Changed_Successfully_1n)
            f.close()
        print(self._lang_._mframe_emsg__language_f_is_done)
        pass

    def _about_f(self, event):
        print(self._lang_._mframe_emsg__about_f_is_running)
        infoFrame = _InfoFrame.InfoFrame(None,self._lang_)
        infoFrame.Show(True)
        print(self._lang_._mframe_emsg__about_f_is_done)
        pass

    def _initOperators(self):
        self.txtInputBname = wx.StaticText(parent=self.panelMainFrame, id=-1, label=self._lang_._mframe_panel_txtInputBname,
                                           pos=(10, 10), size=(100, 20), style=wx.ALIGN_CENTER_HORIZONTAL)
        self.inputBname = wx.TextCtrl(
            parent=self.panelMainFrame, pos=(10, 30), size=(100, 25))
        self.btSelectBname = wx.Button(parent=self.panelMainFrame, pos=(110, 30), size=(100, 25),
                                       label=self._lang_._mframe_panel_btSelect)
        self.Bind(wx.EVT_BUTTON, self._btSelectBname_f, self.btSelectBname)
        self.btInsertBname = wx.Button(parent=self.panelMainFrame, pos=(220, 30), size=(100, 25),
                                       label=self._lang_._mframe_panel_btInsert)
        self.Bind(wx.EVT_BUTTON, self._btInsertBname_f, self.btInsertBname)
        self.btDeleteBname = wx.Button(parent=self.panelMainFrame, pos=(330, 30), size=(100, 25),
                                       label=self._lang_._mframe_panel_btDelete)
        self.Bind(wx.EVT_BUTTON, self._btDeleteBname_f, self.btDeleteBname)
        pass

    def _btSelectBname_f(self, event):
        bname = str(self.inputBname.GetValue())
        sql = '''
        select * from Books
        where Bname="'''+bname+'"'
        print(sql)
        result = self._DB._SQL(sql, False)
        colNo = 0
        print(result)
        for row in result:
            for it in row:
                self.grid.SetCellValue(0, colNo, str(it))
                colNo += 1
        pass

    def _btInsertBname_f(self, event):
        bno = str(self.grid.GetCellValue(0, 0))
        bname = str(self.grid.GetCellValue(0, 1))
        author = str(self.grid.GetCellValue(0, 2))
        publisher = str(self.grid.GetCellValue(0, 3))
        date = str(self.grid.GetCellValue(0, 4))
        price = str(self.grid.GetCellValue(0, 5))
        data = [(bno, bname, author, publisher, date, price)]
        list = [bname, author, date, publisher, price]
        self._DB.cursor.executemany(
            '''insert into Books(Bno,Bname,Author,Publisher,Date,Price) values(?,?,?,?,?,?)''', data
        )
        self._DB.conn.commit()
        csvPath = self.srcPath+r'\\books.csv'
        f = open(csvPath, mode="a", encoding="UTF-8-SIG")
        csvWtriter = csv.writer(f)
        key = [0, 1, 2, 3, 4, 5]
        dic = dict(zip(key, list))
        print(list)
        print(type(list))
        print(dic)
        print(type(dic))
        csvWtriter.writerow(list)
        pass

    def _btDeleteBname_f(self, event):
        bname = str(self.inputBname.GetValue())
        sql = '''
        delete from Books
        where Bname="'''+bname+'"'
        print(sql)
        result = self._DB._SQL(sql, False)
        colNo = 0
        print(result)
        for row in result:
            for it in row:
                self.grid.SetCellValue(0, colNo, str(it))
                colNo += 1
        pass

    def _initGrid(self):
        self.grid = wx.grid.Grid(self.panelMainFrame, -1, pos=(0, 90),
                                 size=(980, 80), style=wx.WANTS_CHARS, name=self._lang_._mframe_grid_Name)
        self.grid.CreateGrid(1, 6, selmode=wx.grid.Grid.SelectCells)
        self.grid.EnableEditing(True)
        self.grid.SetRowSize(0, 30)
        self.grid.SetColLabelValue(0, self._lang_._mframe_grid_BookNumber)
        self.grid.SetColSize(0, 100)
        self.grid.SetColLabelValue(1, self._lang_._mframe_grid_BookName)
        self.grid.SetColSize(1, 100)
        self.grid.SetColLabelValue(2, self._lang_._mframe_grid_Author)
        self.grid.SetColSize(2, 100)
        self.grid.SetColLabelValue(3, self._lang_._mframe_grid_Publisher)
        self.grid.SetColSize(3, 130)
        self.grid.SetColLabelValue(4, self._lang_._mframe_grid_PublishDate)
        self.grid.SetColSize(4, 100)
        self.grid.SetColLabelValue(5, self._lang_._mframe_grid_Price)
        self.grid.SetColSize(5, 100)
        pass

    # This method is a placeholder.
    # 此方法为占位符.
    def _empty(self, event):
        pass
