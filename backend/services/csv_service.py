import pandas as pd

def export_csv(cards):

    df = pd.DataFrame(cards)

    filename = "crispdeck_output.csv"

    df.to_csv(filename, index=False)

    return filename