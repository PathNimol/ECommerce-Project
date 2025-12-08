"""
Management command to load sample computer products data
Usage: python manage.py load_sample_data
"""
from django.core.management.base import BaseCommand
from ECommerceApp.models import Category, Product, ProductDetail, TblBanner, ImageType, Image, Menu, MenuDetail, QRCode, Order, OrderItem, ProductDetailImage
from django.core.files.base import ContentFile
try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False


class Command(BaseCommand):
    help = 'Load sample computer products data for Tech Com Service and Repair'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Clearing existing data...'))
        
        # Delete all existing data
        OrderItem.objects.all().delete()
        Order.objects.all().delete()
        ProductDetailImage.objects.all().delete()
        ProductDetail.objects.all().delete()
        Product.objects.all().delete()
        Category.objects.all().delete()
        TblBanner.objects.all().delete()
        Image.objects.all().delete()
        MenuDetail.objects.all().delete()
        Menu.objects.all().delete()
        QRCode.objects.all().delete()
        
        self.stdout.write(self.style.SUCCESS('Existing data cleared.'))
        self.stdout.write(self.style.SUCCESS('Starting to load new sample data...'))

        # Create Categories
        categories_data = [
            {'name': 'Laptops', 'image': None},
            {'name': 'Desktops', 'image': None},
            {'name': 'Gaming PCs', 'image': None},
            {'name': 'Accessories', 'image': None},
            {'name': 'Components', 'image': None},
            {'name': 'Monitors', 'image': None},
        ]

        categories = {}
        for cat_data in categories_data:
            cat = Category.objects.create(
                categoryName=cat_data['name'],
                categoryImage=cat_data['image']
            )
            categories[cat_data['name']] = cat
            self.stdout.write(self.style.SUCCESS(f'Created category: {cat_data["name"]}'))

        # Create Products - 26 Computer Products
        products_data = [
            # Laptops
            {
                'name': 'ASUS ROG Strix G15 Gaming Laptop',
                'category': 'Laptops',
                'price': '1299.99',
                'weight': '2.3 kg',
                'availability': 'In Stock',
                'shipping': 'Free Shipping',
                'description': '<p>Powerful gaming laptop with RTX 3060, AMD Ryzen 7, 16GB RAM, 512GB SSD. Perfect for gaming and professional work.</p>',
                'image_url': 'https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=800&h=600&fit=crop'
            },
            {
                'name': 'Dell XPS 15 Professional Laptop',
                'category': 'Laptops',
                'price': '1899.99',
                'weight': '1.9 kg',
                'availability': 'In Stock',
                'shipping': 'Free Shipping',
                'description': '<p>Premium professional laptop with 4K display, Intel i7, 32GB RAM, 1TB SSD. Ideal for content creators.</p>',
                'image_url': 'https://images.unsplash.com/photo-1525547719571-a2d4ac8945e2?w=800&h=600&fit=crop'
            },
            {
                'name': 'MacBook Pro 16" M3 Max',
                'category': 'Laptops',
                'price': '3499.99',
                'weight': '2.1 kg',
                'availability': 'In Stock',
                'shipping': 'Free Shipping',
                'description': '<p>Apple MacBook Pro with M3 Max chip, 36GB RAM, 1TB SSD. Professional-grade performance.</p>',
                'image_url': 'https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=800&h=600&fit=crop'
            },
            {
                'name': 'HP Spectre x360 14" Convertible',
                'category': 'Laptops',
                'price': '1399.99',
                'weight': '1.4 kg',
                'availability': 'In Stock',
                'shipping': 'Free Shipping',
                'description': '<p>Ultra-slim 2-in-1 laptop with Intel i7, 16GB RAM, 1TB SSD, OLED touchscreen display.</p>',
                'image_url': 'https://images.unsplash.com/photo-1541807084-5c52b6b3adef?w=800&h=600&fit=crop'
            },
            {
                'name': 'Lenovo ThinkPad X1 Carbon',
                'category': 'Laptops',
                'price': '1599.99',
                'weight': '1.1 kg',
                'availability': 'In Stock',
                'shipping': 'Free Shipping',
                'description': '<p>Business laptop with Intel i7, 32GB RAM, 1TB SSD, 14" 4K display. Military-grade durability.</p>',
                'image_url': 'https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?w=800&h=600&fit=crop'
            },
            {
                'name': 'Acer Predator Helios 300',
                'category': 'Laptops',
                'price': '1199.99',
                'weight': '2.4 kg',
                'availability': 'In Stock',
                'shipping': 'Free Shipping',
                'description': '<p>Gaming laptop with RTX 4060, Intel i7, 16GB RAM, 512GB SSD, 144Hz display.</p>',
                'image_url': 'https://images.unsplash.com/photo-1603302576837-37561b2e2302?w=800&h=600&fit=crop'
            },
            # Desktops
            {
                'name': 'HP Pavilion Desktop PC',
                'category': 'Desktops',
                'price': '799.99',
                'weight': '8.5 kg',
                'availability': 'In Stock',
                'shipping': 'Free Shipping',
                'description': '<p>Reliable desktop PC with Intel i5, 16GB RAM, 512GB SSD, Windows 11. Great for home and office use.</p>',
                'image_url': 'https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=800&h=600&fit=crop'
            },
            {
                'name': 'Dell OptiPlex 7090 Business Desktop',
                'category': 'Desktops',
                'price': '999.99',
                'weight': '7.8 kg',
                'availability': 'In Stock',
                'shipping': 'Free Shipping',
                'description': '<p>Business desktop with Intel i7, 16GB RAM, 512GB SSD, Windows 11 Pro. Compact design.</p>',
                'image_url': 'https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=800&h=600&fit=crop'
            },
            {
                'name': 'Apple iMac 24" M3',
                'category': 'Desktops',
                'price': '1799.99',
                'weight': '4.5 kg',
                'availability': 'In Stock',
                'shipping': 'Free Shipping',
                'description': '<p>All-in-one desktop with M3 chip, 16GB RAM, 512GB SSD, 24" 4.5K Retina display.</p>',
                'image_url': 'https://images.unsplash.com/photo-1527482797697-8795b05a13fe?w=800&h=600&fit=crop'
            },
            # Gaming PCs
            {
                'name': 'Custom Gaming PC - RTX 4070',
                'category': 'Gaming PCs',
                'price': '2499.99',
                'weight': '15 kg',
                'availability': 'In Stock',
                'shipping': 'Free Shipping',
                'description': '<p>High-performance gaming PC with RTX 4070, Intel i7-13700K, 32GB DDR5, 1TB NVMe SSD. Ready for 4K gaming.</p>',
                'image_url': 'https://images.unsplash.com/photo-1587825140708-dfaf72ae4b04?w=800&h=600&fit=crop'
            },
            {
                'name': 'Alienware Aurora R15 Gaming Desktop',
                'category': 'Gaming PCs',
                'price': '2999.99',
                'weight': '18 kg',
                'availability': 'In Stock',
                'shipping': 'Free Shipping',
                'description': '<p>Premium gaming desktop with RTX 4080, Intel i9-13900KF, 32GB DDR5, 2TB NVMe SSD, liquid cooling.</p>',
                'image_url': 'https://images.unsplash.com/photo-1591488320449-011701bb6704?w=800&h=600&fit=crop'
            },
            {
                'name': 'Custom Gaming PC - RTX 4090',
                'category': 'Gaming PCs',
                'price': '3999.99',
                'weight': '16 kg',
                'availability': 'Limited Stock',
                'shipping': 'Free Shipping',
                'description': '<p>Ultimate gaming PC with RTX 4090, AMD Ryzen 9 7950X, 64GB DDR5, 2TB NVMe SSD, RGB lighting.</p>',
                'image_url': 'https://images.unsplash.com/photo-1555617981-dac3880eac6e?w=800&h=600&fit=crop'
            },
            # Accessories
            {
                'name': 'Mechanical Gaming Keyboard RGB',
                'category': 'Accessories',
                'price': '129.99',
                'weight': '0.8 kg',
                'availability': 'In Stock',
                'shipping': 'Free Shipping',
                'description': '<p>Premium mechanical keyboard with RGB backlighting, Cherry MX switches, and programmable keys.</p>',
                'image_url': 'https://images.unsplash.com/photo-1541140532154-b024d705b90a?w=800&h=600&fit=crop'
            },
            {
                'name': 'Logitech G Pro Wireless Mouse',
                'category': 'Accessories',
                'price': '149.99',
                'weight': '0.08 kg',
                'availability': 'In Stock',
                'shipping': 'Free Shipping',
                'description': '<p>Professional gaming mouse with HERO sensor, wireless connectivity, and 60-hour battery life.</p>',
                'image_url': 'https://images.unsplash.com/photo-1527814050087-3793815479db?w=800&h=600&fit=crop'
            },
            {
                'name': 'Razer DeathAdder V3 Pro',
                'category': 'Accessories',
                'price': '159.99',
                'weight': '0.063 kg',
                'availability': 'In Stock',
                'shipping': 'Free Shipping',
                'description': '<p>Ergonomic gaming mouse with Focus Pro 30K sensor, wireless, 90-hour battery life.</p>',
                'image_url': 'https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=800&h=600&fit=crop'
            },
            {
                'name': 'SteelSeries Arctis 7P+ Wireless Headset',
                'category': 'Accessories',
                'price': '199.99',
                'weight': '0.35 kg',
                'availability': 'In Stock',
                'shipping': 'Free Shipping',
                'description': '<p>Wireless gaming headset with 24-hour battery, 3D audio, and Discord-certified microphone.</p>',
                'image_url': 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=800&h=600&fit=crop'
            },
            {
                'name': 'Corsair K70 RGB TKL Keyboard',
                'category': 'Accessories',
                'price': '179.99',
                'weight': '0.7 kg',
                'availability': 'In Stock',
                'shipping': 'Free Shipping',
                'description': '<p>Tenkeyless mechanical keyboard with Cherry MX switches, per-key RGB lighting, aluminum frame.</p>',
                'image_url': 'https://images.unsplash.com/photo-1587825140708-dfaf72ae4b04?w=800&h=600&fit=crop'
            },
            # Components
            {
                'name': 'NVIDIA RTX 4080 Graphics Card',
                'category': 'Components',
                'price': '1199.99',
                'weight': '1.5 kg',
                'availability': 'Limited Stock',
                'shipping': 'Free Shipping',
                'description': '<p>High-end graphics card with 16GB GDDR6X, ray tracing, and DLSS 3.0 support.</p>',
                'image_url': 'https://images.unsplash.com/photo-1591488320449-011701bb6704?w=800&h=600&fit=crop'
            },
            {
                'name': 'Corsair 32GB DDR5 RAM Kit',
                'category': 'Components',
                'price': '199.99',
                'weight': '0.1 kg',
                'availability': 'In Stock',
                'shipping': 'Free Shipping',
                'description': '<p>High-speed DDR5 RAM kit, 6000MHz, optimized for gaming and content creation.</p>',
                'image_url': 'https://images.unsplash.com/photo-1587825140708-dfaf72ae4b04?w=800&h=600&fit=crop'
            },
            {
                'name': 'Samsung 980 PRO 2TB NVMe SSD',
                'category': 'Components',
                'price': '249.99',
                'weight': '0.01 kg',
                'availability': 'In Stock',
                'shipping': 'Free Shipping',
                'description': '<p>PCIe 4.0 NVMe SSD with read speeds up to 7,000 MB/s, perfect for gaming and professional work.</p>',
                'image_url': 'https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=800&h=600&fit=crop'
            },
            {
                'name': 'AMD Ryzen 9 7950X Processor',
                'category': 'Components',
                'price': '699.99',
                'weight': '0.05 kg',
                'availability': 'In Stock',
                'shipping': 'Free Shipping',
                'description': '<p>16-core, 32-thread processor with 5.7GHz boost clock, AM5 socket, unlocked for overclocking.</p>',
                'image_url': 'https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=800&h=600&fit=crop'
            },
            {
                'name': 'ASUS ROG Strix B650E-F Motherboard',
                'category': 'Components',
                'price': '299.99',
                'weight': '1.2 kg',
                'availability': 'In Stock',
                'shipping': 'Free Shipping',
                'description': '<p>AM5 motherboard with PCIe 5.0, DDR5 support, WiFi 6E, and comprehensive cooling solutions.</p>',
                'image_url': 'https://images.unsplash.com/photo-1555617981-dac3880eac6e?w=800&h=600&fit=crop'
            },
            {
                'name': 'Corsair RM1000x Power Supply',
                'category': 'Components',
                'price': '199.99',
                'weight': '1.8 kg',
                'availability': 'In Stock',
                'shipping': 'Free Shipping',
                'description': '<p>1000W 80 Plus Gold certified modular PSU, fully modular cables, quiet operation.</p>',
                'image_url': 'https://images.unsplash.com/photo-1527482797697-8795b05a13fe?w=800&h=600&fit=crop'
            },
            # Monitors
            {
                'name': 'Samsung 32" 4K Monitor',
                'category': 'Monitors',
                'price': '599.99',
                'weight': '6.2 kg',
                'availability': 'In Stock',
                'shipping': 'Free Shipping',
                'description': '<p>Ultra HD 4K monitor with HDR support, 144Hz refresh rate, and USB-C connectivity.</p>',
                'image_url': 'https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=800&h=600&fit=crop'
            },
            {
                'name': 'LG UltraGear 27" 1440p 240Hz',
                'category': 'Monitors',
                'price': '699.99',
                'weight': '5.8 kg',
                'availability': 'In Stock',
                'shipping': 'Free Shipping',
                'description': '<p>Gaming monitor with QHD resolution, 240Hz refresh rate, 1ms response time, G-Sync compatible.</p>',
                'image_url': 'https://images.unsplash.com/photo-1541807084-5c52b6b3adef?w=800&h=600&fit=crop'
            },
            {
                'name': 'ASUS ROG Swift 34" Ultrawide',
                'category': 'Monitors',
                'price': '1299.99',
                'weight': '8.5 kg',
                'availability': 'In Stock',
                'shipping': 'Free Shipping',
                'description': '<p>Ultrawide curved gaming monitor, 3440x1440, 180Hz, HDR600, G-Sync Ultimate.</p>',
                'image_url': 'https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?w=800&h=600&fit=crop'
            },
        ]

        for prod_data in products_data:
            category = categories.get(prod_data['category'])
            if category:
                # Download and save product image
                product_image = None
                if prod_data.get('image_url') and REQUESTS_AVAILABLE:
                    try:
                        response = requests.get(prod_data['image_url'], timeout=10)
                        if response.status_code == 200:
                            # Get file extension from URL or use jpg as default
                            ext = 'jpg'
                            if '.' in prod_data['image_url'].split('/')[-1]:
                                ext = prod_data['image_url'].split('.')[-1].split('?')[0]
                            
                            # Create a safe filename from product name
                            safe_name = "".join(c for c in prod_data['name'] if c.isalnum() or c in (' ', '-', '_')).rstrip()
                            safe_name = safe_name.replace(' ', '_')[:50]  # Limit length
                            filename = f'images/Products/{safe_name}.{ext}'
                            
                            # Save the image
                            product_image = ContentFile(response.content)
                            product_image.name = filename
                            self.stdout.write(self.style.SUCCESS(f'Downloaded image for: {prod_data["name"]}'))
                        else:
                            self.stdout.write(self.style.WARNING(f'Failed to download image for {prod_data["name"]}: HTTP {response.status_code}'))
                    except Exception as e:
                        self.stdout.write(self.style.WARNING(f'Error downloading image for {prod_data["name"]}: {str(e)}'))
                elif prod_data.get('image_url') and not REQUESTS_AVAILABLE:
                    self.stdout.write(self.style.WARNING(f'requests library not available. Install it with: pip install requests'))
                
                product = Product.objects.create(
                    productName=prod_data['name'],
                    categoryID=category,
                    price=prod_data['price'],
                    weight=prod_data['weight'],
                    availability=prod_data['availability'],
                    shipping=prod_data['shipping'],
                    productDescript=prod_data['description'],
                    productImage=product_image
                )
                self.stdout.write(self.style.SUCCESS(f'Created product: {prod_data["name"]}'))
                
                # Create product detail
                ProductDetail.objects.create(
                    productID=product,
                    productDetailName=f'{prod_data["name"]} - Full Specifications',
                    Description=prod_data['description'],
                    Information=f'<p><strong>Category:</strong> {prod_data["category"]}<br><strong>Weight:</strong> {prod_data["weight"]}<br><strong>Shipping:</strong> {prod_data["shipping"]}<br><strong>Availability:</strong> {prod_data["availability"]}</p>',
                    Reviews='<p>⭐⭐⭐⭐⭐ "Excellent product! Highly recommended." - Verified Customer<br>⭐⭐⭐⭐⭐ "Great quality and fast shipping!" - Happy Buyer<br>⭐⭐⭐⭐ "Good value for money." - Satisfied Customer</p>'
                )

        # Create Banners
        banners_data = [
            {'name': 'Summer Sale - Up to 30% Off'},
            {'name': 'New Gaming PCs Arrived'},
            {'name': 'Free Shipping on All Orders'},
        ]
        
        for banner_data in banners_data:
            TblBanner.objects.create(
                BannerName=banner_data['name']
            )
            self.stdout.write(self.style.SUCCESS(f'Created banner: {banner_data["name"]}'))

        # Create Image Types
        image_types = [
            'Banner',
            'Slider',
            'Sidebar Left',
            'Sidebar Right',
            'Footer',
            'Logo'
        ]
        
        for img_type_name in image_types:
            img_type = ImageType.objects.create(
                ImageTypeName=img_type_name
            )
            self.stdout.write(self.style.SUCCESS(f'Created image type: {img_type_name}'))

        # Create Menus
        menus_data = [
            {'name_kh': 'ទំព័រដើម', 'name_en': 'Home'},
            {'name_kh': 'ផលិតផល', 'name_en': 'Products'},
            {'name_kh': 'សេវាកម្ម', 'name_en': 'Services'},
            {'name_kh': 'អំពីយើង', 'name_en': 'About Us'},
            {'name_kh': 'ទំនាក់ទំនង', 'name_en': 'Contact'},
        ]
        
        for menu_data in menus_data:
            menu = Menu.objects.create(
                MenuNameEN=menu_data['name_en'],
                MenuNameKH=menu_data['name_kh']
            )
            self.stdout.write(self.style.SUCCESS(f'Created menu: {menu_data["name_en"]}'))
            
            # Create menu detail
            MenuDetail.objects.create(
                MenuID=menu,
                Description=f'<p>Information about {menu_data["name_en"]} section.</p>'
            )

        # Create QR Codes
        qr_codes = [
            {'name': 'ABA Bank QR Code'},
            {'name': 'Wing Bank QR Code'},
            {'name': 'ACLEDA Bank QR Code'},
        ]
        
        for qr_data in qr_codes:
            QRCode.objects.create(
                qrName=qr_data['name']
            )
            self.stdout.write(self.style.SUCCESS(f'Created QR code: {qr_data["name"]}'))

        self.stdout.write(self.style.SUCCESS(f'\n✅ Successfully loaded {len(products_data)} products!'))
        self.stdout.write(self.style.SUCCESS('✅ Sample data loaded successfully!'))
        self.stdout.write(self.style.WARNING('\nNote: You need to upload product images, banners, and QR codes through the admin panel or API.'))

