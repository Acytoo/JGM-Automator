from target import TargetType
import cv2


class UIMatcher:
    @staticmethod
    def match(screen, target:TargetType):
        template = cv2.imread(target.value)
        th, tw = template.shape[:2]

        res = cv2.matchTemplate(screen, template, cv2.TM_SQDIFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        tl = min_loc

        if min_val > 0.15:
            return None

        return tl[0] + tw / 2 + 15, tl[1] + th / 2 + 15

    @staticmethod
    def read(filepath:str):
        return cv2.imread(filepath)
