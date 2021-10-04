class SpaceAge:
    def __init__(self, spacial_age):
        self.spacial_age = spacial_age

    def seconds(self):
        return self.spacial_age

    def standar_calculation(self, age_on_seconds):
        return round(self.on_earth() / age_on_seconds, 2)

    def on_earth(self):
        return round(self.spacial_age / 31557600, 2)

    def on_mercury(self):
        return self.standar_calculation(0.2408467)

    def on_venus(self):
        return self.standar_calculation(0.61529726)

    def on_mars(self):
        return self.standar_calculation(1.8808158)

    def on_jupiter(self):
        return self.standar_calculation(11.862615)

    def on_saturn(self):
        return self.standar_calculation(29.447498)

    def on_uranus(self):
        return self.standar_calculation(84.016846)

    def on_neptune(self):
        return self.standar_calculation(164.79132)
