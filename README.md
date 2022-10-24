# Flood Mapping Comparison PH

This repository contains the results from the study: `An Intercomparison of Sentinel-1 based Change
Detection Algorithms for Flood Mapping`.

The comparisons focus on the change detection flood mapping methods using Sentinel-1 SAR data. 

## Methods
The research project aims to compare change detection methods that utilizes time-series parameters derived from 
Sentinel-1 datacube. Methods compared include:
* Normalized Scattering Difference Index (NSDI) 
* and its Shannon's Entropy (SNDSI)
* Standardized Residuals (SR)
* TU Wien flood mapping method based on Bayes inference (TUWB)

## Parameterization
The intercomparisons also shed light on method parameterizations specifically testing various:

### No flood reference
no flood reference scenes tests prior image, and datacube computed references.
* prior image (PRI)
* harmonic day of year estimate (HDOY)
* mean (MEAN)

### Thresholding
Thresholding 

* Fixed threhold values from literature (FIX)
* Otsu's (OTSU)
* KA Illingsworth (KI)

### HAND index filtering
Spatial filtering in aid of histogram thresholding can either be performed using the HAND filtering technique (HAND) or 
with no filtering (NONE).

### TUW Bayes Method Parameterization
* Bayes Inference prior probability
  - non-informed prior or equal 50-50 proir (EQ)
  - HAND based prior (HAND)

* PDF based exclusion of pixels with low probability of labelling accuracy could either be applied (PDFX) or not applied 
(NONE).

## File naming
The change detection flood maps are labelled as follows:

`<Method>_<NoFloodRef>_<Thresolding>_<HANDfiltering>.tif`

ex.: `NSDI_HDOY_OTSU_HAND.tif`, `SNSDI_PRI_KI_NONE.tif` 

TUW Flood maps are labelled as:

`<Method>_<NoFloodRef>_<Priors>_<PDFExclusion>.tif`

ex.: `TUWB_MEAN_HAND_PDFX.tif`

## Validation

### External Sentinel-1 Reference Flood Maps
Reference flood maps from operation flood mapping activation used in the study were retrieved from:
* Philippine Department of Science and Techonology (DOST) Advanced Science and Technology Institute 
([ASTI](https://asti.dost.gov.ph/)). Method is based on U-net framework document in this 
[paper](https://www.int-arch-photogramm-remote-sens-spatial-inf-sci.net/XLIII-B3-2020/1663/2020/).
* Sentinel Asia [access point here](https://sentinel-asia.org/EO/2020/article20201111PH.html). Flood map generated using
a change detection workflow with manually selected threshold (*from direct communication).
Both flood maps retrieved in shapefile format.

### Sentinel-2 Reference
Sentinel-2 flood map was generated using MDWI change detection method. Sentinel-2 data used were:
* S2A_MSIL2A_20201113T021941_N0214_R003_T51QUV_20201113T055836 (flood)
* S2B_MSIL2A_20200909T021609_N0214_R003_T51QUV_20200909T065335 (no flood)

### Software
Accuracy assessment metrics were performed using [ABCRaster](https://github.com/TUW-GEO/ABCRaster) software. ABCRaster 
can accept refrence flood maps in shapefile format, and features random sampling and accuracy metric computations.

## Miscellaneous information
Other relevant information:

### Grid and Projection
Analysis was done on E058N117T1 tile using [Equi7grid](https://github.com/TUW-GEO/Equi7Grid) tiling and projection 
system.

### Data and File format
Flood maps are encoded as uint8, where: 
* 1 - flood
* 0 - no flood 
* 255 - no data.

