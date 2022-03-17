print('hello git')
import streamlit as st
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import io  
API_key = 'BbQRggRFUKV-cuLo2ULqhPNn2-mqxUJQ4_3F8AAoitwb'
url = "https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/69c30025-d0b1-4f8d-b963-3e889e3ffb6d"

# autheniticating the API key

authenticator = IAMAuthenticator(apikey=API_key)

# setting our language translator object

langtranslator = LanguageTranslatorV3(version='2022-02-07',
                                     authenticator=authenticator)

# establishing the connection with the service

langtranslator.set_service_url(url)

st.title('Language Translator')

lang_dict={'French':'fr','Arabic':'ar','Bengali':'bn','Russian':'ru','English':'en',
           'Portuguese':'pt'}

add_selectbox= st.sidebar.selectbox('From which source do you want to translate'
                                    ,["text","file"])
#print(add_selectbox)
#print(type(add_selectbox))


if (add_selectbox == "text") :
    col1, col2 = st.columns(2)
    with col1:
        st.subheader('select original language')
        lang_select1=st.selectbox("Select language 1 " , ('French','Arabic','Bengali',
                                              'Russian','English','Portuguese'))
        st.write('enter the text in ',lang_select1)
        origin_txt = st.text_area('text to translate', " " )

    with col2 :
        st.subheader('select translation language')
        lang_select2=st.selectbox('Select language 2 ',('French','Arabic','Bengali',
                                              'Russian','English','Portuguese'))
    if st.button('Translate'):
        if(lang_select1==lang_select2):
            st.error('Please enter differents languages')
        else:    
            model=lang_dict[lang_select1]+'-'+lang_dict[lang_select2]
            translation = langtranslator.translate(text=origin_txt,model_id=str(model))    
            final_txt =str(translation.get_result()['translations'][0]['translation'])
            with col2:
                st.write(final_txt)
              
#################################
#################################
#################################
#################################
#################################
################################
else :
    
    uploaded_file = st.file_uploader("Choose a .txt file", accept_multiple_files=False,type='txt')
    if uploaded_file is not None:
        
        
        if st.button('Load'):
            
            #st.write("filename:", uploaded_file.name)
            #f = io.StringIO("some initial text data")
            f_data =str(uploaded_file.read(),'utf-8')
            with st.expander("See the text"):
                
                st.write(f_data)

            #with open (uploaded_file,'r') as file :
             #   lines=file.read()            
              #  st.write(lines)
        
            st.subheader('language selections')
            col3,col4=st.columns(2)
            with col3:
            
                lang_select3=st.selectbox('Select original text language',('French','Arabic','Bengali',
                                              'Russian','English','Portuguese'))
            with col4:
                
                st.write('Select translated text language')
                lang_select4=st.selectbox('Select translated text language',('French','Arabic','Bengali',
                                              'Russian','English','Portuguese'))
        else :
             pass
            
        if st.button('translate file'):
            
            if(lang_select3==lang_select4):
                    st.error('Please enter differents languages')
            else:
                
                model1=lang_dict[lang_select3]+'-'+lang_dict[lang_select4]
                translation = langtranslator.translate(text=f_data,model_id=str(model1))    
                final_txt =str(translation.get_result()['translations'][0]['translation'])
                with st.expander("See the text"):
                    st.write(final_txt)
        
        
    


        
#translation.get_result()
