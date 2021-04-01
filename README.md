<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Input Image             |Output depth map
:----------------------:|:-----------------------:
<img src="https://raw.githubusercontent.com/Gvanderl/Soft3DReconstruction/master/inputs/teddy1.png" width="500" />|<img src="https://raw.githubusercontent.com/Gvanderl/Soft3DReconstruction/master/outputs/teddy_Depth_map.png" width="350"/>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* For virtual envs: [Pipenv](https://pipenv-fork.readthedocs.io/en/latest/install.html)
  ```sh
  pip install --user pipenv
  ```
Or use your virtual environment manager of choice, requirements are in the [Pipfile](Pipfile)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/Gvanderl/StyleSegments.git
   ```
2. Install packages
   ```sh
   pipenv install
   ```
3. Run the script
    ```sh
    pipenv shell
    pipenv main.py
    ```


<!-- USAGE EXAMPLES -->
## Usage

Edit the config, either set Pahtlib image paths for `image_1_path` and `image_2_path` to to run certain images, or set those variables to `None` to run on all image pairs in `/inputs/`. 

The outputs and intermediary steps will be displayed and saved to `/outputs/`



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact


Project Link: [https://github.com/gvanderl/Soft3DReonstruction](https://github.com/gvanderl/Soft3DReonstruction)


<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [Soft 3D Reconstruction for View Synthesis](https://ericpenner.github.io/soft3d/Soft_3D_Reconstruction.pdf)
* [Real-time local stereo matching using guided image filtering](https://publik.tuwien.ac.at/files/PubDat_206200.pdf)
* [Guided Image Filtering](http://kaiminghe.com/publications/eccv10guidedfilter.pdf)

