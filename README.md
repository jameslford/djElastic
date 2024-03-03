### Description

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
>>> car = Cars(name='Ferrari', price=1000000, year=2019, created_at='2019-01-01', updated_at='2019-01-01')
>>> car.save()
>>> car = Cars.models.filter(name='Ferrari').get()
>>> car.name
... 'Ferrari'

```
