# Configuration of the parameters for the 3-FinalRasterAnalysis.ipynb notebook
class Configuration:
    '''
    Configuration for the notebook where objects are predicted in the image.
    Copy the configTemplate folder and define the paths to input and output data.
    '''
    def __init__(self):
        
        # Input related variables
        self.input_image_dir = '/projectnb/modislc/users/seamorez/HLS_FCover/UAV/TOR/CA_TOR_KOMR_RGB_20180805/'
        self.input_image_type = '.tif'
        self.raw_image_prefix = 'CA_TOR_KOMR_RGB_20180805_rgb_10cm'
        self.r_fn_st = 'red_'
        self.g_fn_st = 'green_'
        self.b_fn_st = 'blue_'
        self.trained_model_path = '/projectnb/modislc/users/seamorez/HLS_FCover/UAV/CNN_scripts/saved_models/UNet/shrubs_20250418-1013_AdaDelta_weightmap_tversky_0123_256.h5'

        # Output related variables
        self.output_dir = '/projectnb/modislc/users/seamorez/HLS_FCover/UAV/TOR/CA_TOR_KOMR_RGB_20180805/cnn_output/'
        self.output_image_type = '.tif'
        self.output_prefix = 'det_'
        self.output_shapefile_type = '.shp'
        self.overwrite_analysed_files = False
        self.output_dtype='uint8'

        # Variables related to batches and model
        self.BATCH_SIZE = 200 # Depends upon GPU memory and WIDTH and HEIGHT (Note: Batch_size for prediction can be different then for training.
        self.WIDTH=256 # Should be same as the WIDTH used for training the model
        self.HEIGHT=256 # Should be same as the HEIGHT used for training the model
        self.STRIDE=224 #224 or 196   # STRIDE = WIDTH means no overlap, STRIDE = WIDTH/2 means 50 % overlap in prediction
