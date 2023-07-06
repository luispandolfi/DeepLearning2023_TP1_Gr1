import pandas as pd

class DataFrameHelper:

    @classmethod
    def append_row(cls, df, new_row, id):
        if id == None:
            new_row["id"] = df.id.max() + 1
        elif id in df.id.values:
            raise ValueError("Id no válido, ya se encuentra en el DataFrame")
        else:
            new_row["id"] = id
        
        return df.append(new_row, ignore_index = True)