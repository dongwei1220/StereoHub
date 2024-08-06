# Shiny
from shiny import ui

# Utils
import markdown

# Module
import components.icons as icons
from .spatio_temporal_page.stereo_data import stereo_data
from .spatio_temporal_page.quality_control import quality_control
from .spatio_temporal_page.filter_cells_genes import filter_cells_genes
from .spatio_temporal_page.normalization import normalization
from .spatio_temporal_page.highly_variable_genes import highly_variable_genes
from .spatio_temporal_page.pca_selection import pca_selection
from .spatio_temporal_page.neighbor_graph import neighbor_graph
from .spatio_temporal_page.umap_visual import umap_visual
from .spatio_temporal_page.cluster_scatter import cluster_scatter
from .spatio_temporal_page.marker_genes import marker_genes
from .spatio_temporal_page.annotation import annotation
from .spatio_temporal_page.subset_samples import subset_samples
from .spatio_temporal_page.integrate_samples import integrate_samples


def spatio_temporal():
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
                    filter_cells_genes(),
                    value=None,
                    icon=icons.app(),
                ),
                ui.nav_panel(
                    " 4. Normalization",
                    normalization(),
                    value=None,
                    icon=icons.app(),
                ),
                ui.nav_panel(
                    " 5. Highly Variable Genes",
                    highly_variable_genes(),
                    value=None,
                    icon=icons.app(),
                ),
                ui.nav_panel(
                    " 6. PCA Selection",
                    pca_selection(),
                    value=None,
                    icon=icons.app(),
                ),
                ui.nav_panel(
                    " 7. Neighbor Graph",
                    neighbor_graph(),
                    value=None,
                    icon=icons.app(),
                ),
                ui.nav_panel(
                    " 8. UMAP Visual",
                    umap_visual(),
                    value=None,
                    icon=icons.app(),
                ),
                ui.nav_menu(
                    " 9. Cluster Scatter",
                    ui.nav_panel(
                        " 9.1 Leiden Cluster",
                        "Leiden Cluster",
                        value=None,
                        icon=icons.app(),
                    ),
                    ui.nav_panel(
                        " 9.2 Louvain Cluster",
                        "Louvain Cluster",
                        value=None,
                        icon=icons.app(),
                    ),
                    ui.nav_panel(
                        " 9.3 Phenograph",
                        "Phenograph",
                        value=None,
                        icon=icons.app(),
                    ),
                    icon=icons.app(),
                ),
                ui.nav_panel(
                    " 10. Marker Genes",
                    marker_genes(),
                    value=None,
                    icon=icons.app(),
                ),
                ui.nav_panel(
                    " 11. Annotation",
                    annotation(),
                    value=None,
                    icon=icons.app(),
                ),
                ui.nav_panel(
                    " 12. Subset Samples",
                    subset_samples(),
                    value=None,
                    icon=icons.app(),
                ),
                ui.nav_panel(
                    " 13. Integrate Samples",
                    integrate_samples(),
                    value=None,
                    icon=icons.app(),
                ),
                id="tab_spatio_temporal",
                selected=None,
                header=None,
                footer=None,
                well=True,
                widths=(2, 10),
            ),
        ),
    )
