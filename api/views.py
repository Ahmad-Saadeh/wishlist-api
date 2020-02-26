from .serializers import UserCreateSerializer,ItemListSerializer,ItemDetailSerializer
from items.models import Item
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView
from api.permissions import IsStaffOrWhoAdded
from rest_framework.filters import OrderingFilter,SearchFilter
from rest_framework.permissions import AllowAny


class UserCreate(CreateAPIView):
    serializer_class = UserCreateSerializer



class ItemList(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['id','name']
    permission_classes = [AllowAny]



class ItemDetail(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'item_id'
    permission_classes = [IsStaffOrWhoAdded,]
