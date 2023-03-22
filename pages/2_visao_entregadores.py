import pandas as pd 
import re
import streamlit as st
from PIL import Image
from streamlit_folium import folium_static
import datetime as dt
import streamlit as st
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# Libraries
import haversine 
import plotly.express as px
import plotly.graph_objs as go
import folium

#-----------------------------------------------
# Funções 
#-----------------------------------------------

#------------------------------------------------------------------------------------------------






def clean_code( df1 ):
    """ Está função tem a responsabilidade de limpar o dataframe
    
        Tipos de limpeza: 
        1. Remoção dos dados NaN
        2. Mudança do tipo da coluna de dados
        3. Remoção dos espeços das variaveis de texto
        4. Formatação da coluna de datas
        5. Limpeza da coluna de tempo ( Remoção do texto da variavel numérica )
        
        Input: Dataframe
        Output: Dataframe 
        
     """    

    # Conversao de texto/categoria/strings para numeros decimais
    df1['Delivery_person_Ratings'] = df1['Delivery_person_Ratings'].astype( float )

    # Coversão de texto para data 
    df1['Order_Date'] = pd.to_datetime( df1['Order_Date'], format='%d-%m-%Y')



  # Removendo (NaN)
    linhas_vazias = (df1['Delivery_person_Age'] != 'NaN ' )
    df1 = df1.loc[linhas_vazias, :].copy()

    linhas_vazias = (df1['Delivery_person_Age'] != 'NaN ' )
    df1 = df1.loc[linhas_vazias, :].copy()

    linhas_vazias = (df1['multiple_deliveries'] != 'NaN ')
    df1 = df1.loc[linhas_vazias, :].copy()

    linhas_vazias = (df1['Road_traffic_density'] != 'NaN ')
    df1 = df1.loc[linhas_vazias, :].copy()

    linhas_vazias = (df1['City'] != 'NaN' )
    df1 = df1.loc[linhas_vazias, :].copy()

    linhas_vazias = (df1['Festival'] != 'NaN ' )
    df1 = df1.loc[linhas_vazias, :].copy()

    linhas_vazias = (df1['Time_taken(min)'] != 'NaN ' )
    df1 = df1.loc[linhas_vazias, :].copy()


    # Removendo espaços de strings/ texto/ object ( Solução mais rapida sem o FOR)

    df1.loc[:, 'ID'] = df1.loc[:, 'ID'].str.strip()
    df1.loc[:, 'Road_traffic_density'] = df1.loc[:, 'Road_traffic_density'].str.strip()
    df1.loc[:, 'Type_of_order'] = df1.loc[:, 'Type_of_order'].str.strip()
    df1.loc[:, 'Type_of_vehicle'] = df1.loc[:, 'Type_of_vehicle'].str.strip()
    df1.loc[:, 'City'] = df1.loc[:, 'City'].str.strip()
    df1.loc[:, 'Festival'] = df1.loc[:, 'Festival'].str.strip()

    # Limpando a coluna de Tiem Taken

    df1['Time_taken(min)' ] = df1['Time_taken(min)' ].apply(lambda x: x.split( '(min)')[1] )
    df1['Time_taken(min)' ] = df1['Time_taken(min)' ].astype( int )

    return df1

#------------------- Inicio da estrutura logica do código -------------------------------------

# Import dataset
df = pd.read_csv( 'dataset/train.csv' )

# Limpando dados
df1 = clean_code( df )


#====================================================================
# Barra lateral
#====================================================================

#image = Image.open('')
#st.sidebar.image(image, caption='')

#image_path ='Documents/Rapos/logo.png'
#mage = image.open(image_path )
#st.sidebar.image( image, width=120 ) 

st.header('Marketplace - Visão Entregadores')
st.sidebar.markdown("# Curry Company")
st.sidebar.markdown("## Entrega mais rápida da cidade")
st.sidebar.markdown("""___""")

st.sidebar.markdown('## Selecione Uma Data Limite')
date_slider = st.sidebar.slider(
    'Até qual valor?',
    value=pd.datetime( 2022, 4, 13),
    min_value=pd.datetime(2022, 2, 11),
    max_value=pd.datetime( 2022, 4, 6),
    format='DD-MM-YYYY')


st.sidebar.markdown("""___""")

# Filtro de data
#linhas_selecionadas = df1['Order_Date']<date_slider
#df1 = df1.loc[linhas_selecionadas, :]



traffic_options = st.sidebar.multiselect(
    'Quais as condições do transito',
    ['Low', 'Medium', 'High', 'Jam'],
    default=['Low', 'Medium', 'High', 'Jam'] )

#Filtro de transito
linhas_selecionadas = df1['Road_traffic_density'].isin( traffic_options )
df1 = df1.loc[linhas_selecionadas, :]

st.sidebar.markdown("""___""")
st.sidebar.markdown('### Powerd By Comunidade DS')

linhas_selecionadas = df1['Order_Date']<date_slider
df1 = df1.loc[linhas_selecionadas, :]


                          

#====================================================================
# Layout streamlit
#====================================================================

tab1, tab2, tab3 =st.tabs(['Visão Gerencial' ,'', ''])                    

with tab1:
    with st.container():
        st.title('Overall Metrics')
        col1, col2, col3, col4 = st.columns(4, gap='large')
        
        with col1:
            st.markdown ( ' # Delivery Person Age')
            # A maior idade dos entregadores 
            maior_idade =df1.loc[:, 'Delivery_person_Age'].max() 
            col1.metric( ' Maior de idade', maior_idade)

        
         
        with col2:
            # A menor idade dos entregadores 
            
            menor_idade =df.loc[:, 'Delivery_person_Age'].min() 
            col2.metric( ' Menor de idade', menor_idade)
            
        with col3:
            # A melhor condição de veiculo:
            
            melhor_condicao = df.loc[:, 'Vehicle_condition'].max() 
            col3.metric( ' Melhor condição  ', melhor_condicao)
            
            
        with col4:
            pior_condicao = df.loc[:, 'Vehicle_condition'].min() 
            col4.metric( ' Pior condição  ', pior_condicao)
            
            
        with st.container():
            st.markdown("""___""")
            st.title( ' Avaliações' )
            
            
           
                     
            col1, col2 = st.columns(2)
            with col1:
                st.markdown( '##### Avaliação média por entregador ')
                df_avg_ratings_per_deliver = (df1.loc[:,                               ['Delivery_person_ID','Delivery_person_Ratings']]
                                              .groupby('Delivery_person_ID')
                                              .mean()
                                              .reset_index())
                st.dataframe( df_avg_ratings_per_deliver )

                
            with col2:
                st.markdown( '##### Avaliação média por Transito ')
                df_avg_std_by_traffic = (df1.loc[:, ['Delivery_person_Ratings', 'Road_traffic_density']]
                                         .groupby('Road_traffic_density')
                                         .agg( {'Delivery_person_Ratings': ['mean', 'std'] } ) )
                df_avg_std_by_traffic.columns = ['Delivery_mean', 'delivery_std']
                df_avg_std_by_traffic = df_avg_std_by_traffic.reset_index()
                st.dataframe( df_avg_std_by_traffic ) 



            st.markdown( '##### Avaliação média por clima' )
            
            df_avg_std_by_rating_weather = (df1.loc[:, ['Delivery_person_Ratings', 'Weatherconditions']]
                                               .groupby('Weatherconditions')
                                               .agg( {'Delivery_person_Ratings': ['mean', 'std'] } ) )
            df_avg_std_by_rating_weather.columns = ['Weatherconditions_mean', 'Weatherconditions_std']
            df_avg_std_by_rating_weather = df_avg_std_by_rating_weather.reset_index()
            st.dataframe( df_avg_std_by_rating_weather )



                
                
        with st.container():
            st.markdown( """___""")
            st.title(' Velocidade de entrega')
            
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown('##### Top Entregadores mais rapidos')
            df1 = (df1.loc[: ,['Delivery_person_ID' , 'City', 'Time_taken(min)']]
                   .groupby(['City', 'Delivery_person_ID'])
                   .min()
                   .sort_values(['City', 'Time_taken(min)'], ascending=True).reset_index() )
            df_aux01 = df1.loc[df1['City'] == 'Metropolitian', :].head(10)
            df_aux02 = df1.loc[df1['City'] == 'Urban', :].head(10)
            df_aux03 = df1.loc[df1['City'] == 'Semi-Urban', :].head(10)
            df2 = pd.concat( [df_aux01, df_aux02, df_aux03] ).reset_index( drop=True)
            st.dataframe(df2)
            
            
            
        with col2:
            st.markdown('##### Top Entregadores mais lentos')
            df1 = (df1.loc[: ,['Delivery_person_ID' , 'City', 'Time_taken(min)']]
                   .groupby(['City', 'Delivery_person_ID'])
                   .max()
                   .sort_values(['City', 'Time_taken(min)'], ascending=False)
                   .reset_index() )
            df_aux01 = df1.loc[df1['City'] == 'Metropolitian', :].head(10)
            df_aux02 = df1.loc[df1['City'] == 'Urban', :].head(10)
            df_aux03 = df1.loc[df1['City'] == 'Semi-Urban', :].head(10)
            df2 = pd.concat( [df_aux01, df_aux02, df_aux03] ).reset_index( drop=True)
            st.dataframe(df2)
            