import requests

from urllib.parse import urljoin

URL = 'https://pokeapi.co/api/v2/'
ENDPOINTS = [
    "ability",
    "berry",
    "berry-firmness",
    "berry-flavor",
    "characteristic",
    "contest-effect",
    "contest-type",
    "egg-group",
    "encounter-condition",
    "encounter-condition-value",
    "encounter-method",
    "evolution-chain",
    "evolution-trigger",
    "gender",
    "generation",
    "growth-rate",
    "item",
    "item-attribute",
    "item-category",
    "item-fling-effect",
    "item-pocket",
    "language",
    "location",
    "location-area",
    "machine",
    "move",
    "move-ailment",
    "move-battle-style",
    "move-category",
    "move-damage-class",
    "move-learn-method",
    "move-target",
    "nature",
    "pal-park-area",
    "pokeathlon-stat",
    "pokedex",
    "pokemon",
    "pokemon-color",
    "pokemon-form",
    "pokemon-habitat",
    "pokemon-shape",
    "pokemon-species",
    "region",
    "stat",
    "super-contest-effect",
    "type",
    "version",
    "version-group",
]

ATTACK_NAMES = ['bulbasaur', 'ivysaur', 'venusaur', 'charmander', 'charmeleon', 'charizard', 'squirtle', 'wartortle', 'blastoise', 'caterpie', 'metapod', 'butterfree', 'weedle', 'kakuna', 'beedrill', 'pidgey', 'pidgeotto', 'pidgeot', 'rattata', 'raticate', 'spearow', 'fearow', 'ekans', 'arbok', 'pikachu', 'raichu', 'sandshrew', 'sandslash', 'nidoran-f', 'nidorina', 'nidoqueen', 'nidoran-m', 'nidorino', 'nidoking', 'clefairy', 'clefable', 'vulpix', 'ninetales', 'jigglypuff', 'wigglytuff', 'zubat', 'golbat', 'oddish', 'gloom', 'vileplume', 'paras', 'parasect', 'venonat', 'venomoth', 'diglett', 'dugtrio', 'meowth', 'persian', 'psyduck', 'golduck', 'mankey', 'primeape', 'growlithe', 'arcanine', 'poliwag', 'poliwhirl', 'poliwrath', 'abra', 'kadabra', 'alakazam', 'machop', 'machoke', 'machamp', 'bellsprout', 'weepinbell', 'victreebel', 'tentacool', 'tentacruel', 'geodude', 'graveler', 'golem', 'ponyta', 'rapidash', 'slowpoke', 'slowbro', 'magnemite', 'magneton', 'farfetchd', 'doduo', 'dodrio', 'seel', 'dewgong', 'grimer', 'muk', 'shellder', 'cloyster', 'gastly', 'haunter', 'gengar', 'onix', 'drowzee', 'hypno', 'krabby', 'kingler', 'voltorb', 'electrode', 'exeggcute', 'exeggutor', 'cubone', 'marowak', 'hitmonlee', 'hitmonchan', 'lickitung', 'koffing', 'weezing', 'rhyhorn', 'rhydon', 'chansey', 'tangela', 'kangaskhan', 'horsea', 'seadra', 'goldeen', 'seaking', 'staryu', 'starmie', 'mr-mime', 'scyther', 'jynx', 'electabuzz', 'magmar', 'pinsir', 'tauros', 'magikarp', 'gyarados', 'lapras', 'ditto', 'eevee', 'vaporeon', 'jolteon', 'flareon', 'porygon', 'omanyte', 'omastar', 'kabuto', 'kabutops', 'aerodactyl', 'snorlax', 'articuno', 'zapdos', 'moltres', 'dratini', 'dragonair', 'dragonite', 'mewtwo', 'mew', 'chikorita', 'bayleef', 'meganium', 'cyndaquil', 'quilava', 'typhlosion', 'totodile', 'croconaw', 'feraligatr', 'sentret', 'furret', 'hoothoot', 'noctowl', 'ledyba', 'ledian', 'spinarak', 'ariados', 'crobat', 'chinchou', 'lanturn', 'pichu', 'cleffa', 'igglybuff', 'togepi', 'togetic', 'natu', 'xatu', 'mareep', 'flaaffy', 'ampharos', 'bellossom', 'marill', 'azumarill', 'sudowoodo', 'politoed', 'hoppip', 'skiploom', 'jumpluff', 'aipom', 'sunkern', 'sunflora', 'yanma', 'wooper', 'quagsire', 'espeon', 'umbreon', 'murkrow', 'slowking', 'misdreavus', 'unown', 'wobbuffet', 'girafarig', 'pineco', 'forretress', 'dunsparce', 'gligar', 'steelix', 'snubbull', 'granbull', 'qwilfish', 'scizor', 'shuckle', 'heracross', 'sneasel', 'teddiursa', 'ursaring', 'slugma', 'magcargo', 'swinub', 'piloswine', 'corsola', 'remoraid', 'octillery', 'delibird', 'mantine', 'skarmory', 'houndour', 'houndoom', 'kingdra', 'phanpy', 'donphan', 'porygon2', 'stantler', 'smeargle', 'tyrogue', 'hitmontop', 'smoochum', 'elekid', 'magby', 'miltank', 'blissey', 'raikou', 'entei', 'suicune', 'larvitar', 'pupitar', 'tyranitar', 'lugia', 'ho-oh', 'celebi', 'treecko', 'grovyle', 'sceptile', 'torchic', 'combusken', 'blaziken', 'mudkip', 'marshtomp', 'swampert', 'poochyena', 'mightyena', 'zigzagoon', 'linoone', 'wurmple', 'silcoon', 'beautifly', 'cascoon', 'dustox', 'lotad', 'lombre', 'ludicolo', 'seedot', 'nuzleaf', 'shiftry', 'taillow', 'swellow', 'wingull', 'pelipper', 'ralts', 'kirlia', 'gardevoir', 'surskit', 'masquerain', 'shroomish', 'breloom', 'slakoth', 'vigoroth', 'slaking', 'nincada', 'ninjask', 'shedinja', 'whismur', 'loudred', 'exploud', 'makuhita', 'hariyama', 'azurill', 'nosepass', 'skitty', 'delcatty', 'sableye', 'mawile', 'aron', 'lairon', 'aggron', 'meditite', 'medicham', 'electrike', 'manectric', 'plusle', 'minun', 'volbeat', 'illumise', 'roselia', 'gulpin', 'swalot', 'carvanha', 'sharpedo', 'wailmer', 'wailord', 'numel', 'camerupt', 'torkoal', 'spoink', 'grumpig', 'spinda', 'trapinch', 'vibrava', 'flygon', 'cacnea', 'cacturne', 'swablu', 'altaria', 'zangoose', 'seviper', 'lunatone', 'solrock', 'barboach', 'whiscash', 'corphish', 'crawdaunt', 'baltoy', 'claydol', 'lileep', 'cradily', 'anorith', 'armaldo', 'feebas', 'milotic', 'castform', 'kecleon', 'shuppet', 'banette', 'duskull', 'dusclops', 'tropius', 'chimecho', 'absol', 'wynaut', 'snorunt', 'glalie', 'spheal', 'sealeo', 'walrein', 'clamperl', 'huntail', 'gorebyss', 'relicanth', 'luvdisc', 'bagon', 'shelgon', 'salamence', 'beldum', 'metang', 'metagross', 'regirock', 'regice', 'registeel', 'latias', 'latios', 'kyogre', 'groudon', 'rayquaza', 'jirachi', 'deoxys-normal', 'turtwig', 'grotle', 'torterra', 'chimchar', 'monferno', 'infernape', 'piplup', 'prinplup', 'empoleon', 'starly', 'staravia', 'staraptor', 'bidoof', 'bibarel', 'kricketot', 'kricketune', 'shinx', 'luxio', 'luxray', 'budew', 'roserade', 'cranidos', 'rampardos', 'shieldon', 'bastiodon', 'burmy', 'wormadam-plant', 'mothim', 'combee', 'vespiquen', 'pachirisu', 'buizel', 'floatzel', 'cherubi', 'cherrim', 'shellos', 'gastrodon', 'ambipom', 'drifloon', 'drifblim', 'buneary', 'lopunny', 'mismagius', 'honchkrow', 'glameow', 'purugly', 'chingling', 'stunky', 'skuntank', 'bronzor', 'bronzong', 'bonsly', 'mime-jr', 'happiny', 'chatot', 'spiritomb', 'gible', 'gabite', 'garchomp', 'munchlax', 'riolu', 'lucario', 'hippopotas', 'hippowdon', 'skorupi', 'drapion', 'croagunk', 'toxicroak', 'carnivine', 'finneon', 'lumineon', 'mantyke', 'snover', 'abomasnow', 'weavile', 'magnezone', 'lickilicky', 'rhyperior', 'tangrowth', 'electivire', 'magmortar', 'togekiss', 'yanmega', 'leafeon', 'glaceon', 'gliscor', 'mamoswine', 'porygon-z', 'gallade', 'probopass', 'dusknoir', 'froslass', 'rotom', 'uxie', 'mesprit', 'azelf', 'dialga', 'palkia', 'heatran', 'regigigas', 'giratina-altered', 'cresselia', 'phione', 'manaphy', 'darkrai', 'shaymin-land', 'arceus', 'victini', 'snivy', 'servine', 'serperior', 'tepig', 'pignite', 'emboar', 'oshawott', 'dewott', 'samurott', 'patrat', 'watchog', 'lillipup', 'herdier', 'stoutland', 'purrloin', 'liepard', 'pansage', 'simisage', 'pansear', 'simisear', 'panpour', 'simipour', 'munna', 'musharna', 'pidove', 'tranquill', 'unfezant', 'blitzle', 'zebstrika', 'roggenrola', 'boldore', 'gigalith', 'woobat', 'swoobat', 'drilbur', 'excadrill', 'audino', 'timburr', 'gurdurr', 'conkeldurr', 'tympole', 'palpitoad', 'seismitoad', 'throh', 'sawk', 'sewaddle', 'swadloon', 'leavanny', 'venipede', 'whirlipede', 'scolipede', 'cottonee', 'whimsicott', 'petilil', 'lilligant', 'basculin-red-striped', 'sandile', 'krokorok', 'krookodile', 'darumaka', 'darmanitan-standard', 'maractus', 'dwebble', 'crustle', 'scraggy', 'scrafty', 'sigilyph', 'yamask', 'cofagrigus', 'tirtouga', 'carracosta', 'archen', 'archeops', 'trubbish', 'garbodor', 'zorua', 'zoroark', 'minccino', 'cinccino', 'gothita', 'gothorita', 'gothitelle', 'solosis', 'duosion', 'reuniclus', 'ducklett', 'swanna', 'vanillite', 'vanillish', 'vanilluxe', 'deerling', 'sawsbuck', 'emolga', 'karrablast', 'escavalier', 'foongus', 'amoonguss', 'frillish', 'jellicent', 'alomomola', 'joltik', 'galvantula', 'ferroseed', 'ferrothorn', 'klink', 'klang', 'klinklang', 'tynamo', 'eelektrik', 'eelektross', 'elgyem', 'beheeyem', 'litwick', 'lampent', 'chandelure', 'axew', 'fraxure', 'haxorus', 'cubchoo', 'beartic', 'cryogonal', 'shelmet', 'accelgor', 'stunfisk', 'mienfoo', 'mienshao', 'druddigon', 'golett', 'golurk', 'pawniard', 'bisharp', 'bouffalant', 'rufflet', 'braviary', 'vullaby', 'mandibuzz', 'heatmor', 'durant', 'deino', 'zweilous', 'hydreigon', 'larvesta', 'volcarona', 'cobalion', 'terrakion', 'virizion', 'tornadus-incarnate', 'thundurus-incarnate', 'reshiram', 'zekrom', 'landorus-incarnate', 'kyurem', 'keldeo-ordinary', 'meloetta-aria', 'genesect', 'chespin', 'quilladin', 'chesnaught', 'fennekin', 'braixen', 'delphox', 'froakie', 'frogadier', 'greninja', 'bunnelby', 'diggersby', 'fletchling', 'fletchinder', 'talonflame', 'scatterbug', 'spewpa', 'vivillon', 'litleo', 'pyroar', 'flabebe', 'floette', 'florges', 'skiddo', 'gogoat', 'pancham', 'pangoro', 'furfrou', 'espurr', 'meowstic-male', 'honedge', 'doublade', 'aegislash-shield', 'spritzee', 'aromatisse', 'swirlix', 'slurpuff', 'inkay', 'malamar', 'binacle', 'barbaracle', 'skrelp', 'dragalge', 'clauncher', 'clawitzer', 'helioptile', 'heliolisk', 'tyrunt', 'tyrantrum', 'amaura', 'aurorus', 'sylveon', 'hawlucha', 'dedenne', 'carbink', 'goomy', 'sliggoo', 'goodra', 'klefki', 'phantump', 'trevenant', 'pumpkaboo-average', 'gourgeist-average', 'bergmite', 'avalugg', 'noibat', 'noivern', 'xerneas', 'yveltal', 'zygarde', 'diancie', 'hoopa', 'volcanion', 'rowlet', 'dartrix', 'decidueye', 'litten', 'torracat', 'incineroar', 'popplio', 'brionne', 'primarina', 'pikipek', 'trumbeak', 'toucannon', 'yungoos', 'gumshoos', 'grubbin', 'charjabug', 'vikavolt', 'crabrawler', 'crabominable', 'oricorio-baile', 'cutiefly', 'ribombee', 'rockruff', 'lycanroc-midday', 'wishiwashi-solo', 'mareanie', 'toxapex', 'mudbray', 'mudsdale', 'dewpider', 'araquanid', 'fomantis', 'lurantis', 'morelull', 'shiinotic', 'salandit', 'salazzle', 'stufful', 'bewear', 'bounsweet', 'steenee', 'tsareena', 'comfey', 'oranguru', 'passimian', 'wimpod', 'golisopod', 'sandygast', 'palossand', 'pyukumuku', 'type-null', 'silvally', 'minior-red-meteor', 'komala', 'turtonator', 'togedemaru', 'mimikyu-disguised', 'bruxish', 'drampa', 'dhelmise', 'jangmo-o', 'hakamo-o', 'kommo-o', 'tapu-koko', 'tapu-lele', 'tapu-bulu', 'tapu-fini', 'cosmog', 'cosmoem', 'solgaleo', 'lunala', 'nihilego', 'buzzwole', 'pheromosa', 'xurkitree', 'celesteela', 'kartana', 'guzzlord', 'necrozma', 'magearna', 'marshadow', 'poipole', 'naganadel', 'stakataka', 'blacephalon', 'zeraora', 'meltan', 'melmetal', 'grookey', 'thwackey', 'rillaboom', 'scorbunny', 'raboot', 'cinderace', 'sobble', 'drizzile', 'inteleon', 'skwovet', 'greedent', 'rookidee', 'corvisquire', 'corviknight', 'blipbug', 'dottler', 'orbeetle', 'nickit', 'thievul', 'gossifleur', 'eldegoss', 'wooloo', 'dubwool', 'chewtle', 'drednaw', 'yamper', 'boltund', 'rolycoly', 'carkol', 'coalossal', 'applin', 'flapple', 'appletun', 'silicobra', 'sandaconda', 'cramorant', 'arrokuda', 'barraskewda', 'toxel', 'toxtricity-amped', 'sizzlipede', 'centiskorch', 'clobbopus', 'grapploct', 'sinistea', 'polteageist', 'hatenna', 'hattrem', 'hatterene', 'impidimp', 'morgrem', 'grimmsnarl', 'obstagoon', 'perrserker', 'cursola', 'sirfetchd', 'mr-rime', 'runerigus', 'milcery', 'alcremie', 'falinks', 'pincurchin', 'snom', 'frosmoth', 'stonjourner', 'eiscue-ice', 'indeedee-male', 'morpeko', 'cufant', 'copperajah', 'dracozolt', 'arctozolt', 'dracovish', 'arctovish', 'duraludon', 'dreepy', 'drakloak', 'dragapult', 'zacian-hero', 'zamazenta-hero', 'eternatus', 'kubfu', 'urshifu-single-strike', 'zarude', 'regieleki', 'regidrago', 'glastrier', 'spectrier', 'calyrex']
print(type(ATTACK_NAMES))
def get_requset_data():
    """
    Descryption:
        This function will get data from pokemon api 
    Output:
        Type: Dict
        
        Example:
            The output will contain URL values as values and keys as the URL detail name
            {'ability':'https://pokeapi.co/api/v2/ability/',.....}    
    """

    response = requests.get(url=URL)
    json_response = response.json()
    return json_response

def is_validate(validate_input):
    if validate_input in ENDPOINTS:
        return True
    else:
        return False

def get_ability():
    """ Get Abiluty of Pokemon
        
        Descryption:
            This function will get value of the ability key from the json response of
            get_request_data() function and again get the data from ability URL
        Output:
            Type: JSON

    """
    pass


def get_all_names_list(name):
    """
        Descryption:
            This function will get all the names of type you mention if the type is in endpoint
                Type: List
    """
    names_list = []
    if is_validate(name):
        name_url = urljoin(URL, name)

        response = requests.get(url=name_url)
        json_resone = response.json()
        for i in json_resone['results']:
            names_list.append(i['name'])

        return names_list
    else:
        return ValueError("{0} is not a Valid name".format(name))


def get_berry_details(berry_name):
    """This function will retutn berry details """
    berry_to_fetch = 'berry/' + berry_name
    berry_url = urljoin(URL,berry_to_fetch)
    berry_details = {}

    # First I need to get berry response call
    berry_response = requests.get(url=berry_url)

    # Return the response in the form of JSON format
    json_response = berry_response.json()
    # print(json_response)
    berry_attributes = []

    # json_response['flavors'] is a list of dicts with each dict has its name and
    # its APIresouce link of the individual flavir under 'url' key so we are removing
    # url key and adding all names as list to 'flavors'

    # json_response['flavors'] = [x['flavor'] for x in json_response['flavors']]
    # json_response['potenct'] = 

    for jr in json_response['flavors']:
        jr['flavor'] = jr['flavor']['name']

    # This will loop through the json_response and will check if the value type of a
    # is a dict or not. If it is a dict then then it will only take 'name' value of that
    # and assign it to that key attribute 
    # Example {'attr':{'name':'filiusfall','url':'filiusfall.github.io'}} will be converted
    # to {'attr':'filiusfall'}

    for j in json_response:
        if type(json_response[j]) == dict:
            json_response[j] = json_response[j]['name']
    return json_response


def get_all_flavors():
    """This function will get all the flavor names and its potencies as a dictionary
        Output:
            Type: Dict
            Example: {<flavor-name>:{'berries':<list-of-berries>},'contest_type':<type:str>,'id':<type:int>}
    """

    flavors_url = urljoin(URL,'berry-flavor')
    flavor_response = requests.get(url=flavors_url)

    flavor_json_response = flavor_response.json()

    flavors = {}
    for i in flavor_json_response['results']:


        flav_url = i['url']
        flav_url_response = requests.get(url=flav_url).json()

        flavors[i['name']] = {}
        flavors[i['name']]['berries'] = [j['berry']['name'] for j in flav_url_response['berries']]
        flavors['contest_type'] = flav_url_response['contest_type']['name']
        flavors['id'] = flav_url_response['id']
    
    return flavors


def get_firemness(firmness):
    """Get all firmness values and which berries have those firmness"""

    firmness_name = 'berry-firmness/' + firmness
    firmness_url = urljoin(URL, firmness_name)

    firmness_response = requests.get(url=firmness_url).json()
    
    firmness_output = {}

    firmness_output['name'] = firmness
    firmness_output['berries'] = [i['name'] for i in firmness_response['berries']]

    return firmness_output



def get_pokemo_details(poke_name):
    ...
    pokemon = 'pokemon/' + str(poke_name)
    poke_url = urljoin(URL,pokemon)
    poke_response = requests.get(url=poke_url).json()

    result = {
        'abilities' : [],
        'base_experience': poke_response['base_experience'],
        'height': poke_response['height'],
        'weight': poke_response['weight'],
        'forms' : [],
        'moves':[],
        'types':[],
        'stats' : {}

    }

    for i in poke_response['abilities']:
        result['abilities'].append(i['ability']['name'])
    
    for j in poke_response['moves']:
        result['moves'].append(j['move']['name'])

    for k in poke_response['types'] :
        result['types'].append(k['type']['name'])

    for l in poke_response['stats']:
        # print(l['stat']['name'])
        result['stats'][str(l['stat']['name'])] = l['base_stat']
    
    for m in poke_response['forms']:
        result['forms'].append(m['name'])


    return result

l = get_pokemo_details('pikachu')
# print(l['abilities'])


def get_pokemon_name():
    """This function will get list of all pokemon names """

def move_damages(move_name):

    moves = 'move/' + str(move_name)
    moves_url = urljoin(URL, moves)
    try:
        moves_response = requests.get(url=moves_url).json()
    except:
        raise(ValueError("Move entered is not in the database"))
        return None

    output = {
        'name':move_name, 
        'damage': moves_response['power'],
        "pp" : moves_response['pp']
    
    }

    return output

# print(move_damages('pound'))

# class Pokemon:
#     def __init__(self,name):
#         self.name = name
#         self._health = 100

class Pokemon:

    def __init__(self,name):
        self.pokemon_list = ['pikachu','bulbasaur']
        self.name = self.validate_name(name)
        self.health = 1000
        

    def attack(self,attack_name,defender_name):
        damage = self.damage_by_each_move(attack_name)
        print("damage given by {0} to {1} for {2}".format(self.name,defender_name.name,damage))
        try:
            def_damage = defender_name.damage_taken(damage)
        except:
            raise KeyError("check defender name")

    def damage_taken(self,damage):
        self.health -= damage
        print("{0}'s health = {1}".format(self.name,self.health))

    def validate_name(self,poke_name):
        print(poke_name)
        if poke_name not in self.pokemon_list:
            raise NameError("Pokemon not found!!!.Check the spelling of name once or try another pokemon")
            return False
        else:
            return poke_name
    
    def damage_by_each_move(self,move_name):

        poke_details = get_pokemo_details(self.name)
        damage = move_damages(move_name)['damage']

        return int(damage)

k = Pokemon('pikachu')
y = Pokemon('bulbasaur')
# print(y.name)
k.attack('pound', y)
# print(d)