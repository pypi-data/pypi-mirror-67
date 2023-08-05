from tqdm import tqdm


class ProgressBar():
    def __init__(self, step_size=100):
        self._step_size = step_size
        self._cur_bar = tqdm(step_size)
        self._cur_pos = 0
        self._total = 0

    def update(self):
        self._cur_pos = self._cur_pos + 1
        self._total = self._total + 1
        self._cur_bar.update(1)
        self._cur_bar.set_description_str('Processing: %s/%s,total: %s' % (self._cur_pos, self._step_size, self._total))
        if self._cur_pos == self._step_size:
            self._reset()

    def _reset(self):
        self._cur_bar.reset()
        self._cur_pos = 0

    def close(self):
        self._cur_bar.close()
