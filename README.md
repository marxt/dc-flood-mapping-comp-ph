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

## Validation Software
Accuracy assessment metrics were performed using [ABCRaster]() software.