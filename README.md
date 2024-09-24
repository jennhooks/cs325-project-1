# Project 1

## Description

This program takes several text prompts in a file named input.txt and passes them to the [Phi 3 Mini](https://ollama.com/library/phi3) AI model. The responses are saved in a text file named output.txt.

## Requirements

[Ollama](https://ollama.com)

[Conda](https://github.com/conda/conda)

## Installation

Clone the repository and setup the Python environment using Conda.

`git clone https://github.com/jennhooks/cs325-project-1.git`

`conda env create -f requirements.yaml`

`conda activate cs325-project-1`

## Usage

After setting up the environment, start the Ollama server (if it's not currently running) and run main.py.

`ollama serve`

`python main.py`

After completion, output.txt will hold the responses to the prompts placed in input.txt.
