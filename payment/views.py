import stripe
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from basket.basket import Basket


@login_required()
def BasketView(request):
    basket = Basket(request)
    total = str(basket.get_total_price())
    total = total.replace('.', '')
    total = int(total)
    stripe.api_key = 'pk_test_51J7GxpCNwARdG6DH8Sd1SF3uaKp1C3Ti9bJ5cbjVb9Fw5Wp08UVvJns6ab0jq778w3AjnbNReCthx6KjCK2TNq7H00NeUoDDXw'
    intent = stripe.PaymentIntent.create(
        amount=total,
        currency='gbr',
        metadata={'userid': request.user.id}
    )
    return render(request, 'payment/home.html')