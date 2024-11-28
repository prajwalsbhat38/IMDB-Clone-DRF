from rest_framework import serializers
from .models import StreamingPlatform, WatchList, Reviews

class WatchList_Serializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = '__all__'

class StreamingPlatform_Serializer(serializers.ModelSerializer):
    class Meta:
        model = StreamingPlatform
        fields = '__all__'

class Review_Serializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only = True)
    class Meta:
        model = Reviews
        fields = '__all__'
    def save(self, **kwargs):
        request = self.context.get('request')
        kwargs['review_user'] = request.user
        watchlist = self.validated_data['watchlist']
        rating = self.validated_data['rating']
        watchlist.avg_rating = (watchlist.avg_rating * watchlist.number_of_rating + rating)/watchlist.number_of_rating + 1
        watchlist.number_of_rating += 1
        watchlist.save()
        return super().save(**kwargs)