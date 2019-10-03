from automator import Automator
from target import TargetType

if __name__ == '__main__':
    # 声明货物要移动到的建筑 ID 。
    targets = {
        # TargetType.Chair: 1,
        # TargetType.Box: 2,
        # TargetType.Dogfood: 2,
        # TargetType.Sofa: 3,
        # TargetType.Plant: 3,
        # TargetType.Microphone: 4,
        # TargetType.Shoes: 5,
        # TargetType.Chicken: 6,
        # TargetType.Bottle: 4,
        # TargetType.Vegetable: 5,
        # TargetType.Food: 8,
        # TargetType.Book: 5,
        # TargetType.Bag: 6,
        # TargetType.Wood: 7,
        # TargetType.Oil: 8,
        # # TargetType.Food: 8,
        # TargetType.Iron: 8,
        # TargetType.Grass:9,
        # TargetType.Tool: 8,
        # TargetType.Quilt: 9,
        TargetType.Chair: 1,
        TargetType.Wood: 9,
        TargetType.Bottle: 5,
        TargetType.Vegetable: 4,
        TargetType.Box: 2,
        TargetType.Food: 7,
        TargetType.Chicken: 6,
        TargetType.Iron: 8,
        TargetType.Sofa: 3
    }
    # 此处的设备换成你自己的
    instance = Automator('3204539b871a2181', targets)

    instance.start()
    # 如果火车不再送货，可以使用下面这个函数，仅仅收取金币。
    # instance.grabOnly()
