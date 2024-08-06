# Shiny
from shiny import ui

# Utils
import markdown

# Module
import components.icons as icons


def home():
    return ui.layout_columns(
        ui.card(
            ui.h3("1. StereoHub:"),
            ui.card(
                ui.markdown(
                    """
                    **1.1 StereoHub Introduction:**

                    **StereoHub: An interactive cloud platform for downstream analytics at Stereo-Seq.** The `StereoHub` user interface is designed and developed based on the `Shiny v1.0.0` framework of `Python v3.8.10`, providing rich web components for data manipulation, function parameters, and result display, making data analytics parameters as completely intuitive as possible for scientists. The functions of `StereoHub` for Stereo-Seq spatiotemics data analytics are realized by important functional modules such as `stereopy v3.1.3`, `anndata v0.9.2`, `biopython v1.83.0`, `hdf5 v1.14.0`, `panel v0.14.4`, `bokeh v2.4.3`, `plotly v5.23.0`, etc. Thanks to these excellent open-source modules.

                    **1.2 StereoHub User Interface:**
                    """
                ),
                ui.img(
                    src="/image/StereoHub-UI.jpg",
                    width="100%",
                    class_="image-shadow"
                ),
                ui.markdown(
                    """
                    **1.3 StereoHub Resources:**

                    [***1. Github Team: https://github.com/StereoHub/***](https://github.com/StereoHub/)

                    [***2. Source Repository: https://github.com/StereoHub/StereoHub***](https://github.com/StereoHub/StereoHub)

                    [***3. Documents: https://stereohub.github.io***](https://stereohub.github.io)

                    [***4. Cloud Platform: https://hiplot.com.cn/stereohub***](https://hiplot.com.cn/stereohub)

                    **1.4 StereoHub Develop or Deploy:**

                    ```bash
                    # 1. Environment
                    git clone git@github.com:StereoHub/StereoHub.git
                    cd StereoHub

                    conda env create -f stereohub.yml
                    conda activate stereohub

                    # 2. Development
                    # 2.1 For Windows
                    .\start-win.bat

                    # 2.2 For Linux
                    bash start-linux.sh

                    # 2.3 All terminals
                    python -m shiny run \\
                    --host 127.0.0.1 \\
                    --port 5000 \\
                    --reload \\
                    --reload-includes "*.py,*.css,*.js,*.html" \\
                    --reload-excludes "*.png,*.pdf" \\
                    --log-level info \\
                    --app-dir "." \\
                    --launch-browser \\
                    --dev-mode \\
                    app.py
                    ```
                    """
                ),
                full_screen=True,
                height=None,
                max_height=None,
                min_height=None,
                fill=True,
                class_=None,
                id=None,
            ),
            ui.h3("2. Stereo-Seq:"),
            ui.card(
                ui.markdown(
                    """
                    **2.1 Stereo-Seq Resources:**

                    [***1. STomics Stereo-Seq: https://stomics.tech***](https://stomics.tech)

                    [***2. STomics Cloud: https://cloud.stomics.tech***](https://cloud.stomics.tech)

                    [***3. STOmics Database: https://db.cngb.org/stomics/***](https://db.cngb.org/stomics/)

                    [***4. ImageStudio, StereoMap: https://stomics.tech/products/BioinfoTools/OfflineSoftware***](https://stomics.tech/products/BioinfoTools/OfflineSoftware)

                    [***5. STomics Github: https://github.com/STOmics/***](https://github.com/STOmics/)

                    [***6. Stereopy: https://github.com/STOmics/Stereopy/***](https://github.com/STOmics/Stereopy/)

                    **2.2 Stereo-Seq Paper:**

                    > Ao Chen, Sha Liao, Mengnan Cheng, Longqi Liu, Xun Xu, Jian Wang. **Spatiotemporal transcriptomic atlas of mouse organogenesis using DNA nanoball-patterned arrays.** ***Cell***, 2022, doi: **https://doi.org/10.1016/j.cell.2022.04.003**

                    **Figure 1. Graphical Abstract:**
                    """
                ),
                ui.img(
                    src="/image/stereo-seq-paper-1.jpg",
                    width="100%",
                    class_="image-shadow"
                ),
                ui.markdown(
                    """
                    **Figure 2. Stereo-Seq Technology:**
                    """
                ),
                ui.img(
                    src="/image/stereo-seq-paper-2.jpg",
                    width="100%",
                    class_="image-shadow"
                ),
                ui.markdown(
                    """
                    **Figure 3. Stereo-Seq in Mouse Brain:**
                    """
                ),
                ui.img(
                    src="/image/stereo-seq-paper-3.jpg",
                    width="100%",
                    class_="image-shadow"
                ),
                full_screen=True,
                height=None,
                max_height=None,
                min_height=None,
                fill=True,
                class_=None,
                id=None,
            ),
            full_screen=True,
            height=None,
            max_height=None,
            min_height=None,
            fill=True,
            class_=None,
            id=None,
        ),
        ui.card(
            ui.tags.b(
                icons.update(),
                " Version Update:",
            ),
            ui.tags.hr(),
            ui.output_ui("version_update"),
            full_screen=True,
            height=None,
            max_height="840px",
            min_height=None,
            fill=True,
            class_=None,
            id="version_update",
        ),
        col_widths=(9, 3),
        row_heights=None,
        fill=True,
        fillable=True,
        gap=None,
        class_=None,
        height=None,
        min_height=None,
        max_height=None,
    ).add_style("width: 80%; margin: auto; padding: 10px;")
