# Shiny
from shiny import ui

def home():
    return (
        ui.layout_sidebar(
            ui.sidebar(
                ui.input_slider("n", "N", min=0, max=100, value=20),
            ),
            ui.card(
                ui.output_plot("plot"),
            ),
            height="880px",
        ),
    )
