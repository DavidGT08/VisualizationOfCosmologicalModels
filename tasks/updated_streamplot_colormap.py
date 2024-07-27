import sys
from PyQt5 import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

class DialogApplication(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        # Set up the dialog
        self.setWindowTitle('Streamplot con PyQt5')
        self.setGeometry(100, 100, 800, 600)

        # Create the matplotlib canvas
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        # Create the spin box for L
        self.L_spinbox = QtWidgets.QSpinBox()
        self.L_spinbox.setValue(1)  # Set initial value
        self.L_spinbox.setMinimum(1)  # Set minimum value
        self.L_spinbox.setMaximum(10)  # Set maximum value

        # Create the QComboBox for choosing colormaps
        self.colormap_combobox = QtWidgets.QComboBox()
        self.colormap_combobox.addItems(['viridis', 'plasma', 'inferno', 'magma', 'cividis'])
        self.colormap_combobox.setCurrentIndex(0)  # Set default to 'viridis'

        # Create the "Replot" button
        self.replot_button = QtWidgets.QPushButton("Replot")
        self.replot_button.clicked.connect(self.update_plot)

        # Add widgets to layout
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.canvas)
        layout.addWidget(self.L_spinbox)
        layout.addWidget(self.colormap_combobox)
        layout.addWidget(self.replot_button)
        self.setLayout(layout)

        # Create initial plot
        self.update_plot()

    def update_plot(self):
        # Get the current value of L from the spin box
        L = self.L_spinbox.value()

        # Get the selected colormap from the combobox
        colormap = self.colormap_combobox.currentText()

        # Create data for the streamplot
        g = 9.8  # m/s^2
        theta_val, omega_val = np.meshgrid(np.arange(3.5, 10, 0.1), np.arange(-10, 10, 0.1))
        theta_dot = omega_val
        omega_dot = -g/L * np.sin(theta_val)

        # Clear the previous plot
        self.figure.clear()
        ax = self.figure.add_subplot(111)

        # Create the new streamplot
        strm = ax.streamplot(theta_val, omega_val, theta_dot, omega_dot, color=omega_val, cmap=colormap)

        # Add title and axis labels
        ax.set_title('Streamplot - Espacio de Fase')
        ax.set_xlabel('Theta')
        ax.set_ylabel('Omega')

        # Add a colorbar
        cbar = self.figure.colorbar(strm.lines)
        cbar.set_label('Omega')

        # Update the canvas
        self.canvas.draw()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = DialogApplication()
    dialog.show()
    sys.exit(app.exec_())