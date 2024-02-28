from scr import (
    FileDialog, FileTree, TabEditor, SideBar,
    SettingsActionMenu, IconPaths, WelcomeScreen,
    FileChecker, FileLoader, PythonCodeEditorArea,
    HtmlCodeEditorArea, StyleCodeEditorArea, JsonCodeEditorArea,
    ImageViewer, TextEditorArea, WINDOW_SIZE, Restarter,
    ThemeChanger, EditorFontManager, SettingsMenu, WorkbenchFontManager,
    EditorSettingsUpdater, FileRunner, TabsSwitcher
)
from scr.interface.basic import Splitter

import os
import sys

from PySide6.QtWidgets import (
    QWidget, QApplication, QMainWindow,
    QHBoxLayout, QVBoxLayout
)
from PySide6.QtCore import QModelIndex, Qt
from PySide6.QtGui import QIcon, QShortcut


class MainWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()

        # self
        self.setObjectName("main-widget")

        # init layouts
        self.mainLayout = QVBoxLayout()
        self.workbenchLayout = QHBoxLayout()

        # init
        self.fileTree = FileTree()
        self.tabEditor = TabEditor()
        self.sideBar = SideBar()
        self.settingActionMenu = SettingsActionMenu()
        self.restarter = Restarter(self)
        self.themeChanger = ThemeChanger(self, restarter=self.restarter)
        self.settingsMenu = SettingsMenu(self, restarter=self.restarter)
        self.tabsSwitcher = TabsSwitcher(self)
        self.tabsSwitcher.open_connect(lambda t: print(t))
        self.splitter = Splitter("horizontal")

        self.init_ui()
        self.setup_ui()

    def init_ui(self) -> None:
        # to splitter
        self.splitter.addWidget(self.fileTree)
        self.splitter.addWidget(self.tabEditor)

        # layouts
        self.workbenchLayout.addWidget(self.sideBar, stretch=1)
        self.workbenchLayout.addWidget(self.splitter)

        self.mainLayout.addLayout(self.workbenchLayout)

    def test(self):
        # print(self.tabEditor.get_all_info_tabs(True, ["path", "widget"]))
        self.tabsSwitcher.set_items(*self.tabEditor.get_all_paths())
        self.tabsSwitcher.show()

    def setup_ui(self) -> None:
        self.tabEditor.addTab(WelcomeScreen(), "Welcome!", IconPaths.SystemIcons.WELCOME)

        # connections
        self.fileTree.clicked.connect(self.__click_file_tree)

        self.sideBar.settings_opener_connect(self.settingActionMenu.show)
        self.sideBar.file_tree_opener_connect(self.fileTree.show_hide_file_tree)

        self.settingActionMenu.connect_by_title("Themes...", self.show_theme_changer)
        self.settingActionMenu.connect_by_title("Open Settings...", self.settingsMenu.show)
        QShortcut("Ctrl+T", self).activated.connect(self.show_theme_changer)
        QShortcut("Ctrl+,", self).activated.connect(self.settingsMenu.show)
        QShortcut("Ctrl+Tab", self).activated.connect(self.test)

        QShortcut("Ctrl+O", self).activated.connect(
            lambda: self.fileTree.open_directory(FileDialog.get_open_directory())
        )
        QShortcut("Ctrl+P", self).activated.connect(
            lambda: self.__click_file_tree(self.fileTree.open_file(FileDialog.get_open_file_name()))
        )
        QShortcut("Ctrl+F5", self).activated.connect(
            lambda: FileRunner.run_python_file(self.tabEditor.get_current_path(), self.fileTree.get_current_directory())
        )

        EditorFontManager.add_font_updater(self.tabEditor.update_all_tabs_font)
        EditorSettingsUpdater.add_updater(self.tabEditor.update_all_tabs_settings)
        WorkbenchFontManager.add_font_updater(self.fileTree.update_font)

        # set layout (draw)
        self.setLayout(self.mainLayout)

    def __click_file_tree(self, __index: QModelIndex) -> None:
        path = self.fileTree.get_path_by_index(__index)

        if os.path.isfile(path):
            self.__open_file_for_edit(path, self.fileTree.get_file_icon(__index))

    def __open_file_for_edit(self, __path: str, __icon) -> None:
        if FileChecker.is_python_file(__path):
            self.tabEditor.addTab(
                PythonCodeEditorArea(__path), os.path.basename(__path), __icon
            )

        elif FileChecker.is_style_file(__path):
            self.tabEditor.addTab(
                StyleCodeEditorArea(__path), os.path.basename(__path), __icon
            )

        elif FileChecker.is_json_file(__path):
            self.tabEditor.addTab(
                JsonCodeEditorArea(__path), os.path.basename(__path), __icon
            )

        elif FileChecker.is_picture_file(__path):
            self.tabEditor.addTab(
                ImageViewer(__path), os.path.basename(__path), __icon
            )

        elif FileChecker.is_html_file(__path):
            self.tabEditor.addTab(
                HtmlCodeEditorArea(__path), os.path.basename(__path), __icon
            )

        elif FileChecker.is_readable(__path):
            try:
                self.tabEditor.addTab(
                    TextEditorArea(__path), os.path.basename(__path), __icon
                )
            except UnicodeDecodeError:
                pass

        self.tabEditor.setCurrentWidget(self.tabEditor.find_by_path(__path))

    def show_theme_changer(self):
        themes = [FileLoader.load_json(f"scr/data/themes/{i}")["name"] for i in os.listdir("scr/data/themes")]

        self.themeChanger.set_items(*themes)
        self.themeChanger.show()


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(*WINDOW_SIZE)
        self.setWindowTitle("PyPad")
        self.setWindowIcon(QIcon(":/system_icons/icon.ico"))
        self.setStyleSheet(
            FileLoader.load_style("scr/style/main.css") + FileLoader.load_style("scr/subwidgets/styles/action_menu.css")
        )
        self.setObjectName("window")

        self.mainWidget = MainWidget()

        self.setCentralWidget(self.mainWidget)

    def __toggle_full_screen(self):
        if self.isFullScreen():
            self.showMaximized()
        else:
            self.showFullScreen()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_F11:
            self.__toggle_full_screen()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.showMaximized()

    app.exec()
