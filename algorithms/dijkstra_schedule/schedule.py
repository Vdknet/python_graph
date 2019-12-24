

class Schedule(dict):
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
                if note.get('s') == a and note.get('d') == b and note.get('t') == t:
                    result = False
                    break
        return result

    def nearest_step(self, a, b, t, max_t=10):
        for i in range(t+1, max_t):
            if self.is_free(a, b, i):
                return i
        return None
