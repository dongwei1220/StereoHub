# Shiny
from shiny import ui

# Utils
import markdown

# Module
import components.icons as icons


def readme():
    return ui.layout_columns(
        ui.card(
            ui.tags.hr(),
            ui.output_ui("readme"),
            full_screen=True,
            height=None,
            max_height=None,
            min_height=None,
            fill=True,
            class_=None,
            id="readme",
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
