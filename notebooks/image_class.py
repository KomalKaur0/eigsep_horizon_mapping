from eigsep_terrain.marjum_dem import MarjumDEM as DEM

class Image:
    def __init__(self, pathname, label, lat=None, lon=None, alt=None, angle_up=None, angle_side=None) -> None:
        '''
        constructor for image class

        parameters
        ----------
        pathname : str
            path to image
        label : str
            name for image
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
        
        self.photo = pathname
        self.label = label
        self.lat = lat
        self.lon = lon
        self.alt = alt
        self.angle_up = angle_up
        self.angle_side = angle_side

        #TODO: think about storing error bars

    def check_valid_position(self, lat=None, lon=None, alt=None) -> bool:
        '''
        checks if a position on the canyon is valid (ie: not falling off a cliff, 
        entombed in stone, or other such unfortunate places to be taking a photo)
        via comparison to terrain maps.
        default paramters are the image's attributes but optional other parameters can be passed in

        parameters
        ----------
        lat : float, optional
            latitude the photo was taken at
        lon : float, optional
            longitude the photo was taken at
        alt : float, optional
            altitude the photo was taken at

        returns
        ----------
        valid : bool
            True if the position is valid, False if not
        '''

        #TODO
        # use the lat and lon to find the correct altitude and see if the given alt is acceptable (+- 5m)
        if not lat:
            lat = self.lat
        if not lon:
            lon = self.lon
        if not alt:
            alt = self.alt

        assert lat is not None
        assert lon is not None
        assert alt is not None

        # lla to emu
        enus = DEM.latlon_to_enu(lat, lon, alt)

        # correct alt
        interped_alt = DEM.interp_alt(**enus)
        acceptable_offset = 5 #m

        return interped_alt - acceptable_offset < alt < interped_alt + acceptable_offset
    
    def open(self) -> None:
        '''
        function to open the photo
        TODO: think about use cases, maybe healpy related or something
        '''
        pass
