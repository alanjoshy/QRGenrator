# QR Code Generator 🖼️

A simple web-based QR Code Generator built with **Flask** and **qrcode** library. This application allows users to generate QR codes from any text or URL and display or download the generated QR code image.

---

## Features ✨
- Generate QR codes instantly.
- Customizable input for text or URLs.
- Easy-to-use web interface.
- Lightweight and fast.

---

## Installation 📦

Follow these steps to install and run the QR Code Generator:

### **1. Clone the Repository**
```bash
git clone https://github.com/alanjoshy/QRGenrator
cd qr-code-generator
```

### **2. Set Up a Virtual Environment (Optional but Recommended)**
```bash
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate     # For Windows
```

### **3. Install Dependencies**
Run the following command to install the required Python packages:
```bash
pip install -r requirements.txt
```

| **Package**      | **Version** |
|-------------------|-------------|
| `blinker`        | 1.9.0       |
| `click`          | 8.1.7       |
| `colorama`       | 0.4.6       |
| `Flask`          | 3.1.0       |
| `itsdangerous`   | 2.2.0       |
| `Jinja2`         | 3.1.4       |
| `MarkupSafe`     | 3.0.2       |
| `pillow`         | 11.0.0      |
| `pip`            | 24.0        |
| `qrcode`         | 8.0         |
| `Werkzeug`       | 3.1.3       |

---

## Usage 🚀

### **1. Start the Application**
Run the Flask application:
```bash
python app.py
```

### **2. Access the Web Interface**
Open your browser and go to:
```
http://127.0.0.1:5000
```

### **3. Generate QR Codes**
- Enter the text or URL you want to encode.
- Click "Generate" to view the QR Code.
- Download the generated QR Code image.

---

## Screenshots 📸
Include images of the web interface and generated QR codes (optional).

---

## Technologies Used 🛠️
- **Backend:** Flask
- **QR Code Generation:** `qrcode` Python library
- **Image Handling:** Pillow

---

## Contributing 🤝
Contributions are welcome! Feel free to submit a pull request or report issues in the repository.

---

## License 📜
This project is licensed under the MIT License.

---

Let me know if you'd like help setting up the `requirements.txt` file or improving the README further!
