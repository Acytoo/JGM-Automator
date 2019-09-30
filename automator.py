from target import TargetType
from cv import UIMatcher
import uiautomator2 as u2


class Automator:
    def __init__(self, device:str, targets:dict):
        self.d = u2.connect(device)
        self.targets = targets

    def start(self):
        while True:
            for target in TargetType:
                self._match_target(target)

            self.d.click(550, 1650)

            self._swipe()

    def _swipe(self):
        for i in range(3):
            sx, sy = self._get_position(i * 3 + 1)
            ex, ey = self._get_position(i * 3 + 3)
            self.d.swipe(sx, sy, ex, ey)

    @staticmethod
    def _get_position(key):
        positions = {
            1: (294, 1184),
            2: (551, 1061),
            3: (807, 961),
            4: (275, 935),
            5: (535, 810),
            6: (799, 687),
            7: (304, 681),
            8: (541, 568),
            9: (787, 447)
        }
        return positions.get(key)

    def _get_target_position(self, target: TargetType):
        return self._get_position(self.targets.get(target))

    def _match_target(self, target: TargetType):
        screen = self.d.screenshot(format="opencv")

        counter = 6
        while counter != 0:
            counter = counter - 1

            result = UIMatcher.match(screen, target)

            if result is None:
                break

            sx, sy = result
            ex, ey = self._get_target_position(target)

            self.d.swipe(sx, sy, ex, ey)
