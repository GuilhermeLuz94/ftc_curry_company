import streamlit as st
from PIL import Image


st.set_page_config(
    page_title="Home",
    
)    

#image_path = '/Users/macbookpro/Documents/Rapos/Ftc_python/'
#image= image.open('logo.png')
#st.sidebar.image( image, width=120 )
                  
                  

st.sidebar.markdown("# Curry Company")
st.sidebar.markdown("## Entrega mais rápida da cidade")
st.sidebar.markdown("""___""")


st.write( "# Curry Company Growth Dashboard" )



st.sidebar.markdown("""___""")

# Filtro de data
#linhas_selecionadas = df1['Order_Date']<date_slider
#df1 = df1.loc[linhas_selecionadas, :]



st.markdown(
    """
    Growth Dashboard foi contruido para acompahar as métricas de crescimento dos Entregadores e Restaurantes. 
    
    ### Como utilizar esse Growth Dashboard?
    - Visão Empresa:
       - Visão Gerencial: Métricas gerais de comportamento.
       - Visão Tática: Indicadores semanais de crescimento. 
       - Visão Geográfica: Insights de geolocalização. 
       
   - Visão Entregadoror:
       - Acompanhamento dos indicadores semanais de crescimento
       
       ### Ask for Help
        - Time de Data Science no Discord
           -@guilherme
""")           
    

                          
                  

                  
