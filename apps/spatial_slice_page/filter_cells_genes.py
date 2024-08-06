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
                title=ui.tags.b(icons.setting(), " Parameters"),
            ),
            ui.tags.b(
                icons.vis(),
                " 1. Filter Cells Genes",
            ),
            ui.card(
                full_screen=True,
                min_height="720px",
                max_height="720px",
            ),
        ),
    )
