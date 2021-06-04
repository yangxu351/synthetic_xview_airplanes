# synthetic_xview_airplanes

1. Open **CityEngine**

2. Create a New CityEngine Project(*.cej), which should be in the "scene" folder (in [scenes](https://github.com/yangxu351/synthetic_xview_airplanes/tree/master/scenes/scenes_of_xview)/*.cej)

3. prepare background images ([maps](https://github.com/yangxu351/synthetic_xview_airplanes/tree/master/maps/*.jpg)/*.jpg or *.png)
  for example: [background](https://github.com/yangxu351/synthetic_xview_airplanes/tree/master/maps/310_bkg_4_4.jpg) 

4. create a rule to design the loacation, size, color of 3D airpplane models [assets](https://github.com/yangxu351/synthetic_xview_airplanes/tree/master/assets)/*.obj

5. use python script ([scripts](https://github.com/yangxu351/synthetic_xview_airplanes/tree/master/scripts/gaussian_square)/*.py) to capture overhead images, and to control virtual camera height, environment parameters(e.g. solar elevation angle, solar azumith angle and shadow intensity)

6. run python files (F9) in CityEngine, then all captured files will be saved in the folder of [images](https://github.com/yangxu351/synthetic_xview_airplanes/tree/master/images)

![images/images/1.png](https://github.com/yangxu351/synthetic_xview_airplanes/raw/master/images/syn_xview_bkg_new_bkg_unif_shdw_split_scatter_gauss_rndsolar_ssig0.08_color_square_bias0_CC1_v50/color_all_images_step182.4/color_airplanes_xview_background_sd1038_1.png)

![images/annos/1.png](https://github.com/yangxu351/synthetic_xview_airplanes/raw/master/images/syn_xview_bkg_new_bkg_unif_shdw_split_scatter_gauss_rndsolar_ssig0.08_color_square_bias0_CC1_v50/color_all_annos_step182.4/color_airplanes_xview_background_sd1038_1.png)

**Note: there is a bug of math log function in CityEngine**
