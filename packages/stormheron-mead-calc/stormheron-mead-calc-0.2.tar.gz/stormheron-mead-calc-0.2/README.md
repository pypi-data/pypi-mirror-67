# Stormheron Mead-Calculator

## Installation
This package can be installed with pip: `pip install stormheron-mead-calc`

### Examples
Solve for ABV given Sugar and Final-Gravity
```python
from mead import Sugar, SugarType, Recipe

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
```

Solve for Sugar given ABV and Final-Gravity
```python
from mead import Sugar, SugarType, Recipe

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
                    abv_pct=0.87)

    results = recipe.calculate()

    print(results)
```

Solve for Final-Gravity given Sugar and ABV
```python
from mead import Sugar, SugarType, Recipe

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
                    abv_pct=0.87,
                    sugar_loads=[
                        Sugar(sugar_type=SugarType(name="Sugar", sugar_content=1.0), qty_lbs=30.34)
                    ])

    results = recipe.calculate()

    print(results)
```

### Updating the PyPi package
[Packaging Python Projects](https://packaging.python.org/tutorials/packaging-projects/)
1. make sure you have the latest versions of twine, setuptools, and wheel installed  
`pip install --upgrade setuptools twine wheel`
2. !!! Adjust the version in `setup.py` appropriately !!!
3. build the package by running this command from the same directory where `setup.py` is located  
`setup.py sdist bdist_wheel`
4. deploy the package by running this command from the same directory where `setup.py` is located
`twine upload --repository pypi dist/*`
    - this step requires a valid PyPi account