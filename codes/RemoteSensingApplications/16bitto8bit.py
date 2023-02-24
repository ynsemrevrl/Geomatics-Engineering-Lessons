import os
os.environ['PROJ_LIB'] = ''
os.environ['GDAL_DATA'] = ''

from osgeo import osr, gdal
import glob
import tifffile

paths = glob.glob("../*.TIF") # set path for files that will be transform
try:
    os.mkdir("/8bit")
except FileExistsError:
    pass

for i in paths:
    img = tifffile.imread(i)
    row = img.shape[0]
    column = img.shape[1]
    ds = gdal.Open(i)
    prj = ds.GetProjection()
    srs = osr.SpatialReference(wkt=prj)
    tfw = ds.GetGeoTransform()
    driver = gdal.GetDriverByName("GTiff")
    img = img / 2**16 * 2**8
    main, fn = os.path.split(i)
    save_path_dir = "8bit/8bit_{}".format(fn)
    outdata = driver.Create(save_path_dir, column, row, 1, gdal.GDT_Byte)
    outdata.SetGeoTransform(tfw)##sets same geotransform as input
    outdata.SetProjection(prj)##sets same projection as input
    outdata.GetRasterBand(1).WriteArray(img)
    band = outdata.GetRasterBand(1)
    datatype = gdal.GetDataTypeName(band.DataType)
    outdata.FlushCache() ##saves to disk!!
    outdata = None