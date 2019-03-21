# Key item randomization data for open mode.

from . import items
from . import locations


class KeyItemLocation(locations.ItemLocation):
    """Class for randomizing which key item is gotten in different locations."""
    pass


# ********************************** Actual location classes.
class MariosBed(KeyItemLocation):
    area = locations.Area.MariosPad
    addresses = [0x1e620f]
    item = items.DryBonesFlag


class Croco1(KeyItemLocation):
    area = locations.Area.BanditsWay
    addresses = [0x1e94e1]
    item = items.RareFrogCoin


class RareFrogCoinReward(KeyItemLocation):
    area = locations.Area.MushroomKingdom
    addresses = [0x1e6610]
    item = items.CricketPie

    @staticmethod
    def can_access(inventory):
        # Rare frog coin is needed to access this location.
        return inventory.has_item(items.RareFrogCoin)


class RoseTownSign(KeyItemLocation):
    area = locations.Area.RoseTown
    addresses = [0x1e6226, 0x1e623d]
    item = items.GreaperFlag


class CricketJamChest(KeyItemLocation):
    area = locations.Area.KeroSewers
    addresses = [0x1e625b, 0x1e6266]
    item = items.CricketJam


class MelodyBaySong1(KeyItemLocation):
    area = locations.Area.TadpolePond
    addresses = [0x1e6280]
    item = items.AltoCard


class MelodyBaySong2(KeyItemLocation):
    area = locations.Area.TadpolePond
    addresses = [0x1e6295]
    item = items.AltoCard

    @staticmethod
    def can_access(inventory):
        # Songs must be played in order, and Bambino Bomb is needed to access this location (beat minecart minigame).
        return MelodyBaySong1.can_access(inventory) and locations.can_access_mines_back(inventory)


class MelodyBaySong3(KeyItemLocation):
    area = locations.Area.TadpolePond
    addresses = [0x1e62ac]
    item = items.AltoCard

    @staticmethod
    def can_access(inventory):
        # Songs must be played in order.
        return MelodyBaySong2.can_access(inventory)


class YosterIsleGoal(KeyItemLocation):
    area = locations.Area.YosterIsle
    addresses = [0x1e62c5]
    item = items.BigBooFlag


class Croco2(KeyItemLocation):
    area = locations.Area.MolevilleMines
    addresses = [0x1e95ae]
    item = items.BambinoBomb


class BoosterTowerAncestors(KeyItemLocation):
    area = locations.Area.BoosterTower
    addresses = [0x1e62df]
    item = items.ElderKey


class BoosterTowerCheckerboard(KeyItemLocation):
    area = locations.Area.BoosterTower
    addresses = [0x1e62fe]
    item = items.RoomKey


class SeasideTownKey(KeyItemLocation):
    area = locations.Area.SeasideTown
    addresses = [0x1e6312]
    item = items.ShedKey


class MonstroTownKey(KeyItemLocation):
    area = locations.Area.MonstroTown
    addresses = [0x1e6326]
    item = items.TempleKey


class Seed(KeyItemLocation):
    area = locations.Area.BeanValley
    addresses = [0x1e633a]
    item = items.Seed


class NimbusLandCastleKey(KeyItemLocation):
    area = locations.Area.NimbusLand
    addresses = [0x1e635a]
    item = items.CastleKey1


class Birdo(KeyItemLocation):
    area = locations.Area.NimbusLand
    addresses = [0x1e6378]
    item = items.CastleKey2

    @staticmethod
    def can_access(inventory):
        return locations.can_access_birdo(inventory)


class Fertilizer(KeyItemLocation):
    area = locations.Area.NimbusLand
    addresses = [0x1e63a1]
    item = items.Fertilizer

    @staticmethod
    def can_access(inventory):
        return locations.can_clear_nimbus_castle(inventory)


# ********************* Default lists for the world.

def get_default_key_item_locations(world):
    """Gets default key item locations.

    Args:
        world (randomizer.logic.main.GameWorld):

    Returns:
        list[ItemLocation]: List of default key item locations.

    """
    return [
        MariosBed(world),
        Croco1(world),
        RareFrogCoinReward(world),
        RoseTownSign(world),
        CricketJamChest(world),
        MelodyBaySong1(world),
        MelodyBaySong2(world),
        MelodyBaySong3(world),
        YosterIsleGoal(world),
        Croco2(world),
        BoosterTowerAncestors(world),
        BoosterTowerCheckerboard(world),
        SeasideTownKey(world),
        MonstroTownKey(world),
        Seed(world),
        NimbusLandCastleKey(world),
        Birdo(world),
        Fertilizer(world),
    ]
