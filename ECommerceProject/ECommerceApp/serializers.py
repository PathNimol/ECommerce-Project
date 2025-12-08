from rest_framework import serializers
from .models import *
import json


class TblBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblBanner
        fields = '__all__'

class ImageTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageType
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        # Ensure ImageTypeID is always a number (not an object) for frontend compatibility
        if instance.ImageTypeID:
            data['ImageTypeID'] = instance.ImageTypeID.id if hasattr(instance.ImageTypeID, 'id') else instance.ImageTypeID
        # Ensure ImageURL is properly formatted as full URL
        if instance.ImageURL:
            request = self.context.get('request')
            if request:
                data['ImageURL'] = request.build_absolute_uri(instance.ImageURL.url)
            else:
                # Fallback: return relative URL starting with /media/
                url = instance.ImageURL.url
                if not url.startswith('/'):
                    url = '/' + url
                if not url.startswith('/media/'):
                    url = '/media' + url if url.startswith('/') else '/media/' + url
                data['ImageURL'] = url
        return data

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class MenuDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuDetail
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    categoryID = CategorySerializer(read_only=True)
    categoryID_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='categoryID', write_only=True)
    categoryName = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'
    
    def get_categoryName(self, obj):
        """Return category name for easy display"""
        if obj.categoryID:
            return obj.categoryID.categoryName
        return None
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        # Ensure productImage URL is properly formatted
        if instance.productImage:
            request = self.context.get('request')
            if request:
                data['productImage'] = request.build_absolute_uri(instance.productImage.url)
            else:
                data['productImage'] = instance.productImage.url
        # Ensure categoryID is returned as ID number (not object) for form compatibility
        if instance.categoryID:
            data['categoryID'] = instance.categoryID.id
        return data

class ProductDetailSerializer(serializers.ModelSerializer):
    productID = ProductSerializer(read_only=True)
    productID_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), source='productID', write_only=True)

    class Meta:
        model = ProductDetail
        fields = '__all__'

class ProductDetailImageSerializer(serializers.ModelSerializer):
    productID = ProductSerializer(read_only=True)
    productID_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), source='productID', write_only=True)

    class Meta:
        model = ProductDetailImage
        fields = '__all__'

class QRCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QRCode
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['productName', 'price', 'qty']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        # Get items from request data (sent as JSON string)
        request = self.context.get('request')
        items_data = []
        
        if request and hasattr(request, 'data'):
            items_str = request.data.get('items', '[]')
            if isinstance(items_str, str):
                items_data = json.loads(items_str)
            elif isinstance(items_str, list):
                items_data = items_str
        
        # Handle QR code upload
        qr_file = None
        if request and hasattr(request, 'FILES'):
            qr_file = request.FILES.get('QRCodeInvoice')
            if qr_file:
                validated_data['QRCodeInvoice'] = qr_file
        
        # Create order
        order = Order.objects.create(**validated_data)

        # Create order items
        for item in items_data:
            OrderItem.objects.create(
                order=order,
                productName=item.get('productName', ''),
                price=item.get('price', 0),
                qty=item.get('qty', 1)
            )

        return order