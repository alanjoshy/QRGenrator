from flask import Flask, render_template, request, send_file
import qrcode 
from io import BytesIO
import base64

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    qr_image = None
    if request.method == 'POST':
        # Get data from form
        data = request.form.get('data', '')
        color = request.form.get('color', 'black')
        bg_color = request.form.get('bg_color', 'white')
        size = int(request.form.get('size', 10))
        
        # Create QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=size,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        
        # Create image
        img = qr.make_image(fill_color=color, back_color=bg_color)
        
        # Save to BytesIO
        img_io = BytesIO()
        img.save(img_io, 'PNG')
        img_io.seek(0)
        
        # Convert to base64 for displaying in HTML
        qr_image = base64.b64encode(img_io.getvalue()).decode()
        
    return render_template('index.html', qr_image=qr_image)

if __name__ == '__main__':
    app.run(debug=True)