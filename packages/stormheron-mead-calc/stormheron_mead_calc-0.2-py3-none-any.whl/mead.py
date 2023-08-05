import attr
from typing import List
import json
import requests


@attr.s
class SugarType:
    sugar_content: float = attr.ib()
    name: str = attr.ib(default=None)

    @classmethod
    def sugar(cls):
        return cls(name='Sugar', sugar_content=1.0)

    @classmethod
    def honey(cls):
        return cls(name='Honey', sugar_content=0.796)


@attr.s
class Sugar:
    sugar_type: SugarType = attr.ib()
    qty_lbs: float = attr.ib()


def required(instance, attribute, value):
    if value is None:
        raise ValueError(f'{attribute.name} is required')


def check_solver(instance, attribute, value):
    if attribute.name == 'final_gravity_pct':
        if value is None and (instance.abv_pct is None or instance.sugar_loads is None):
            raise ValueError("If solving for 'final_gravity_pct', both 'abv_pct' and 'sugar_loads' are required")
    elif attribute.name == 'abv_pct':
        if value is None and (instance.final_gravity_pct is None or instance.sugar_loads is None):
            raise ValueError("If solving for 'abv_pct', both 'final_gravity_pct' and 'sugar_loads' are required")
    elif attribute.name == 'sugar_loads':
        if value is None and (instance.abv_pct is None or instance.final_gravity_pct is None):
            raise ValueError("If solving for 'sugar_loads', both 'abv_pct' and 'final_gravity_pct' are required")


@attr.s
class Recipe:
    # BASE INPUTS
    batch_volume_gal: float = attr.ib(validator=[required, attr.validators.instance_of((float, int))])
    yan_offset: float = attr.ib(validator=[required, attr.validators.instance_of((float, int))])
    yeast_gram_per_gal: float = attr.ib(validator=[required, attr.validators.instance_of((float, int))])
    sna_step_count: int = attr.ib(validator=[required, attr.validators.instance_of(int)])
    # Nutrition Need reference: HIGH = 1.25, MED = 0.9, LOW = 0.75, VERY_LOW = 0.50
    nutrition_need: float = attr.ib(validator=[required, attr.validators.instance_of((float, int))])
    yeast_abv_pct: float = attr.ib(validator=[required, attr.validators.instance_of((float, int))])

    # REGIMEN
    # Units: Density / Mass
    goferm_ppm_per_g: float = attr.ib(validator=[required, attr.validators.instance_of((float, int))])
    ferm_k_ppm_per_g: float = attr.ib(validator=[required, attr.validators.instance_of((float, int))])
    dap_ppm_per_g: float = attr.ib(validator=[required, attr.validators.instance_of((float, int))])
    ferm_o_ppm_per_g: float = attr.ib(validator=[required, attr.validators.instance_of((float, int))])
    # Units: Density
    goferm_max_gpl: float = attr.ib(validator=[required, attr.validators.instance_of((float, int))])
    ferm_k_max_gpl: float = attr.ib(validator=[required, attr.validators.instance_of((float, int))])
    dap_max_gpl: float = attr.ib(validator=[required, attr.validators.instance_of((float, int))])
    ferm_o_max_gpl: float = attr.ib(validator=[required, attr.validators.instance_of((float, int))])

    # SOLVE FOR INPUTS
    final_gravity_pct: float = attr.ib(default=None,
                                       validator=[check_solver, attr.validators.instance_of((float, int, type(None)))])
    abv_pct: float = attr.ib(default=None,
                             validator=[check_solver, attr.validators.instance_of((float, int, type(None)))])
    sugar_loads: List[Sugar] = attr.ib(default=None,
                                       validator=[check_solver, attr.validators.instance_of((list, type(None)))])

    def __attrs_post_init__(self):
        if self.final_gravity_pct is not None and self.abv_pct is not None and self.sugar_loads is not None:
            raise ValueError(
                "Inputs are over defined!  must solve for one of either; final_gravity_pct, abv_pct, or sugar_loads")

    def calculate(self):
        data = json.dumps(attr.asdict(self))

        response = requests.post('https://stormheron.com/api/v1/mead/calculate/recipe', data=data)

        return json.loads(json.loads(response.text)['results'])


if __name__ == '__main__':
    recipe = Recipe(batch_volume_gal=5,
                    yan_offset=0,
                    yeast_gram_per_gal=2,
                    sna_step_count=3,
                    nutrition_need=0.9,
                    yeast_abv_pct=30,
                    goferm_ppm_per_g=132,
                    ferm_k_ppm_per_g=177,
                    dap_ppm_per_g=210,
                    ferm_o_ppm_per_g=160,
                    goferm_max_gpl=1.32,
                    ferm_k_max_gpl=0.5,
                    dap_max_gpl=0.96,
                    ferm_o_max_gpl=2,
                    final_gravity_pct=1.05,
                    sugar_loads=[
                        Sugar(sugar_type=SugarType(name="Sugar", sugar_content=1.0), qty_lbs=30.34)
                    ])

    results = recipe.calculate()

    print(results)
