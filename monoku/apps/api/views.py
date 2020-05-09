from rest_framework.generics import ListAPIView


class RegionsCountry(ListAPIView):
    http_method_names = ('get', )

    # analyze csv file columns
    # import CSV file to database to use models
    # alternatively try 'pandas' or any other library
    # use those models for query data
    # generate json responses with serializers
    # don't use 'modelserializer' to improve performance
