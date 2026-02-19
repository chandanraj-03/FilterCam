import cv2
import numpy as np
from filters import FILTERS


class FilterEngine:
    """Camera filter engine — applies Instagram-style filters to frames."""

    def __init__(self):
        self.filters = FILTERS
        self.current_index = 0
        self.intensity = 1.0
        self.watermark_enabled = False

    @property
    def filter_count(self):
        return len(self.filters)

    @property
    def current_name(self):
        return self.filters[self.current_index][0]

    def set_filter(self, idx):
        if 0 <= idx < self.filter_count:
            self.current_index = idx

    def next_filter(self):
        self.current_index = (self.current_index + 1) % self.filter_count

    def prev_filter(self):
        self.current_index = (self.current_index - 1) % self.filter_count

    def random_filter(self):
        import random
        self.current_index = random.randint(0, self.filter_count - 1)

    def reset(self):
        self.current_index = 0
        self.intensity = 1.0

    def process_frame(self, frame):
        """Apply the current filter. Returns the result frame."""
        name, fn = self.filters[self.current_index]
        filtered = fn(frame.copy())

        if self.intensity < 1.0:
            result = cv2.addWeighted(frame, 1.0 - self.intensity, filtered, self.intensity, 0)
        else:
            result = filtered

        if self.watermark_enabled:
            self._apply_watermark(result)

        return result

    def _apply_watermark(self, frame):
        text = "By- Chandan Raj"
        h, w = frame.shape[:2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        scale, thickness = 0.4, 1
        (tw, th), _ = cv2.getTextSize(text, font, scale, thickness)
        x, y = w - tw - 20, h - 20
        overlay = frame.copy()
        cv2.putText(overlay, text, (x + 2, y + 2), font, scale, (0, 0, 0), thickness)
        cv2.putText(overlay, text, (x, y), font, scale, (255, 255, 255), thickness)
        cv2.addWeighted(overlay, 0.7, frame, 0.3, 0, frame)
