# Shiny
from shiny import App, Inputs, Outputs, Session, render, ui
from shiny.types import ImgData
from shinywidgets import render_widget, render_bokeh
from IPython.display import display
from ipywidgets import IntSlider

# Data
import stereo as st
import numpy as np
import pandas as pd

# Vis
import matplotlib.pyplot as plt

# Utils
from pathlib import Path
from faicons import icon_svg
import warnings

# Module
from components.footer import footer
import components.icons as icons
from apps.spatial_slice import home

# Setting
warnings.filterwarnings("ignore")

app_ui = ui.page_fluid(
    ui.include_css(path=Path(__file__).parent / "styles.css", method="link_files"),
    # ui.include_css(
    #     path=Path(__file__).parent / "assets/css/iconfont.css", method="link_files"
    # ),
    ui.navset_pill(
        ui.nav_control(
            ui.a(
                "StereoHub ",
                ui.img(
                    src="/logo.png",
                    height="36px",
                    width="36px",
                ),
                href="https://stereohub.github.io",
                target="_blank",
                class_="name",
            )
        ),
        # ui.nav_spacer(),
        ui.nav_panel(
            " Home",
            "Home",
            footer(),
            value="nav_home",
            icon=icons.home(),
        ),
        ui.nav_panel(
            " Spatial Slice",
            home(),
            footer(),
            value="nav_spatial",
            icon=icons.brain(),
        ),
        ui.nav_panel(
            " Spatio-Temporal Slices",
            "Visualization Content",
            footer(),
            value="nav_temporal",
            icon=icons.time(),
        ),
        ui.nav_control(
            ui.a(
                icons.github(),
                " GitHub",
                href="https://github.com/StereoHub/",
                target="_blank",
                class_="name",
            )
        ),
        ui.nav_menu(
            " About",
            ui.nav_panel(
                " About",
                "About",
                footer(),
                value="nav_about",
                icon=icons.github(),
            ),
            ui.nav_panel(
                " Stereo-Seq",
                "Stereo-Seq",
                footer(),
                value="nav_seq",
                icon=icons.dna(),
            ),
            "---",
            "Software:",
            ui.nav_control(
                ui.a(
                    icons.github(),
                    "OmicsSuite",
                    href="https://omicssuite.github.io/#/",
                    target="_blank",
                )
            ),
            ui.nav_control(
                ui.a(
                    icons.github(),
                    "TOmicsVis",
                    href="https://benben-miao.github.io/TOmicsVis/",
                    target="_blank",
                )
            ),
            icon=icons.build(),
        ),
        id="navset",
        selected="nav_home",
        header=None,
        footer=None,
    ),
)


def server(input: Inputs, output: Outputs, session: Session):
    @render.table()
    def gef_info():
        data_path = str(Path(__file__).parent / "data/SS200000135TL_D1.cellbin.gef")
        gef_info_dict = st.io.read_gef_info(data_path)
        gef_info_df = pd.DataFrame(gef_info_dict, index=[0])
        return gef_info_df.style.set_table_attributes(
            'class="dataframe shiny-table table"'
        )

    def sed_info():
        # data_path = str(Path(__file__).parent / "data/SS200000135TL_D1.cellbin.gef")
        data_path = input.gef_path()
        sed = st.io.read_gef(file_path=data_path, bin_type="cell_bins")
        return sed

    @render.text()
    def sed_cells_genes():
        return sed_info().shape

    @render.text()
    def sed_bin_type():
        return sed_info().bin_type

    @render.text()
    def sed_bin_size():
        return sed_info().bin_size

    @render.text()
    def sed_cell_attrs():
        return sed_info().cells

    @render.text()
    def sed_cell_names():
        return sed_info().cell_names

    @render.text()
    def sed_gene_attrs():
        return sed_info().genes

    @render.text()
    def sed_gene_names():
        return sed_info().gene_names

    @render.image
    def qc_violin():
        sed = sed_info()
        sed.tl.cal_qc()
        sed.plt.violin()
        pc = st.plots.PlotCollection(sed)
        pc.violin(out_path="./temp/qc_violin.png", out_dpi=input.image_dpi())
        pc.violin(out_path="./temp/qc_violin.pdf", out_dpi=input.image_dpi())
        dir = Path(__file__).parent
        img: ImgData = {"src": str(dir / "temp/qc_violin.png"), "width": "80%"}
        return img

    @render.download()
    def qc_violin_dl_pdf():
        path = Path(__file__).parent / "temp/qc_violin.pdf"
        return str(path)

    @render.download()
    def qc_violin_dl_png():
        path = Path(__file__).parent / "temp/qc_violin.png"
        return str(path)


app = App(app_ui, server, static_assets=Path(__file__).parent / "assets", debug=False)
