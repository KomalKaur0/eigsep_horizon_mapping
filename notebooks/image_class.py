# class to hold image data and metadata

class Image:
    def __init__(self, pathname, lat=None, lon=None, alt=None, angle_up=None, angle_side=None) -> None:
        '''
        constructor for image class

        parameters
        ----------
        pathname : str
            path to image
        lat : float, optional
            latitude the photo was taken at
        lon : float, optional
            longitude the photo was taken at
        alt : float, optional
            altitude the photo was taken at
        angle_up : float, optional
            angle above the horizontal the camera was pointed
        angle_side : float, optional
            angle WRT the normal to the lens along the horizontal the camera was pointed
        '''
        
        self.photo = #TODO: read the photo
        self.lat = lat
        self.lon = lon
        self.alt = alt
        self.angle_up = angle_up
        self.angle_side = angle_side

        #TODO: think about storing error bars