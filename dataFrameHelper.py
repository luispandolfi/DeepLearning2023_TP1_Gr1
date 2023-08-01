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
        
        new_row_df = pd.DataFrame(new_row, index=[0])
        return pd.concat([df, new_row_df], ignore_index=True)
