import streamlit as st

st.title("Hello Streamlit")

st.header("Header") 

st.subheader("Sub header")

st.text("lorem ipsum dneduni cweniun")

st.markdown(""" 
# H1 tag
## H2 tag
### H3 tag
:moon: <br>
:sunglasses:
# ** bold **

""" ,True)



st.latex(r'''  ∫ (x2-1)(4+3x)dx  = 4(x3/3) + 3(x4/4)- 3(x2/2) – 4x + C

The antiderivative of the given function ∫  (x2-1)(4+3x)dx is 4(x3/3) + 3(x4/4)- 3(x2/2) – 4x + C. ''')

st.write("Harsh" , " Rajneesh" ," Yashwant")