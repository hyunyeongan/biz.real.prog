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
