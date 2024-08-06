# Shiny
from shiny import ui

# Utils
import markdown

# Module
import components.icons as icons


def saw_docs():
    return ui.layout_columns(
        ui.card(
            ui.tags.iframe(src="/pdf/SAW.pdf", frameborder="0").add_style(
                "width: 100%; height: 800px;"
            ),
            full_screen=True,
            height=None,
            max_height=None,
            min_height=None,
            fill=True,
            class_=None,
            id=None,
        ),
        col_widths=(12),
        row_heights=None,
        fill=True,
        fillable=True,
        gap=None,
        class_=None,
        height=None,
        min_height=None,
        max_height=None,
    ).add_style("width: 60%; margin: auto; padding: 10px;")
