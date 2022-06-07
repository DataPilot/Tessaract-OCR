# import principal
import streamlit as st
# imports relacionados
from PIL import Image
import pytesseract


class OCR:

    def __init__(self):
        # altera titulo da pagina
        st.set_page_config(page_title="Python OCR")
        # inicializa variveis
        self.text = ""
        self.analisar_text = False

    def initial(self):
        # conteudo inicial da pagina
        st.title("OCR")
        st.write("Optical Character Recognition (OCR)")
        imagem = st.file_uploader(
            "Upload Image for OCR", type=["png", "jpg"])
        # se selecionar alguma imagem...
        if imagem:
            img = Image.open(imagem)
            st.image(img, width=400)
            st.info("Text")
            self.text = self.extrair_texto(img)
            st.write("{}".format(self.text))

    def extrair_text(self, img):
        # extrai text from image
        # text = pytesseract.image_to_string(img)
        text = pytesseract.image_to_data(img)
        return text


ocr = OCR()
ocr.initial()
