
# Pacote de Processamento de Imagens

Criação de pacote de processamento de imagens em Python para o curso da DIO.

## Introdução

Este pacote fornece funcionalidades para combinar imagens e transferir histogramas entre imagens, utilizando bibliotecas como `numpy` e `skimage`.

## Instalação

Para instalar o pacote, você pode clonar este repositório e instalar as dependências listadas no arquivo `requirements.txt`:

```sh
git clone https://github.com/Lacerdajp/Pacote-de-Proecessamento-de-Imagens.git
cd Pacote-de-Proecessamento-de-Imagens
pip install -r requirements.txt
```

## Uso

### Combinação de Imagens

A função `combine_images` combina duas imagens e retorna a diferença normalizada entre elas.

```python
from image_processing.processing.combination import combine_images
import numpy as np

image1 = np.random.rand(100, 100, 3)
image2 = np.random.rand(100, 100, 3)

diff_image = combine_images(image1, image2)
print(diff_image)
```

### Transferência de Histograma

A função `transfer_histogram` transfere o histograma de uma imagem para outra.

```python
from image_processing.processing.combination import transfer_histogram
import numpy as np

image1 = np.random.rand(100, 100, 3)
image2 = np.random.rand(100, 100, 3)

hist_transferred_image = transfer_histogram(image1, image2)
print(hist_transferred_image)
```
### Transformações de Imagem
A função resize_image redimensiona uma imagem para as dimensões especificadas.
```python
from image_processing.processing.transform import resize_image
import numpy as np

image = np.random.rand(100, 100, 3)
resized_image = resize_image(image, (50, 50))
print(resized_image)
```
### Plotagem de Imagens
A função plot_image exibe uma imagem usando matplotlib.
```python
from image_processing.processing.plot import plot_image
import numpy as np

image = np.random.rand(100, 100, 3)
plot_image(image)
```
### Entrada e Saída de Imagens
A função read_image lê uma imagem de um arquivo e a função save_image salva uma imagem em um arquivo.
```python
from image_processing.processing.io import read_image, save_image

image_path = 'path/to/image.png'
image = read_image(image_path)
save_image(image, 'path/to/saved_image.png')
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Autor

João Pedro Lacerda de Souza - [joaopedro.jplsouza@gmail.com](mailto:joaopedro.jplsouza@gmail.com)
