from django.test import TestCase, Client
from django.urls import reverse
from PIL import Image
import tempfile

class UploadViewTest(TestCase):
    def test_upload_imagem_valida(self):
        # Cria uma imagem temporária
        image = Image.new('RGB', (224, 224), color='white')
        tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
        image.save(tmp_file, format='JPEG')
        tmp_file.seek(0)

        client = Client()
        response = client.post(reverse('upload_file'), {'arquivo': tmp_file}, follow=True) #Reverse acha a URL onde se encontra o 'upload_file'
        self.assertEqual(response.status_code, 200)                     # Resultado HTTP é 200? Ok, segue pois deu certo
        self.assertContains(response, 'A foto enviada é de um...')      # Verifica se a resposta contém o texto esperado

    def test_upload_arquivo_invalido(self):
        client = Client()
        with tempfile.NamedTemporaryFile(suffix='.txt') as tmp_file:
            tmp_file.write(b'arquivo de teste')  # grava o texto "arquivo de teste" (em bytes) dentro do arquivo temporário criado com extensão .txt 
            tmp_file.seek(0)              # Volta o ponteiro do arquivo para o início, para que ele possa ser lido corretamente
            response = client.post(reverse('upload_file'), {'arquivo': tmp_file}, follow=True)
            self.assertEqual(response.status_code, 200)
            # Espera que não apareça o resultado, pois não é imagem
            self.assertNotContains(response, 'A foto enviada é de um...')

    def test_pagina_carrega(self):    # Verifica se a página de upload carrega corretamente
        client = Client()
        response = client.get(reverse('upload_file'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Qual animal está na foto?')