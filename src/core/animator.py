class BezierCurve:
    def __init__(self, p0, p1, p2, p3):
        self.points = np.array([p0, p1, p2, p3])
    
    def evaluate(self, t):
        return (1-t)**3*self.points[0] + 3*(1-t)**2*t*self.points[1] \
            + 3*(1-t)*t**2*self.points[2] + t**3*self.points[3]

class Animator:
    def __init__(self):
        self.timelines = {}
        self.easing = BezierCurve(0.25, 0.1, 0.25, 1)
    
    def animate(self, target, prop, start, end, duration):
        # Stores interpolation jobs
        self.timelines[target] = {
            'prop': prop,
            'start_val': start,
            'end_val': end,
            'start_time': time.time(),
            'duration': duration
        }