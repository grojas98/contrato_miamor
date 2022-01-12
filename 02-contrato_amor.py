# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 19:24:30 2022

@author: groja
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
import pandas as pd
from itertools import count
import seaborn as sns
import time
import psycopg2 as pg
from PIL import Image

#%%

def equivocado():
    st.write("""
             
             """)
    

state = 0
st.title('Renovación 2do contrato')
st.markdown("""**versión digital **""")

image = Image.open('parral.png')
st.image(image, use_column_width=True)


st.write("""
Hola mi amor, llegamos hasta aquí y vamos a seguir sumando momentos bonitos junto al otro,
quiero decirte que eres una personita muy especial para mi y me encantas muchisimos mundossssssssssss,
no puedo poner el numero exacto ahora porque va aumentando cada segundo <3.

Ahora mismo te extraño muchísimo pero sé que te veré más pronto que nunca <3 el sábado en el mágico campo de Parral
(no puedo poner emojis, aun no se programar tan bien yia)

Ahora que tal si firmas este contrato para que sigamos escribiendo esta historia tan bonita que tenemos los dos wawita
linda hermosa mía (carita enamorada carita enamorada yia), PERO ANTEEEEES UN TEST (carita del lente)
         
Empecemos mi amor<3
         
""")

    
if state == 0:
    genre = st.radio(
         "EL AYER ESSSSS.....",
         ('HISTORIA', 'MISTERIO', 'OBSEQUIO'),index=1,key=1)
    
    if genre == 'HISTORIA':
         state = 1
    else:
         st.write("ay intentalo de nuevo wawi<3")
         state = 0
if state == 1:
    # st.write('CORRECTOOOOOOOOO MI AMORRRRRRR<333')
    st.write("""
        CORRECTOOOOOOOOO MI AMORRRRRRR<333
        siguienteeee.....
    """)
    genre = st.radio(
         "EL MAÑANA ESSSSSS.....",
         ('HISTORIA', 'MISTERIO', 'OBSEQUIO'),index=0,key=2)
    
    if genre == 'MISTERIO':
          state = 2
    else:
          st.write("ay intentalo de nuevo wawi<3")
if state == 2:
    st.write("""
        CORRECTOOOOOOOOO MI AMORRRRRRR<333
        siguienteeee.....
    """)
    genre = st.radio(
         "EL HOYYY ES.....",
         ('HISTORIA', 'MISTERIO', 'OBSEQUIO'),index=1,key=3)
    
    if genre == 'OBSEQUIO':
         st.write('CORRECTOOOOOOOOO MI AMORRRRRRR<333')
         state = 3
    else:
         st.write("ay intentalo de nuevo wawi<3")
if state == 3:
    st.write("""
        Ahora,  firmaras???
             
    """)
    firmar = st.button('FIRMAR')
    if firmar:
        image = Image.open('heart.png')
        st.image(image, use_column_width=True)
        st.write("""
            
            POR MUCHISIMO TIEMPO MÁS JUNTITOOOOOOOOOOS<3
            ME ENCANTAS DEMASIADO MI AMOR, ERES LO MÁS PRECIOSO QUE HE
            TENIDOOOOOO<3
            
            MI FIRMA: Gonzalo Rojas B.
                 
                 
        """)
        

# if comenzar:
#     st.write("""
#     1era pregunta....

#     EL **AYER** ESSSS.....
             
#     """)
#     if state == 0:
#         if decide('HISTORIA','MISTERIO','OBSEQUIO') == 1:
#             st.write("""
                     
#                 hola
#                      """)
    
    # if state == 1:
    #     st.write("""
    #     2da pregunta....
    
    #     EL **MAÑANA** ESSSS.....
    #     """)
        
    #     decide('MISTERIO','OBSEQUIO','HISTORIA')
# but = st.empty()
# but2 = st.empty()
# but3 = st.empty()


# if decide(pa2,pa3,pa) == 1:
#     st.write("""
#         EL **MAÑANA** ESSSSS.....
             
#     """)
#     ma = but.button('HISTORIA!')
#     ma2 = but2.button('MISTERIO!')
#     ma3 = but3.button('OBSEQUIO!')
#     if decide(ma,ma3,ma2) == 1:
#         st.write("""
#             hola
                 
#         """)



# if state == 0:

#     if pa:
#         st.write("""
#             CORRECTOOOOOOOOOOOO MI AMORRRRRRRRR     
#         """)
#         st.write("""
#             2da pregunta......
                 
#         """)
#         state = 1
#     elif pa2:
#         st.write("""
#             ay:( intentalo de nuevo wawi   
#         """)
#         state = 0
#     elif pa3:
#         st.write("""
#             ay:( intentalo de nuevo wawi   
#         """)
#         state = 0


# if state == 1:


    
#     st.write("""
    
        
#         EL **MAÑANA** ESSSS....
             
#     """)
#     ma = st.button('HISTORIA2')
#     ma2 = st.button('MISTERIO2')
#     ma3 = st.button('OBSEQUIO2')

# if state == 2:
#     st.write("""
#              hola
#              """)
