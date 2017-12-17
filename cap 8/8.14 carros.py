def car_info(fabricante, modelo, **car_add):
    info = {'fabricante': fabricante, 'modelo': modelo}
    for key, value in car_add.items():
        info[key] = value
    return info


car = car_info('subaru', 'outback', cor='preta', ano="2017")
for k, v in car.items():
    print("{} : {}".format(k, v))
