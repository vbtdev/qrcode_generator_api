import tempfile
import os

from app.models.qr_model import QRModel
from app.views.qr_view import QRView

class QRController:
    def __init__(self):
        self.model = QRModel()
        self.view = QRView()

    def generate_qr(self, data):
        qr_img = self.model.generate_qr(data)

        # Salvar a imagem em um arquivo temporário
        temp_dir = tempfile.mkdtemp()
        temp_file_path = os.path.join(temp_dir, 'qrcode_generator_api.png')
        qr_img.save(temp_file_path)

        return temp_file_path