# Shiny
from shiny import ui

# Utils
import markdown

# Module
import components.icons as icons


def home():
    return (
        (
            ui.navset_pill_list(
                ui.nav_panel(
                    " 1. Stereo Data",
                    ui.layout_sidebar(
                        ui.sidebar(
                            ui.input_slider(
                                "n",
                                "input_slider()",
                                min=10,
                                max=100,
                                value=50,
                                step=5,
                                animate=True,
                            ),
                        ),
                        ui.tags.b(
                            icons.github(),
                            "1. GEF (Gene Expression Format) Information",
                        ),
                        ui.card(
                            ui.output_table("gef_info"),
                            max_height="150px",
                        ),
                        ui.tags.b(
                            icons.github(),
                            "2. SED (Stereo Expression Data) Information",
                        ),
                        ui.card(
                            ui.row(
                                ui.column(
                                    3,
                                    "Cells x Genes Number:",
                                ),
                                ui.column(
                                    9,
                                    ui.output_text_verbatim("sed_cells_genes"),
                                ),
                            ),
                            ui.row(
                                ui.column(
                                    1,
                                    "Bin Type:",
                                ),
                                ui.column(
                                    5,
                                    ui.output_text_verbatim("sed_bin_type"),
                                ),
                                ui.column(
                                    1,
                                    "Bin Size:",
                                ),
                                ui.column(
                                    5,
                                    ui.output_text_verbatim("sed_bin_size"),
                                ),
                            ),
                            ui.row(
                                ui.column(
                                    1,
                                    "Cell Attributes:",
                                ),
                                ui.column(
                                    5,
                                    ui.output_text_verbatim("sed_cell_attrs"),
                                ),
                                ui.column(
                                    1,
                                    "Cell Names:",
                                ),
                                ui.column(
                                    5,
                                    ui.output_text_verbatim("sed_cell_names"),
                                ),
                            ),
                            ui.row(
                                ui.column(
                                    1,
                                    "Gene Attributes:",
                                ),
                                ui.column(
                                    5,
                                    ui.output_text_verbatim("sed_gene_attrs"),
                                ),
                                ui.column(
                                    1,
                                    "Gene Names:",
                                ),
                                ui.column(
                                    5,
                                    ui.output_text_verbatim("sed_gene_names"),
                                ),
                            ),
                        ),
                    ),
                    value=None,
                    icon=icons.app(),
                ),
                ui.nav_panel(
                    " 2. Quality Control",
                    "Panel B content",
                    value=None,
                    icon=icons.app(),
                ),
                ui.nav_panel(
                    " 3. Filter Cells | Genes",
                    "Panel C content",
                    value=None,
                    icon=icons.app(),
                ),
                ui.nav_panel(
                    " 4. Normalization",
                    "Panel C content",
                    value=None,
                    icon=icons.app(),
                ),
                ui.nav_panel(
                    " 5. Highly Variable Genes",
                    "Panel C content",
                    value=None,
                    icon=icons.app(),
                ),
                # ui.nav_menu(
                #     "Other links",
                #     ui.nav_panel("D", "Panel D content"),
                #     "----",
                #     "Description:",
                #     ui.nav_control(
                #         ui.a("Shiny", href="https://shiny.posit.co", target="_blank")
                #     ),
                # ),
                id="tab",
            ),
        ),
    )
