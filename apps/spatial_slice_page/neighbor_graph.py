# Shiny
from shiny import ui

# Utils
import markdown

# Module
import components.icons as icons


def neighbor_graph():
    return (
        ui.layout_sidebar(
            ui.sidebar(
                ui.input_select(
                    id="neighbor_method",
                    label=ui.tags.b("1. Method:"),
                    choices={
                        "umap": "Umap",
                        "gauss": "Gauss",  
                    },
                    selected="umap",
                    multiple=False,
                    selectize=None,
                    width=None,
                    size=None,
                ),
                ui.input_select(
                    id="neighbor_metric",
                    label=ui.tags.b("2. Metric:"),
                    choices={
                        "euclidean": "Umap",
                        "manhattan": "Gauss",  
                        "correlation": "Correlation",
                        "hamming": "Hamming",
                        "cosine": "Cosine",
                        "jaccard": "Jaccard",
                    },
                    selected="euclidean",
                    multiple=False,
                    selectize=None,
                    width=None,
                    size=None,
                ), 
                ui.input_slider(
                    id="neighbor_num",
                    label=ui.tags.b("3. Num of neighbors:"),
                    min=0,
                    max=100,
                    value=10,
                    step=10,
                    ticks=True,
                    animate=True,
                    width=None,
                    drag_range=True,
                ),
                ui.input_switch(
                    id="neighbor_knn",
                    label=ui.tags.b("4. KNN:"),
                    value=True,
                    width=None,
                ),
                title=ui.tags.b(icons.setting(), " Parameters"),
            ),
            ui.tags.b(
                icons.vis(),
                " 1. Neighbor Graph",
            ),
            ui.card(
                full_screen=True,
                min_height="720px",
                max_height="720px",
            ),
        ),
    )
