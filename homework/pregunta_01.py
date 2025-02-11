# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

def pregunta_01():
    if os.path.isdir("docs") == False:
        os.mkdir("docs")

    df = pd.read_csv(os.path.join("files","input", "shipping-data.csv"))

    df_warehouse = df.copy()

    plt.figure()
    counts = df_warehouse["Warehouse_block"].value_counts()
    counts.plot.bar(
        title = "Shipping per warehouse",
        xlabel = "Warehouse bloc",
        ylabel = "Record count",
        color=  "tab:blue",
        fontsize = 8
    )
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.savefig(os.path.join("docs", "shipping_per_warehouse.png"))

    df_mode = df.copy()

    plt.figure()

    counts = df_mode["Mode_of_Shipment"].value_counts()

    counts.plot.pie(
        title="Modeof shipment",
        wedgeprops=dict(width=0.35),
        ylabel="",
        colors=["tab:blue", "tab:orange", "tab:green"],
    )
    plt.savefig(os.path.join("docs", "mode_of_shipment.png"))


    df_rating = df.copy()

    plt.figure()

    df_rating = (
        df_rating[["Mode_of_Shipment", "Customer_rating"]]
        .groupby("Mode_of_Shipment")
        .describe()
    )

    df_rating.columns = df_rating.columns.droplevel()

    df_rating = df_rating[["mean","min","max"]]
    plt.barh(
        y=df_rating.index.values,
        width=df_rating["max"].values - 1,
        left=df_rating["min"].values,
        height=0.9,
        color="lightgray",
        alpha=0.8,
    )

    colors = [
    "tab:green" if value >= 3.0 else "tab:orange" for value in df_rating ["mean"]. values]

    plt.barh(
        y=df_rating.index.values,
        width=df_rating ["mean"].values - 1,
        left=df_rating ["min"].values,
        color=colors,
        height=0.5,
        alpha=1.0,
    )
    plt.title("Average Customer Rating")
    plt.gca().spines["left"].set_color("gray")
    plt.gca().spines["bottom"].set_color("gray")
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)

    plt.savefig(os.path.join("docs", "average_customer_rating.png"))

    df_weight = df.copy()
    plt.figure()
    df_weight.Weight_in_gms.plot.hist(
        title="Shipped Weight Distribution",
        color="tab:orange",
        edgecolor="white",
    )
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.savefig(os.path.join("docs", "weight_distribution.png"))
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """
