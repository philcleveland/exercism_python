class SpaceAge:

    # Planet Years in seconds
    EARTH_YEAR = 31557600.0
    MERCURY_YEAR_RATIO = 0.2408467
    VENUS_YEAR_RATIO = 0.61519726
    MARS_YEAR_RATIO = 1.8808158
    JUPITER_YEAR_RATIO = 11.862615
    SATURN_YEAR_RATIO = 29.447498
    URANUS_YEAR_RATIO = 84.016846
    NEPTUNE_YEAR_RATIO = 164.79132

    def __init__(self, seconds):
        self.seconds = seconds

    def calculate_planet_year(self, secondsPerPlanetYear):
        return round(self.seconds / secondsPerPlanetYear, 2)

    def on_earth(self):
        return self.calculate_planet_year(SpaceAge.EARTH_YEAR)

    def on_mercury(self):
        return self.calculate_planet_year(SpaceAge.EARTH_YEAR * SpaceAge.MERCURY_YEAR_RATIO)

    def on_venus(self):
        return self.calculate_planet_year(SpaceAge.EARTH_YEAR * SpaceAge.VENUS_YEAR_RATIO)

    def on_mars(self):
        return self.calculate_planet_year(SpaceAge.EARTH_YEAR * SpaceAge.MARS_YEAR_RATIO)

    def on_jupiter(self):
        return self.calculate_planet_year(SpaceAge.EARTH_YEAR * SpaceAge.JUPITER_YEAR_RATIO)

    def on_saturn(self):
        return self.calculate_planet_year(SpaceAge.EARTH_YEAR * SpaceAge.SATURN_YEAR_RATIO)

    def on_uranus(self):
        return self.calculate_planet_year(SpaceAge.EARTH_YEAR * SpaceAge.URANUS_YEAR_RATIO)

    def on_neptune(self):
        return self.calculate_planet_year(SpaceAge.EARTH_YEAR * SpaceAge.NEPTUNE_YEAR_RATIO)
