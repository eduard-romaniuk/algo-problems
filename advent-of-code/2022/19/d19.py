import math
import re
from enum import Enum
from functools import lru_cache


class Resource(Enum):
    ORE = 0
    CLAY = 1
    OBSIDIAN = 2
    GEODE = 3


class Blueprint:
    def __init__(self,
                 id: int,
                 ore_robot_ore: int,
                 clay_robot_ore: int,
                 obsidian_robot_ore: int,
                 obsidian_robot_clay: int,
                 geode_robot_ore: int,
                 geode_robot_obsidian: int):
        self.id = id
        self.recipes = {
            Resource.ORE: {
                Resource.ORE: ore_robot_ore
            },
            Resource.CLAY: {
                Resource.ORE: clay_robot_ore
            },
            Resource.OBSIDIAN: {
                Resource.ORE: obsidian_robot_ore,
                Resource.CLAY: obsidian_robot_clay
            },
            Resource.GEODE: {
                Resource.ORE: geode_robot_ore,
                Resource.OBSIDIAN: geode_robot_obsidian
            }
        }


def max_spend(blueprint: Blueprint) -> dict[Resource, int]:
    result = {
        Resource.ORE: 0,
        Resource.CLAY: 0,
        Resource.OBSIDIAN: 0
    }

    for robot_type, recipe in blueprint.recipes.items():
        if robot_type != Resource.ORE:
            for resource_type, count in recipe.items():
                result[resource_type] = max(result[resource_type], count)

    return result


FILENAME = 'input.txt'
NUM = re.compile(r'\d+')
BLUEPRINTS = [Blueprint(*tuple(map(int, NUM.findall(line)))) for line in open(FILENAME, 'r').read().split('\n')]


def dfs(blueprint: Blueprint, max_spend: dict[Resource, int],
        cache: dict, time: int, robots: dict[Resource, int],
        resources: dict[Resource, int]) -> int:
    if time == 0:
        return resources[Resource.GEODE]
    key = tuple([time, *robots.values(), *resources.values()])
    if key in cache:
        return cache[key]

    max_value = resources[Resource.GEODE] + robots[Resource.GEODE] * time

    for robot_type, recipe in blueprint.recipes.items():
        if robot_type != Resource.GEODE and robots[robot_type] >= max_spend[robot_type]:
            continue

        wait = 0
        for resource_type, needed_amount in recipe.items():
            if robots[resource_type] == 0:
                break
            wait = max(wait, math.ceil((needed_amount - resources[resource_type]) / robots[resource_type]))
        else:
            remaining_time = time - wait - 1
            if remaining_time <= 0:
                continue
            _robots = dict(robots)
            _resources = {}
            for resource_type in Resource:
                _resources[resource_type] = resources[resource_type] + robots[resource_type] * (wait + 1)
            for resource_type, needed_amount in recipe.items():
                _resources[resource_type] -= needed_amount
            _robots[robot_type] += 1
            for resource_type in Resource:
                if resource_type != Resource.GEODE:
                    _resources[resource_type] = min(_resources[resource_type],
                                                    max_spend[resource_type] * remaining_time)
            max_value = max(max_value, dfs(blueprint, max_spend, cache, remaining_time, _robots, _resources))

    cache[key] = max_value
    return max_value


time = 24
total = 0
for blueprint in BLUEPRINTS:
    robots = {r: 0 for r in Resource}
    robots[Resource.ORE] = 1
    resources = {r: 0 for r in Resource}
    geodes_produced = dfs(blueprint, max_spend(blueprint), {}, time, robots, resources)
    total += blueprint.id * geodes_produced

print('Task 1:', total)

time = 32
total = 1
for blueprint in BLUEPRINTS[:3]:
    robots = {r: 0 for r in Resource}
    robots[Resource.ORE] = 1
    resources = {r: 0 for r in Resource}
    geodes_produced = dfs(blueprint, max_spend(blueprint), {}, time, robots, resources)
    total *= geodes_produced

print('Task 2:', total)
