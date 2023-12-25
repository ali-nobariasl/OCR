from fastapi import FastAPI, File, UploadFile
import shutil
import pytesseract


app = FastAPI()

@app.post('/')
def ocr(img: UploadFile=File(...)):
    filePath = 'txtfile'
    with open(filePath, "w+b") as f:
        shutil.copyfileobj(img.file, f)
    return pytesseract.image_to_string(filePath, lang='eng')