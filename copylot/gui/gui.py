import json
import os.path
import sys
import qdarkstyle
from pathlib import Path
from qtpy.QtCore import Qt, QThreadPool
from qtpy.QtWidgets import (
    QMainWindow,
    QStatusBar,
    QApplication,
    QDockWidget,
    QLabel,
    QAction,
)

from copylot.gui._qt.custom_widgets.dock_placeholder import DockPlaceholder
from copylot import __version__


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.threadpool = QThreadPool()

        self.title = "Pisces Parameter Controller"
        self.version = __version__

        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        height, width = self.screenRect.height(), self.screenRect.width()

        self.width = width // 3
        self.height = height // 2
        self.left = (width - self.width) // 2
        self.top = (height - self.height) // 2

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setDockOptions(QMainWindow.AnimatedDocks | QMainWindow.AllowNestedDocks)

        self.init_defaults = [
            ["exposure", 0.001, 1, 0.02],
            ["nb_timepoints", 1, 10000, 600],
            ["scan_step", 0.01, 1, 0.1],
            ["stage_scan_range", 0, 10000, 1000],
            ["vertical_pixels", 0, 4000, 2048],
            ["num_samples", 0, 100, 20],
            ["offset_view1", 0, 3180, 1550],
            ["offset_view2", 0, 3180, 1650],
            ["view1_galvo1", -10, 10, 4.2],
            ["view1_galvo2", -10, 10, -4.08],
            ["view2_galvo1", -10, 10, -4.37],
            ["view2_galvo2", -10, 10, 3.66],
            ["stripe_reduction_range", 0, 10, 0.1],
            ["stripe_reduction_offset", -10, 10, 0.58],
        ]

        try:
            with open(
                os.path.join(str(Path.home()), ".coPylot", "coPylot_parameters.txt"),
                "r",
            ) as json_file:
                self.defaults = json.load(json_file)

        except FileNotFoundError:  # construct initial defaults.txt fileself.defaults = [3, 6, 25, 100]
            if not os.path.isdir(os.path.join(str(Path.home()), ".coPylot")):
                os.mkdir(os.path.join(str(Path.home()), ".coPylot"))

            self.defaults = {
                "parameters": {},
                "live": {"view": 0, "laser": 0},
                "timelapse": {"view": 0, "laser": 0},
                "water": {
                    "interval": 3,
                    "duration": 6,
                    "freq": 25,
                    "amp": 100,
                    "serial port": 0,
                    "baudrate": 0,
                },
            }
            for i in range(0, len(self.init_defaults)):
                obj = self.init_defaults[i]
                self.defaults["parameters"][obj[0]] = [obj[3], obj[1], obj[2]]

            with open(
                os.path.join(str(Path.home()), ".coPylot", "coPylot_parameters.txt"),
                "w",
            ) as outfile:
                json.dump(self.defaults, outfile)

        # set common configurations for docks
        self.dock_list = []

        # initialize docks
        self.live_dock = QDockWidget(self)
        self.live_dock.setTitleBarWidget(QLabel("Live Mode"))
        self.dock_list.append(self.live_dock)

        self.timelapse_dock = QDockWidget(self)
        self.timelapse_dock.setTitleBarWidget(QLabel("Timelapse Mode"))
        self.dock_list.append(self.timelapse_dock)

        self.water_dock = QDockWidget(self)
        self.water_dock.setTitleBarWidget(QLabel("Water Dispenser"))
        self.dock_list.append(self.water_dock)

        self.parameters_dock = QDockWidget(self)
        self.parameters_dock.setTitleBarWidget(QLabel("NI DAQ Parameters"))
        self.dock_list.append(self.parameters_dock)

        self.laser_dock = QDockWidget(self)
        self.laser_dock.setTitleBarWidget(QLabel("Laser"))
        self.dock_list.append(self.laser_dock)

        for dock in self.dock_list:
            _apply_dock_config(dock)

        # initialize widgets and assign to their dock
        self.live_dock.setWidget(
            DockPlaceholder(
                self, self.live_dock, "live_control", [self, self.threadpool]
            )
        )
        # self.addDockWidget(Qt.RightDockWidgetArea, self.live_dock)
        #
        # self.timelapse_widget = TimelapseControl(self, self.threadpool)
        self.timelapse_dock.setWidget(
            DockPlaceholder(
                self, self.timelapse_dock, "timelapse_control", [self, self.threadpool]
            )
        )
        # self.addDockWidget(Qt.RightDockWidgetArea, self.timelapse_dock)

        # self.water_widget = WaterDispenser(self, self.threadpool)
        self.water_dock.setWidget(
            DockPlaceholder(
                self, self.water_dock, "water_dispenser", [self, self.threadpool]
            )
        )
        # self.addDockWidget(Qt.RightDockWidgetArea, self.water_dock)
        self.laser_dock.setWidget(
            DockPlaceholder(self, self.laser_dock, "laser", [self])
        )

        # self.parameters_widget = ParametersDockWidget(self)
        self.parameters_placeholder = DockPlaceholder(
            self, self.parameters_dock, "parameters", [self]
        )
        self.parameters_dock.setWidget(self.parameters_placeholder)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.parameters_dock)

        # split horizontal and vertical space between docks
        self.splitDockWidget(self.parameters_dock, self.live_dock, Qt.Horizontal)
        self.splitDockWidget(self.live_dock, self.timelapse_dock, Qt.Vertical)
        self.splitDockWidget(self.timelapse_dock, self.water_dock, Qt.Vertical)
        self.splitDockWidget(self.water_dock, self.laser_dock, Qt.Vertical)

        # create status bar that is updated from live and timelapse control classes
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

        # Menu bar
        self.setupMenubar()

    def closeEvent(self, event):
        print("closeEvent of mainwindow is called")
        app = QApplication.instance()
        app.quit()

    def setupMenubar(self):
        """Method to populate menubar."""
        mainMenu = self.menuBar()
        mainMenu.setNativeMenuBar(False)

        helpMenu = mainMenu.addMenu(' &Help')

        # Help Menu
        versionButton = QAction("ver" + self.version, self)
        helpMenu.addAction(versionButton)


def _apply_dock_config(dock):
    dock.setFeatures(QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetFloatable)
    dock.setAllowedAreas(
        Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea | Qt.TopDockWidgetArea
    )


def run():
    """Method to run GUI

    Parameters
    ----------
    ver : str
        string of aydin version number

    """
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    run()
