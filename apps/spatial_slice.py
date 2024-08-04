# Shiny
from shiny import ui

# Utils
import markdown

# Module
import components.icons as icons
from .spatial_slice_page.stereo_data import stereo_data
from .spatial_slice_page.quality_control import quality_control

def home():
    return (
        (
            ui.navset_pill_list(
                ui.nav_panel(
                    " 1. Stereo Data",
                    stereo_data(),
                    value=None,
                    icon=icons.app(),
                ),
                ui.nav_panel(
                    " 2. Quality Control",
                    quality_control(),
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
