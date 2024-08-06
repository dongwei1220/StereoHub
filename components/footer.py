# Shiny
from shiny import ui

# Utils
from faicons import icon_svg

# Module
import components.icons as icons


def footer():
    return ui.row(
        ui.column(
            2,
            ui.img(
                src="https://avatars.githubusercontent.com/u/177035861?s=200&v=4",
                height="180px",
                width="180px",
            ),
        ),
        ui.column(
            5,
            ui.row(
                ui.a(
                    icons.copyright(),
                    " Copyright © StereoHub 2024",
                    href="https://github.com/StereoHub/",
                    target="_blank",
                    class_="footer_a",
                ),
            ),
            ui.row(
                ui.a(
                    icons.github(),
                    " GitHub: https://github.com/StereoHub/",
                    href="https://github.com/StereoHub/",
                    target="_blank",
                    class_="footer_a",
                ),
            ),
            ui.row(
                ui.a(
                    icons.email(),
                    " Email: benben.miao@outlook.com",
                    href="benben.miao@outlook.com",
                    target="_blank",
                    class_="footer_a",
                ),
            ),
            ui.hr(),
            ui.row(
                ui.card(
                    "StereoHub is dedicated to developing downstream open-source analysis and visualization software based on Stereo-Seq spatiotemics technology, and provides free cloud computing services.",
                    class_="footer_card",
                ),
            ),
        ),
        ui.column(
            5,
            ui.row(
                ui.a(
                    icons.dna(),
                    " STomics: https://stomics.tech",
                    href="https://stomics.tech",
                    target="_blank",
                    class_="footer_a",
                ),
            ),
            ui.row(
                ui.a(
                    icons.cloud(),
                    " STOmics Cloud: https://cloud.stomics.tech",
                    href="https://cloud.stomics.tech",
                    target="_blank",
                    class_="footer_a",
                ),
            ),
            ui.hr(),
            ui.row(
                ui.a(
                    icons.github(),
                    " OmicsSuite: https://github.com/OmicsSuite/",
                    href="https://github.com/OmicsSuite/",
                    target="_blank",
                    class_="footer_a",
                ),
            ),
            ui.row(
                ui.a(
                    icons.microsoft(),
                    " OmicsSuite: https://omicssuite.github.io",
                    href="https://omicssuite.github.io",
                    target="_blank",
                    class_="footer_a",
                ),
            ),
            ui.hr(),
            ui.row(
                ui.a(
                    icons.github(),
                    " TOmicsVis: https://github.com/benben-miao/TOmicsVis/",
                    href="https://github.com/benben-miao/TOmicsVis/",
                    target="_blank",
                    class_="footer_a",
                ),
            ),
            ui.row(
                ui.a(
                    icons.r_project(),
                    " TOmicsVis: https://benben-miao.github.io/TOmicsVis/",
                    href="https://benben-miao.github.io/TOmicsVis/",
                    target="_blank",
                    class_="footer_a",
                ),
            ),
        ),
        class_="footer",
    )
