# PROYECTO DE CONSOLIDACION STREAMLIT: FUNCION eda_app.py
# Importaciones: streamlit, pandas, matplotlib, seaborn
import streamlit as st
import pandas as pd
import matplotlib as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px


# Declaracion de constantes
ED_DESCR = "Descriptivo"
ED_GRPH = "Gráfico"
ED_LIST=[ED_DESCR,ED_GRPH]

def load_df():
	# Cargar los dataframes 
	df_du = pd.read_csv("data/diabetes_data_upload.csv")
	df_cl= pd.read_csv("data/diabetes_data_upload_clean.csv")
	df_fd = pd.read_csv("data/freqdist_of_age_data.csv")

	return df_du,df_cl, df_fd


# Función principal que emplearemos en la APP
def run_eda_app():
	# Cargar los dataframes
	df_du, df_cl, df_fd = load_df()

	# eda submenu
	es = st.sidebar.selectbox("SubMenu",(ED_LIST))

	st.markdown("## Sección EDA")

	if es== ED_DESCR:
		ed_descr_n(df_du, df_cl )
	elif es== ED_GRPH:
		ed_grph_fn(df_du, df_fd,df_cl )

# Conteo summatorio de dataframes
def summary_groups(df, value):
	st.dataframe(df.groupby([value])[value].count())

# Function de generacion graficos de pie
def build_pie_graph(df, value):
			val_count = df[value].value_counts()
			fig = go.Figure(data=[go.Pie(labels=val_count.index, values=val_count.values)])
			fig.update_layout(title='Gender Distribution' , width = 300 , height= 300)
			st.plotly_chart(fig)

def ed_descr_n(df_du, df_cl ):	
	#Construir la pagina
	st.markdown("### Análisis descriptivo")
	st.dataframe(df_du)

	with st.expander("Tipos de datos" ):
		st.dataframe(df_du.dtypes)

	with st.expander("Resumen descriptivo" ):
		st.dataframe(df_du)

	with st.expander("Distribución por género (Gender)" ):
		summary_groups(df_du, 'Gender')

	with st.expander("Distribución por clase/label (Class)" ):
		summary_groups(df_du, 'class')


def ed_grph_fn(df_du, df_fd , df_cl):
	#Construir la pagina
	
	with st.empty():
		ex1, ex2 =st.columns(2)
		with ex1.expander("Gráfico de distribución por género (Gender)"):
			# Create a Pie chart
			build_pie_graph(df_du, 'Gender')
		with ex2.expander("Gender Distribution"):
			summary_groups(df_du, 'Gender')

	with st.empty():
		ex3, ex4 =st.columns(2)
		with ex3.expander("Gráfico de distribución por class(Class)"):
			build_pie_graph(df_du, 'class')

		with ex4.expander("Class Distribution"):
			summary_groups(df_du, 'class')

	with st.expander("Frequency Dist Plot og Age"):
			fig = px.bar(df_fd, x='Age', y='count' , color = "count" , range_color= [0 , 180] , color_continuous_scale=[(0.00, "green"),(0.5, "yellow"),(1, "red")])
			fig.update_layout(title='Conteo de frecuencia de por edad' , width=600 )
			st.plotly_chart(fig)	

	with st.expander("Outlier Detection Plot"):
			#Set color for each gender
			fig = px.box(df_du, x='Gender', y='Age', color='Gender', points='outliers' , color_discrete_map={'Female': 'rgb(131, 29, 180)', 'Male': 'rgb(20, 180, 15)'})
			fig.update_layout(title='Age Distribution by Gender',xaxis_title='Gender',yaxis_title='Age')
			st.plotly_chart(fig)			

	with st.expander("Correlation Plot"):
			#Correlation matrix
			cm = df_cl.corr()

			# Generate correlation heatmap
			fig = px.imshow(cm.values,
							labels=dict(color="Correlation"),
							x=list(cm.columns),
							y=list(cm.columns),
							color_continuous_scale='YlOrRd')

			fig.update_xaxes(side="top")  # Show x-axis labels on top
			fig.update_layout(width=600, height=600, title="Correlation Heatmap")
			st.plotly_chart(fig)	




# Fin de la FUNCION






# Los gráficos con la librería plotly son más vistosos e incorporan más funcionalidades. Intenta hacer los gráficos de la sección “EDA \ Gráfico” con plotly.
# Sugerencias:
# • Los gráficos de barras de “Gender” y “Class” sustitúyelos por gráficos de tarta.
# • Los demás sustitúyelos por su equivalente en plotly o cualquier otro que
# consideres adecuado.
# • Puedes usar plotly express.
# • Utiliza las diapositivas de la sesión para ver ejemplos de uso. Para información
# más detallada, utiliza la documentación oficial de plotly para python
