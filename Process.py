import os

# Cria o diretório do projeto
project_name = 'image_processor'
os.makedirs(project_name, exist_ok=True)
os.makedirs(os.path.join(project_name, project_name), exist_ok=True)
os.makedirs(os.path.join(project_name, 'tests'), exist_ok=True)

# Cria o arquivo __init__.py
init_content = '''from .processing import convert_to_grayscale
'''
with open(os.path.join(project_name, project_name, '__init__.py'), 'w') as f:
    f.write(init_content)

# Cria o arquivo processing.py
processing_content = '''from PIL import Image

def convert_to_grayscale(image_path: str, output_path: str):
    \"""
    Converte a imagem especificada para escala de cinza e a salva no caminho de saída.

    :param image_path: Caminho para a imagem original.
    :param output_path: Caminho para salvar a imagem convertida.
    \"""
    with Image.open(image_path) as img:
        grayscale_img = img.convert("L")
        grayscale_img.save(output_path)
'''
with open(os.path.join(project_name, project_name, 'processing.py'), 'w') as f:
    f.write(processing_content)

# Cria o arquivo test_processing.py
test_processing_content = '''import unittest
from image_processor.processing import convert_to_grayscale
import os

class TestImageProcessor(unittest.TestCase):
    def test_convert_to_grayscale(self):
        # Testa a função de conversão de imagem para escala de cinza
        input_image = 'test_image.jpg'
        output_image = 'test_image_grayscale.jpg'
        
        # Criar uma imagem de teste
        with open(input_image, 'wb') as f:
            f.write(b'\\xFF' * 100)
        
        convert_to_grayscale(input_image, output_image)
        
        # Verifica se o arquivo de saída foi criado
        self.assertTrue(os.path.exists(output_image))
        
        # Limpeza
        os.remove(input_image)
        os.remove(output_image)

if __name__ == '__main__':
    unittest.main()
'''
with open(os.path.join(project_name, 'tests', 'test_processing.py'), 'w') as f:
    f.write(test_processing_content)

# Cria o arquivo setup.py
setup_content = '''from setuptools import setup, find_packages

setup(
    name='image_processor',
    version='0.1',
    description='Um pacote para processamento de imagens, incluindo conversão para escala de cinza.',
    author='Seu Nome',
    author_email='seu.email@example.com',
    packages=find_packages(),
    install_requires=[
        'Pillow',  # Biblioteca para processamento de imagens
    ],
    tests_require=[
        'unittest',
    ],
    python_requires='>=3.6',
)
'''
with open(os.path.join(project_name, 'setup.py'), 'w') as f:
    f.write(setup_content)

# Cria o arquivo README.md
readme_content = '''# Image Processor

Um pacote Python para processamento de imagens, incluindo conversão para escala de cinza.

## Instalação

Você pode instalar o pacote usando pip:

```bash
pip install image_processor
