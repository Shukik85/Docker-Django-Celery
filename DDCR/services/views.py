from rest_framework.viewsets import ReadOnlyModelViewSet
from services.serializers import SubscriptionSerializer
from services.models import Subscription
from django.db.models import Prefetch, Sum
from clients.models import Client
from django.conf import settings
from django.core.cache import cache #redis caches


# Create your views here.
class SubscriptionView(ReadOnlyModelViewSet):
    queryset = Subscription.objects.all().prefetch_related(
        "plan",
        Prefetch(
            "client",
            queryset=Client.objects.all()
            .select_related("user")
            .only("company_name", "user__email"),
        ),
    )
    serializer_class = SubscriptionSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        response = super().list(request, *args, **kwargs)

        price_cache = cache.get(settings.PRICE_CACHE_NAME)

        # aggregate
        if price_cache:
            total_price = price_cache
        else:
            total_price = queryset.aggregate(total=Sum("price")).get("total")
            cache.set(settings.PRICE_CACHE_NAME, total_price, 60 * 60) #caches timeout = 10 seconds
        response_data = {"result": response.data}
        response_data["total_amount"] = total_price
        response.data = response_data
        # end aggregate

        return response
