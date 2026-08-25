from django import template
from django.templatetags.static import static

register = template.Library()

# Digital Shop USA product image map — keeps DB media paths intact while
# serving a consistent new catalog visual system.
CATEGORY_IMAGES = {
    "Laptop": "assets/products/cat-laptop.webp",
    "Processor": "assets/products/cat-processor.webp",
    "Motherboard": "assets/products/cat-motherboard.webp",
    "RAM": "assets/products/cat-ram.webp",
    "HDD": "assets/products/cat-hdd.webp",
    "SSD": "assets/products/cat-ssd.webp",
    "Graphics Card": "assets/products/cat-gpu.webp",
    "Power Supply": "assets/products/cat-psu.webp",
    "Casing": "assets/products/cat-casing.webp",
    "CPU Cooler": "assets/products/cat-cooler.webp",
    "Keyboard": "assets/products/cat-keyboard.webp",
    "Mouse": "assets/products/cat-mouse.webp",
}

CATEGORY_BLURBS = {
    "Laptop": "Portable computers for work, study, and everyday computing.",
    "Processor": "Desktop CPUs that power responsive multi-core performance.",
    "Motherboard": "Foundational boards for stable builds and expandability.",
    "RAM": "Fast memory kits to keep applications running smoothly.",
    "HDD": "High-capacity hard drives for bulk storage and archives.",
    "SSD": "Solid-state storage for quicker boots and load times.",
    "Graphics Card": "Graphics hardware for gaming, creative work, and visuals.",
    "Power Supply": "Reliable PSUs to deliver clean, consistent power.",
    "Casing": "PC chassis designed for airflow, access, and clean builds.",
    "CPU Cooler": "Cooling solutions that help keep processors under control.",
    "Keyboard": "Keyboards for typing comfort and everyday control.",
    "Mouse": "Pointers built for accuracy, comfort, and daily use.",
}

# Optional per-product overrides (product id -> static path)
productImages = {}


@register.simple_tag
def product_image(product):
    """Return Digital Shop USA catalog image for a product instance."""
    if product is None:
        return static("assets/products/cat-laptop.webp")
    pid = getattr(product, "id", None)
    if pid in productImages:
        return static(productImages[pid])
    category = getattr(getattr(product, "Category", None), "Category_Name", None)
    path = CATEGORY_IMAGES.get(category, "assets/products/cat-laptop.webp")
    return static(path)


@register.simple_tag
def category_image(category):
    """Return Digital Shop USA image for a category instance or name."""
    name = category
    if hasattr(category, "Category_Name"):
        name = category.Category_Name
    path = CATEGORY_IMAGES.get(name, "assets/products/cat-laptop.webp")
    return static(path)


@register.simple_tag
def category_blurb(category):
    name = category
    if hasattr(category, "Category_Name"):
        name = category.Category_Name
    return CATEGORY_BLURBS.get(
        name, "Explore technology products selected for modern setups."
    )


@register.filter
def shop_price(value):
    """Format catalog prices for display without inventing currency conversion."""
    try:
        amount = float(value)
    except (TypeError, ValueError):
        return value
    return f"{amount:,.0f} ৳"
