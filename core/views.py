from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, View
from django.shortcuts import redirect
from django.utils import timezone
from .forms import CheckoutForm, CouponForm, RefundForm
from .models import Item, OrderItem, Order, BillingAddress, Payment, Coupon, Refund, Category
from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
import random
import string
import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY



class PaymentView(View):
    def get(self, *args, **kwargs):
        # order
        order = Order.objects.get(user=self.request.user, ordered=False)
        if order.billing_address:
            context = {
                'order': order,
                'DISPLAY_COUPON_FORM': False
            }
            return render(self.request, "payment.html", context)
        else:
            messages.warning(
                self.request, "u have not added a billing address")
            return redirect("core:checkout")

    def post(self, *args, **kwargs):
        order = Order.objects.get(user=self.request.user, ordered=False)
        token = self.request.POST.get('stripeToken')
        amount = int(order.get_total() * 100)
        
        charge = stripe.Charge.create(
            amount=amount,  # cents
            currency="usd",
            source=token
        )
        # create the payment
        payment = Payment()
        payment.stripe_charge_id = charge['id']
        payment.user = self.request.user
        payment.amount = order.get_total()
        payment.save()

        # assign the payment to the order
        order.ordered = True
        order.payment = payment
        # TODO : assign ref code
        order.ref_code = create_ref_code()
        order.save()

        messages.success(self.request, "Order was successful")
        return redirect("/")


class HomeView(ListView):
    template_name = "index.html"
    queryset = Item.objects.filter(is_active=True)
    context_object_name = 'items'
