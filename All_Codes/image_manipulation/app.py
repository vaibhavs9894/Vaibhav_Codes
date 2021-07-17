from PIL import Image
import streamlit as st


file = st.file_uploader("select an image",type=['jpg','jpeg','png'])
if file:
    st.image(file)
    im = Image.open(file)
    st.write(im.width, im.height)
    st.write(im.mode)
    st.write(im.format) 

    st.title("rotate and save")
    rotation = st.slider("rotate by",0,360,0)
    color = st.color_picker("select a fill color",value='#ffffff')
    im2 = im.rotate(rotation,fillcolor=color)
    st.image(im2)
    if st.button("save rotated"):
        im2.save(f"rotated_{file.name}.{im.format}")
        st.success(f"rotated_{file.name}.{im.format} saved")

    st.title("crop and save")
    c1,c2,c3,c4 = st.beta_columns(4)
    left = c1.slider("left",0,im.width,0)
    top = c2.slider("top",0,im.height,0)
    right = c3.slider("right",left+1,im.width ,0)
    bottom = c4.slider("bottom",top+1,im.height ,0)
    try:
        im2 = im.crop((left,top,right,bottom))
        st.image(im2)
        if st.button("save cropped"):
            im2.save(f"cropped_{file.name}.{im.format}")
            st.success(f"cropped_{file.name}.{im.format} saved")
    except Exception as e:
        st.error(f"invalid crop {e}")