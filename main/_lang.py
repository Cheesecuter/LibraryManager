import os
import _FrozenDir


class _Language:
    def __init__(self):
        path = _FrozenDir.app_path()+r'\\src\\langType.txt'
        print(path)
        f = open(path,
                 mode="r", encoding="UTF-8")
        langType = f.readline()
        if(langType == 'en_US'):
            print("lang: "+langType)
            self._en_US()
            f.close()
        if(langType == 'zh_CN'):
            print("语言: "+langType)
            self._zh_CN()
            f.close()
        pass

    def _en_US(self):
        # ********************
        # Main Frame
        # ********************
        # frames
        self._mframe_FrameTitle = "Library Manager"
        # menus
        self._mframe_menu_file = "File"
        self._mframe_menu_file_initTables = "Init Tables"
        self._mframe_menu_file_initDatas = "Init Datas"
        self._mframe_menu_file_exit = "Exit"
        self._mframe_menu_view = "View"
        self._mframe_menu_view_bookGrid = "Books Grid"
        self._mframe_menu_tools = "Tools"
        self._mframe_menu_tools_language = "Language"
        self._mframe_menu_help = "Help"
        self._mframe_menu_help_about = "About"
        # end message
        self._mframe_emsg__initTables_f_is_running = "_initTables_f is running"
        self._mframe_emsg_Database_initiated = "Database initiated"
        self._mframe_emsg__initTables_f_is_done = "_initTables_f is done"
        self._mframe_emsg__initDatas_f_is_running = "_initDatas_f is running"
        self._mframe_emsg_Craw_data_initiated = "Craw data initiated"
        self._mframe_emsg__initDatas_f_is_done = "_initDatas_f is done"
        self._mframe_emsg__exit_f_is_running = "_exit_f is running"
        self._mframe_emsg__booksGrid_f_is_running = "_booksGrid_f is running"
        self._mframe_emsg__booksGrid_f_is_done = "_booksGrid_f is done"
        self._mframe_emsg__language_f_is_running = "_language_f is running"
        self._mframe_emsg_Language_Changed_Successfully_1n = "Language Changed Successfully\n"
        self._mframe_emsg__language_f_is_done = "_language_f is done"
        self._mframe_emsg__about_f_is_running = "_about_f is running"
        self._mframe_emsg__about_f_is_done = "_about_f is done"
        # panels
        self._mframe_panel_txtInputBname = "Book Name"
        self._mframe_panel_btSelect = "Select"
        self._mframe_panel_btInsert = "Insert"
        self._mframe_panel_btDelete = "Delete"
        # grid
        self._mframe_grid_Name = "Books"
        self._mframe_grid_BookNumber = "Number"
        self._mframe_grid_BookName = "Book Name"
        self._mframe_grid_Author = "Author"
        self._mframe_grid_Publisher = "Publisher"
        self._mframe_grid_PublishDate = "Publish Date"
        self._mframe_grid_Price = "Price"

        # ********************
        # DB Grid
        # ********************
        # frames
        self._dbgrid_FrameTitle = "Books"
        # grid
        self._dbgrid_GridTitle = "Books"
        self._dbgrid_gridCOL_Book_Number = "Number"
        self._dbgrid_gridCOL_Book_Name = "Book Name"
        self._dbgrid_gridCOL_Author = "Author"
        self._dbgrid_gridCOL_Publish_Date = "Publish Date"
        self._dbgrid_gridCOL_Publisher = "Publisher"
        self._dbgrid_gridCOL_Price = "Price"

        # ********************
        # Info Frame
        # ********************
        # frames
        self._abframe_FrameTitle = "About"
        # informations
        self._abframe_info_1 = "Library Manager"
        self._abframe_info_2 = "v0.0.2"
        self._abframe_info_3 = "2004010525"
        self._abframe_info_4 = "HRBUST"
        pass

    def _zh_CN(self):
        # ********************
        # 主窗口
        # ********************
        # 窗口
        self._mframe_FrameTitle = "图书管理器"
        # 菜单
        self._mframe_menu_file = "文件"
        self._mframe_menu_file_initTables = "初始化表"
        self._mframe_menu_file_initDatas = "初始化数据"
        self._mframe_menu_file_exit = "退出"
        self._mframe_menu_view = "视图"
        self._mframe_menu_view_bookGrid = "图书表"
        self._mframe_menu_tools = "工具"
        self._mframe_menu_tools_language = "语言"
        self._mframe_menu_help = "帮助"
        self._mframe_menu_help_about = "关于"
        # 终端信息
        self._mframe_emsg__initTables_f_is_running = "调用 _initTables_f"
        self._mframe_emsg_Database_initiated = "数据库初始化成功"
        self._mframe_emsg__initTables_f_is_done = "_initTables_f 调用完成"
        self._mframe_emsg__initDatas_f_is_running = "调用 _initDatas_f"
        self._mframe_emsg_Craw_data_initiated = "数据爬取完成"
        self._mframe_emsg__initDatas_f_is_done = "_initDatas_f 调用完成"
        self._mframe_emsg__exit_f_is_running = "调用 _exit_f"
        self._mframe_emsg__booksGrid_f_is_running = "调用 _booksGrid_f"
        self._mframe_emsg__booksGrid_f_is_done = "_booksGrid_f 调用完成"
        self._mframe_emsg__language_f_is_running = "调用 _language_f"
        self._mframe_emsg_Language_Changed_Successfully_1n = "语言切换成功\n"
        self._mframe_emsg__language_f_is_done = "_language_f 调用完成"
        self._mframe_emsg__about_f_is_running = "调用 _about_f"
        self._mframe_emsg__about_f_is_done = "_about_f 调用完成"
        # 面板
        self._mframe_panel_txtInputBname = "书名"
        self._mframe_panel_btSelect = "筛选"
        self._mframe_panel_btInsert = "插入"
        self._mframe_panel_btDelete = "删除"
        # 表格
        self._mframe_grid_Name = "图书"
        self._mframe_grid_BookNumber = "书号"
        self._mframe_grid_BookName = "书名"
        self._mframe_grid_Author = "作者"
        self._mframe_grid_Publisher = "出版商"
        self._mframe_grid_PublishDate = "发行日期"
        self._mframe_grid_Price = "价格"

        # ********************
        # 数据表格
        # ********************
        # 窗口
        self._dbgrid_FrameTitle = "图书"
        # 表格
        self._dbgrid_GridTitle = "图书"
        self._dbgrid_gridCOL_Book_Number = "书号"
        self._dbgrid_gridCOL_Book_Name = "书名"
        self._dbgrid_gridCOL_Author = "作者"
        self._dbgrid_gridCOL_Publish_Date = "发行日期"
        self._dbgrid_gridCOL_Publisher = "出版商"
        self._dbgrid_gridCOL_Price = "价格"

        # ********************
        # 信息窗口
        # ********************
        # 窗口
        self._abframe_FrameTitle = "关于"
        # 信息
        self._abframe_info_1 = "图书管理器"
        self._abframe_info_2 = "v0.0.2"
        self._abframe_info_3 = "2004010525"
        self._abframe_info_4 = "HRBUST"
        pass
