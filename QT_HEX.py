import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton, QHBoxLayout, QFileDialog
from PyQt5.QtGui import QFont
import secp256k1 as ice

class AddressFinder(QWidget):
    BUFFER_SIZE = 8192

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Address Finder")
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()
        self.setGeometry(100, 100, 600, 450)
        title_label = QLabel("HEX Address Finder")
        title_label.setFont(QFont("Arial", 16, QFont.Bold))
        title_label.setStyleSheet("color: purple;")
        count_label = QLabel()
        count_label.setStyleSheet("font-weight: bold;")
        input_layout = QHBoxLayout()
        label = QLabel("Enter Address to Find (BTC or ETH):")
        self.address_input = QLineEdit()
        find_button = QPushButton("Find", self)
        find_button.clicked.connect(self.find_addresses)
        input_layout.addWidget(label)
        input_layout.addWidget(self.address_input)
        input_layout.addWidget(find_button)
        file_layout = QHBoxLayout()
        file_label = QLabel("Load Addresses from File:")
        self.file_input = QLineEdit()
        browse_button = QPushButton("Browse", self)
        browse_button.clicked.connect(self.browse_file)
        load_button = QPushButton("Load", self)
        load_button.clicked.connect(self.load_addresses)
        file_layout.addWidget(file_label)
        file_layout.addWidget(self.file_input)
        file_layout.addWidget(browse_button)
        file_layout.addWidget(load_button)
        scan_result_layout = QVBoxLayout()
        self.scan_result_output = QTextEdit()
        self.scan_result_output.setReadOnly(True)
        scan_result_layout.addWidget(QLabel("Scan Results:"))
        scan_result_layout.addWidget(self.scan_result_output)
        progress_layout = QVBoxLayout()
        self.progress_label_output = QTextEdit()
        self.progress_label_output.setReadOnly(True)
        progress_layout.addWidget(QLabel("Progress:"))
        progress_layout.addWidget(self.progress_label_output)
        found_result_layout = QVBoxLayout()
        self.found_result_output = QTextEdit()
        self.found_result_output.setReadOnly(True)
        found_result_layout.addWidget(QLabel("Found Results:"))
        found_result_layout.addWidget(self.found_result_output)
        main_layout.addWidget(title_label)
        main_layout.addWidget(count_label)
        main_layout.addLayout(input_layout)
        main_layout.addLayout(file_layout)
        main_layout.addLayout(scan_result_layout)
        main_layout.addLayout(progress_layout)
        main_layout.addLayout(found_result_layout)
        self.setLayout(main_layout)
        self.count_hex_addresses(count_label)

    def count_hex_addresses(self, count_label):
        line_count = 0
        with open("hex.txt", "r") as file:
            for line in file:
                if line.strip():
                    line_count += 1
        count_label.setText(f"Total HEX addresses loaded in hex.txt: {line_count}")

    def save_progress(self, filename, pvk, addr):
        with open(filename, 'a') as file:
            file.write(f'Address = {addr}\nPrivate Key = {pvk}\n')

    def generate_addresses(self, dec):
        caddr = ice.privatekey_to_address(0, True, dec)
        uaddr = ice.privatekey_to_address(0, False, dec)
        p2sh = ice.privatekey_to_address(1, True, dec)
        bech32 = ice.privatekey_to_address(2, True, dec)
        ethaddr = ice.privatekey_to_ETH_address(dec)
        return caddr, uaddr, p2sh, bech32, ethaddr

    def read_file_chunks(self, file):
        while True:
            data = file.read(self.BUFFER_SIZE)
            if not data:
                break
            yield data

    def find_addresses(self):
        addfind = self.address_input.text()
        c = 0
        i = 0
        line_10 = 10000
        with open('hex.txt', 'rb') as f:
            for chunk in self.read_file_chunks(f):
                lines = chunk.split(b'\n')
                for line in lines:
                    if line_10 == i:
                        line_10 += 10000
                        self.progress_label_output.setText(f"Checking BTC, ETH [{line_10}]")

                    text = line.strip().decode('utf-8')
                    pvk = text
                    dec = int(pvk, 16)
                    HEX = "%064x" % dec
                    caddr, uaddr, p2sh, bech32, ethaddr = self.generate_addresses(dec)
                    result = f"pvk:                    {text}\n"
                    result += f"BTC p2pkh comp:         {caddr}\n"
                    result += f"BTC p2pkh uncomp:       {uaddr}\n"
                    result += f"BTC p2sh:               {p2sh}\n"
                    result += f"BTC bech32:             {bech32}\n"
                    result += f"ETH:                    {ethaddr}\n\n"
                    self.scan_result_output.append(result)
                    c += 1
                    i += 1
                    if caddr == addfind or uaddr == addfind or p2sh == addfind or bech32 == addfind or ethaddr == addfind:
                        found_result = f"          FOUND          \n"
                        found_result += f"pvk:                    {text}\n"
                        if caddr == addfind:
                            found_result += f"BTC p2pkh comp:         {caddr}\n"
                        if uaddr == addfind:
                            found_result += f"BTC p2pkh uncomp:       {uaddr}\n"
                        if p2sh == addfind:
                            found_result += f"BTC p2sh:               {p2sh}\n"
                        if bech32 == addfind:
                            found_result += f"BTC bech32:             {bech32}\n"
                        if ethaddr == addfind:
                            found_result += f"ETH:                    {ethaddr}\n"
                        found_result += "\n"
                        self.found_result_output.append(found_result)
                        self.save_progress('found.txt', HEX, addfind)
        QApplication.processEvents()

    def browse_file(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Load Addresses", "", "Text Files (*.txt)")
        if file_path:
            self.file_input.setText(file_path)

    def load_addresses(self):
        self.progress_label_output.setText("Loading addresses... Please wait.")
        filename = self.file_input.text()
        with open(filename) as file:
            addfind_load = file.read().split()
        
        for addfind in addfind_load:
            self.address_input.setText(addfind)
            self.find_addresses()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AddressFinder()
    window.show()
    sys.exit(app.exec_())