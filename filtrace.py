import numpy as np
import gdal
import gdalnumeric
from osgeo.gdalnumeric import *


rastPath =r"D:\Tomas-PC\Škola\VŠB-TUO\4SEMESTER\Programovani1\cv_15_4_2020\data\teren"
dataset = gdal.Open(rastPath)
band = dataset.GetRasterBand(1)
# print(str(dataset.RasterCount))
hodnoty = band.ReadAsArray()
# print(hodnoty)
# print(hodnoty.shape)
vyska = band.ReadAsArray()
sloupce = dataset.RasterXSize
radky = dataset.RasterYSize
noveHodnoty = np.zeros((radky,sloupce))
for radek in range (1, radky-1):
    for sloupec in range (1, sloupce-1):
        stredBunka = vyska[radek][sloupec]
        lhBunka = vyska[radek-1][sloupec-1]
        hBunka = vyska[radek-1][sloupec]
        phBunka = vyska[radek-1][sloupec+1]
        pBunka = vyska[radek][sloupec+1]
        pdBunka = vyska[radek+1][sloupec+1]
        dBunka = vyska[radek+1][sloupec]
        ldBunka = vyska[radek+1][sloupec-1]
        lBunka = vyska[radek][sloupec-1]
        novaHodnota = (stredBunka + lhBunka + hBunka + phBunka + pBunka + pdBunka + dBunka + ldBunka + lBunka) / 9
        noveHodnoty[radek][sloupec] = novaHodnota
driver = gdal.GetDriverByName("GTiff")
dsOut = driver.Create(r"D:\Tomas-PC\Škola\VŠB-TUO\4SEMESTER\Programovani1\cv_15_4_2020\data\dmt2.tiff", sloupce, radky, 1, band.DataType)
gdalnumeric.CopyDatasetInfo(dataset,dsOut)
bandOut=dsOut.GetRasterBand(1)
BandWriteArray(bandOut, noveHodnoty)
bandOut.FlushCache()