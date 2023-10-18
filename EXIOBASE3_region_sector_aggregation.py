# coding: utf-8

# Install package and import module & input data
pip install country_converter

import numpy as np
import pymrio
import country_converter as coco

exio = pymrio.parse_exiobase3(path='/Users/.../EXIO_2015_pxp_3.8.2.zip')
exio.calc_all()


# # Sector aggregation
sec_agg_vec = np.array([1,	1,	1,	2,	3,	3,	3,	3,	4,	5,	5,	5,	5,	4,	5,	4,	4,	6,	7,	8,	8,	8,	8,	8,	8,	8,	8,	9,	9,	9,	9,	10,	10,	10,	10,	10,	10,	10,	10,	11,	11,	11,	12,	12,	12,	12,	14,	12,	14,	14,	14,	15,	13,	16,	17,	18,	19,	20,	52,	21,	52,	22,	23,	24,	24,	24,	25,	25,	25,	25,	25,	25,	25,	25,	25,	25,	25,	25,	25,	25,	25,	25,	25,	25,	27,	26,	52,	30,	30,	29,	29,	29,	29,	29,	29,	28,	31,	52,	32,	32,	33,	52,	34,	35,	52,	36,	52,	36,	52,	36,	52,	36,	52,	36,	52,	37,	38,	43,	39,	42,	40,	41,	44,	45,	46,	52,	52,	47,	47,	47,	47,	47,	47,	47,	47,	47,	47,	47,	47,	47,	47,	48,	48,	48,	48,	48,	48,	49,	50,	53,	52,	54,	54,	54,	71,	61,	55,	56,	56,	57,	57,	58,	59,	60,	62,	62,	62,	63,	65,	65,	64,	65,	66,	67,	68,	52,	52,	52,	52,	52,	52,	52,	52,	52,	51,	52,	52,	51,	51,	52,	52,	52,	52,	52,	52,	70,	69,	72,	72,	66])
exio_agg = exio.calc_all().aggregate(sector_agg=sec_agg_vec,inplace=False)

print("Sectors: {sec}".format(sec=exio_agg.get_sectors().tolist()))


# # Region aggregation (K, RoW)
reg_agg_coco = coco.agg_conc(original_countries=exio_agg.get_regions(),
                             aggregates={'KR': 'South Korea'},
                             missing_countries='RoW')
exio_agg.aggregate(region_agg=reg_agg_coco)

print("Sectors: {sec},\nRegions: {reg}".format(sec=exio_agg.get_sectors().tolist(),
                                               reg=exio_agg.get_regions().tolist()))


# # Save
save_folder_full = '/Users/.../exio_agg'
exio_agg.save_all(path=save_folder_full)
