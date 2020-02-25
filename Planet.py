class PLanet(object):

    def __init__(self, planet, decription):
        self.planet = planet
        self.description = description

    def __str__(self):
        return f"Planet: {self.planet}"
        return f"Description: {self.description}"
