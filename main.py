from automator import Automator
from target import TargetType

if __name__ == '__main__':

    targets = {
        TargetType.Chair: 1,
        TargetType.Wood: 9,
        TargetType.Bottle: 5,
        TargetType.Vegetable: 4,
        TargetType.Box: 2,
        TargetType.Food: 7,
        TargetType.Chick: 6,
        TargetType.Rock: 8,
        TargetType.Sofa: 3
    }

    # cat your 'adb devices' here
    instance = Automator('3204539b871a2181', targets)

    instance.start()
