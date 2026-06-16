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

import matplotlib.pyplot as plt

# 단일 데이터 플롯 (y값만 제공 시 x값은 0부터 자동 생성)
plt.plot([1, 4, 9, 16])
plt.show()

# 쌍 데이터 플롯 (x값과 y값 모두 제공)
plt.plot([10, 20, 30, 40], [1, 4, 9, 16])
plt.show()
''' [link]2[/link] [link]3[/link] '''
