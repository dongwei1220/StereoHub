# Shiny
from shiny import ui

# Utils
import markdown

# Module
import components.icons as icons


def normalization():
    return (
        ui.layout_sidebar(
            ui.sidebar(
                ui.input_slider(
                    id="nor_target_sum",
                    label=ui.tags.b("1. Target Sum:"),
                    min=0,
                    max=30000,
                    value=10000,
                    step=1000,
                    ticks=True,
                    animate=True,
                    width=None,
                    drag_range=True,
                ),
                title=ui.tags.b(icons.setting(), " Parameters"),
            ),
            ui.tags.b(
                icons.vis(),
                " 1. Normalization",
            ),
            ui.card(
                full_screen=True,
                min_height="720px",
                max_height="720px",
            ),
        ),
    )
