# Shiny
from shiny import ui

# Utils
import markdown

# Module
import components.icons as icons


def quality_control():
    return (
        ui.layout_sidebar(
            ui.sidebar(
                ui.input_slider(
                    id="image_dpi",
                    label=ui.tags.b("1. Image DPI:"),
                    min=96,
                    max=1000,
                    value=300,
                    step=10,
                    ticks=True,
                    animate=True,
                    width=None,
                    drag_range=True,
                ),
                ui.tags.b("2. Download PDF / PNG"),
                ui.download_button(
                    id="qc_violin_dl_pdf",
                    label=" QC Violin",
                    icon=icons.pdf(),
                    width=None,
                    class_="button_primary"
                ),
                ui.download_button(
                    id="qc_violin_dl_png",
                    label=" QC Violin",
                    icon=icons.png(),
                    width=None,
                    class_="button_primary"
                ),
                title=ui.tags.b(icons.setting(), " Parameters"),
            ),
            ui.tags.b(
                icons.table(),
                " 1. Quality Control Violin",
            ),
            ui.card(
                ui.tags.b("Notes:"),
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
                ui.output_image("qc_violin"),
                full_screen=True,
                min_height="890px",
                max_height="890px",
            ),
        ),
    )
