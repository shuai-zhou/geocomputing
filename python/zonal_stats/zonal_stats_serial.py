from rasterstats import zonal_stats
import time
import geopandas as gpd
from fiona.crs import from_epsg

#input zones
zones_in = "/wrk/ekkylli/geocomputing/python/zonal_stats/zones.shp"
#output zonal stats
zones_out = "/wrk/ekkylli/geocomputing/python/zonal_stats/zonal_stats.shp"
#Raster you want to use to compute zonal stastics from.
vrt = "/wrk/project_ogiir-csc/mml/dem10m_vrt/etrs-tm35fin-n2000/whole_finland_direct.vrt"
#Which statistics to calculate
statistics = ['count', 'min' ,'mean', 'max','median']        
            
def main():
    #Calculate zonal statistics.
    z_stats = zonal_stats(zones_in,vrt, stats=statistics)	
    
    #Add the results to original shape file and save as new shape file
    results = gpd.read_file(zones_in)
    
    for index, row in results.iterrows():
        for stat in statistics:			
            results.loc[index, stat] = z_stats[index][stat]
            
    results.crs=from_epsg(3067)     
    results.to_file(zones_out) 
		
if __name__ == '__main__':
	t0 = time.time()
	main()	
	t1 = time.time()
	total = t1-t0
	print ("Everything done, took: ", str(total)+'s' )
