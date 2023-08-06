"""{{ scaffold.name }} script"""
import pandas as pd
from datapane import api

# TODO - enter your code here...
df = pd.DataFrame.from_dict({"x": [4, 3, 2, 1], "y": [10.5, 20.5, 30.5, 40.5]})


def render():
    """Render and return your datapane report components"""
    return [
        # api.Markdown(f"Dummy Markdown block - {parameters.val}"),
        api.Markdown(f"Dummy Markdown block"),
        api.Asset.upload_df(df)
    ]
