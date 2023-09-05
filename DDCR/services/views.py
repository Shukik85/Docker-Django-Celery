from rest_framework.viewsets import ReadOnlyModelViewSet
from services.serializers import SubscriptionSerializer
from services.models import Subscription
from django.db.models import Prefetch, Sum
from clients.models import Client


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

        # aggregate
        response_data = {"result": response.data}
        response_data["total_amount"] = queryset.aggregate(total=Sum("price")).get(
            "total"
        )
        response.data = response_data
        # end aggregate

        return response
