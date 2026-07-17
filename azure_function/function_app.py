import io
import logging

import azure.functions as func
import pandas as pd

from shared.clean_data import clean_data


app = func.FunctionApp()


@app.function_name(name="process_animal_data")
@app.blob_trigger(
    arg_name="input_blob",
    path="animal-data/raw/{name}",
    connection="AnimalDataStorage",
)
@app.blob_output(
    arg_name="output_blob",
    path="animal-data/processed/cleaned_{name}",
    connection="AnimalDataStorage",
)
def process_animal_data(
    input_blob: func.InputStream,
    output_blob: func.Out[bytes],
) -> None:
    logging.info(
        "Processing blob: %s, size: %s bytes",
        input_blob.name,
        input_blob.length,
    )

    file_bytes = input_blob.read()

    dataframe = pd.read_csv(
        io.BytesIO(file_bytes),
        sep=";",
    )

    cleaned_dataframe = clean_data(dataframe)

    output_bytes = cleaned_dataframe.to_csv(
        index=False,
    ).encode("utf-8")

    output_blob.set(output_bytes)

    logging.info(
        "Cleaned %s rows and wrote the processed CSV.",
        len(cleaned_dataframe),
    )