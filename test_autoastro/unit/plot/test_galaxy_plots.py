import autoarray as aa
import autoastro.plot as aplt
import autoastro as aast
import os

import pytest
from os import path

directory = path.dirname(path.realpath(__file__))


@pytest.fixture(name="galaxy_plotter_path")
def make_galaxy_plotter_setup():
    return "{}/../../../test_files/plotting/model_galaxy/".format(
        os.path.dirname(os.path.realpath(__file__))
    )


@pytest.fixture(autouse=True)
def set_config_path():
    aa.conf.instance = aa.conf.Config(
        path.join(directory, "../test_files/plot"), path.join(directory, "output")
    )


def test__individual_images_are_output(
    gal_x1_lp_x1_mp,
    sub_grid_7x7,
    mask_7x7,
    positions_7x7,
    include_all,
    galaxy_plotter_path,
    plot_patch,
):

    aplt.galaxy.profile_image(
        galaxy=gal_x1_lp_x1_mp,
        grid=sub_grid_7x7,
        positions=positions_7x7,
        include=include_all,
        plotter=aplt.Plotter(output=aplt.Output(galaxy_plotter_path, format="png")),
    )

    assert galaxy_plotter_path + "profile_image.png" in plot_patch.paths

    aplt.galaxy.convergence(
        galaxy=gal_x1_lp_x1_mp,
        grid=sub_grid_7x7,
        positions=positions_7x7,
        include=include_all,
        plotter=aplt.Plotter(output=aplt.Output(galaxy_plotter_path, format="png")),
    )

    assert galaxy_plotter_path + "convergence.png" in plot_patch.paths

    aplt.galaxy.potential(
        galaxy=gal_x1_lp_x1_mp,
        grid=sub_grid_7x7,
        positions=positions_7x7,
        include=include_all,
        plotter=aplt.Plotter(output=aplt.Output(galaxy_plotter_path, format="png")),
    )

    assert galaxy_plotter_path + "potential.png" in plot_patch.paths

    aplt.galaxy.deflections_y(
        galaxy=gal_x1_lp_x1_mp,
        grid=sub_grid_7x7,
        positions=positions_7x7,
        include=include_all,
        plotter=aplt.Plotter(output=aplt.Output(galaxy_plotter_path, format="png")),
    )

    assert galaxy_plotter_path + "deflections_y.png" in plot_patch.paths

    aplt.galaxy.deflections_x(
        galaxy=gal_x1_lp_x1_mp,
        grid=sub_grid_7x7,
        positions=positions_7x7,
        include=include_all,
        plotter=aplt.Plotter(output=aplt.Output(galaxy_plotter_path, format="png")),
    )

    assert galaxy_plotter_path + "deflections_x.png" in plot_patch.paths

    aplt.galaxy.magnification(
        galaxy=gal_x1_lp_x1_mp,
        grid=sub_grid_7x7,
        positions=positions_7x7,
        include=include_all,
        plotter=aplt.Plotter(output=aplt.Output(galaxy_plotter_path, format="png")),
    )

    assert galaxy_plotter_path + "magnification.png" in plot_patch.paths

    gal_x1_lp_x1_mp.hyper_galaxy = aast.HyperGalaxy()
    gal_x1_lp_x1_mp.hyper_model_image = aa.array.ones(shape_2d=(7, 7), pixel_scales=0.1)
    gal_x1_lp_x1_mp.hyper_galaxy_image = aa.array.ones(
        shape_2d=(7, 7), pixel_scales=0.1
    )

    aplt.galaxy.contribution_map(
        galaxy=gal_x1_lp_x1_mp,
        mask=mask_7x7,
        positions=positions_7x7,
        include=include_all,
        plotter=aplt.Plotter(output=aplt.Output(galaxy_plotter_path, format="png")),
    )

    assert galaxy_plotter_path + "contribution_map.png" in plot_patch.paths


def test__individual_galaxy_quantities__all_are_output(
    gal_x1_lp_x1_mp,
    sub_grid_7x7,
    positions_7x7,
    include_all,
    galaxy_plotter_path,
    plot_patch,
):
    aplt.galaxy.profile_image_subplot(
        galaxy=gal_x1_lp_x1_mp,
        grid=sub_grid_7x7,
        positions=positions_7x7,
        include=include_all,
        sub_plotter=aplt.SubPlotter(
            output=aplt.Output(galaxy_plotter_path, format="png")
        ),
    )

    assert galaxy_plotter_path + "profile_image_subplot.png" in plot_patch.paths

    aplt.galaxy.convergence_subplot(
        galaxy=gal_x1_lp_x1_mp,
        grid=sub_grid_7x7,
        positions=positions_7x7,
        include=include_all,
        sub_plotter=aplt.SubPlotter(
            output=aplt.Output(galaxy_plotter_path, format="png")
        ),
    )

    assert galaxy_plotter_path + "convergence_subplot.png" in plot_patch.paths

    aplt.galaxy.potential_subplot(
        galaxy=gal_x1_lp_x1_mp,
        grid=sub_grid_7x7,
        positions=positions_7x7,
        include=include_all,
        sub_plotter=aplt.SubPlotter(
            output=aplt.Output(galaxy_plotter_path, format="png")
        ),
    )

    assert galaxy_plotter_path + "potential_subplot.png" in plot_patch.paths

    aplt.galaxy.deflections_y_subplot(
        galaxy=gal_x1_lp_x1_mp,
        grid=sub_grid_7x7,
        positions=positions_7x7,
        include=include_all,
        sub_plotter=aplt.SubPlotter(
            output=aplt.Output(galaxy_plotter_path, format="png")
        ),
    )

    assert galaxy_plotter_path + "deflections_y_subplot.png" in plot_patch.paths

    aplt.galaxy.deflections_x_subplot(
        galaxy=gal_x1_lp_x1_mp,
        grid=sub_grid_7x7,
        positions=positions_7x7,
        include=include_all,
        sub_plotter=aplt.SubPlotter(
            output=aplt.Output(galaxy_plotter_path, format="png")
        ),
    )

    assert galaxy_plotter_path + "deflections_x_subplot.png" in plot_patch.paths
