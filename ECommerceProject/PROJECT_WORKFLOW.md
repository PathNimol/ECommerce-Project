# Tech Com Service and Repair - E-Commerce Project Workflow

## Project Overview

This is a professional e-commerce platform for selling computers and computer-related products, built with Django REST Framework and Bootstrap.

**Primary Color:** `#172488` (Deep Blue)
**Business:** Tech Com Service and Repair - Computer Store

---

## System Architecture

### Technology Stack

- **Backend:** Django 6.0 + Django REST Framework
- **Frontend:** Bootstrap 5.3 + Vanilla JavaScript
- **Database:** SQLite (development)
- **Rich Text Editor:** CKEditor with Uploader
- **Image Processing:** Pillow

---

## Project Structure

```
ECommerceProject/
├── ECommerceApp/              # Main application
│   ├── models.py             # Database models
│   ├── views.py              # API viewsets and template views
│   ├── serializers.py        # DRF serializers
│   ├── urls.py               # URL routing
│   ├── admin.py              # Django admin configuration
│   ├── management/
│   │   └── commands/
│   │       └── load_sample_data.py  # Sample data loader
│   └── templates/
│       └── ECommerceApp/
│           ├── ECommerceFrontEnd.html    # Customer-facing store
│           ├── ECommerceBackEnd.html     # Admin dashboard
│           └── ListProductWithAddToCartCheckoutOrder.html
├── ECommerceProject/         # Project settings
│   ├── settings.py          # Django settings
│   ├── urls.py              # Root URL configuration
│   └── wsgi.py              # WSGI configuration
└── media/                    # User-uploaded files
    └── images/              # Product images, banners, etc.
```

---

## Database Models & Roles

### 1. **Category Model**

**Purpose:** Organize products into categories

- `categoryName`: Name of the category (e.g., "Laptops", "Desktops")
- `categoryImage`: Category thumbnail image

**Role:** Product organization and navigation

---

### 2. **Product Model**

**Purpose:** Store product information

- `productName`: Product name
- `categoryID`: Foreign key to Category
- `price`: Product price
- `productDescript`: Rich text description
- `weight`: Product weight
- `availability`: Stock status
- `shipping`: Shipping information
- `productImage`: Product image
- `productDate`: Creation timestamp

**Role:** Core product data storage

---

### 3. **ProductDetail Model**

**Purpose:** Detailed product specifications

- `productID`: Foreign key to Product
- `productDetailName`: Detail section name
- `Description`: Full product description
- `Information`: Technical specifications
- `Reviews`: Customer reviews

**Role:** Extended product information display

---

### 4. **ProductDetailImage Model**

**Purpose:** Additional product images

- `productID`: Foreign key to Product
- `productDetailImageName`: Image name
- `productDetailImage`: Image file

**Role:** Product gallery management

---

### 5. **Order Model**

**Purpose:** Customer orders

- `customerName`: Customer name
- `customerPhone`: Contact phone
- `orderDate`: Order timestamp
- `totalAmount`: Total order value
- `QRCodeInvoice`: Payment QR code image

**Role:** Order management and tracking

---

### 6. **OrderItem Model**

**Purpose:** Individual items in an order

- `order`: Foreign key to Order
- `productName`: Product name (snapshot)
- `price`: Price at time of order
- `qty`: Quantity ordered

**Role:** Order line items tracking

---

### 7. **TblBanner Model**

**Purpose:** Homepage banners/promotions

- `BannerName`: Banner title
- `BannerImage`: Banner image
- `BannerDate`: Creation date

**Role:** Marketing and promotions display

---

### 8. **Image Model**

**Purpose:** Dynamic image management

- `ImageName`: Image name
- `ImageURL`: Image file
- `ImageLink`: Optional link URL
- `ImageTypeID`: Foreign key to ImageType
- `Active`: Status flag
- `ImageDate`: Creation date

**Role:** Flexible image content management

---

### 9. **ImageType Model**

**Purpose:** Categorize images by usage

- `ImageTypeName`: Type name (Logo, Banner, Sidebar, etc.)

**Image Types:**

- Type 1: Banner
- Type 2: Slider
- Type 3: Sidebar Left
- Type 4: Sidebar Right
- Type 5: Footer
- Type 6: Logo

**Role:** Image organization and placement

---

### 10. **Menu Model**

**Purpose:** Navigation menu items

- `MenuNameKH`: Khmer name
- `MenuNameEN`: English name
- `OrderBy`: Display order
- `CreatedDate`: Creation date

**Role:** Site navigation structure

---

### 11. **MenuDetail Model**

**Purpose:** Menu item descriptions

- `MenuID`: Foreign key to Menu
- `Description`: Rich text content
- `MenuDetailDate`: Creation date

**Role:** Menu content management

---

### 12. **QRCode Model**

**Purpose:** Payment QR codes

- `qrName`: QR code name (e.g., "ABA Bank")
- `qrImage`: QR code image

**Role:** Payment processing integration

---

## API Endpoints

### REST API (Django REST Framework)

All endpoints are available at: `http://127.0.0.1:8000/`

| Endpoint                       | Method    | Description               |
| ------------------------------ | --------- | ------------------------- |
| `/banners/`                    | GET, POST | Banner management         |
| `/imagetypes/`                 | GET, POST | Image type management     |
| `/images/`                     | GET, POST | Image management          |
| `/menus/`                      | GET, POST | Menu management           |
| `/menudetails/`                | GET, POST | Menu detail management    |
| `/categories/`                 | GET, POST | Category management       |
| `/products/`                   | GET, POST | Product listing           |
| `/products/?categoryID=X`      | GET       | Filter by category        |
| `/productdetails/`             | GET, POST | Product detail management |
| `/productdetails/?productID=X` | GET       | Filter by product         |
| `/productdetailimages/`        | GET, POST | Product image gallery     |
| `/qrcodes/`                    | GET, POST | QR code management        |
| `/orders/`                     | GET, POST | Order management          |

---

## Frontend Pages

### 1. **Customer Storefront**

**URL:** `http://127.0.0.1:8000/ECommerceFrontEnd/`

**Features:**

- Product browsing by category
- Product search and filtering
- Shopping cart
- Order placement
- Invoice generation
- Order history
- Banner carousel
- Product slider
- Menu navigation

**User Role:** Customer

---

### 2. **Admin Dashboard**

**URL:** `http://127.0.0.1:8000/ECommerceBackEnd/`

**Features:**

- CRUD operations for all models
- Statistics dashboard
- Order management
- Product management
- Banner management
- Image management
- Menu management

**User Role:** Administrator

---

### 3. **Product Listing with Cart**

**URL:** `http://127.0.0.1:8000/ListProductWithAddToCartCheckoutOrder/`

**Features:**

- Simplified product listing
- Shopping cart
- Checkout process

**User Role:** Customer

---

## System Workflow

### 👤 **Customer Journey**

The actual customer journey in this project follows this flow:

```
1. Homepage
   ↓
2. Product Listing Page
   ↓
3. Product Detail (Modal)
   ↓
4. Add to Cart → Cart Sidebar
   ↓
5. Checkout (Customer Info + QR Code)
   ↓
6. Place Order
   ↓
7. Invoice Display
   ↓
8. Order History
```

#### **Step-by-Step Customer Flow (Actual Implementation):**

1. **Homepage**

   - Customer lands on `/ECommerceFrontEnd/`
   - Views hero section with welcome message and call-to-action buttons
   - Sees Services section (Computer Sales, Repair, Support, E-Commerce Solutions)
   - Views Featured Promotions carousel (banners)
   - Sees Latest Products carousel
   - Can scroll down to product listing or click "Browse Products"

2. **Product Listing Page**

   - Main content area displays product grid (3 cards per row)
   - Left sidebar shows:
     - Category filter buttons
     - "All Products" button
     - Search by product name
     - Price filter (min/max)
     - Sidebar images
   - Right sidebar shows:
     - Shopping cart
     - Customer info form
     - QR code selection
     - Order history
   - Customer can filter by category, search, or filter by price
   - Clicks on product card or "Details" button to view product details

3. **Product Detail** (Modal Popup)

   - Modal opens showing complete product information
   - Displays product image, name, price
   - Shows weight, shipping, availability
   - Displays product description
   - Shows detailed specifications (if available)
   - Customer can click "Add to Cart" button

4. **Add to Cart**

   - Product added to shopping cart (stored in JavaScript array)
   - Cart sidebar updates automatically showing:
     - Product name, price, quantity
     - Increase/decrease quantity buttons
     - Remove item button
     - Cart total calculation
   - Cart count badge updates in header

5. **Checkout** (Right Sidebar)

   - Customer fills in:
     - Full Name (required)
     - Phone Number (required)
   - Selects payment QR code:
     - Dropdown with available QR codes
     - Or uploads custom QR code image
   - Reviews cart total
   - Clicks "Place Order" button

6. **Place Order**

   - Order data sent to `/orders/` API endpoint
   - Order created in database
   - OrderItems created for each cart item
   - Success modal appears
   - Cart cleared
   - Form reset

7. **Invoice Display**

   - Invoice section appears below checkout form
   - Shows order number, date, customer info
   - Lists all ordered items with quantities and prices
   - Displays total amount
   - Shows payment QR code (if provided)
   - Customer can view invoice details

8. **Order History**
   - Right sidebar shows list of all orders
   - Displays order date, customer name, total amount
   - Customer can click "View Invoice" to see order details
   - Invoice can be printed

---

### 👨‍💼 **Admin Journey**

The admin journey follows this flow:

```
1. Login
   ↓
2. Admin Dashboard
   ↓
3. [Access Management Modules]
```

#### **Step-by-Step Admin Flow:**

1. **Login**

   - Admin accesses `/ECommerceBackEnd/` directly (no separate login page)
   - Or accesses Django Admin at `/admin/` for superuser login
   - Authentication handled via Django sessions

2. **Admin Dashboard**

   - Views dashboard overview
   - Sees real-time statistics:
     - Total Products
     - Total Categories
     - Total Orders
     - Total Revenue
   - Views analytics charts:
     - Orders & Revenue Trend
     - Products By Category
     - New Orders vs Completed
     - Orders Per Week Day

3. **Admin Dashboard Modules** (Actual Implementation)

From the Admin Dashboard sidebar, admin can access the following management modules:

**Dashboard Section:**

- **Dashboard Overview** - View statistics and analytics charts

**Content Section:**

- **Banners CRUD** - Manage promotional banners (Featured Promotions carousel)
- **Images CRUD** - Upload and manage all website images (logos, sidebars, footer, etc.)
- **Menus CRUD** - Create and manage navigation menu items
- **Menu Details CRUD** - Add detailed content for menu items (rich text)
- **ImageType CRUD** - Manage image type categories

**E-Commerce Section:**

- **Category CRUD** - Create and manage product categories
- **Product CRUD** - Create, edit, and delete products
- **ProductDetail CRUD** - Add detailed product specifications
- **ProductDetailImage CRUD** - Upload multiple images for products
- **QRCode CRUD** - Manage payment QR codes
- **Order CRUD** - View and manage all customer orders
- **OrderItem CRUD** - View individual items within orders

**Preview Section:**

- **Carousel Preview** - Preview how banners appear in carousels
- **Menu & Detail Preview** - Preview menu navigation and content

#### **Admin Module Functions (Actual Implementation):**

**Dashboard Overview**

- View real-time business statistics
- Analyze sales trends with interactive charts
- Monitor product distribution
- Track order patterns

**Banners CRUD**

- Create promotional banners
- Upload banner images
- Manage banner display order
- Delete banners

**Images CRUD**

- Upload images for different sections
- Assign ImageTypeID (1-6):
  - Type 1: Banners
  - Type 2: Slider (Latest Products)
  - Type 3: Sidebar Left
  - Type 4: Sidebar Right
  - Type 5: Footer
  - Type 6: Logo (Header)
- Set active/inactive status
- Add image links

**Menus CRUD**

- Create navigation menu items
- Set menu names (English and Khmer)
- Set display order
- Manage menu structure

**Menu Details CRUD**

- Add rich text content for menus
- Link menu details to menu items
- Format content with CKEditor

**ImageType CRUD**

- Create image type categories
- Organize images by usage type
- Define where images appear

**Category CRUD**

- Create product categories
- Upload category images
- Edit category information
- Delete categories

**Product CRUD**

- Create new products
- Upload product images
- Set product prices
- Add rich text descriptions
- Set product availability
- Assign products to categories
- Edit product information
- Delete products

**ProductDetail CRUD**

- Add detailed product specifications
- Create product detail sections
- Add product descriptions
- Add product information
- Add product reviews
- Link details to products

**ProductDetailImage CRUD**

- Upload multiple images per product
- Create product image galleries
- Organize product photos
- Link images to products

**QRCode CRUD**

- Add payment QR codes
- Upload QR code images
- Name QR codes (e.g., "ABA Bank", "ACLEDA Bank")
- Manage QR codes for checkout

**Order CRUD**

- View all customer orders
- View order details
- See customer information (name, phone)
- View order date and total amount
- View payment QR code invoices
- Track order history

**OrderItem CRUD**

- View individual items in orders
- See product names, prices, quantities
- Track order line items
- View subtotals

**Carousel Preview**

- Preview banner carousel display
- Test carousel functionality
- See how banners rotate

**Menu & Detail Preview**

- Preview menu navigation
- Test menu content display
- See how menus appear to customers

---

### 🔧 **Developer Workflow**

1. **Setup**

   ```bash
   # Activate virtual environment
   cd ECommerceProject
   python manage.py migrate
   python manage.py createsuperuser
   ```

2. **Load Sample Data**

   ```bash
   python manage.py load_sample_data
   ```

3. **Run Development Server**

   ```bash
   python manage.py runserver
   ```

4. **Access Admin Panel**

   - Visit `http://127.0.0.1:8000/admin/`
   - Login with superuser credentials

5. **API Testing**
   - Visit `http://127.0.0.1:8000/` for API root
   - Use browser or Postman for API testing

---

## System Flow Diagram

### Customer Journey Flow

```
┌─────────────┐
│  Homepage   │
│ (Hero,      │
│ Services,   │
│ Banners,    │
│ Products)   │
└──────┬──────┘
       │
       ↓
┌─────────────────────┐
│ Product Listing Page │
│ (Grid + Sidebars)    │
└──────┬──────────────┘
       │
       ↓
┌─────────────────────┐
│  Product Detail      │
│    (Modal)           │
└──────┬───────────────┘
       │
       ↓
┌─────────────────────┐
│   Add to Cart        │
│  (Cart Sidebar)      │
└──────┬───────────────┘
       │
       ↓
┌─────────────────────┐
│   Checkout           │
│ (Customer Info +     │
│  QR Code Selection)  │
└──────┬───────────────┘
       │
       ↓
┌─────────────────────┐
│   Place Order        │
│  (API Call)          │
└──────┬───────────────┘
       │
       ↓
┌─────────────────────┐
│   Invoice Display    │
│  (Order Details)     │
└──────┬───────────────┘
       │
       ↓
┌─────────────────────┐
│   Order History      │
│  (Sidebar List)      │
└─────────────────────┘
```

### Admin Journey Flow

```
┌─────────┐
│  Login  │
│(Direct  │
│ Access) │
└────┬────┘
     │
     ↓
┌──────────────────┐
│ Admin Dashboard  │
│  (Overview)      │
└────┬─────────────┘
     │
     ├─────────────────────────────────────────────────────────────┐
     │                                                               │
     ↓                                                               ↓
┌─────────────────────────────────────────────────────────────────┐ │
│                    Management Modules                           │ │
│                                                                 │ │
│  ┌──────────────────────────────────────────────────────────┐  │ │
│  │              Dashboard Section                            │  │ │
│  │  ┌──────────────────┐                                    │  │ │
│  │  │Dashboard Overview │                                    │  │ │
│  │  └──────────────────┘                                    │  │ │
│  └──────────────────────────────────────────────────────────┘  │ │
│                                                                 │ │
│  ┌──────────────────────────────────────────────────────────┐  │ │
│  │              Content Section                              │  │ │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐   │  │ │
│  │  │Banners CRUD   │  │ Images CRUD  │  │ Menus CRUD   │   │  │ │
│  │  └──────────────┘  └──────────────┘  └──────────────┘   │  │ │
│  │  ┌──────────────┐  ┌──────────────┐                     │  │ │
│  │  │Menu Details   │  │ImageType CRUD│                     │  │ │
│  │  │CRUD           │  │              │                     │  │ │
│  │  └──────────────┘  └──────────────┘                     │  │ │
│  └──────────────────────────────────────────────────────────┘  │ │
│                                                                 │ │
│  ┌──────────────────────────────────────────────────────────┐  │ │
│  │            E-Commerce Section                             │  │ │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐   │  │ │
│  │  │Category CRUD │  │Product CRUD │  │ProductDetail │   │  │ │
│  │  └──────────────┘  └──────────────┘  │CRUD          │   │  │ │
│  │  ┌──────────────┐  ┌──────────────┐  └──────────────┘   │  │ │
│  │  │ProductDetail │  │QRCode CRUD  │  ┌──────────────┐   │  │ │
│  │  │Image CRUD    │  │             │  │Order CRUD    │   │  │ │
│  │  └──────────────┘  └──────────────┘  └──────────────┘   │  │ │
│  │  ┌──────────────┐                                      │  │ │
│  │  │OrderItem CRUD │                                      │  │ │
│  │  └──────────────┘                                      │  │ │
│  └──────────────────────────────────────────────────────────┘  │ │
│                                                                 │ │
│  ┌──────────────────────────────────────────────────────────┐  │ │
│  │              Preview Section                              │  │ │
│  │  ┌──────────────┐  ┌──────────────┐                      │  │ │
│  │  │Carousel       │  │Menu & Detail │                      │  │ │
│  │  │Preview        │  │Preview       │                      │  │ │
│  │  └──────────────┘  └──────────────┘                      │  │ │
│  └──────────────────────────────────────────────────────────┘  │ │
│                                                                 │ │
└─────────────────────────────────────────────────────────────────┘ │
                                                                   │
                                                                   └─ All modules accessible from Admin Dashboard Sidebar
```

## Data Flow

### Product Display Flow

```
Category → Product → ProductDetail → ProductDetailImage
     ↓
Frontend Display (Product Page → Product Detail)
```

### Order Processing Flow

```
Homepage → Product Page → Product Detail
     ↓
Add to Cart → Cart Page
     ↓
Place Order → checkout
     ↓
Fill customer information + Select QR code
     ↓
Order created → OrderItem records created
     ↓
Invoice generated → Order history updated
     ↓
Account Login Register
```

### Image Management Flow

```
Admin Dashboard → Images Module
     ↓
Upload image → Assign ImageType
     ↓
Image displayed based on ImageTypeID:
  - Type 1: Banners (Featured Promotions)
  - Type 2: Slider (Latest Products)
  - Type 3: Sidebar Left
  - Type 4: Sidebar Right
  - Type 5: Footer
  - Type 6: Logo (Header)
```

---

## Key Features

### ✅ **Implemented Features**

- Product catalog with categories
- Shopping cart functionality
- Order management system
- Invoice generation
- Payment QR code integration
- Banner and slider management
- Responsive design
- API-first architecture
- Admin dashboard
- Order history tracking
- Product search and filtering
- Rich text product descriptions

### 🎨 **Design Features**

- Professional color scheme (#172488)
- Modern UI with Bootstrap 5
- Font Awesome icons
- Smooth animations and transitions
- Responsive mobile design
- Professional product cards
- Clean admin interface

---

## File Upload Locations

All uploaded files are stored in `media/images/`:

- `media/images/Banners/` - Banner images
- `media/images/Categories/` - Category images
- `media/images/Products/` - Product images
- `media/images/Dynamic/` - Dynamic images (sliders, sidebars, etc.)
- `media/images/qrcodes/` - QR code images
- `media/images/QRCodeInvoice/` - Order payment QR codes

---

## Configuration

### Settings (settings.py)

- `MEDIA_URL = '/media/'`
- `MEDIA_ROOT = BASE_DIR / 'media'`
- `STATIC_URL = 'static/'`
- CKEditor configured for rich text editing

### Installed Apps

- `rest_framework` - API framework
- `ECommerceApp` - Main application
- `ckeditor` - Rich text editor
- `ckeditor_uploader` - Image upload for editor

---

## Security Notes

⚠️ **For Production:**

- Change `SECRET_KEY`
- Set `DEBUG = False`
- Configure `ALLOWED_HOSTS`
- Use PostgreSQL instead of SQLite
- Implement authentication/authorization
- Add CSRF protection
- Use HTTPS
- Implement rate limiting
- Add input validation

---

## Support & Contact

**Tech Com Service and Repair**

- Website: Your domain
- Phone: (855) 123-4567
- Email: info@techcom.com

---

## Version History

- **v1.0** - Initial release with full e-commerce functionality
- Professional styling with #172488 color scheme
- Computer product focus
- Complete admin dashboard
- API-first architecture

---

_Last Updated: December 2025_
