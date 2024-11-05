# Dynamic Energy and Cost-Efficient Multi-UAV Routing Problem Using Enhanced Genetic Algorithm

This repository contains the code and research paper for the project *Dynamic Energy and Cost-Efficient Multi-UAV Routing Problem Using Enhanced Genetic Algorithm.* This study focuses on optimizing UAV routes by dynamically adjusting speeds and energy use based on payloads, utilizing an Enhanced Genetic Algorithm (EGA) to achieve efficient UAV delivery operations in complex routes.

## Table of Contents

- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Methodology](#methodology)
- [Results](#results)
- [Citation](#citation)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Introduction

This research addresses the need for energy-efficient UAV delivery operations by developing a capacitated multi-UAV routing model that optimizes both energy and cost. The study integrates an Enhanced Genetic Algorithm (EGA) with K-Means clustering for grouping delivery points and 2-Opt heuristic methods for route refinement. By dynamically adjusting UAV speeds based on payload weights, this model offers a scalable solution to minimize operational costs and energy consumption.

This work is published in *Journal of Optimization & Decision Making*.

## Project Structure

The repository includes the following files:

Dynamic_Energy_Efficient_Multi_UAV/ ├── docs/ │ └── Dynamic Energy and Cost Efficient Multi-UAV Routing Problem.pdf # Research paper ├── src/ │ └── main.py # Python code for optimization model ├── README.md # Project documentation └── LICENSE # License information


- **docs/**: Contains the published research paper.
- **src/**: Contains the Python script for running the optimization model.
- **README.md**: Provides an overview, installation instructions, and usage details.
- **LICENSE**: Specifies the licensing information for the project.

## Installation

To set up and run the code, install [Python](https://www.python.org/downloads/) and required packages. Follow these steps:

1. **Install Python**:
   - Download and install Python from [https://www.python.org/downloads/](https://www.python.org/downloads/).

2. **Install Required Python Packages**:
   - Open a terminal and install the necessary packages:
     ```bash
     pip install numpy pandas gurobipy sklearn
     ```
   - **Note**: Gurobi requires a license. Obtain and set up a Gurobi license from [https://www.gurobi.com/](https://www.gurobi.com/).

## Usage

1. **Clone the Repository**:
   - In a terminal, clone this repository and navigate to the `src` directory:
     ```bash
     git clone https://github.com/yourusername/Dynamic_Energy_Efficient_Multi_UAV.git
     cd Dynamic_Energy_Efficient_Multi_UAV/src
     ```

2. **Run the Python Code**:
   - Execute the script to run the multi-UAV routing optimization model:
     ```bash
     python main.py
     ```
   - The script will compute optimized routes for UAVs based on the defined parameters, focusing on energy efficiency.

## Methodology

The proposed model combines clustering, routing, and optimization techniques to improve UAV efficiency:
1. **K-Means Clustering**: Groups delivery points for UAV assignment, reducing the overall travel distance.
2. **Enhanced Genetic Algorithm (EGA)**: Explores potential routing solutions with adjustments in UAV speeds based on payload weight to optimize energy consumption.
3. **2-Opt Heuristic**: Fine-tunes each UAV route by swapping points to reduce travel time and energy consumption.

### Parameters
- **Payload Weight**: Adjusted dynamically to optimize speed and energy use.
- **UAV Speed and Energy Constraints**: Determines route efficiency and ensures UAVs do not exceed energy limits.

## Results

The model demonstrates substantial energy savings through speed adjustments relative to payload weight. For example, by beginning at a higher speed with heavier loads and gradually reducing speed as payloads are delivered, energy efficiency is improved by up to 30%.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

This research was conducted at Istanbul University by Alparslan Güzey and Mehmet Hakan Satman. Special thanks to all contributors who supported this project.



