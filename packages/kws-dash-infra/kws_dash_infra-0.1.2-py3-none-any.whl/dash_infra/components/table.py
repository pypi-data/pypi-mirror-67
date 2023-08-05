import pandas as pd
from dash_infra.core import Component, as_callback
from dash_table import DataTable

from .store_user import StoreUser


class PandasTable(StoreUser):
    """
    A Figure component uses a Storage Component as a temporary
    output for all registered callback inputs.
    Each output is stored as a key in the state of the output
    and can be accessed as a dataset.
    """

    def __init__(self, id, key, **kwargs):
        super().__init__(
            id,
            display_component=DataTable,
            display_properties=["columns", "data"],
            keys=[key],
            **kwargs
        )

    def display(self, df):
        columns = [{"name": i, "id": i} for i in df.columns]
        data = df.to_dict("records")
        return columns, data
