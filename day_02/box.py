class Box:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def compute_wrapping_required(self):
        sites = [self.x * self.y, self.y * self.z, self.x * self.z]
        return 2 * sum(sites) + min(sites)

    def volume(self):
        return self.x * self.y * self.z

    def compute_ribbon_required(self):
        return 2 * sum(sorted([self.x, self.y, self.z])[0:2]) + self.volume()
