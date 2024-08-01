# Shiny
from shiny import App, Inputs, Outputs, Session, render, ui

# Utils
from pathlib import Path
from faicons import icon_svg

# Data
import numpy as np

# Vis
import matplotlib.pyplot as plt
import seaborn as sns

# Module
from components.footer import footer
from apps.home import home

app_ui = ui.page_fluid(
    ui.include_css(path=Path(__file__).parent / "styles.css"),
    ui.navset_pill(
        ui.nav_control(
            ui.a(
                "StereoHub ",
                ui.img(
                    src="https://avatars.githubusercontent.com/u/177035861?s=200&v=4",
                    height="36px",
                    width="36px",
                ),
                href="https://stereohub.github.io",
                target="_blank",
                class_="name",
            )
        ),
        # ui.nav_spacer(),
        ui.nav_panel(
            " Home",
            home(),
            footer(),
            value="nav_home",
            icon=icon_svg("house"),
        ),
        ui.nav_panel(
            " Analysis",
            "Analysis Content",
            footer(),
            value="nav_ana",
            icon=icon_svg("layer-group"),
        ),
        ui.nav_panel(
            " Visualization",
            "Visualization Content",
            footer(),
            value="nav_vis",
            icon=icon_svg("paint-roller"),
        ),
        ui.nav_control(
            ui.a(
                icon_svg("github"),
                " GitHub",
                href="https://github.com/StereoHub/",
                target="_blank",
                class_="name",
            )
        ),
        ui.nav_menu(
            " About",
            ui.nav_panel(
                " About", "About", footer(), value="nav_about", icon=icon_svg("star")
            ),
            ui.nav_panel(
                " Stereo-Seq",
                "Stereo-Seq",
                footer(),
                value="nav_seq",
                icon=icon_svg("rocket"),
            ),
            "---",
            "Software:",
            ui.nav_control(
                ui.a(
                    "OmicsSuite",
                    href="https://omicssuite.github.io/#/",
                    target="_blank",
                )
            ),
            ui.nav_control(
                ui.a(
                    "Shiny",
                    href="https://benben-miao.github.io/TOmicsVis/",
                    target="_blank",
                )
            ),
            icon=icon_svg("compass"),
        ),
        id="navset",
        selected="nav_home",
        header=None,
        footer=None,
    ),
)


def server(input: Inputs, output: Outputs, session: Session):
    @render.plot(alt="A histogram")
    def plot() -> object:
        np.random.seed(19680801)
        x = 100 + 15 * np.random.randn(437)

        fig, ax = plt.subplots()
        ax.hist(x, input.n(), density=True)
        return fig


app = App(app_ui, server)
