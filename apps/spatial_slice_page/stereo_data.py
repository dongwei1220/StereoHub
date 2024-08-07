# Shiny
from shiny import ui

# Utils
import markdown

# Module
import components.icons as icons


def stereo_data():
    return (
        ui.layout_sidebar(
            ui.sidebar(
                ui.input_select(
                    id="format_select",
                    label=ui.tags.b("1. Stereo Formats:"),
                    choices={
                        "Stereo": {
                            "GEM": "Gene Expression Matrix",
                            "GEF": "Gene Expression Format",
                            "H5MS": "HDF5 MSData",
                        },
                        "Scanpy/Seurat": {
                            "H5AD": "HDF5 AnnData",
                            "Anndata": "AnnData",
                        },
                    },
                    selected="GEF",
                    multiple=False,
                    selectize=None,
                    width=None,
                    size=None,
                ),
                ui.input_text_area(
                    id="gef_path",
                    label=ui.tags.b("2. GEF Path:"),
                    value="./data/SS200000135TL_D1.cellbin.gef",
                    width=None,
                    height=None,
                    cols=None,
                    rows=5,
                    placeholder="Absolute path (recommended) or relative path.",
                    resize="vertical",
                    autoresize=False,
                    autocomplete=None,
                    spellcheck=False,
                ),
                ui.input_select(
                    id="bin_type",
                    label=ui.tags.b("3. Bin Type:"),
                    choices={
                        "bins": "Bins",
                        "cell_bins": "Cell Bins",
                    },
                    selected="cell_bins",
                    multiple=False,
                    selectize=None,
                    width=None,
                    size=None,
                ),
                ui.input_slider(
                    id="bin_size",
                    label=ui.tags.b("4. Bin Size:"),
                    min=1,
                    max=500,
                    value=100,
                    step=10,
                    ticks=True,
                    animate=True,
                    width=None,
                    drag_range=True,
                ),
                ui.input_slider(
                    id="num_threads",
                    label=ui.tags.b("5. Threads Number:"),
                    min=-1,
                    max=100,
                    value=-1,
                    step=1,
                    ticks=True,
                    animate=True,
                    width=None,
                    drag_range=True,
                ),
                title=ui.tags.b(icons.setting(), " Parameters"),
            ),
            ui.tags.b(
                icons.table(),
                " 1. GEF (Gene Expression Format) Information",
            ),
            ui.card(
                ui.output_table("gef_info"),
                full_screen=True,
                min_height="150px",
                max_height="150px",
            ),
            ui.tags.b(
                icons.table(),
                " 2. SED (Stereo Expression Data) Information",
            ),
            ui.card(
                ui.row(
                    ui.column(
                        3,
                        "Cells x Genes Number:",
                    ),
                    ui.column(
                        9,
                        ui.output_text_verbatim("sed_cells_genes", placeholder=True),
                    ),
                ),
                ui.row(
                    ui.column(
                        1,
                        "Bin Type:",
                    ),
                    ui.column(
                        5,
                        ui.output_text_verbatim("sed_bin_type", placeholder=True),
                    ),
                    ui.column(
                        1,
                        "Bin Size:",
                    ),
                    ui.column(
                        5,
                        ui.output_text_verbatim("sed_bin_size", placeholder=True),
                    ),
                ),
                ui.row(
                    ui.column(
                        1,
                        "Cell Attributes:",
                    ),
                    ui.column(
                        5,
                        ui.output_text_verbatim("sed_cell_attrs", placeholder=True),
                    ),
                    ui.column(
                        1,
                        "Cell Names:",
                    ),
                    ui.column(
                        5,
                        ui.output_text_verbatim("sed_cell_names", placeholder=True),
                    ),
                ),
                ui.row(
                    ui.column(
                        1,
                        "Gene Attributes:",
                    ),
                    ui.column(
                        5,
                        ui.output_text_verbatim("sed_gene_attrs", placeholder=True),
                    ),
                    ui.column(
                        1,
                        "Gene Names:",
                    ),
                    ui.column(
                        5,
                        ui.output_text_verbatim("sed_gene_names", placeholder=True),
                    ),
                ),
                full_screen=True,
                min_height="520px",
                max_height="520px",
            ),
        ),
    )
