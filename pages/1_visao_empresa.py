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
import seaborn as sns

#-----------------------------------------------
# Funções 
#-----------------------------------------------

def country_maps( df1 ):
    df_aux = (df1.loc[:, ['City', 'Road_traffic_density', 'Delivery_location_latitude', 'Delivery_location_longitude']]
                  .groupby( ['City', 'Road_traffic_density'])
                  .median()
                  .reset_index())
    df_aux = df_aux.loc[df_aux['City']  != 'NaN', :]

    df_aux = df_aux.loc[df_aux['Road_traffic_density']  != 'NaN', :]

    map = folium.Map( )


    for index, location_info in df_aux.iterrows():
        folium.Marker( [location_info['Delivery_location_latitude'],
                        location_info['Delivery_location_longitude']], 
                        popup=location_info[['City','Road_traffic_density' ]] ).add_to(map)
            
        folium_static( map, width=1024 , height=600 )          
        return None
        





def order_share_by_week( df1 ):
    df_aux01 = (df1.loc[:, ['ID','Week_of_year']]
                            .groupby('Week_of_year')
                            .count()
                            .reset_index() )

    df_aux02 = df.loc[:, ['Delivery_person_ID', 'Week_of_year']].groupby('Week_of_year').nunique().reset_index()
    df_aux = pd.merge( df_aux01, df_aux02, how='inner' )
    df_aux['order_by_deliver'] = df_aux['ID'] / df_aux['Delivery_person_ID']
    fig =  px.line(df_aux, x= 'Week_of_year' ,  y = 'order_by_deliver' )
              
    return fig 





def order_by_week( df1 ):
    df1['Week_of_year'] = df1['Order_Date'].dt.strftime('%U')
    df_aux =df1.loc[:, ['ID','Week_of_year']].groupby('Week_of_year').count().reset_index()
    fig = px.line( df_aux, x='Week_of_year', y='ID')
        
    return fig




def traffic_order_city( df1 ):
    
    df_aux =(df1.loc[: , ["ID", 'City', 'Road_traffic_density']]
                 .groupby(['City', 'Road_traffic_density'])
                 .count()
                 .reset_index() )
    df_aux =  df_aux.loc[df_aux ['City'] != 'NaN' , :]
    df_aux =  df_aux.loc[df_aux ['Road_traffic_density'] != 'NaN' , :]
    fig = px.scatter(df_aux, x = 'City', y= 'Road_traffic_density', size ='ID', color= 'City')

    return fig



def traffic_order_share ( df1 ):
    df_aux = (df1.loc[:, ['ID', 'Road_traffic_density']]
                  .groupby('Road_traffic_density')
                  .count()
                  .reset_index() )
    df_aux = df_aux.loc[df_aux ['Road_traffic_density'] != "NaN", :]
    df_aux ['entregas_perc'] = df_aux['ID'] / df_aux['ID'].sum()
    
    return fig 



def order_metric(df1 ):
    with st.container():
        cols= ['ID', 'Order_Date']
            
        df_aux = df1.loc[:, cols].groupby('Order_Date').count().reset_index()
        fig = px.bar( df_aux, x= 'Order_Date' , y= 'ID')
        
   
        return fig 


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

    # Coversão de texto para data 
    df1['Order_Date'] = pd.to_datetime( df1['Order_Date'], format='%d-%m-%Y')

    # Removendo (NaN)
    linhas_vazias = (df1['Delivery_person_Age'] != 'NaN ' )
    df1 = df1.loc[linhas_vazias, :].copy()

    linhas_vazias = (df1['Delivery_person_Age'] != 'NaN ' )
    df1 = df1.loc[linhas_vazias, :].copy()

    linhas_vazias = (df1['multiple_deliveries'] != 'NaN ')
    df1 = df1.loc[linhas_vazias, :].copy()

    df1['multiple_deliveries'] = df1['multiple_deliveries'].astype( int )

    linhas_vazias = (df1['Road_traffic_density'] != 'NaN ')
    df1 = df1.loc[linhas_vazias, :].copy()

    linhas_vazias = (df1['City'] != 'NaN' )
    df1 = df1.loc[linhas_vazias, :].copy()

    linhas_vazias = (df1['Festival'] != 'NaN ' )
    df1 = df1.loc[linhas_vazias, :].copy()
    
    









    # Removendo espaços de strings/ texto/ object
    #df = df.reset_index( drop=True )
    #for i in range(len(df)): 
     # df.loc[i, 'ID'] =  df.loc[i, "ID"].strip()

     # Removendo espaços de strings/ texto/ object ( Solução mais rapida sem o FOR)

    df1.loc[:, 'ID'] = df1.loc[:, 'ID'].str.strip()
    df1.loc[:, 'Road_traffic_density'] = df1.loc[:, 'Road_traffic_density'].str.strip()
    df1.loc[:, 'Type_of_order'] = df1.loc[:, 'Type_of_order'].str.strip()
    df1.loc[:, 'Type_of_vehicle'] = df1.loc[:, 'Type_of_vehicle'].str.strip()
    df1.loc[:, 'City'] = df1.loc[:, 'City'].str.strip()
    df1.loc[:, 'Festival'] = df1.loc[:, 'Festival'].str.strip()
    
    # Conversao de texto/categoria/strings para numeros decimais
    df['Delivery_person_Ratings'] = df['Delivery_person_Ratings'].astype( float )


    # Limpando a coluna de Tiem Taken

    df1['Time_taken(min)' ] = df1['Time_taken(min)' ].apply(lambda x: x.split( '(min)')[1] )
    df1['Time_taken(min)' ] = df1['Time_taken(min)' ].astype( int )
    
    # Criando a coluna Weel_of_year 
    df['Week_of_year'] = df['Order_Date'].dt.strftime('%U')

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

st.header('Marketplace - Visão cliente')
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

tab1, tab2, tab3 =st.tabs(['Visão Gerencial', 'Visão Tática', 'Visão Geografica'])
#Order Metric
with tab1:
    with st.container():
        fig = order_metric( df1 )
        st.markdown ( ' # Pedidos Por Dia')
        st.plotly_chart(fig, use_container_width=True)


        
with st.container():
    col1, col2 = st.columns( 2 )
        

  
    with col1:
        fig = traffic_order_share( df1 ) 
        st.header( "Traffic order share")
        st.plotly_chart(fig, use_container_width=True)
        
        
                
    with col2:
        st.header ("Traffic Order City")
        fig = traffic_order_city( df1 )
        st.plotly_chart( fig, use_container_width=True )
        
        
with tab2:
    with st.container():
        st.markdown( "# Order by Week" )
        fig = order_by_week( df1 )
        st.plotly_chart(fig , use_container_width=True )
        
        
        
    with st.container():
        st.markdown( "# Order Share by Week" )
        fig = order_share_by_week( df1 )
        st.plotly_chart(fig , use_container_width=True )   
            
            
        
with tab3:
    st.markdown( "# Country Maps" )
    country_maps( df1 )
    
    
    
        
        
           
    






