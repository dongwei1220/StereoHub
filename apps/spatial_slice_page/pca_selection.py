# Shiny
from shiny import ui

# Utils
import markdown

# Module
import components.icons as icons


def pca_selection():
    return (
        ui.layout_sidebar(
            ui.sidebar(
                ui.input_slider(
                    id="pca_ndims",
                    label=ui.tags.b("1. Num of PCs:"),
                    min=0,
                    max=100,
                    value=30,
                    step=10,
                    ticks=True,
                    animate=True,
                    width=None,
                    drag_range=True,
                ),
                ui.input_switch(
                    id="pca_use_highly_genes",
                    label=ui.tags.b("2. Use Highly Genes:"),
                    value=True,
                    width=None,
                ),
                ui.input_select(
                    id="pca_svd_solver",
                    label=ui.tags.b("3. SVD Solver:"),
                    choices={
                        "auto": "Auto",
                        "full": "Full",
                        "arpack": "Arpack", 
                        "randomized": "Randomized",  
                    },
                    selected="auto",
                    multiple=False,
                    selectize=None,
                    width=None,
                    size=None,
                ),
                ui.tags.hr(),
                ui.input_slider(
                    id="image_dpi5",
                    label=ui.tags.b("4. Image DPI:"),
                    min=96,
                    max=1000,
                    value=300,
                    step=10,
                    ticks=True,
                    animate=True,
                    width=None,
                    drag_range=True,
                ),
                ui.tags.b("5. Download PDF / PNG"),
                ui.download_button(
                    id="pca_elbow_dl_pdf",
                    label=" PCA Elbow Plot",
                    icon=icons.pdf(),
                    width=None,
                    class_="button_primary",
                ),
                ui.download_button(
                    id="pca_elbow_dl_png",
                    label=" PCA Elbow Plot",
                    icon=icons.png(),
                    width=None,
                    class_="button_primary",
                ),
                title=ui.tags.b(icons.setting(), " Parameters"),
            ),
            ui.tags.b(
                icons.vis(),
                " 1. Principal Component Analysis",
            ),
            ui.card(
                ui.output_image("pca_elbow"),
                full_screen=True,
                min_height="720px",
                max_height="720px",
            ),
        ),
    )
