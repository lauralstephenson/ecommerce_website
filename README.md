This fake ecommerce website was set up using Bootstrap and the educational videos by Codemy and 100DaysofCode.

Photos are from Pixabay from Terranaut, Diversicat, keilasmile24, and Vinoth85.

I used Canva.com to make the artwork for this fake website.

Please do NOT attempt to buy anything from this webpage because the ebooks, templates, courses, and other content
are not real and are for educational purposes only. If you want to make the kaiju products shown here in real life
and sell them on your own website, do so! I'm sure people will love them!

Directly copying this website WILL NOT WORK. Django does NOT work that way. I strongly suggest watching Codemy's
exhaustive list of free YouTube videos on how to set up and use Django to create your own eCommmerce website.

I left my "secret code" in this website because it is not a real website. REMEMBER TO HIDE ALL SECRET KEYS, SUCH
AS LOGIN AND API KEYS, USING A CONFIG FILE OR OTHER METHOD.

I DID NOT set up actual payment functionality because this is not a real website.

How to set up Stripe:
Stripe Configuration:
Sign up for a Stripe account and get your API keys.
Install the stripe Python package (pip install stripe).
Configure your Stripe settings in your Django project.

Stripe Checkout:
Use Stripe Checkout for a low-code payment integration.
Create a view to create a checkout session using the Stripe API.
Return the checkout session ID in a JSON response.
Handle payment confirmation and success/failure URLs.

To integrate PayPal functionality into your Django e-commerce project, you have a few options:

Manual Integration:
You can manually integrate PayPal by following the official PayPal documentation. This involves setting up your PayPal
account, obtaining API credentials, and implementing the necessary views and templates in your Django project.
Create views for handling payment processing, including redirecting users to PayPal for payment and handling the
return URL after successful payment.

Use the PayPal API to create transactions, verify payments, and update order status.

Django Packages:
There are Django packages that simplify PayPal and Stripe integration:
django-paypal: This package provides an easy way to integrate PayPal payments.
dj-stripe: If you’re looking to integrate other payment gateways (like Stripe) alongside PayPal, consider using
dj-stripe. It supports multiple gateways and provides a unified interface for handling payments.

Third-Party Tutorials:
You can follow tutorials like the one on YouTube that demonstrate step-by-step integration of PayPal into a Django
e-commerce project.

These tutorials cover creating checkout pages, handling payments, and integrating with order management.
Remember to secure your API credentials and thoroughly test your payment flow before deploying it to production.

