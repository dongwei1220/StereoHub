# Shiny
from shiny import App, Inputs, Outputs, Session, render, ui, run_app
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
import os
import tempfile
from pathlib import Path
from faicons import icon_svg
import warnings

# Module
from components.footer import footer
import components.icons as icons
from apps.home import home
from apps.about import about
from apps.readme import readme
from apps.stereo_seq import stereo_seq
from apps.image_studio import image_studio
from apps.saw_docs import saw_docs
from apps.stereo_map import stereo_map
from apps.stereopy import stereopy
from apps.spatial_slice import spatial_slice
from apps.spatio_temporal import spatio_temporal

# Setting
warnings.filterwarnings("ignore")

app_ui = ui.page_fluid(
    ui.include_css(
        path=Path(__file__).parent.resolve() / "styles.css", method="link_files"
    ),
    ui.navset_bar(
        ui.nav_control(
            ui.a(
                "StereoHub ",
                ui.img(
                    src="./logo.png",
                    height="36px",
                    width="36px",
                ),
                href="https://stereohub.github.io",
                target="_blank",
                class_="name",
            )
        ),
        ui.nav_panel(
            " Home",
            home(),
            value="nav_home",
            icon=icons.home(),
        ),
        ui.nav_panel(
            " Spatial Slice",
            spatial_slice(),
            value="nav_spatial",
            icon=icons.brain(),
        ),
        ui.nav_panel(
            " Spatio-Temporal Slices",
            spatio_temporal(),
            value="nav_temporal",
            icon=icons.time(),
        ),
        ui.nav_panel(
            " About",
            about(),
            value="nav_about",
            icon=icons.build(),
        ),
        ui.nav_menu(
            " Documents",
            ui.nav_panel(
                " Documents",
                readme(),
                value="nav_docs",
                icon=icons.book(),
            ),
            "---",
            "Stereo Docs:",
            ui.nav_panel(
                " Stereo-Seq",
                stereo_seq(),
                value="nav_seq",
                icon=icons.dna(),
            ),
            ui.nav_panel(
                " ImageStudio",
                image_studio(),
                value="nav_image_studio",
                icon=icons.microsoft(),
            ),
            ui.nav_panel(
                " SAW Docs",
                saw_docs(),
                value="nav_saw",
                icon=icons.terminal(),
            ),
            ui.nav_panel(
                " StereoMap",
                stereo_map(),
                value="nav_stereo_map",
                icon=icons.microsoft(),
            ),
            ui.nav_panel(
                " Stereopy",
                stereopy(),
                value="nav_stereopy",
                icon=icons.python(),
            ),
            icon=icons.book(),
        ),
        ui.nav_menu(
            "Our Works:",
            ui.nav_control(
                ui.a(
                    icons.cloud(),
                    " Hiplot Pro",
                    href="https://hiplot.com.cn",
                    target="_blank",
                )
            ),
            ui.nav_control(
                ui.a(
                    icons.microsoft(),
                    " OmicsSuite",
                    href="https://omicssuite.github.io/#/",
                    target="_blank",
                )
            ),
            ui.nav_control(
                ui.a(
                    icons.r_project(),
                    " TOmicsVis",
                    href="https://benben-miao.github.io/TOmicsVis/",
                    target="_blank",
                )
            ),
            icon=icons.analysis(),
        ),
        ui.nav_control(
            ui.a(
                icons.github(),
                " GitHub",
                href="https://github.com/StereoHub/",
                target="_blank",
            )
        ),
        ui.nav_spacer(),
        title="",
        id="navset",
        selected="nav_home",
        sidebar=None,
        fillable=True,
        gap=None,
        padding="70px 0px 0px 0px",
        position="fixed-top",
        header=None,
        footer=footer(),
        bg="#008888ee",
        inverse=True,
        underline=True,
        collapsible=True,
        fluid=True,
    ),
)


def server(input: Inputs, output: Outputs, session: Session):
    @render.table()
    def gef_info():
        gef_info_dict = st.io.read_gef_info(input.gef_path())
        gef_info_df = pd.DataFrame(gef_info_dict, index=[0])
        return gef_info_df.style.set_table_attributes(
            'class="dataframe shiny-table table"'
        )

    def sed_info():
        sed = st.io.read_gef(
            file_path=input.gef_path(),
            bin_type=input.bin_type(),  # "bins" or "cell_bins"
            bin_size=input.bin_size(),
            is_sparse=True,
            gene_list=None,
            region=None,
            gene_name_index=None,
            num_threads=input.num_threads(),
        )
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
    
    temp_dir = tempfile.gettempdir()
    stereo_temp = os.path.join(temp_dir, "stereohub")
    os.makedirs(stereo_temp, exist_ok=True)

    @render.image
    def qc_violin():
        sed = sed_info()
        sed.tl.cal_qc()
        sed.plt.violin()
        pc = st.plots.PlotCollection(sed)
        pc.violin(
            out_path=os.path.join(stereo_temp, "qc_violin.png"),
            out_dpi=input.image_dpi(),
            show_stripplot=False,
            jitter=0.20,
            dot_size=input.violin_dot_size(),
            log=False,
            rotation_angle=input.violin_x_angle(),
            group_by=None,
            multi_panel=input.violin_multi_panel(),
            scale="width",  # "area", "count", "width"
            ax=None,
            order=None,
            use_raw=False,
            palette=input.palette(),  # Discrete: "tab10", "hls", "husl", "Set2", "Paired", Rainbow: "rocket", "mako", "flare", "crest", "magma", "viridis", "cubehelix", "Blues", "YlOrBr", "vlag", "icefire", "Spectral", "coolwarm"
            title=None,
        )
        pc.violin(
            out_path=os.path.join(stereo_temp, "qc_violin.pdf"),
            out_dpi=input.image_dpi(),
            show_stripplot=False,
            jitter=0.20,
            dot_size=input.violin_dot_size(),
            log=False,
            rotation_angle=input.violin_x_angle(),
            group_by=None,
            multi_panel=input.violin_multi_panel(),
            scale="width",  # "area", "count", "width"
            ax=None,
            order=None,
            use_raw=False,
            palette=input.palette(),  # Discrete: "tab10", "hls", "husl", "Set2", "Paired", Rainbow: "rocket", "mako", "flare", "crest", "magma", "viridis", "cubehelix", "Blues", "YlOrBr", "vlag", "icefire", "Spectral", "coolwarm"
            title=None,
        )
        img: ImgData = {"src": os.path.join(stereo_temp, "qc_violin.png"), "width": "100%"}
        return img

    @render.download()
    def qc_violin_dl_pdf():
        path = os.path.join(stereo_temp, "qc_violin.pdf")
        return path

    @render.download()
    def qc_violin_dl_png():
        path = os.path.join(stereo_temp, "qc_violin.png")
        return path

    @render.ui()
    def version_update():
        markdown_path = "./assets/markdown/version_update.md"
        with open(markdown_path, "r", encoding="utf-8") as file:
            content = file.read()
        ui_markdown = ui.markdown(content)
        return ui_markdown

    @render.ui()
    def readme():
        markdown_path = "./README.md"
        with open(markdown_path, "r", encoding="utf-8") as file:
            content = file.read()
        ui_markdown = ui.markdown(content)
        return ui_markdown


app = App(
    app_ui,
    server,
    static_assets=Path(__file__).parent.resolve() / "assets",
    debug=False,
)

# if __name__ == "__main__":
#     run_app(
#         app="app",
#         host="0.0.0.0",
#         port=5000,
#         autoreload_port=0,
#         reload=True,
#         reload_dirs=None,
#         reload_includes="*.py,*.css,*.js,*.html,*.md",
#         reload_excludes="*.png,*.pdf",
#         ws_max_size=16777216,
#         log_level=None,
#         app_dir=".",
#         factory=False,
#         launch_browser=False,
#         dev_mode=False,
#     )
