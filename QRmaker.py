import streamlit as st
import qrcode
from PIL import Image

st.title("QRコード自動生成アプリ")

url = st.text_input('QRコードを生成したいURL:')

if st.button('QRコード生成'):
    _img = qrcode.make(url)
    _img.save('qrcode.png')
    img =Image.open('qrcode.png')
    st.write(str(url))
    st.image(img)    
    with open('qrcode.png', 'rb') as file:
        btn = st.download_button(
            label='QRコードをダウンロードする',
            data = file,
            file_name ='qrcode.png',
            mime="image/png"
        )