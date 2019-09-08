"""
Name: app_callback.py
Description:
Created by: Masato Shima
Created on: 2019/09/09
"""

# **************************************************
# ----- Import Library
# **************************************************
import dash
import dash_core_components as dcc
import dash_html_components as dhc
import plotly.graph_objs as go
import pandas as pd

import logging
import traceback
from typing import *


# **************************************************
# ----- Variables
# **************************************************
STATUS_SUCCESS = "SUCCESS"
STATUS_FAILED = "FAILED"


# **************************************************
# ----- Set logger
# **************************************************
logger = logging.getLogger()
logger.setLevel(logging.INFO)


# **************************************************
# ----- Function Main
# **************************************************
def main() -> Dict[str, str]:
	logger.info("Start -- Main Function")

	status = STATUS_FAILED

	try:
		# Data Load
		data_ken_gdp = pd.read_csv(
			"./data/longform.csv",
			sep=",",
			header=0,
			index_col=0,
			encoding="utf-8"
		)

		data_ken_gdp_hokkaido = data_ken_gdp.query("area == '北海道'")

		# Create graph
		external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

		colors = {
			"background": "darkred",
			"text": "white"
		}

		app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

		app.layout = dhc.Div(
			style={
				"backgroundColor": colors["background"]
			},
			children=[
				dhc.H1(
					"北海道の GDP, 人口, 一人あたり GDP の推移",
					style={
						"textAlign": "center",
						"color": colors["text"]
					}
				),
				dhc.Div(
					"This is Sample",
					style={
						"textAlign": "center",
						"color": colors["text"]
					}
				),
				dcc.Dropdown(
					id="dropdown-for-hokkaido",
					options=[{"label": i, "value": 1} for i in data_ken_gdp_hokkaido["item"].unique()],
					value="GDP"
				),
				dcc.Graph(
					id="hokkaidoGraph",
					figure={
						"layout": {
							"title": "Sample graph",
							"font": {
								"color": colors["text"]
							},
							"paper_bgcolor": colors["background"],
							"plot_bgcolor": colors["text"]
						}
					}
				)
			]
		)

		@app.callback(
			dash.dependencies.Output("hokkaidoGraph", "figure"),
			[dash.dependencies.Input("dropdown-for-hokkaido", "value")]
		)
		def update_graph(factor):
			dff = data_ken_gdp_hokkaido.query(f"item == '{factor}'")

			return {
				"data": [
					go.Scatter(
						x=dff["year"],
						y=dff["value"]
					)
				]
			}

		app.run_server(debug=True)

		status = STATUS_SUCCESS

	except Exception as error_info:
		status = STATUS_FAILED

		logger.error(
			f"Failed... "
			f"\n{error_info}"
			f"\n{traceback.format_exc()}"
		)

	finally:
		logger.info("End -- Main Function")

		return {"status": status}


# **************************************************
# ----- Process Main
# **************************************************
if __name__ == '__main__':
	main()


# **************************************************
# ----- End
# **************************************************
