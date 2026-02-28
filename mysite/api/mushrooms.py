from fastapi import APIRouter
import joblib
from mysite.database.schema import MushroomPredictSchema

mushroom_router = APIRouter(prefix='/Mushrooms')

scaler = joblib.load('mysite/ml_models/mush_scaler.pkl')
random_model = joblib.load('mysite/ml_models/mush_model.pkl')


@mushroom_router.post('/',  response_model=dict)
async def mushroom_predicted(mushroom: MushroomPredictSchema):
    mushroom_dict = mushroom.dict()

    new_cap_shape = mushroom_dict.pop('cap_shape')

    cap_shapes = ['c', 'f', 'k', 's', 'x']

    cap_shape1or_0 = [
        1 if new_cap_shape == n else 0
        for n in cap_shapes
    ]

    new_cap_surface = mushroom_dict.pop('cap_surface')

    cap_surfaces = ['g', 's', 'y']

    cap_surface1or_0 = [
        1 if new_cap_surface == n else 0
        for n in cap_surfaces
    ]

    new_cap_color = mushroom_dict.pop('cap_color')

    cap_color = ['c', 'e', 'g', 'n', 'p', 'r', 'u', 'w', 'y']

    cap_color1or_0 = [
        1 if new_cap_color == n else 0
        for n in cap_color
    ]

    new_bruises = mushroom_dict.pop('bruises')

    bruises1or_0 = [
        1 if new_bruises == 't' else 0]

    new_odor = mushroom_dict.pop('odor')

    odor = ['c', 'f', 'l', 'm', 'n', 'p', 's', 'y']

    odor1or_0 = [
        1 if new_odor == n else 0
        for n in odor
    ]

    new_gill_attachment = mushroom_dict.pop('gill_attachment')

    gill_attachment1or_0 = [1 if new_gill_attachment == 'f' else 0]

    new_gill_spacing = mushroom_dict.pop('gill_spacing')

    gill_spacing1or_0 = [1 if new_gill_spacing == 'w' else 0]

    new_gill_size = mushroom_dict.pop('gill_size')

    gill_size1or_0 = [1 if new_gill_size == 'n' else 0]

    new_gill_color = mushroom_dict.pop('gill_color')

    gill_color = ['e', 'g', 'h', 'k', 'n', 'o', 'p', 'r', 'u', 'w', 'y']

    gill_color1or_0 = [
        1 if new_gill_color == n else 0
        for n in gill_color
    ]

    new_stalk_shape = mushroom_dict.pop('stalk_shape')

    stalk_shape1or_0 = [1 if new_stalk_shape == 't' else 0]

    new_stalk_root = mushroom_dict.pop('stalk_root')

    stalk_root = ['c', 'e', 'r']

    stalk_root1or_0 = [
        1 if new_stalk_root == n else 0
        for n in stalk_root
    ]

    new_stalk_surface_above_ring = mushroom_dict.pop('stalk_surface_above_ring')

    stalk_surface_above_ring = ['k', 's', 'y']

    stalk_surface_above_ring1or_0 = [
        1 if new_stalk_surface_above_ring == n else 0
        for n in stalk_surface_above_ring
    ]

    new_stalk_surface_below_ring = mushroom_dict.pop('stalk_surface_below_ring')

    stalk_surface_below_ring = ['k', 's', 'y']

    stalk_surface_below_ring1or_0 = [
        1 if new_stalk_surface_below_ring == n else 0
        for n in stalk_surface_below_ring
    ]

    new_stalk_color_above_ring = mushroom_dict.pop('stalk_color_above_ring')

    stalk_color_above_ring = ['c', 'e', 'g', 'n', 'o', 'p', 'w', 'y']

    stalk_color_above_ring1or_0 = [
        1 if new_stalk_color_above_ring == n else 0
        for n in stalk_color_above_ring
    ]

    new_stalk_color_below_ring = mushroom_dict.pop('stalk_color_below_ring')

    stalk_color_below_ring = ['c', 'e', 'g', 'n', 'o', 'p', 'w', 'y']

    stalk_color_below_ring1or_0 = [
        1 if new_stalk_color_below_ring == n else 0
        for n in stalk_color_below_ring
    ]

    new_veil_color = mushroom_dict.pop('veil_color')

    veil_color = ['o', 'w', 'y']

    veil_color1or_0 = [
        1 if new_veil_color == n else 0
        for n in veil_color
    ]

    new_ring_number = mushroom_dict.pop('ring_number')

    ring_number = ['o', 't']

    ring_number1or_0 = [
        1 if new_ring_number == n else 0
        for n in ring_number
    ]

    new_ring_type = mushroom_dict.pop('ring_type')

    ring_type = ['f', 'l', 'n', 'p']

    ring_type1or_0 = [
        1 if new_ring_type == n else 0
        for n in ring_type
    ]

    new_spore_print_color = mushroom_dict.pop('spore_print_color')

    spore_print_color = ['h', 'k', 'n', 'o', 'r', 'u', 'w', 'y']

    spore_print_color1or_0 = [
        1 if new_spore_print_color == n else 0
        for n in spore_print_color
    ]

    new_population = mushroom_dict.pop('population')

    population = ['c', 'n', 's', 'v', 'y']

    population1or_0 = [
        1 if new_population == n else 0
        for n in population
    ]

    new_habitat = mushroom_dict.pop('habitat')

    habitat = ['g', 'l', 'm', 'p', 'u', 'w']

    habitat1or_0 = [
        1 if new_habitat == n else 0
        for n in habitat
    ]

    features = (
            cap_shape1or_0 + cap_surface1or_0 + cap_color1or_0 +
            bruises1or_0 + odor1or_0 + gill_attachment1or_0 + gill_spacing1or_0 +
            gill_size1or_0 + gill_color1or_0 + stalk_shape1or_0 + stalk_root1or_0 +
            stalk_surface_above_ring1or_0 + stalk_surface_below_ring1or_0 +
            stalk_color_above_ring1or_0 + stalk_color_below_ring1or_0 +
            veil_color1or_0 + ring_number1or_0 + ring_type1or_0 +
            spore_print_color1or_0 + population1or_0 + habitat1or_0
    )

    scaled_data = scaler.transform([features])
    mushroom = random_model.predict_proba(scaled_data)[0]
    probability = float(mushroom[1])
    if probability > 0.5:
        mushrooms_label = "Edible"
    else:
        mushrooms_label = "Poisonous"

    return {
        'poisonous': mushrooms_label
    }