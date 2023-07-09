
#  PROYECTO CONSOLIDACION STREAMLIT: FUNCION app.py

# Importaciones
import streamlit as st
import streamlit.components.v1 as stc
from eda_app import run_eda_app
from ml_app import run_ml_app




PAGE_HOME = "Home"
PAGE_EDA = "EDA"
PAGE_ML = "ML"
PAGE_INFO = "Info"
PAGE_SELECT=[PAGE_HOME,PAGE_EDA , PAGE_ML , PAGE_INFO]



# Función main()
def main():
	#page selector
	ps = st.sidebar.selectbox("Selector de sección",(PAGE_SELECT))

	

	if ps== PAGE_HOME:
		home_app()
	elif ps == PAGE_EDA:
		run_eda_app()
	elif ps == PAGE_INFO:
		info()
	else:
		run_ml_app()		


def header():
	stc.html("""
<style>
.header {
    background-color: blue;
    padding: 20px;
    color: white;
    text-align: center;
    border-radius: 10px;
}
	  
.header h1, .header p {
    color: white;
    font-size: 26px;
}
</style>

<div class="header">
    <h1>App para la detección temprana de DM</h1>
    <p>(Diabetes Mellitus)</p>
</div>
""")

def home_app():
	
	st.markdown("# Home")
	st.markdown("## App para la detección temprana de DM")

	st.write("Dataset que contiene señanles y sintmoas que puedan indicar diabetes o posibilidad de diabetes.")

	st.markdown("## Fuente de datos")
	st.info("https://archive.ics.uci.edu/ml/datasets/Early+stage+diabetes+risk+prediction+dataset")

	st.write("Contenidos de la App")
	st.info("""
	-Eda Section: Analisís exploratorio de los datos
	 
	-ML Section: Predicción de Diabetes basada en ML (Machine Learning)
	""")

def info():
	st.subheader("Info")
	st.text("""MBIT, Proyecto de consolidación, librería Streamlit.
	 		* * *
	 """)
	#stc.iframe("https://www.w3schools.com")
	
	stc.html("""
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
body {margin:0;}

.icon-bar {
  width: 100%;
  background-color: #555;
  overflow: auto;
}

.icon-bar a {
  float: left;
  width: 20%;
  text-align: center;
  padding: 12px 0;
  transition: all 0.3s ease;
  color: white;
  font-size: 36px;
}

.icon-bar a:hover {
  background-color: #000;
}

.active {
  background-color: #04AA6D;
}
</style>
<body>
<div class="icon-bar">
  <a class="active" href="https://www.linkedin.com/in/jesusalvarezcrespo/" target="_blank"><i class="fa fa-linkedin" aria-hidden="true"></i></a> 
  <a href="" target="_blank"><i class="fa fa-github"></i></a> 
  <a href="https://www.mbitschool.com" target="_blank"><i class="fa fa-globe"></i></a> 	  
  <a class="active" href="https://www.linkedin.com/in/jesusalvarezcrespo/" target="_blank"><i class="fa fa-linkedin"></i></a> 
  <a href="#"><i class="fa fa-envelope"></i></a> 
</div>

</body>
""")


if __name__ == '__main__':
	header()
	main()