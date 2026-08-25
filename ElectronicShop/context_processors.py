from Products.models import Categoriys, Cart, wishlist


def storefront(request):
    """Shared Digital Shop USA navigation/cart context for all templates."""
    context = {
        "cat": Categoriys.objects.all(),
        "count": 0,
        "count_wish": 0,
        "cat_prod": [],
        "total_amount": 0,
    }
    user = request.user
    if user.is_authenticated:
        carts = Cart.objects.filter(user=user)
        context["count"] = carts.count()
        context["cat_prod"] = carts[:2]
        context["count_wish"] = wishlist.objects.filter(user=user).count()
        amount = 0
        for item in carts:
            amount += item.quantity * item.products.Special_Price
        context["total_amount"] = amount + 100 if amount else 0
    return context
