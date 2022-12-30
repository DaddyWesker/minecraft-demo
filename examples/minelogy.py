import minecraft_data
log_names = []
planks_names = []
leaves_names = []
leaves_names_t = []
door_names_t = []
trapdoor_names_t = []
log_names_t = []
planks_names_t = []
drs = []
# versions = minecraft_data.common().protocolVersions
mcd = minecraft_data('1.18.1')  # here we must put current minecraft version
fuel_priority = {}
for item in mcd.items_list:
    iname = item['name']
    if 'log' in iname:
        log_names.append(iname)
        log_names_t.append({'type': iname})
        fuel_priority[iname] = 2
    elif 'planks' in iname:
        planks_names.append(iname)
        planks_names_t.append({'type': iname})
        fuel_priority[iname] = 1
    elif 'leaves' in iname:
        leaves_names.append(iname)
        leaves_names_t.append({'type': iname})
    elif '_door' in iname:
        door_names_t.append({'type': iname})
    elif 'trapdoor' in iname:
        trapdoor_names_t.append({'type': iname})
    elif 'sapling' in iname:
        fuel_priority[iname] = 0

fuel_priority['stick'] = 3
fuel_priority['coal'] = 4

mines = [({'blocks': [{'type': 'log'}],
           'tools': ['stone_axe', 'wooden_axe', None]},
          {'type': 'log'}
         ),
         ({'blocks': [{'type': 'grass'}, {'type': 'dirt'}],
           'tools': ['stone_shovel', 'wooden_shovel', None]},
          {'type': 'dirt'}
         ),
         ({'blocks': [{'type': 'sand'}],
           'tools': ['stone_shovel', 'wooden_shovel', None]},
          {'type': 'sand'}
         ),
         ({'blocks': [{'type': 'sand'}],
           'tools': ['stone_shovel', 'wooden_shovel', None]},
          {'type': 'sand'}
         ),
         ({'blocks': [{'type': 'clay'}],
           'tools': ['stone_shovel', 'wooden_shovel', None]},
          {'type': 'clay_ball'}
         ),
         ({'blocks': [{'type': 'gravel'}],
           'tools': [None]},
          {'type': 'gravel'}
         ),
         ({'blocks': [{'type': 'sandstone'}],
           'tools': ['iron_pickaxe', 'stone_pickaxe', 'wooden_pickaxe']},
          {'type': 'sandstone'}
         ),
         ({'blocks': [{'type': 'stone'}],
           'tools': ['iron_pickaxe', 'stone_pickaxe', 'wooden_pickaxe']},
          {'type': 'stone'}
         ),
         ({'blocks': [{'type': 'stone', 'variant': 'stone'}],
           'tools': ['iron_pickaxe', 'stone_pickaxe', 'wooden_pickaxe']},
          {'type': 'cobblestone'}
         ),
         ({'blocks': [{'type': 'cobblestone'}],
          'tools': ['iron_pickaxe', 'stone_pickaxe', 'wooden_pickaxe']},
         {'type': 'cobblestone'}
         ),
         ({'blocks': [{'type': 'coal_ore'}],
           'tools': ['iron_pickaxe', 'stone_pickaxe', 'wooden_pickaxe']},
          {'type': 'coal'}
         ),
        ({'blocks': [{'type': 'diamond_ore'}],
           'tools': ['iron_pickaxe']},
          {'type': 'diamond'}
         ),
        ({'blocks': [{'type': 'copper_ore'}],
           'tools': ['iron_pickaxe', 'stone_pickaxe']},
          {'type': 'raw_copper'}
         ),
         ({'blocks': [{'type': 'iron_ore'}],
           'tools': ['iron_pickaxe', 'stone_pickaxe']},
          {'type': 'raw_iron'}
         ),
         ({'blocks': [{'type': 'pumpkin'}],
           'tools': [None]},
          {'type': 'pumpkin'}
         ),
         ({'blocks': [{'type': 'leaves', 'variant': 'oak'}],
           'tools': [None]},
          {'type': 'apple'}
         ),
         ({'blocks': [{'type': 'leaves'}],
           'tools': [None]},
          {'type': 'sapling'}
         ),
         ({'blocks': [{'type': 'tallgrass'}],
           'tools': [None]},
          {'type': 'wheat_seeds'}
         ),
         ({'blocks': [{'type': 'deadbush'}],
          'tools': [None]},
         {'type': 'stick'}
         ),
         ({'blocks': [{'type': 'tallgrass'}],
           'tools': [None]},
          {'type': 'wheat_seeds'}
         ),
        ]
crafts = [([{'type': 'log', 'quantity': 1}],
           {'type': 'planks', 'quantity': 4}),
          ([{'type': 'planks', 'quantity': 2}],
            {'type': 'stick', 'quantity': 4}),
          ([{'type': 'stick', 'quantity': 2}, {'type': 'planks', 'quantity': 3}],
           {'type': 'wooden_axe'}),
          ([{'type': 'stick', 'quantity': 2}, {'type': 'planks', 'quantity': 3}],
           {'type': 'wooden_pickaxe'}),
          ([{'type': 'stick', 'quantity': 2}, {'type': 'planks', 'quantity': 1}],
           {'type': 'wooden_shovel'}),
          ([{'type': 'stick', 'quantity': 2}, {'type': 'cobblestone', 'quantity': 3}],
           {'type': 'stone_axe'}),
          ([{'type': 'stick', 'quantity': 2}, {'type': 'cobblestone', 'quantity': 3}],
           {'type': 'stone_pickaxe'}),
          ([{'type': 'stick', 'quantity': 2}, {'type': 'cobblestone', 'quantity': 1}],
           {'type': 'stone_shovel'}),
          ([{'type': 'raw_iron', 'quantity': 1}, {'type': 'furnace', 'quantity': 1}, {'type': 'fuel', 'quantity': 1}],
           {'type': 'iron_ingot'}),
          ([{'type': 'stick', 'quantity': 2}, {'type': 'iron_ingot', 'quantity': 3}],
           {'type': 'iron_axe'}),
          ([{'type': 'cobblestone', 'quantity': 8}],
           {'type': 'furnace'}),
          ([{'type': 'stick', 'quantity': 2}, {'type': 'iron_ingot', 'quantity': 3}],
           {'type': 'iron_pickaxe'}),
          ([{'type': 'stick', 'quantity': 2}, {'type': 'iron_ingot', 'quantity': 1}],
           {'type': 'iron_shovel'}),
          ([{'type': 'stick', 'quantity': 1}, {'type': 'coal', 'quantity': 1}],
           {'type': 'torch', 'quantity': 4}),
          ([{'type': 'planks', 'quantity': 2}],
            {'type': 'pressure_plate'}),
          ([{'type': 'planks', 'quantity': 3}],
            {'type': 'slab', 'quantity': 6}),
          ([{'type': 'planks', 'quantity': 1}],
            {'type': 'button'}),
          ([{'type': 'planks', 'variant': 'spruce', 'quantity': 6}],
            {'type': 'spruce_door', 'quantity': 3}),
          ([{'type': 'planks', 'variant': 'birch', 'quantity': 6}],
            {'type': 'birch_door', 'quantity': 3}),
          ([{'type': 'planks', 'variant': 'oak', 'quantity': 6}],
            {'type': 'wooden_door', 'quantity': 3}),
          ([{'type': 'planks', 'quantity': 6}],
            {'type': 'trapdoor', 'quantity': 2}),
          ([{'type': 'cobblestone', 'quantity': 3}],
            {'type': 'stone_slab', 'quantity': 6}),
          ([{'type': 'cobblestone', 'quantity': 3}],
            {'type': 'cobblestone_wall', 'quantity': 6}),
          ([{'type': 'stick', 'quantity': 1}, {'type': 'cobblestone', 'quantity': 1}],
           {'type': 'lever'}),
          ([{'type': 'pumpkin', 'quantity': 1}],
            {'type': 'pumpkin_seeds'}),
          ([{'type': 'sand', 'quantity': 1}, {'type': 'furnace', 'quantity': 1}, {'type': 'fuel', 'quantity': 1}],
            {'type': 'glass'}),
          ([{"type": "stick", "quantity": 4}, {"type": "planks", "quantity": 2}],
            {"type": "fence_gate", "quantity": 1}),
          ([{"type": "planks", "quantity": 6}, {"type": "stick", "quantity": 1}],
            {"type": "sign", "quantity": 3}),
          ([{"type": "planks", "quantity": 5}],
            {"type": "boat", "quantity": 1})
         ]

def get_otype(obj):
    t = None
    if 'type' in obj:
        t = obj['type']
    elif 'name' in obj:
        t = obj['name']
    return t

def get_oatargets(obj):
    # t = get_otype(obj)
    t = obj
    if t == 'log':
        return log_names_t + leaves_names_t
    if t == 'stone':
        return [{'type': 'dirt'}, {'type': 'grass'}]
    elif t == 'coal_ore' or t == 'iron_ore':
        return [{'type': 'stone'}]
    return []

def get_ovariant(obj):
    v = None
    if 'variant' in obj:
        v = obj['variant']
    elif 'variation' in obj:
        v = obj['variation']
    return v

def mimic_target(target, variants):
    res = []
    for var in variants:
        var_target = target.copy()
        var_target['type'] = var['type']
        res.append(var_target)
    return res

def get_target_variants(target):
    if target['type'] == "planks":
        res = []
        for p_name in planks_names:
            res.append({'type': p_name, 'quantity': target['quantity']})
        return res
    elif target['type'] == "door":
        return door_names_t
    elif target['type'] == "trapdoor":
        return trapdoor_names_t
    elif target['type'] == "log":
        return mimic_target(target, log_names_t)
    return target

def get_log_names():
    return log_names

def get_new_type(obj):
    splitted_obj = obj['type'].split("_")
    if len(splitted_obj) != 1:
        res = ''
        for splitted in splitted_obj[:-1]:
            res += splitted + "_"
        obj_type = res[:-1]
        return obj_type
    return None

def get_craft_variants(to_craft, target):
    if to_craft['type'] == "planks":
        target_type = get_new_type(target)
        res = []
        exact_res = []
        for p_name in planks_names:
            temp = {'type': p_name, 'quantity': to_craft['quantity']}
            craft_type = get_new_type(temp)
            res.append(temp)
            if craft_type == target_type:
                exact_res.append(temp)
                return exact_res
        return res
    elif to_craft['type'] == "door":
        return door_names_t
    elif to_craft['type'] == "trapdoor":
        return trapdoor_names_t
    elif to_craft['type'] == "log":
        target_type = get_new_type(target)
        for log_name in log_names_t:
            log_type = get_new_type(log_name)
            if target_type == log_type:
                return log_name
        return log_names_t
    return to_craft

def get_otlist(objs):
    return list(map(get_otype, objs))

def matchEntity(source, target):
    if source is None:
        return False
    source_type = get_otype(source) if isinstance(source, dict) else source
    target_type = get_otype(target) if isinstance(target, dict) else target
    if target_type == 'fuel' and source_type in fuel_priority:
        return True
    if (source_type != target_type) and (source_type != target_type.split("_")[-1]) and (target_type != source_type.split("_")[-1]):
        return False
    target_v = get_ovariant(target)
    if target_v is not None:
        if target_v != get_ovariant(source) and target_v[0] != '$':
            return False
    return True

def find_mine_by_block(block):
    for mine in mines:
        for b in mine[0]['blocks']:
            if matchEntity(b, block):
                return mine
    return None

def find_mines_by_result(entity):
    return list(filter(lambda mine: matchEntity(mine[1], entity), mines))

def find_crafts_by_result(entity):
    return list(filter(lambda craft: matchEntity(craft[1], entity), crafts))

def find_fuel(invent):
    return list(filter(lambda item: item is not None, list(findInInventory(invent, fl) for fl in fuel_priority)))

def select_minetool(invent, mine_entry):
    if mine_entry is None:
        return None
    result = None
    for tool in reversed(mine_entry[0]['tools']):
        for item in invent:
            if tool is None and (result is None or result['quantity'] < item['quantity']):
                result = item
            elif tool == item['type']:
                return item
    return result

def findInInventory(invent, target):
    for item in invent:
        if not matchEntity(item, target):
            continue
        if 'quantity' in target:
            if item['quantity'] < target['quantity']:
                continue
        return item
    return None

def isInInventory(invent, target):
    return findInInventory(invent, target) is not None

def lackCraftItems(invent, craft_entry):
    missing = []
    for item in craft_entry[0]:
        if not isInInventory(invent, item):
            missing += [item]
    return missing

def assoc_blocks(blocks):
    assoc = {'log': log_names+leaves_names,
             'coal_ore': ['stone'],
             'iron_ore': ['stone'],
             'diamond_ore': ['stone', 'iron_ore', 'coal_ore', 'copper_ore']}
    blocks2 = []
    for b in blocks:
        if b in assoc:
            blocks2 += assoc[b]
    return blocks2

def checkCraftType(to_craft, to_mine):
    craft_is_str = False
    if isinstance(to_craft, str):
        craft_is_str = True
        to_craft_dict = {"type" : to_craft}
    else:
        to_craft_dict = to_craft

    if isinstance(to_mine, str):
        to_mine = {"type" : to_mine}
    if (to_craft_dict['type'] == 'planks' or to_craft_dict['type'] == 'fence_gate' or to_craft_dict['type'] == 'sign'
        or to_craft_dict['type'] == "pressure_plate" or to_craft_dict['type'] == "button" or to_craft_dict['type'] == "boat"
        or to_craft_dict['type'] == "slab"):
        to_mine_type = get_otype(to_mine)
        to_craft_type = get_otype(to_craft_dict)

        if (to_mine_type in leaves_names) or (to_mine_type in log_names):
            if matchEntity(to_craft_dict, planks_names_t[0]):
                to_craft_type = get_new_type(to_mine) + "_" + to_craft_type
                if ('stripped' in to_mine_type):
                    to_craft_type = to_craft_type.split("stripped_")[1]
                if craft_is_str:
                    return to_craft_type
                else:
                    return {"type" : to_craft_type, "quantity": to_craft_dict['quantity']}
    return to_craft

def addFuel(to_craft, invent):
    if (to_craft == 'iron_ingot' or to_craft == 'glass'):
        fuels = find_fuel(invent)
        least_priority = 999
        least_prior_fuel = ''
        for fuel in fuels:
            cur_priority = fuel_priority[fuel['type']]
            if cur_priority < least_priority:
                least_priority = cur_priority
                least_prior_fuel = fuel['type']
        return f'{to_craft} {least_prior_fuel}'
    return to_craft
