# synthetic_xview_airplanes

1. Open **CityEngine**

2. Create a New CityEngine Project(*.cej), which should be in the "scene" folder (in [scenes](https://github.com/yangxu351/synthetic_xview_airplanes/tree/master/scenes/scenes_of_xview)/*.cej), and in the top bar, use "Rectangular shape creation" to draw a rectangle in the 3d scene. ![image](https://user-images.githubusercontent.com/12199053/120770167-75d6d080-c550-11eb-9904-e33dbff1a866.png) 
 <img  alt = "image" src="https://user-images.githubusercontent.com/12199053/120770448-bb939900-c550-11eb-8354-12504507994b.png" width="304" height="304">


3. Prepare background images ([maps](https://github.com/yangxu351/synthetic_xview_airplanes/tree/master/maps/*.jpg)/*.jpg or *.png), we can directly drag the background image into the shape you draw in the scene. for example: 

  <img  alt = "maps/310_bkg_4_4.jpg" src="https://github.com/yangxu351/synthetic_xview_airplanes/raw/master/maps/310_bkg_4_4.jpg" width="304" height="304">

4. Prepare 3D airplane models ([assets](https://github.com/yangxu351/synthetic_xview_airplanes/raw/master/assets/aircraft/) (\*.OBJ, \*.glb, \*.fbx) 

5. Create a rule ([rules](https://github.com/yangxu351/synthetic_xview_airplanes/raw/master/rules/xview_gaussian/xsbw_xcolor_uniform_CC1/)/\*.cga) to design the loacation, size, color of 3D airpplane models [assets](https://github.com/yangxu351/synthetic_xview_airplanes/tree/master/assets)/\*.obj

6. Write a python script ([scripts](https://github.com/yangxu351/synthetic_xview_airplanes/tree/master/scripts/gaussian_square)/\*.py) to capture overhead images, and to control virtual camera height, environment parameters(e.g. solar elevation angle, solar azumith angle and shadow intensity)

7. Run python files (F9) in CityEngine, then all captured files will be saved in the folder of [images](https://github.com/yangxu351/synthetic_xview_airplanes/tree/master/images)

<img  alt = "images/images/1.png" src="https://github.com/yangxu351/synthetic_xview_airplanes/raw/master/images/syn_xview_bkg_new_bkg_unif_shdw_split_scatter_gauss_rndsolar_ssig0.08_color_square_bias0_CC1_v50/color_all_images_step182.4/color_airplanes_xview_background_sd1038_1.png" width="304" height="304">

<img  alt = "images/annos/1.png" src="https://github.com/yangxu351/synthetic_xview_airplanes/raw/master/images/syn_xview_bkg_new_bkg_unif_shdw_split_scatter_gauss_rndsolar_ssig0.08_color_square_bias0_CC1_v50/color_all_annos_step182.4/color_airplanes_xview_background_sd1038_1.png" width="304" height="304">

**Note: there is a bug of math log function in CityEngine**

### Citation ###

If you find these models useful for your resesarch, please cite with these bibtexs.

@article{yangxu2021,
  title={SIMPL: Generating Synthetic Overhead Imagery of Rare Target Objects to Enhance Zero-shot and Few-Shot Detection Problems},
  author={Yang Xu, Bohao Huang, Kyle Bradbury, Xiong Luo, and Jordan M. Malof}
  
}
