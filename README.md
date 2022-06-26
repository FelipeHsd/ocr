# FastTrack de OCR em Python com Tesseract

Retirando facilmente texto de imagem com Python.

<sub>Diga "Oi" <br> 
    [<img src = "https://img.shields.io/badge/github-black.svg?&style=for-the-badge&logo=github&logoColor=white">](https://github.com/hideraldus13)
    [<img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/hideraldoluis/) 
    [<img src = "https://img.shields.io/badge/instagram-%23E4405F.svg?&style=for-the-badge&logo=instagram&logoColor=white">](https://www.instagram.com/hideraldojunior/) 
</sub>

## :runner: Fast Track
* Pré requisitos: <b>Python e [Tesseract](https://digi.bib.uni-mannheim.de/tesseract/ "Página de Download do Tesseract")</b>
```bash
$ git clone https://github.com/hideraldus13/ocr_python_fast_track.git
$ cd ocr_python_fast_track
$ pip install -r requirements.txt

//Comandos para Windows. Linux ou Mac não sei como funciona, mas é por aí.
```

## :candy: Testando a aplicação

```bash
$ python ocr.py
```

Veja que a saída no console é o texto da imagem <i>teste.png</i> disponível neste repositório. 

### :boom: Deu erro?
```python
pytesseract.pytesseract.TesseractNotFoundError: tesseract is not installed or it's not in your path
```

- Procure no arquivo <i>ocr.py</i> o comando: 

```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
```

- Altere o valor para o local onde o Tesseract foi instalado

```python
pytesseract.pytesseract.tesseract_cmd = r'SEU CAMINHO AQUI\tesseract.exe'
```

### :smiling_imp: Mais, eu quero mais

Neste repositório há também o arquivo <i>preprocessing.py</i> que traz algumas rotinas de preparação da imagem com o OpenCV, para melhorar a performance do OCR. 
Utilize do código comentado em <i>ocr.py</i> e brinque à vontade. :gift:


#### :floppy_disk: Fonte original de pesquisa:
https://nanonets.com/blog/ocr-with-tesseract/
