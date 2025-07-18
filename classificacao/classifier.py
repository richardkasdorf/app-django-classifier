import numpy as np
from PIL import Image
import fitz
import tensorflow as tf
import os

# Carregue o modelo apenas uma vez ao iniciar o servidor
#modelo = tf.keras.models.load_model( r"C:\Users\richa\OneDrive\Área de Trabalho\DevOps_Python\Separa_imagens\modelo_cao_gato.h5" )

# Caminho absoluto seguro
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
modelo_path = os.path.join(BASE_DIR, "modelos", "modelo_cao_gato.h5")

# Carrega o modelo de forma portátil
modelo = tf.keras.models.load_model(modelo_path)


def extrair_imagem_do_pdf(path_pdf):
    doc = fitz.open(path_pdf)
    pagina = doc.load_page(0)
    pix = pagina.get_pixmap()
    imagem = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    return imagem

def classificar_imagem(imagem):
    imagem = imagem.resize((224, 224))
    array = np.array(imagem) / 255.0
    array = np.expand_dims(array, axis=0)
    pred = modelo.predict(array)[0]
    return "gato" if pred[0] > 0.5 else "cao"

def processar_pdf(path_pdf):
    img = extrair_imagem_do_pdf(path_pdf)
    return classificar_imagem(img)