"""
Name: app.py
Description: 
Created by: Masato Shima
Created on: 2019/09/07
"""

# **************************************************
# ----- Import Library
# **************************************************
import dash
import dash_core_components as dcc
import dash_html_components as dhc

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
					"Hello Dash !!!",
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
				dcc.Graph(
					id="first_graph",
					figure={
						"data": [
							{
								"x": [1, 2, 3, 4],
								"y": [3, 2, 4, 6],
								"type": "bar",
								"name": "Tokyo"
							},
							{
								"x": [1, 2, 3, 4],
								"y": [2, 4, 3, 2],
								"type": "bar",
								"name": "Osaka"
							},
							{
								"x": [1, 2, 3, 4],
								"y": [2, 1, 4, 6],
								"type": "bar",
								"name": "Kyoto"
							},
							{
								"x": [1, 2, 3, 4],
								"y": [1, 3, 4, 7],
								"type": "bar",
								"name": "Fukuoka"
							}
						],
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
