from PIL import Image, ImageFilter
import streamlit as st

def filter(im):
    im1 = im.filter(ImageFilter.GaussianBlur(20))
    im2 = im.filter(ImageFilter.SHARPEN)
    im3 = im.filter(ImageFilter.SMOOTH)
    im4 = im.filter(ImageFilter.SMOOTH_MORE)
    im5 = im.filter(ImageFilter.EDGE_ENHANCE)
    im6 = im.filter(ImageFilter.CONTOUR)
    im7 = im.filter(ImageFilter.FIND_EDGES)
    im8 = im.filter(ImageFilter.MinFilter(3))
    im9 = im.filter(ImageFilter.MaxFilter(3))
    im10 = im.filter(ImageFilter.MedianFilter(3))+
    im11 = im.filter(ImageFilter.EMBOSS)

    return im1,im2,im3,im4,im5,im6,im7,im8,im9,im10,im11

st.title("image Basic working")
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

    st.title("filter on image")
    filtered_images = filter(im)
    c = st.beta_columns(3)
    for i,im in enumerate(filtered_images):
        c[i%3].image(im)
    

st.title("image blending")
f1 = st.file_uploader("select 1 image",type=['jpg','jpeg','png'])
f2 = st.file_uploader("select 2 image",type=['jpg','jpeg','png'])
if f1 and f2:
    im1 = Image.open(f1)
    im2 = Image.open(f2)
    # make them equal in size , mode
    im1 = im1.resize(im2.size) 
    im1 = im1.convert(im2.mode)
    
    c = st.beta_columns(2)
    c[0].image(f1)
    c[1].image(f2)
    c[0].write(im1.size)
    c[0].write(im1.mode)
    c[1].write(im2.size)
    c[1].write(im2.mode)
    
    mix = st.slider("mix",0.0,1.0,0.5)
    im3 = Image.blend(im1,im2,mix)
    st.image(im3)
    if st.button("save blended"):
        im3.save(f"blended_{f1.name}_{f2.name}.{im2.format}")