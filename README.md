# synthetic_xview_airplanes

1. Download **[CityEngine](https://www.esri.com/en-us/arcgis/products/arcgis-cityengine/overview)**, and open CityEngine

2. Create a New CityEngine Project, then create a 3d scene (*.cej), which should be in the "scene" folder (in [scenes](https://github.com/yangxu351/synthetic_xview_airplanes/tree/master/scenes/scenes_of_xview)/*.cej), and in the top bar, use "Rectangular shape creation" to draw a rectangle in the 3d scene. ![image](https://user-images.githubusercontent.com/12199053/120770167-75d6d080-c550-11eb-9904-e33dbff1a866.png) 
 <img  alt = "image" src="https://user-images.githubusercontent.com/12199053/120770448-bb939900-c550-11eb-8354-12504507994b.png" width="304" height="304">


3. Prepare background images ([maps](https://github.com/yangxu351/synthetic_xview_airplanes/tree/master/maps/*.jpg)/*.jpg or *.png), we can directly drag the background image into the shape you draw in the scene. 

4. Prepare 3D airplane models ([assets](https://github.com/yangxu351/synthetic_xview_airplanes/raw/master/assets/aircraft/) (\*.OBJ, \*.glb, \*.fbx) 

5. Create a rule ([rules](https://github.com/yangxu351/synthetic_xview_airplanes/raw/master/rules/xview_gaussian/xsbw_xcolor_uniform_CC1/)/\*.cga) to design the loacation, size, color of 3D airpplane models [assets](https://github.com/yangxu351/synthetic_xview_airplanes/tree/master/assets)/\*.obj

6. Write a python script ([scripts](https://github.com/yangxu351/synthetic_xview_airplanes/tree/master/scripts/gaussian_square)/\*.py) to capture overhead images, and to control virtual camera height, environment parameters(e.g. solar elevation angle, solar azumith angle and shadow intensity)

7. Run python files (F9) in CityEngine, then all captured files will be saved in the folder of [images](https://github.com/yangxu351/synthetic_xview_airplanes/tree/master/images)

Illustration of synthetic data generation process

<img alt="Illustration of synthetic data generation process" src="https://user-images.githubusercontent.com/12199053/121108937-33a5db80-c83d-11eb-9828-abf8002138f1.png" >


| | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
|Background Images|![](https://github.com/yangxu351/synthetic_xview_airplanes/raw/master/maps/1087_bkg_1_1.jpg) | ![](https://github.com/yangxu351/synthetic_xview_airplanes/raw/master/maps/310_bkg_5_3.jpg) |![](https://github.com/yangxu351/synthetic_xview_airplanes/raw/master/maps/2179_bkg_2_2.jpg) | ![](https://github.com/yangxu351/synthetic_xview_airplanes/raw/master/maps/310_bkg_4_4.jpg) |![](https://github.com/yangxu351/synthetic_xview_airplanes/raw/master/maps/1094_bkg_1_3.jpg)  |
|RGB Images|![](https://github.com/yangxu351/synthetic_xview_airplanes/raw/master/images/syn_xview_bkg_new_bkg_unif_shdw_split_scatter_gauss_rndsolar_ssig0.08_color_square_bias0_CC1_v50/color_all_images_step182.4/color_airplanes_xview_background_sd30_1.png) | ![](https://github.com/yangxu351/synthetic_xview_airplanes/raw/master/images/syn_xview_bkg_new_bkg_unif_shdw_split_scatter_gauss_rndsolar_ssig0.08_color_square_bias0_CC1_v50/color_all_images_step182.4/color_airplanes_xview_background_sd783_1.png) |![](https://github.com/yangxu351/synthetic_xview_airplanes/raw/master/images/syn_xview_bkg_new_bkg_unif_shdw_split_scatter_gauss_rndsolar_ssig0.08_color_square_bias0_CC1_v50/color_all_images_step182.4/color_airplanes_xview_background_sd2532_1.png) | ![](https://github.com/yangxu351/synthetic_xview_airplanes/raw/master/images/syn_xview_bkg_new_bkg_unif_shdw_split_scatter_gauss_rndsolar_ssig0.08_color_square_bias0_CC1_v50/color_all_images_step182.4/color_airplanes_xview_background_sd4818_1.png) |![](https://github.com/yangxu351/synthetic_xview_airplanes/raw/master/images/syn_xview_bkg_new_bkg_unif_shdw_split_scatter_gauss_rndsolar_ssig0.08_color_square_bias0_CC1_v50/color_all_images_step182.4/color_airplanes_xview_background_sd1470_1.png)  |
|GT annotations|![](https://github.com/yangxu351/synthetic_xview_airplanes/raw/master/images/syn_xview_bkg_new_bkg_unif_shdw_split_scatter_gauss_rndsolar_ssig0.08_color_square_bias0_CC1_v50/color_all_annos_step182.4/color_airplanes_xview_background_sd30_1.png) | ![](https://github.com/yangxu351/synthetic_xview_airplanes/raw/master/images/syn_xview_bkg_new_bkg_unif_shdw_split_scatter_gauss_rndsolar_ssig0.08_color_square_bias0_CC1_v50/color_all_annos_step182.4/color_airplanes_xview_background_sd783_1.png) | ![](https://github.com/yangxu351/synthetic_xview_airplanes/raw/master/images/syn_xview_bkg_new_bkg_unif_shdw_split_scatter_gauss_rndsolar_ssig0.08_color_square_bias0_CC1_v50/color_all_annos_step182.4/color_airplanes_xview_background_sd2532_1.png) | ![](https://github.com/yangxu351/synthetic_xview_airplanes/raw/master/images/syn_xview_bkg_new_bkg_unif_shdw_split_scatter_gauss_rndsolar_ssig0.08_color_square_bias0_CC1_v50/color_all_annos_step182.4/color_airplanes_xview_background_sd4818_1.png)| ![](https://github.com/yangxu351/synthetic_xview_airplanes/raw/master/images/syn_xview_bkg_new_bkg_unif_shdw_split_scatter_gauss_rndsolar_ssig0.08_color_square_bias0_CC1_v50/color_all_annos_step182.4/color_airplanes_xview_background_sd1470_1.png) |

**the background images are projected with a certain degree in CE**

### Clone the repository ###

```git clone https://github.com/yangxu351/synthetic_xview_airplanes.git```


**Note: there is a bug of math log function in CityEngine**

### Citation ###

If you find these models useful for your resesarch, please cite with these bibtexs.

[SIMPL: Generating Synthetic Overhead Imagery to Address Zero-shot and Few-Shot Detection Problems](https://arxiv.org/ftp/arxiv/papers/2106/2106.15681.pdf) 

```
@article{xu2021simpl,
      title={SIMPL: generating synthetic overhead imagery to address custom zero-shot and few-shot detection problems}, 
      author={Yang Xu and Bohao Huang and Xiong Luo and Kyle Bradbury and Jordan M. Malof},
      year={2022},
      journal={IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing}
}
```
