### Description

To provide a Django style api and functionality for OpenSearch.

### Example

```python

from db_os.db import models


class Cars(models.OsModel):
    name = models.TextField()
    name.keyword = models.Keyword()
    price = models.FloatField(ignore_malformed=True)
    year = models.IntegerField()
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        index = 'cars'
        doc_type = 'car'
        settings = {
            "number_of_shards": 2,
        }

>>> Cars.create_index()
>>> new_car = Cars(name='Ferrari', price=1000000, year=2019, created_at='2019-01-01', updated_at='2019-01-01')
>>> new_car.save()
>>> new_car = Cars.models.filter(name='Ferrari').get()
>>> new_car.name
... 'Ferrari'
>>> new_car = Cars(name='Lamborghini', price='really expensive', year=2019, created_at='2019-01-01', updated_at='2019-01-01')
>>> new_car.save()
>>> new_car.price
... None # because of ignore_malformed=True
>>> new_car = Cars(name=150, price=1000000, year=2019, created_at='2019-01-01', updated_at='2019-01-01')
>>> new_car.save()
... ValidationError: {'name': 'Value is not a string'} # there is no ignore_malformed=True, so won't index
```
