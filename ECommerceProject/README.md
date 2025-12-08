# Tech Com Service and Repair - E-Commerce Platform

Professional e-commerce platform for selling computers and computer accessories.

## Quick Start

### 1. Install Dependencies
```bash
pip install djangorestframework django-js-asset Pillow django-ckeditor django-ckeditor-uploader
```

### 2. Run Migrations
```bash
cd ECommerceProject
python manage.py migrate
```

### 3. Load Sample Data
```bash
python manage.py load_sample_data
```

This will create:
- 6 Product Categories (Laptops, Desktops, Gaming PCs, etc.)
- 10 Sample Computer Products
- Sample Banners, Menus, and QR Codes

### 4. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 5. Run Server
```bash
python manage.py runserver
```

### 6. Access the Application
- **Customer Storefront:** http://127.0.0.1:8000/ECommerceFrontEnd/
- **Admin Dashboard:** http://127.0.0.1:8000/ECommerceBackEnd/
- **Django Admin:** http://127.0.0.1:8000/admin/
- **API Root:** http://127.0.0.1:8000/

## Adding Your Logo

### Option 1: Via Admin Panel
1. Go to http://127.0.0.1:8000/admin/
2. Navigate to **Images** → **Image Types**
3. Ensure "Logo" image type exists (ID: 6)
4. Go to **Images** → **Add Image**
5. Upload your logo image
6. Select **ImageTypeID = 6** (Logo)
7. Save

### Option 2: Via API
```bash
# Create ImageType for Logo (if not exists)
POST /imagetypes/
{
  "ImageTypeName": "Logo"
}

# Upload Logo Image
POST /images/
{
  "ImageName": "Tech Com Logo",
  "ImageTypeID": 6,
  "ImageURL": [upload file],
  "Active": "Yes"
}
```

### Option 3: Direct Database
You can also add the logo directly through the Django admin interface after creating a superuser.

**Note:** The logo should have a transparent background (PNG format recommended) for best results.

## Project Structure

- `ECommerceApp/` - Main application code
- `ECommerceProject/` - Project settings
- `media/images/` - Uploaded images
- `PROJECT_WORKFLOW.md` - Complete workflow documentation

## Color Scheme

- **Primary Color:** `#172488` (Deep Blue)
- **Primary Light:** `#2d3ba8`
- **Primary Dark:** `#0f1a6b`
- **Accent:** `#4a90e2`

## Features

✅ Product catalog with categories
✅ Shopping cart and checkout
✅ Order management
✅ Invoice generation
✅ Payment QR code integration
✅ Banner and slider management
✅ Responsive design
✅ REST API
✅ Admin dashboard

## Documentation

See `PROJECT_WORKFLOW.md` for complete documentation including:
- Database models and roles
- API endpoints
- User workflows
- Data flow diagrams

## Support

For issues or questions, refer to the workflow documentation or contact the development team.

