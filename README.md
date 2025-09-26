# EGM703 - Week 2 Practical: Hyperspectral image analysis

## Overview
In the lectures and reading this week, you've learned about hyperspectral remote sensing and a number of different 
methods for analyzing hyperspectral data. In this practical, we'll gain some experience working with hyperspectral 
data, using a few examples written in python.

## Objectives

- Open and view data using xarray
- Perform atmospheric correction using dark object subtraction
- Use spectral angle matching to compare spectral signatures and identify surfaces
- Gain some familiarity with [Spectral Python](https://www.spectralpython.net/) (SPy), a python package for analyzing 
  hyperspectral images.

## Data provided
In the `data` folder, you should have the following files:

- combine_spectral_library.py - a python script that can be used to add additional spectra to **spectral_library.csv**
- EO1H0380352003173110PF_MTL_L1T.TXT - the L1T ("level-1 terrain corrected") metadata file for the EO-1 image
- solar_spectra.csv - a csv file containing values of extraterrestrial (top of atmosphere) radiance as a function of wavelength
- spectral_library.csv - a csv file containing example reflectance spectra for different surface types

You'll need to download the hyperspectral data from Blackboard, or from the Google Drive link [here](https://drive.google.com/file/d/18EHJpSbkbARJ2Rt6NndBSPe9SlcYr_iO/view?usp=sharing) - 
be sure to save it to the `data` folder so that it can be opened using the code in the notebook.

## Getting started

Once you clone the repository, you can set up the conda environment using the provided `environment.yml` file.

To get started working through the practical, launch jupyter lab and open the notebook
(`Hyperspectral Image Analysis.ipynb`).
