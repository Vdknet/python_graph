

class Schedule(dict):
    def __init__(self):
        self.submitted = 0
        self.requested = 0
        self.average_latency = 0.0
        self.max_latency = 0

    def write_one(self, s, d, t, query):
        old = self.get(query)
        if old is None:
            old = []
        old.append({'s': s, 'd': d, 't': t})
        self.update({query: old})

    def write(self, path, tacts, query):
        for i in range(len(path)):
            e = path[i]
            t = tacts[i]
            self.write_one(e.get('s'), e.get('d'), t, query)

    def is_free(self, a, b, t):
        values = self.values()
        result = True
        for path in values:
            for note in path:
                if note.get('s') == a and note.get('d') == b and \
                        note.get('t') == t:
                    result = False
                    break
        return result

    def nearest_step(self, a, b, t, max_t=6):
        for i in range(t+1, max_t):
            if self.is_free(a, b, i):
                return i
        return None

    def __str__(self):
        return "\n{requested: " + str(self.requested) +\
               ", submitted: " + str(self.submitted) +\
               ", average L:" + str(self.average_latency) +\
               ", max L:" + str(self.max_latency) + "}"
