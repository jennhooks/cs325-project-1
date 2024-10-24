# Project 2

## Description

This program reads an input file containing several urls that link to different
editions of a textbook and scrapes all of the reviews for each version. 
These reviews are then saved into output files that are named based on
which version the reviews are for.

## Requirements

[Conda](https://github.com/conda/conda)

## Installation

Clone the repository and setup the Python environment using Conda.

`git clone https://github.com/jennhooks/cs325-project-1.git`

`git checkout webScraping`

`conda env create -f requirements.yaml`

`conda activate cs325-project-2`

## Usage

After setting up the environment, run:

`python scraper.py`

After completion, each output file will hold all of the reviews associated 
with that specific version of the product.
