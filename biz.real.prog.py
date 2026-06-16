import streamlit as st

# 제목
st.title('제목:smile:')

""" ### 이건 부제목 """
st.markdown('*마크다운 H1: st.write()*')

st.divider()

st.write('##### 코드블록: st.code()')
st.code('print("Hello World")', language='python')
st.code('print("Hello World")', language='python', line_numbers=True)

st.latex('a=b^2')
st.latex('\int_a^bf(x)dx')

'''###:queen:Magic 적용
1. ordered item
  -강조: **unordered item**
  -기울임: *unordered item*
2. :red[ordered item]
3. :green[ordered item]
'''


img_file = st.file_uploader('이미지를 업로드 하세요.', type=['png', 'jpg', 'jpeg'])

from PTL import Image

img = Image.open('2026_Biz/ori.png')
st.image(img)

         
