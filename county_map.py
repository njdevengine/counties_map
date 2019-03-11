#https://www.census.gov/geo/maps-data/data/cbf/cbf_counties.html

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

def draw_us_map():
    # Set the lower left and upper right limits of the bounding box:
    lllon = -119
    urlon = -64
    lllat = 22.0
    urlat = 50.5
    # and calculate a centerpoint, needed for the projection:
    centerlon = float(lllon + urlon) / 2.0
    centerlat = float(lllat + urlat) / 2.0

    m = Basemap(resolution='i',  # crude, low, intermediate, high, full
                llcrnrlon = lllon, urcrnrlon = urlon,
                lon_0 = centerlon,
                llcrnrlat = lllat, urcrnrlat = urlat,
                lat_0 = centerlat,
                projection='tmerc')

#     # Read state boundaries.
#     shp_info = m.readshapefile('st99_d00', 'states',
#                                drawbounds=True, color='lightgrey')

    # Read county boundaries
    shp_info = m.readshapefile('cb_2017_us_county_500k',
                               'counties',
                               drawbounds=True)

if __name__ == "__main__":
    draw_us_map()
    plt.title('US Counties')
    # Get rid of some of the extraneous whitespace matplotlib loves to use.
    plt.tight_layout(pad=0, w_pad=0, h_pad=0)
    plt.show()
