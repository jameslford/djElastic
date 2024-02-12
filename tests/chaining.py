from .models import EsModel


class ExampleModel(EsModel):
    index_pattern = "example-*"


def test_script():
    exa = ExampleModel.objects.all().filter()
    print("hello")


if __name__ == "__main__":
    test_script()
