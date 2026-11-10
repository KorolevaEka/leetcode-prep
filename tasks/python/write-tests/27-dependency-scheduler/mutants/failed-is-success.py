class Scheduler:

    def __init__(self, dependencies):
        self.deps = {k: list(v) for k, v in dependencies.items()}
        self.states = {k: 'new' for k in dependencies}

    def claim(self):
        for job in sorted(self.deps):
            if self.states[job] == 'new' and all((self.states[x] == 'ok' for x in self.deps[job])):
                self.states[job] = 'running'
                return job
        return None

    def finish(self, job, ok):
        if self.states.get(job) != 'running':
            raise ValueError('state')
        self.states[job] = 'ok'
