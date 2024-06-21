import streamlit as st
st.title("Hello Victor!!! You are learning Streamlit")
st.header("You are awesome")
st.subheader("I am subheader")
st.text("Its a simple text")
st.markdown("# Header 1 ")
st.markdown("## Header 2 ")
st.markdown("### Header 3 ")
st.markdown("#### Header 4 ")
st.markdown("##### Header 5 ")
st.markdown("###### Header 6 ")
st.success("Success")
st.info("Information")
st.warning("Warning")
st.error("Error")
st.exception(ZeroDivisionError("Cannot devide by Zero"))
st.help(ZeroDivisionError)

st.write("range(1,100)")
st.write(1+25+690)
st.write(range(100,200))

st.code('x=10\n'
         'for i in range(x):\n'
          '    print(i)')

st.subheader("Checkbox")

if st.checkbox('Male'):
    st.write('You have selected Male checkbox')
elif st.checkbox('Female'):
    st.write('You have selected Female checkbox')
elif st.checkbox('Other'):
    st.write('You have selected Other checkbox')

st.subheader("Radio Button")

radiobutton = st.radio('Select Gender:',('Male','Female'))
if radiobutton == 'Male':
    st.write('You have selected Male')
else:
    st.write('You have selected FeMale')

radiobutton = st.radio('Select Postion:',['Manager','CEO'])
if radiobutton == 'CEO':
    st.write('You have been selected for CEO')
else:
    st.write('You have selected for Manager')


st.subheader("Select Box")
selected_box_1 = st.selectbox("Data Science :: ",["ML Engineer","Data Analyst"])

if selected_box_1 == 'ML Engineer':
    st.write(f'You have been selected for {selected_box_1}')
else:
    st.write(f'You have been selected for {selected_box_1}')

selected_box_2 = st.selectbox("Full Stack :: ",["Design","Development"])
if selected_box_2 == 'Design':
    st.write(f'You have been selected for {selected_box_2}')
else:
    st.write(f'You have been selected for {selected_box_2}')


st.subheader("Multi Select Box")
multi_selected_box_1 = st.multiselect("Data Science :: ",["ML Engineer","Data Analyst","NLP","Deep Learning"])
len = len(multi_selected_box_1)
for i in range(len):
    st.write(f'You have selected {multi_selected_box_1[i]}')

st.subheader("Button")
button_1 = st.button("Click 1")
button_2 = st.button("Click 2")
if button_1 == 'Click 1':
    st.write("You are redirected to 'Google.com' ")
else:
    st.write("You are redirected to 'FB.com' ")

st.subheader("Slider")
selected_vol = st.slider('Select the number :: ',10,100,step=10)
st.write(f'You selected the {selected_vol}')

st.subheader("Input")

name = st.text_input("Enter your name:: ")
password = st.text_input("Enter your password:: ",type = 'password')
age = st.number_input("Enter your age:: ",10,40,step = 5)
text_area = st.text_area('Write about yourself:: ')
date = st.date_input("Input Date:: ")
time = st.time_input("Input Time:: ")

if age > 20:
    st.success("Hola!! You passed the age test")
    button = st.button("Sign Up")
    if button:
        st.write('You Signed up for Facebook')
else:
    st.warning("You cannot sign in Facebook")
