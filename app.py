import streamlit as st

# Title
st.title("Hello GeeksForGeeks !!!")

# Markdown
st.markdown("### This is a markdown")

# success
st.success("Success")

# success
st.info("Information")

# success
st.warning("Warning")

# success
st.error("Error")

# Write text
st.write("Text with write")

# Writing python inbuilt function range()
st.write(range(10))


# Display Images

# import Image from pillow to open images
from PIL import Image
img = Image.open("images/logo.png")

# display image using streamlit
# width is used to set the width of an image
st.image(img, width=200)
