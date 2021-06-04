# synthetic_xview_airplanes

1. Open **CityEngine**

2. Create a New CityEngine Project(*.cej), which should be in the "scene" folder (in [scenes](https://github.com/yangxu351/synthetic_xview_airplanes/tree/master/scenes/scenes_of_xview)/*.cej)

3. prepare background images ([maps](https://github.com/yangxu351/synthetic_xview_airplanes/tree/master/maps)/*.jpg or *.png) 

4. create a rule to design the loacation, size, color of 3D airpplane models [assets](https://github.com/yangxu351/synthetic_xview_airplanes/tree/master/assets)/*.obj

5. use python script ([scripts](https://github.com/yangxu351/synthetic_xview_airplanes/tree/master/scripts/gaussian_square)/*.py) to capture overhead images, and to control virtual camera height, environment parameters(e.g. solar elevation angle, solar azumith angle and shadow intensity)

6. run python files (F9) in CityEngine, then all captured files will be saved in the folder of [images](https://github.com/yangxu351/synthetic_xview_airplanes/tree/master/images)

![images/images/1.png](https://github.com/yangxu351/synthetic_xview_airplanes/raw/master/images/images/color_airplanes_xview_background_sd1033_1.png)

![images/annos/1.png](https://github.com/yangxu351/synthetic_xview_airplanes/raw/master/images/annos/color_airplanes_xview_background_sd1033_1.png)

**Note: there is a bug of math log function in CityEngine**