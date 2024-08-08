# Shiny
from shiny import ui

# Utils
import markdown

# Module
import components.icons as icons


def highly_variable_genes():
    return (
        ui.layout_sidebar(
            ui.sidebar(
                ui.input_slider(
                    id="hvg_min_mean",
                    label=ui.tags.b("1. Min Mean:"),
                    min=0,
                    max=1,
                    value=0.0125,
                    step=0.01,
                    ticks=True,
                    animate=True,
                    width=None,
                    drag_range=True,
                ),
                ui.input_slider(
                    id="hvg_max_mean",
                    label=ui.tags.b("2. Max Mean:"),
                    min=0,
                    max=10,
                    value=3,
                    step=1,
                    ticks=True,
                    animate=True,
                    width=None,
                    drag_range=True,
                ),
                ui.input_slider(
                    id="hvg_min_disp",
                    label=ui.tags.b("3. Min Disp:"),
                    min=0,
                    max=1,
                    value=0.5,
                    step=0.1,
                    ticks=True,
                    animate=True,
                    width=None,
                    drag_range=True,
                ),
                ui.input_slider(
                    id="hvg_n_top_genes",
                    label=ui.tags.b("4. TopN Genes:"),
                    min=0,
                    max=5000,
                    value=2000,
                    step=1000,
                    ticks=True,
                    animate=True,
                    width=None,
                    drag_range=True,
                ),
                ui.input_select(
                    id="hvg_method",
                    label=ui.tags.b("5. Method:"),
                    choices={
                        "seurat": "Seurat",
                        "cell_ranger": "Cell_Ranger",
                        "seurat_v3": "Seurat_V3", 
                    },
                    selected="seurat",
                    multiple=False,
                    selectize=None,
                    width=None,
                    size=None,
                ),
                ui.tags.hr(),
                ui.input_slider(
                    id="image_dpi4",
                    label=ui.tags.b("6. Image DPI:"),
                    min=96,
                    max=1000,
                    value=300,
                    step=10,
                    ticks=True,
                    animate=True,
                    width=None,
                    drag_range=True,
                ),
                ui.tags.b("7. Download PDF / PNG"),
                ui.download_button(
                    id="hvg_scatter_dl_pdf",
                    label=" HVG Scatter Plot",
                    icon=icons.pdf(),
                    width=None,
                    class_="button_primary",
                ),
                ui.download_button(
                    id="hvg_scatter_dl_png",
                    label=" HVG Scatter Plot",
                    icon=icons.png(),
                    width=None,
                    class_="button_primary",
                ),
                title=ui.tags.b(icons.setting(), " Parameters"),
            ),
            ui.tags.b(
                icons.vis(),
                " 1. Highly Variable Genes",
            ),
            ui.card(
                ui.output_image("hvg_scatter"),
                full_screen=True,
                min_height="720px",
                max_height="720px",
            ),
        ),
    )
