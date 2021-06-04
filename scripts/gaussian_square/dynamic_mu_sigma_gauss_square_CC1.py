'''
Created on 06.26.2019

@author: Fanjie Kong



'''
import os
import time
import math
import random
from scripting import *
# get a CityEngine instance

ce = CE()
TileSize=608
RESOLUTION = 0.3
STEP = RESOLUTION * TileSize

def dynamic_attributes(adjust_list, camera_angle, light_intensity, 
                       solar_elevation_angle, solar_azimuth_angle, dynamic_range, mode):
    '''
    adjust_list: a list of strings
    camera_angle: number between 0~90
    light_angle: number between 0~90
    solar_elevation_angle: number between 0~90
    solar_azimuth_angle: number between 0~3600
    light_instensity: number between 0~1
    dynamic_range: a dictionary has the form
        {'ca': int, 'la': int, 'li': int, 'se':float, 'sa':float}
        The value  will vary in range of [sv-dv, sv+dv]
    '''
    lightSettings = ce.getLighting()
    assert ('se' in adjust_list) or ('ca' in adjust_list) or ('li' in adjust_list) or ('sa' in adjust_list), "Please select an attribute to augment"
    if 'se' in adjust_list:
        solar_elevation_angle = solar_elevation_angle + random.randint(-dynamic_range['se'], dynamic_range['se'])
        lightSettings.setSolarElevationAngle(solar_elevation_angle)
    if 'ca' in adjust_list:
        camera_angle = camera_angle + random.randint(-dynamic_range['ca'], dynamic_range['ca'])
        camera_angle = '-' + str(camera_angle)
    if 'li' in adjust_list:
        light_intensity = min(1, light_intensity + 0.1 * random.randint(-int(10*dynamic_range['li']), int(10*dynamic_range['li'])))
        lightSettings.setSolarIntensity(light_intensity)
    if 'sa' in adjust_list:
        lightSettings.setSolarAzimuthAngle(solar_azimuth_angle)
    if mode == 'GT':
        return camera_angle
    ce.setLighting(lightSettings)
#    print("New attribute triple bracket is ", (solar_elevation_angle, solar_azimuth_angle, light_intensity, camera_angle))
    return camera_angle

'''
parse lines and look for id
prepare cam data in array
non-generic, works for specific fbx part only
'''
def drange(x, y, jump):
      while x < y:
        yield x
        x += jump

def parseLine(lines, id):
    data = False
    for line in lines:
        if line.find(id) >=0 :
            data = line.partition(id)[2]
            break
    if data:
        data = data[:len(data)-1] # strip \n
        data = data.split(",")
    return data

'''
parse lines from fbx file that store cam data
'''
def parseFbxCam(filename):
    f=open(filename)
    lines = f.readlines()
    cnt = 0
    loc =  parseLine(lines, 'Property: "Lcl Translation", "Lcl Translation", "A+",')
    rot =  parseLine(lines, 'Property: "Lcl Rotation", "Lcl Rotation", "A+",')
    return [loc,rot]


'''
helper functions
'''
def setCamPosV(v, vec):
    v.setCameraPosition(vec[0], vec[1], vec[2])

def setCamRotV(v, vec):
    v.setCameraRotation(vec[0], vec[1], vec[2])

'''
sets camera on first CE viewport
'''
def setCamData(data):
    v = ce.getObjectsFrom(ce.get3DViews(), ce.isViewport)[0]
    setCamPosV(v, data[0])
    setCamRotV(v, data[1])
    return v

def setCamHeight(FOV=15, tile_width=TileSize):
    '''
    Calculates proper height of camera in CityEngine based on current camera
    used (FOV in degrees), desired tile size, and desired resolution
    '''
    FOV = math.radians(FOV)
    d = tile_width * RESOLUTION #pixel width of tile * resolution in m/pixel
#    print('height',d / (2*math.tan(FOV/2)) )
    return str(d / (2*math.tan(FOV/2)))


'''
master function
('data:', [['-1546.92522788752', '3662.20346070665', '-1543.6636199449'], ['-51.5999993410019', '-94.3999999999998', '-2.54444374517081e-014']])
'''
def importFbxCamera(fbxfile, axis, angle, height):

    data = parseFbxCam(fbxfile)
    if(data[0] and data[1]) :
        data[0][0]=str(axis[0])
        data[0][1] = height
        data[0][2]= str(axis[1])
        data[1][0] = data[1][1] = angle
        v = setCamData(data)
#        print "Camera set to "+str(data)
        return v
    else:
        print("No camera data found in file " + fbxfile)


def exportImages(directory, v, Tag=""):
   path = directory + "/" + Tag + ".png"
   v.snapshot(path, width = TileSize, height = TileSize)
   
def exportGroundtruths(directory, v, Tag=""):
    path = directory + "/" + Tag + ".png"
    v.snapshot(path, width = TileSize, height = TileSize)


def loop_capturer_dynamic_attributes(center_axis, tag,
                                     mode='RGB', folder_name='test',
                                     adjust_list=('se', 'ca', 'li', 'sa'), 
                                     solar_elevation_angle=90, solar_azimuth_angle=90,
                                     camera_angle=90, light_intensity=1,
                                     dynamic_range={'ca': 0, 'li': 0, 'se':0, 'sa':0}):
    counter = 0
#    print('Start Shooting!')
    camfile = ce.toFSPath("data/camera.fbx")
    height = setCamHeight(tile_width=TileSize)
    angle = dynamic_attributes(adjust_list, camera_angle, light_intensity, 
                               solar_elevation_angle, solar_azimuth_angle, dynamic_range, mode)
#    print('i, j', i, j)
    view = importFbxCamera(camfile, (center_axis[0], center_axis[1]), angle, height)
    counter += 1
    print(counter)
#    time.sleep(0.1)
#    for _ in range(3):
    if mode == 'GT':
        lightSettings = ce.getLighting()
        lightSettings.setSolarElevationAngle(90)
        lightSettings.setSolarIntensity(1)
        ce.setLighting(lightSettings)
        ce.waitForUIIdle()
    exportGroundtruths(ce.toFSPath('images/{}'.format(folder_name)), view, Tag=tag+'_'+str(counter))
                

def load_rule_file(seed, rule_file_path):
    all_shapes = ce.getObjectsFrom(ce.scene, ce.isShape)
    ce.setSeed(all_shapes, seed)
    ce.setRuleFile(all_shapes, rule_file_path)
    ce.generateModels(all_shapes)
    ce.waitForUIIdle()
#    time.sleep(1)
#    print('load rules ok')
    
def raw_rgb(seed, rule_file_path):
#    print('raw_rgb')
    load_rule_file(seed, rule_file_path)
    renderSettings = RenderSettings()
    renderSettings.setOnCameraLight(False)
    renderSettings.setShadows(True)
    renderSettings.setAmbientOcclusion(True)
    renderSettings.setGridVisible(False)
    view = ce.getObjectsFrom(ce.get3DViews(), ce.isViewport)[0]
    view.setRenderSettings(renderSettings)
    
    
def raw_gt(seed, rule_file_path):
#    print('raw_gt')
    load_rule_file(seed, rule_file_path)
    renderSettings = RenderSettings()
    renderSettings.setOnCameraLight(True)
    renderSettings.setShadows(False)
    renderSettings.setAmbientOcclusion(False)
    renderSettings.setGridVisible(False)
    view = ce.getObjectsFrom(ce.get3DViews(), ce.isViewport)[0]
    view.setRenderSettings(renderSettings)
    
    
if __name__ == '__main__':
    '''
    shoot each location with a combination of randomized parameters in a range
    eg:
    adjust_list = ['la', 'ca', 'li'], # list of parameters to be randomized
    light_angle=45,  camera_angle=80, light_intensity=0.8,  # centers of the range
    dynamic_range={'ca': 10, 'la': 15, 'li': 0.3} # the width of the range

    This set of parameters means shoot an image
     where camera angle is a random number in [70, 90],
     light angle is a random number in [30, 60],
     light intensity is a random number in [0.5, 1]

    '''
    '''#### color augmentation ####'''
    rgb_rule_file = 'rules/xview_gaussian/xsbw_xcolor_uniform_CC1/yx_xview_plane_cc1_color_gauss.cga' 
    gt_rule_file = 'rules/xview_gaussian/xsbw_xcolor_uniform_CC1/yx_xview_plane_cc1_color_labeling_gauss.cga'
    '''# ######  '''
    ######### dynamic color sigma
    color_pro = 4
    color_pro_list = [1, 2, 3, 4]
#    for s in color_pro_list:
#        inx = color_pro_list.index(s)
##        parent_folder = 'syn_xview_bkg_unif_shdw_split_scatter_gauss_rndsolar_ssig0.16_color_square_bias{}_CC1_v{}'.format(s, inx + 30)
#        parent_folder = 'syn_xview_bkg_new_bkg_unif_shdw_split_scatter_gauss_rndsolar_ssig0.24_color_square_bias{}_CC1_v{}'.format(s, inx + 46)
#        print(parent_folder)
#        if not os.path.exists(ce.toFSPath('images/{}'.format(parent_folder))):
#            os.makedirs(ce.toFSPath('images/{}'.format(parent_folder)))
    inx = color_pro_list.index(color_pro)
#    parent_folder = 'syn_xview_bkg_unif_shdw_split_scatter_gauss_rndsolar_ssig0.16_color_square_bias{}_CC1_v{}'.format(color_pro, inx + 30)
    parent_folder = 'syn_xview_bkg_new_bkg_unif_shdw_split_scatter_gauss_rndsolar_ssig0.24_color_square_bias{}_CC1_v{}'.format(color_pro, inx + 46)
       
    
    '''#### size augmentation  ####'''
#    rgb_rule_file = 'rules/xview_gaussian/xsbw_xcolor_uniform_CC1/size/yx_xview_plane_cc1_size_gauss.cga' #, 'rules/xview/xsbw_xcolor_uniform_for_one_model_bias_rc1/yx_xview_plane_mixed.cga'
#    gt_rule_file = 'rules/xview_gaussian/xsbw_xcolor_uniform_CC1/size/yx_xview_plane_cc1_size_labeling_gauss.cga' #, 'rules/xview/xsbw_xcolor_uniform_for_one_model_bias_rc1/yx_xview_plane_labeling_mixed.cga'
#    '''########### dynsigma size'''
#    size_pro = 0
#    size_pro_list = [0, 0.08, 0.16, 0.24, 0.32]
##    for s in size_pro_list:
##        inx = size_pro_list.index(s)
###        parent_folder = 'syn_xview_bkg_unif_shdw_split_scatter_gauss_rndsolar_promu_size_square_bias{}_CC1_v{}'.format(s, inx + 20)
##        parent_folder = 'syn_xview_bkg_new_bkg_unif_shdw_split_scatter_gauss_rndsolar_promu_size_square_bias{}_CC1_v{}'.format(s, inx + 40)
##        print(parent_folder)
##        if not os.path.exists(ce.toFSPath('images/{}'.format(parent_folder))):
##            os.makedirs(ce.toFSPath('images/{}'.format(parent_folder)))
#    inx = size_pro_list.index(size_pro)
##    parent_folder = 'syn_xview_bkg_unif_shdw_split_scatter_gauss_rndsolar_promu_size_square_bias{}_CC1_v{}'.format(size_pro, inx + 20)
#    parent_folder = 'syn_xview_bkg_new_bkg_unif_shdw_split_scatter_gauss_rndsolar_promu_size_square_bias{}_CC1_v{}'.format(size_pro, inx + 40)
    
  
    dt = 'color'
    center_axis=(2200 + STEP/2 +1.5, 2200+ STEP/2+1.5)
    
    random.seed(1)
    start_time = time.time()

    print(parent_folder)
    if not os.path.exists(ce.toFSPath('images/{}'.format(parent_folder))):
        os.makedirs(ce.toFSPath('images/{}'.format(parent_folder)))
    rnd_points = random.sample(range(5000), 450)
#    print(rnd_points)
    print('start')
    '''#####  RGB     #######'''
    for sd in rnd_points:
        print('seed', sd)
        tag='{}_airplanes_xview_background_sd{}'.format(dt, sd)        
        mode = 'RGB'
        folder_name='{}/{}_all_images_step{}'.format(parent_folder, dt, STEP)  
#        print('folder_name', folder_name)
        if not os.path.exists(ce.toFSPath('images/{}'.format(folder_name))):
            os.makedirs((ce.toFSPath('images/{}'.format(folder_name))))
        solar_ele_angle = random.randint(40, 70)
        solar_azi_angle = random.randint(100, 280)
        light_intensity = random.randint(4, 8)*0.1 # 1.0 #
#        print('light_intensity', light_intensity)
        camera_angle = 90
        raw_rgb(sd, rgb_rule_file)
        loop_capturer_dynamic_attributes(center_axis=center_axis, 
                                     tag=tag, mode=mode, folder_name=folder_name,
                                     solar_elevation_angle=solar_ele_angle, 
                                     solar_azimuth_angle=solar_azi_angle,
                                     camera_angle=camera_angle,
                                     light_intensity=light_intensity)
        
    '''#####  GT    #######'''
    for sd in rnd_points:
        print('seed', sd)
        tag='{}_airplanes_xview_background_sd{}'.format(dt, sd) 
        mode = 'GT'
        folder_name='{}/{}_all_annos_step{}'.format(parent_folder, dt, STEP)  
        if not os.path.exists(ce.toFSPath('images/{}'.format(folder_name))):
            os.makedirs((ce.toFSPath('images/{}'.format(folder_name))))
        solar_ele_angle = random.randint(40, 70)
        solar_azi_angle = random.randint(100, 280)
        light_intensity = random.randint(4, 8)*0.1 # 1.0 #
        camera_angle = 90
        raw_gt(sd, gt_rule_file)
        loop_capturer_dynamic_attributes(center_axis=center_axis, 
                                     tag=tag, mode=mode, folder_name=folder_name,
                                     solar_elevation_angle=solar_ele_angle, 
                                     solar_azimuth_angle=solar_azi_angle,
                                     camera_angle=camera_angle,
                                     light_intensity=light_intensity)
        
    print('Duration: {}'.format(time.time()-start_time)) 
    
