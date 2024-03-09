from dj_os.db import models


class CarModel(models.OsModel):

    make = models.TextField()
    make_keyword = models.KeywordField()
    year = models.IntegerField()

    class Meta:
        index_pattern = "car-*"

    def __str__(self):
        return self.name


def test_mapping():
    car = CarModel()
    print(car.render_mappings())
    print(car.render_settings())
    print(car.objects.all().filter())
