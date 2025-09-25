import salem
import holoviews as hv

import geoviews as gv
import geoviews.tile_sources as gts

hv.extension("bokeh")


def plot_glacier_map(gdir):
    try:
        sh = salem.transform_geopandas(gdir.read_shapefile("outlines"))
        out = (
            gv.Polygons(sh).opts(fill_color=None, color_index=None)
            * gts.tile_sources["EsriImagery"]
            * gts.StamenLabels
        ).opts(
            width=800,
            height=500,
            active_tools=["pan", "wheel_zoom"],
            title=f"Glacier: {gdir.name}",
        )
    except:
        print("Nothing to do")
        # The rest of the notebook works without this dependency
    return out
