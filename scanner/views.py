import requests
from django.http import JsonResponse
from django.shortcuts import render
from .models import Product

def search_product(request):
    query = request.GET.get('query', '')  # Get barcode input
    product_data = None

    if query:
        try:
            product = Product.objects.get(barcode=query)
        except Product.DoesNotExist:
            # Fetch from OpenFoodFacts API
            api_url = f"https://world.openfoodfacts.org/api/v2/product/{query}.json"
            response = requests.get(api_url)

            if response.status_code == 200:
                data = response.json()
                if "product" in data:
                    product_data = data["product"]
                    
                    # Extract necessary fields
                    name = product_data.get("product_name", "Unknown Product")
                    eco_score = product_data.get("ecoscore_score", 0)
                    recyclability = product_data.get("categories", "Unknown")
                    alternative = "Consider eco-friendly alternatives"
                    image_url = product_data.get("image_url", "")  # Get image URL

                    # Save to database for future searches
                    product = Product.objects.create(
                        name=name,
                        barcode=query,
                        eco_score=eco_score,
                        recyclability=recyclability,
                        alternative=alternative
                    )
                    product.image_url = image_url  # Assign image URL to object

        # Format product details for JSON response
        if product:
            product_data = {
                "name": product.name,
                "eco_score": product.eco_score,
                "recyclability": product.recyclability,
                "alternative": product.alternative,
                "image_url": product.image_url if hasattr(product, 'image_url') else None
            }

    # If it's an AJAX request, return JSON data
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({"product": product_data})

    # Otherwise, render the normal HTML page
    return render(request, 'scanner/search.html', {"product": product_data})
