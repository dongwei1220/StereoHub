# Shiny
from shiny import ui

# Utils
import markdown

# Module
import components.icons as icons


def filter_cells_genes():
    return (
        ui.layout_sidebar(
            ui.sidebar(
                ui.input_slider(
                    id="filter_min_counts",
                    label=ui.tags.b("1. Min Counts:"),
                    min=0,
                    max=10000,
                    value=200,
                    step=100,
                    ticks=True,
                    animate=True,
                    width=None,
                    drag_range=True,
                ),
                ui.input_slider(
                    id="filter_min_genes",
                    label=ui.tags.b("2. Min Genes:"),
                    min=0,
                    max=5000,
                    value=10,
                    step=10,
                    ticks=True,
                    animate=True,
                    width=None,
                    drag_range=True,
                ),
                ui.input_slider(
                    id="filter_max_genes",
                    label=ui.tags.b("3. Max Genes:"),
                    min=0,
                    max=5000,
                    value=3000,
                    step=10,
                    ticks=True,
                    animate=True,
                    width=None,
                    drag_range=True,
                ),
                ui.input_slider(
                    id="filter_pct_counts_mt",
                    label=ui.tags.b("4. Percent MT:"),
                    min=0,
                    max=100,
                    value=5,
                    step=10,
                    ticks=True,
                    animate=True,
                    width=None,
                    drag_range=True,
                ),
                ui.input_slider(
                    id="scatter_dot_size",
                    label=ui.tags.b("5. Dot Size:"),
                    min=0.00,
                    max=10.00,
                    value=0.80,
                    step=0.01,
                    ticks=True,
                    animate=True,
                    width=None,
                    drag_range=True,
                ),
                ui.tags.hr(),
                ui.input_slider(
                    id="image_dpi2",
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
                    id="qc_filter_scatter_dl_pdf",
                    label=" QC Scatter Plot",
                    icon=icons.pdf(),
                    width=None,
                    class_="button_primary",
                ),
                ui.download_button(
                    id="qc_filter_scatter_dl_png",
                    label=" QC Scatter Plot",
                    icon=icons.png(),
                    width=None,
                    class_="button_primary",
                ),
                title=ui.tags.b(icons.setting(), " Parameters"),
            ),
            ui.tags.b(
                icons.vis(),
                " 1. Filter Cells Genes",
            ),
            ui.card(
                ui.div(
                    ui.p(ui.tags.b("total_counts:"), " the total counts per cell;"),
                    ui.p(
                        ui.tags.b("n_genes_by_counts:"),
                        " the number of genes expressed in count matrix;",
                    ),
                    ui.p(
                        ui.tags.b("pct_counts_mt:"),
                        " the percentage of counts in mitochondrial genes.",
                    ),
                ).add_style(
                    "background-color: #eeeeee; padding: 20px;border-radius: 10px;"
                ),
                ui.output_image("qc_filter_scatter"),
                full_screen=True,
                min_height="720px",
                max_height="720px",
            ),
        ),
    )
