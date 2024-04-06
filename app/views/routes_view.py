from flask import request, send_file, render_template, jsonify
from flask_bootstrap import Bootstrap

from app.controllers import qr_controller

from app import app
Bootstrap(app)

qr_controller = qr_controller.QRController()

@app.route('/texto', methods=['GET', 'POST'])
@app.route('/texto/<parametro_url>', methods=['GET', 'POST'])
def generate_qr_teste(parametro_url=None):
    if request.method == 'POST':
        # Se a solicitação for POST, tente obter 'data' do corpo JSON
        data = request.json.get('data')
    else:
        # Se a solicitação for GET, use o parâmetro_url
        data = parametro_url

    max_lenght = 20
    # Verifica tamanho máximo do texto a ser gerado
    if len(data) > max_lenght:
        error = {"erro": "Texto permitido até 20 caracteres."}
        return jsonify(error), 400

    if data:
        qr_img_path = qr_controller.generate_qr(data)
        return send_file(qr_img_path, mimetype='image/png')
    else:
        return "Texto não fornecido.", 400

@app.route('/', methods=['GET', 'POST'])
def generate_qr():
    if request.method == 'POST':
        data = request.form['data']
        max_lenght = 20

        if len(data) > max_lenght:
            error = {"erro": "Texto permitido até 50 caracteres."}
            return render_template('index.html', error=error)

        if data:
            qr_img_path = qr_controller.generate_qr(data)
            return send_file(qr_img_path, mimetype='image/png')
        else:
            error = {"erro": "Texto não fornecido."}
            return render_template('index.html', error=error), 400

    return render_template('index.html')