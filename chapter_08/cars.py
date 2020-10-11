# 8-14. Cars:
def make_car(manufacturer, model_name, **options):
    """Make a dictionary representing a car."""
    car_dict = {
        'manufacturer': manufacturer.title(),
        'model_name': model_name.title(),
    }
    for option, value in options.items():
        car_dict[option] = value

    return car_dict

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

tesla = make_car('tesla', 'model 3', year=2020, color='white',
        range='402 km')
print(tesla)