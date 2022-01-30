import pandas
import plotly.express

url = "http://api.open-notify.org/iss-now.json"
dataframe = pandas.read_json(url)

dataframe["latitude"] = dataframe.loc["latitude", "iss_position"]
dataframe["longitude"] = dataframe.loc["longitude", "iss_position"]
dataframe.reset_index(inplace=True)
dataframe.drop(["index", "message"], axis=1)

figure = plotly.express.scatter_geo(dataframe, lat="latitude", lon="longitude")

figure.show()