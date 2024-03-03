class BaseField:
    pass


class ForeignKey(BaseField):
    """
    This will be a foreign key from an OS record to a Django model.
    An example would be Company field in the OS record to the Company model in Django.
    It will be hard/impossible to enforce referential integrity, but it will be useful for
    python serialization and deserialization.
    """


class AliasField(BaseField):
    """
    This will be a field that is an alias of another field in the same record.
    """


class BinaryField(BaseField):
    """
    This will be a field that is a binary blob.
    """


class ByteField(BaseField):
    """
    This will be a field that is a byte.
    """


class DoubleField(BaseField):
    """
    This will be a field that is a double.
    """


class FloatField(BaseField):
    """
    This will be a field that is a float.
    """


class HalfFloatField(BaseField):
    """
    This will be a field that is a half float.
    """


class IntegerField(BaseField):
    """
    This will be a field that is an integer.
    """


class LongField(BaseField):
    """
    This will be a field that is a long.
    """


class UnsignedLongField(BaseField):
    """
    This will be a field that is an unsigned long.
    """


class ScaledFloatField(BaseField):
    """
    This will be a field that is a scaled float.
    """


class ShortField(BaseField):
    """
    This will be a field that is a short.
    """


class BooleanField(BaseField):
    """
    This will be a field that is a boolean.
    """


class DateField(BaseField):
    """
    This will be a field that is a date.
    """


class DateNanoField(BaseField):
    """
    This will be a field that is a date in nanoseconds.
    """


class IpField(BaseField):
    """
    This will be a field that is an IP address.
    """


class IntegerRangeField(BaseField):
    """
    This will be a field that is an integer range.
    """


class LongRangeField(BaseField):
    """
    This will be a field that is a long range.
    """


class FloatRangeField(BaseField):
    """
    This will be a field that is a float range.
    """


class DoubleRangeField(BaseField):
    """
    This will be a field that is a double range.
    """


class DateRangeField(BaseField):
    """
    This will be a field that is a date range.
    """


class IpRangeField(BaseField):
    """
    This will be a field that is an IP range.
    """


class ObjectField(BaseField):
    """
    This will be a field that is a JSON object.
    """


class NestedField(BaseField):
    """
    This will be a field that is a nested object.
    """


class FlatObjectField(BaseField):
    """
    This will be a field that is a flat object.
    """


class JoinField(BaseField):
    """
    Establishes a parent-child relationship between documents in the same index.
    """


class KeywordField(BaseField):
    """
    This will be a field that is a keyword. I.e., contains a string that is not analyzed.
    """


class TextField(BaseField):
    """
    This will be a field that is a text. I.e., contains a string that is analyzed.
    """


class MatchOnlyTextField(BaseField):
    """
    This will be a space-optimized version of a text field
    """


class TokenCountField(BaseField):
    """
    This will be a field that is a token count.
    """


class CompletionField(BaseField):
    """
    Provides autocomplete functionality through a completion suggester.
    """


class SearchAsYouTypeField(BaseField):
    """
    Provides search-as-you-type functionality using both prefix and infix completion.
    """


class GeoPointField(BaseField):
    """
    This will be a field that is a geo point.
    """


class GeoShapeField(BaseField):
    """
    This will be a field that is a geo shape.
    """


class RankFeatureField(BaseField):
    """
    This will be a field that is a rank feature.
    """


class RankFeaturesField(BaseField):
    """
    This will be a field that is a rank features.
    """


class PercolatorField(BaseField):
    """
    This will be a field that is a percolator.
    """


class KnnVectorField(BaseField):
    """
    This will be a field that is a KNN vector.
    """
