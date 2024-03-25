from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import RequestFactory
from .models import Item, Order
from .views import CategoryView, CheckoutView, HomeView, OrderSummaryView, ShopView, ItemDetailView, add_to_cart, OrderItem, create_item, ItemForm, delete_item
from .models import Item, Order, Category
from django.contrib.messages.middleware import MessageMiddleware
from django.contrib.sessions.middleware import SessionMiddleware


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.category = Category.objects.create(title='Test Category', slug='test-category', description='Test description', image='test.jpg', is_active=True)
        self.item = Item.objects.create(
            title='Test Item',
            price=10.0,
            category=self.category,
            slug='test-item',  # Ensure the slug is provided
            description_short='Short description',
            description_long='Long description',
            stock_no='ABC123',
            image='path/to/image.jpg',
        )
        self.order = Order.objects.create(user=self.user, ordered=False)

    def test_order_summary_view(self):
        request = self.factory.get(reverse('core:order-summary'))
        request.user = self.user
        view = OrderSummaryView()
        view.setup(request)
        response = view.get(request)
        self.assertEqual(response.status_code, 200)  # Assuming the user will be redirected if no order exists

    def test_checkout_view_get(self):
        response = self.client.get(reverse('core:checkout'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout.html')

    def test_checkout_view_post(self):
        request = self.factory.post(reverse('core:checkout'), {'street_address': '123 Street', 'apartment_address': '', 'country': 'US', 'zip': '12345', 'payment_option': 'S'})
        request.user = self.user
        view = CheckoutView()
        view.setup(request)
        response = view.post(request)
        self.assertEqual(response.status_code, 302)  # Assuming the user will be redirected after successful checkout

    def test_home_view(self):
        request = self.factory.get(reverse('core:home'))
        response = HomeView.as_view()(request)
        self.assertEqual(response.status_code, 200)
    
    def test_shop_view(self):
        request = RequestFactory().get(reverse('core:shop'))
        response = ShopView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_item_detail_view(self):
        request = RequestFactory().get(reverse('core:product', kwargs={'slug': self.item.slug}))
        response = ItemDetailView.as_view()(request, slug=self.item.slug)
        self.assertEqual(response.status_code, 200)

    def test_category_view(self):
        url = reverse('core:category', kwargs={'slug': self.category.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category.html')

    def test_add_to_cart(self):
        request = self.factory.get(reverse('core:add-to-cart', kwargs={'slug': self.item.slug}))
        request.user = self.user
        
        # Annotate the request object with session middleware
        session_middleware = SessionMiddleware(lambda x: None) 
        session_middleware.process_request(request)
        request.session.save()
        
        # Annotate the request object with messages middleware
        message_middleware = MessageMiddleware(lambda x: None) 
        message_middleware.process_request(request)
        request.session.save()

        response = add_to_cart(request, self.item.slug)
        
        self.assertEqual(response.status_code, 302)  # Redirect to order summary page
        
        # Check if order item is created
        order_item = OrderItem.objects.filter(item=self.item, user=self.user, ordered=False).first()
        self.assertIsNotNone(order_item)
        
        # Check if the item is added to the order
        order = Order.objects.filter(user=self.user, ordered=False).first()
        self.assertIsNotNone(order)
        self.assertTrue(order.items.filter(item=self.item).exists())

        

    def test_create_item_get(self):
        request = self.factory.get(reverse('core:create_item'))
        request.user = self.user
        response = create_item(request)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context_data['form'], ItemForm)

    def test_delete_item(self):
        # Create a POST request to delete the item
        request = self.factory.post(reverse('core:delete_item'), {'item_id': self.item.id})
        request.user = self.user

        # Call the delete_item view
        response = delete_item(request)

        # Check if the item is deleted successfully
        self.assertEqual(response.status_code, 302)  # Check if redirected
        self.assertFalse(Item.objects.filter(id=self.item.id).exists())

    def tearDown(self):
        self.client.logout()


