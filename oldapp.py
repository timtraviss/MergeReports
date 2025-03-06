from PIL import Image
import streamlit as st

st.set_page_config(layout="wide", page_icon=":clipboard:", page_title="Image Converter")

st.title('Image Converter')
import streamlit as st
st.image('HeaderImage.png', caption='Image Conversion')
st.write('The purpose of this page is to convert .webp files to .jpeg')

uploaded_file1 = st.file_uploader("Upload .webp file", key='1')
if uploaded_file1 is not None:
    input_file = uploaded_file1
    # st.success('File Uploaded!')

    # Define the output file path
    output_file = "output_file.jpeg"

    def convert_webp_to_jpeg(input_file, output_file):
        try:
            # Open the .webp image
            webp_image = Image.open(input_file)
            
            # Convert the image to RGB mode and save as .jpeg
            webp_image.convert('RGB').save(output_file, 'jpeg')
            
            st.success(f"File uploaded and conversion complete: {output_file}")
        except Exception as e:
            st.error(f"Error: {e}")

    # Perform the conversion
    convert_webp_to_jpeg(input_file, output_file)

    # Provide a download button for the converted image
    with open(output_file, "rb") as file:
        btn = st.download_button(
                label="Download image",
                data=file,
                file_name="New_Image.jpeg",
                mime="image/jpeg"
            )
        
# Add a button to refresh the page
if st.button('Refresh Page'):
    st.experimental_rerun()
