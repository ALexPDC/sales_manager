import streamlit as st
from datetime import datetime

#Establecer icono y nombre en el navegador
st.set_page_config(page_title="Sales Dashboard", page_icon="Logo/doge.jpg")

#sidebar
menu = st.sidebar.radio("ventas", ("Registro de ventas", "Dashboard"))

# Obtener la fecha actual
today = datetime.today().date()

if menu=="Registro de ventas":
    
    st.title('Sales Dashboard')

    option = st.selectbox('Selecciona la acción', ('Create', 'Read', 'Update', 'Delete'))

    if option == 'Create':
        sales_advisor=st.selectbox("Asesor Comercial",("Sandro","nombre1","nombre2","nombre3"), index=None, placeholder="Seleccionar Asesor de ventas")
        with st.form(key="Ventas"):
            submitday=today
            date = st.date_input("Fecha de cierre", value=today, format="DD/MM/YYYY")
            col1, col2 = st.columns(2)
            with col1:
                firstname = st.text_input("Nombre")
            with col2:
                lastname = st.text_input("Apellido")

            col1, col2 = st.columns(2)
            with col1:
                currency = st.selectbox("Moneda", ("PEN", "USD"))
            with col2:
                amount = st.number_input('Ingrese el monto', value=None, placeholder="Monto")

            submit_button = st.form_submit_button(label="Registrar")
    elif option == 'Read':
        st.title('Read')
    elif option == 'Update':
        st.title('Update')
    elif option == 'Delete':
        st.title('Delete')
elif menu=="D   ashboard":
    st.title("Dashboard")
