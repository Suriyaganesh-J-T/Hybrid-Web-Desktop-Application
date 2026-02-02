import requests
from PyQt5.QtWidgets import (
    QWidget, QLabel, QPushButton, QFileDialog,
    QVBoxLayout, QHBoxLayout, QGroupBox,
    QMessageBox, QTableWidget, QTableWidgetItem
)
from PyQt5.QtGui import QFont
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

API_UPLOAD = "http://127.0.0.1:8000/api/upload/"
API_PDF = "http://127.0.0.1:8000/api/report/pdf/"


class ChartCanvas(FigureCanvasQTAgg):
    def __init__(self):
        self.fig = Figure(figsize=(4, 3))
        self.ax = self.fig.add_subplot(111)
        super().__init__(self.fig)

    def plot(self, dist):
        self.ax.clear()
        self.ax.bar(dist.keys(), dist.values())
        self.ax.set_title("Equipment Distribution")
        self.ax.set_ylabel("Count")
        self.fig.tight_layout()
        self.draw()


class DashboardWindow(QWidget):
    def __init__(self, login_window):
        super().__init__()
        self.login_window = login_window
        self.setWindowTitle("Chemical Equipment Visualizer")
        self.setGeometry(100, 100, 1100, 650)

        main = QVBoxLayout(self)

        # ===== HEADER =====
        header = QHBoxLayout()
        title = QLabel("Chemical Equipment Analysis")
        title.setFont(QFont("Segoe UI", 14, QFont.Bold))

        logout = QPushButton("Logout")
        logout.clicked.connect(self.logout)

        header.addWidget(title)
        header.addStretch()
        header.addWidget(logout)
        main.addLayout(header)

        body = QHBoxLayout()
        main.addLayout(body)

        # ===== LEFT PANEL =====
        left = QVBoxLayout()
        upload = QPushButton("Upload CSV")
        upload.clicked.connect(self.upload_csv)

        pdf = QPushButton("Download PDF Report")
        pdf.clicked.connect(self.download_pdf)

        left.addWidget(upload)
        left.addWidget(pdf)
        left.addStretch()
        body.addLayout(left, 1)

        # ===== RIGHT PANEL =====
        right = QVBoxLayout()

        self.summary = QLabel("Upload a CSV file to view analysis")
        right.addWidget(self.summary)

        self.chart = ChartCanvas()
        right.addWidget(self.chart)

        self.table = QTableWidget(0, 5)
        self.table.setHorizontalHeaderLabels(
            ["Equipment", "Type", "Flowrate", "Pressure", "Temperature"]
        )
        right.addWidget(self.table)

        body.addLayout(right, 4)

    def upload_csv(self):
        path, _ = QFileDialog.getOpenFileName(self, "Select CSV", "", "CSV Files (*.csv)")
        if not path:
            return

        with open(path, "rb") as f:
            res = requests.post(API_UPLOAD, files={"file": f})

        data = res.json()
        s = data["summary"]

        self.summary.setText(
            f"Total: {s['total_equipment']}   "
            f"Avg Temp: {s['avg_temperature']}   "
            f"Avg Pressure: {s['avg_pressure']}   "
            f"Avg Flowrate: {s['avg_flowrate']}"
        )

        self.chart.plot(s["type_distribution"])
        self.load_table(data["rows"])

    def load_table(self, rows):
        self.table.setRowCount(len(rows))
        for i, r in enumerate(rows):
            self.table.setItem(i, 0, QTableWidgetItem(r["Equipment Name"]))
            self.table.setItem(i, 1, QTableWidgetItem(r["Type"]))
            self.table.setItem(i, 2, QTableWidgetItem(str(r["Flowrate"])))
            self.table.setItem(i, 3, QTableWidgetItem(str(r["Pressure"])))
            self.table.setItem(i, 4, QTableWidgetItem(str(r["Temperature"])))

    def download_pdf(self):
        r = requests.get(API_PDF)
        path, _ = QFileDialog.getSaveFileName(self, "Save PDF", "report.pdf")
        if path:
            with open(path, "wb") as f:
                f.write(r.content)

    def logout(self):
        self.close()
        self.login_window.show()
