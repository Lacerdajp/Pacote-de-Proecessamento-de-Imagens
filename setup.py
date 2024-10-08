from setuptools import setup, find_packages
with open('requeriments.txt','r') as f:
    requirements=f.read()
with open('README.md','r') as f:
    page_description=f.read()

setup(
    name='image_processing_jpls',
    version='0.0.5',
    description='Pacote de processamento de imagens',
    packages=find_packages(),
    install_requires=requirements,  
    python_requires='>=3.6',
    long_description_content_type='text/markdown',
    url='https://github.com/Lacerdajp/Pacote-de-Proecessamento-de-Imagens',
    long_description=page_description,
    author='João Pedro Lacerda de Souza',
    author_email='joaopedro.jplsouza@gmail.com',

)