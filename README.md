# EBL_SWG_circuit_Libray
This code was made as addon SWG-based photonic components for the SiEPIC PDK (These components currently can only be realized by EBL facilities). 

## Requirements
- [KLayout](https://www.klayout.de/)
- [SiEPIC PDK](https://github.com/lukasc-ubc/SiEPIC_EBeam_PDK)

## Installation
1. Download and install KLayout 
2. Install the SiEPIC PDK into Klayout
3. Place all *.lym* files in **Library** folder into your KLayout/tech/EBeam/pymacros folder

## How to use
1. You can create individual SWG-based devices via the **Instance** button in Klayout. This button will only show up after the SiEPIC PDK is installed and you have enabled editing mode.


<img src="https://raw.githubusercontent.com/EnxiaoLuan/Pics/master/fig1.png" width="600">

2. To use the layout script to create automatic designs, open the **Macro Development Window** (F5) and then locate the SWG-based component files. The script can take in arrays of parameters and iterates a whole layout for each combination.

<img src="https://raw.githubusercontent.com/EnxiaoLuan/Pics/master/fig2.png" width="600">

## Package contents
The package serves as an add-on for the SiEPIC PDK which includes the SWG-based photonic components (Parameterizable-Cells and Fixed-Cells) for the full SWG circuits design.

### Components includes:

- **SWG waveguide:** a parameterizable cell to build the SWG waveguide with adjustable parameters, including waveguide width, waveguide length, period and duty cycle. 

<img src="https://raw.githubusercontent.com/EnxiaoLuan/Pics/master/fig5.png" width="400">

- **SWG bend:** a parameterizable cell to build the SWG bend waveguide with adjustable adjustable parameters, including waveguide width, preiod, duty cycle, radius and bend type (1/2 or 1/4 bend).

<img src="https://raw.githubusercontent.com/EnxiaoLuan/Pics/master/fig6.png" width="250">

- **SWG microring resonator:** a parameterizable cell to build the SWG microring resonator with adjustable parameters, including waveguide width, period, duty cycle, radius, coupling gap distance and bus waveguide length.

<img src="https://raw.githubusercontent.com/EnxiaoLuan/Pics/master/fig7.png" width="275">


- **SWG edge coupler:** a fixed cell to build the 80-um-long SWG edge coupler.


<img src="https://raw.githubusercontent.com/EnxiaoLuan/Pics/master/fig8.png" width="450">

- **SWG taper:** a parameterizable cell to build the SWG taper waveguide with adjustable parameters, including waveguide widths on both side, waveguide length, period and duty cycle. 

<img src="https://raw.githubusercontent.com/EnxiaoLuan/Pics/master/Picture1.png" width="450">

- **SWG direction coupler:** two fixed cells to build the SWG contra direction coupler

<img src="https://raw.githubusercontent.com/EnxiaoLuan/Pics/master/fig9.png" width="450">

- **Trapezoidal-SWG bend:** a parameterizable cell to build the T-shape SWG bend waveguide with adjustable adjustable parameters, including waveguide width, preiod, duty cycle, radius, bend type (1/2 or 1/4 bend) and inner and outer block widths.

<img src="https://raw.githubusercontent.com/EnxiaoLuan/Pics/master/fig11.png" width="400">


- **Trapezoidal-SWG microring resonator:** a parameterizable cell to build the T-shape SWG microring resonator with adjustable parameters, including waveguide width, period, duty cycle, radius, coupling gap distance, bus waveguide length, and inner and outer block widths.

<img src="https://raw.githubusercontent.com/EnxiaoLuan/Pics/master/fig10.png" width="400">

- **Multi-box SWG waveguide:** a parameterizable cell to build the multi-box SWG waveguide with adjustable parameters, including Si-box width, waveguide length, period, duty cycle, multi-box row number and row gap distance. 

<img src="https://raw.githubusercontent.com/EnxiaoLuan/Pics/master/fig12.png" width="400">

- **Multi-box microring resonator:** a parameterizable cell to build the multi-box SWG microring resonator with adjustable parameters, including Si-box width, period, duty cycle, multi-box row number, row gap distance, radius, coupling gap distance and bus waveguide length.

<img src="https://raw.githubusercontent.com/EnxiaoLuan/Pics/master/fig13.png" width="550">

- **Multi-box Bragg grating:** a parameterizable cell to build the multi-box SWG Bragg grating waveguide with adjustable parameters, including Si-box width, waveguide length, period, duty cycle, multi-box row number, row gap distance, uniform or phase-shifted geometry and the corrugation width. 

<img src="https://raw.githubusercontent.com/EnxiaoLuan/Pics/master/Screen%20Shot%202020-02-12%20at%209.34.07%20PM.png" width="550">

- **SWG crossing:**

- **SWG Y-branch:**

- **SWG MMI:** a parameterizable cell to build the SWG MMI with adjustable parameters, including MMI width, MMI length, SWG period, duty cycle, SWG taper length and port distance.

<img src="https://raw.githubusercontent.com/EnxiaoLuan/Pics/master/mmi.png" width="700">

- **SWG grating coupler:**

## Technical Support

The principle of Sub-Wavelength has long been known by Hertz in the late 19th century by using a fine grid of parallel metal wires as a polarizer. The first observation at optical wavelength was achieved by Bernhard in 1967, where the reflection from the corneas of night-flying moths is reduced to protect them from nocturnal predators.

### Sub-Wavelength region [1]:
When an object has a structure that is larger than the wavelength of light, its influence on the propagation of light may be described by the laws of diffraction, refraction and reflection.

Between these two extremes is a region in which there is a structure that is too fine to give rise to diffraction but too coarse for the medium to be considered as homogeneous and a full description can only be achieved through a rigorous solution of Maxwell's electromagnetic equation.

<img src="https://raw.githubusercontent.com/EnxiaoLuan/Pics/master/fig3.png" width="400">

For many applications, a full description and rigorous solution of Maxwell's electromagnetic equation is not necessary and solutions can be found with sufficient accuracy by approximating subwavelength structure as an effectively homogeneous medium.

### Sub-Wavelength Gratings in silicon [2]:
Since the first demonstrations of an optical waveguide with an of Sub-Wavelength grating (SWG) metamaterial core by the National Research Council of Canada (NRC) in 2006, SWG waveguides have attracted intense research interest due to their unique potentials to control light propagation in planar waveguides, and been considered to be critical components for developing the next generation of optical communication, biomedical, quantum and sensing technologies. Although similar to Bragg gratings, SWG waveguides also consist of the periodic structure of their core, the period (Λ) is much smaller than the Bragg condition, i.e., Λ<<λ/(2n<sub>eff</sub>). Thus, a true lossless mode is supported in SWG waveguides because the reflection and diffraction effects are suppressed. 

The SWG waveguide core is commonly fabricated by interleaving the high index block (n<sub>1</sub>) with low index materials (n<sub>2</sub>), such as SiO<sub>2</sub>, SU-8, air or water, as one period (a few hundred nanometers in length). By having a reduced
mode effective index step, the guided light propagates in SWG waveguides similar to the one in conventional waveguides but with a large extended modal area, which releases more optical mode into the evanescent field. Therefore, the SWG waveguide gives more freedom for the one to tailor the optical waveguide parameters. 

<img src="https://raw.githubusercontent.com/EnxiaoLuan/Pics/master/fig4.png" width="600">

### Applications in silicon:

SWG have been considered to provide promising solutions in the development of next-generation optical communication, quantum, and biosensing technologies, due to the unique behavior of propagating light in SWG metamaterials. Silicon-based sub-wavelength structures have been employed in a wide range of integrated optical devices, including high-efficiency grating couplers, low-loss waveguide crossings, ultra-broadband directional couplers, as well as high-sensitivity biosensors. Details for these the-state-of-art applications can be found in **Related papers** folder.

<img src="https://raw.githubusercontent.com/EnxiaoLuan/Pics/master/fig14.png" width="1000">

## References
[1] [Pavel Cheben, "Subwavelength silicon photonics," Winter College on Optics: Fundamentals of Photonics-Theory, Devices and Applications, 2014.](http://indico.ictp.it/event/a13188/session/5/contribution/22/material/0/0.pdf)

[2] [Luan, Enxiao, et al. "Silicon photonic biosensors using label-free detection." Sensors 18.10 (2018): 3519.](https://www.mdpi.com/1424-8220/18/10/3519)
