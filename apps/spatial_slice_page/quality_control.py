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
                    id="violin_dot_size",
                    label=ui.tags.b("1. Dot Size:"),
                    min=0.00,
                    max=10.00,
                    value=0.80,
                    step=0.01,
                    ticks=True,
                    animate=True,
                    width=None,
                    drag_range=True,
                ),
                ui.input_slider(
                    id="violin_x_angle",
                    label=ui.tags.b("2. X Label Angle:"),
                    min=0,
                    max=360,
                    value=0,
                    step=5,
                    ticks=True,
                    animate=True,
                    width=None,
                    drag_range=True,
                ),
                ui.input_switch(
                    id="violin_multi_panel",
                    label=ui.tags.b("3. Multi Panel:"),
                    value=True,
                    width=None,
                ),
                ui.input_select(
                    id="palette",
                    label=ui.tags.b("4. Color Palette:"),
                    choices={
                        "Discrete": {
                            "tab10": "Tab10",
                            "hls": "HLS",
                            "husl": "HUSL",
                            "Set2": "Set2",
                            "Paired": "Paired",
                        },
                        "Rainbow": {
                            "rocket": "Rocket",
                            "mako": "Mako",
                            "flare": "Flare",
                            "crest": "Crest",
                            "magma": "Magma",
                            "viridis": "Viridis",
                            "cubehelix": "CubeHelix",
                            "Blues": "Blues",
                            "YlOrBr": "YlOrBr",
                            "vlag": "Vlag",
                            "icefire": "IceFire",
                            "Spectral": "Spectral",
                            "coolwarm": "CoolWarm",
                        },
                    },
                    selected="tab10",
                    multiple=False,
                    selectize=None,
                    width=None,
                    size=None,
                ),
                ui.tags.hr(class_="division"),
                ui.input_slider(
                    id="image_dpi",
                    label=ui.tags.b("5. Image DPI:"),
                    min=96,
                    max=1000,
                    value=300,
                    step=10,
                    ticks=True,
                    animate=True,
                    width=None,
                    drag_range=True,
                ),
                ui.tags.b("6. Download PDF / PNG"),
                ui.download_button(
                    id="qc_violin_dl_pdf",
                    label=" QC Violin",
                    icon=icons.pdf(),
                    width=None,
                    class_="button_primary",
                ),
                ui.download_button(
                    id="qc_violin_dl_png",
                    label=" QC Violin",
                    icon=icons.png(),
                    width=None,
                    class_="button_primary",
                ),
                title=ui.tags.b(icons.setting(), " Parameters"),
            ),
            ui.tags.b(
                icons.vis(),
                " 1. Quality Control Violin",
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
                ui.output_image("qc_violin"),
                full_screen=True,
                min_height="720px",
                max_height="720px",
            ),
        ),
    )
