class BaseField:
    def __init__(self, ignore_malformed=False) -> None:
        self.ignore_malformed = ignore_malformed


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

    field_type = "alias"


class BinaryField(BaseField):
    """
    This will be a field that is a binary blob.
    """

    field_type = "binary"


class ByteField(BaseField):
    """
    This will be a field that is a byte.
    """

    field_type = "byte"


class DoubleField(BaseField):
    """
    This will be a field that is a double.
    """

    field_type = "double"


class FloatField(BaseField):
    """
    This will be a field that is a float.
    """

    field_type = "float"


class HalfFloatField(BaseField):
    """
    This will be a field that is a half float.
    """

    field_type = "half_float"


class IntegerField(BaseField):
    """
    This will be a field that is an integer.
    """

    field_type = "integer"


class LongField(BaseField):
    """
    This will be a field that is a long.
    """

    field_type = "long"


class UnsignedLongField(BaseField):
    """
    This will be a field that is an unsigned long.
    """

    field_type = "unsigned_long"


class ScaledFloatField(BaseField):
    """
    This will be a field that is a scaled float.
    """

    field_type = "scaled_float"


class ShortField(BaseField):
    """
    This will be a field that is a short.
    """

    field_type = "short"


class BooleanField(BaseField):
    """
    This will be a field that is a boolean.
    """

    field_type = "boolean"


class DateField(BaseField):
    """
    This will be a field that is a date.
    """

    field_type = "date"


class DateNanoField(BaseField):
    """
    This will be a field that is a date in nanoseconds.
    """

    field_type = "date_nanos"


class IpField(BaseField):
    """
    This will be a field that is an IP address.
    """

    field_type = "ip"


class IntegerRangeField(BaseField):
    """
    This will be a field that is an integer range.
    """

    field_type = "integer_range"


class LongRangeField(BaseField):
    """
    This will be a field that is a long range.
    """

    field_type = "long_range"


class FloatRangeField(BaseField):
    """
    This will be a field that is a float range.
    """

    field_type = "float_range"


class DoubleRangeField(BaseField):
    """
    This will be a field that is a double range.
    """

    field_type = "double_range"


class DateRangeField(BaseField):
    """
    This will be a field that is a date range.
    """

    field_type = "date_range"


class IpRangeField(BaseField):
    """
    This will be a field that is an IP range.
    """

    field_type = "ip_range"


class ObjectField(BaseField):
    """
    This will be a field that is a JSON object.
    """

    field_type = "object"


class NestedField(BaseField):
    """
    This will be a field that is a nested object.
    """

    field_type = "nested"


class FlatObjectField(BaseField):
    """
    This will be a field that is a flat object.
    """

    field_type = "flattened"


class JoinField(BaseField):
    """
    Establishes a parent-child relationship between documents in the same index.
    """

    field_type = "join"


class KeywordField(BaseField):
    """
    This will be a field that is a keyword. I.e., contains a string that is not analyzed.
    """

    field_type = "keyword"


class TextField(BaseField):
    """
    This will be a field that is a text. I.e., contains a string that is analyzed.
    """

    field_type = "text"


class MatchOnlyTextField(BaseField):
    """
    This will be a space-optimized version of a text field
    """

    field_type = "match_only_text"


class TokenCountField(BaseField):
    """
    This will be a field that is a token count.
    """

    field_type = "token_count"


class CompletionField(BaseField):
    """
    Provides autocomplete functionality through a completion suggester.
    """

    field_type = "completion"


class SearchAsYouTypeField(BaseField):
    """
    Provides search-as-you-type functionality using both prefix and infix completion.
    """

    field_type = "search_as_you_type"


class GeoPointField(BaseField):
    """
    This will be a field that is a geo point.
    """

    field_type = "geo_point"


class GeoShapeField(BaseField):
    """
    This will be a field that is a geo shape.
    """

    field_type = "geo_shape"


class RankFeatureField(BaseField):
    """
    This will be a field that is a rank feature.
    """

    field_type = "rank_feature"


class RankFeaturesField(BaseField):
    """
    This will be a field that is a rank features.
    """

    field_type = "rank_features"


class PercolatorField(BaseField):
    """
    This will be a field that is a percolator.
    """

    field_type = "percolator"


class KnnVectorField(BaseField):
    """
    This will be a field that is a KNN vector.
    """

    field_type = "knn_vector"
