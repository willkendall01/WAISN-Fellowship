
# Django libraries
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.core.mail import send_mail


# Necesary python files
from .models import Product
from .forms import CreateProductForm, UpdateProductForm, DeleteProductForm



# The function responsible for generating the home page of the site
def index(request):
    # The flags to handle possible errors
    #   If true an error occured
    CREATE_ERROR_FLAG = False
    UPDATE_ERROR_FLAG = False
    DELETE_ERROR_FLAG = False

    # The conditional to handle a POST request from the Create New Product from on the site
    if 'create' in request.POST:
        CREATE_ERROR_FLAG = create(request)

    # The conditional to handle a POST request from the Update Existing Product from on the site
    if 'update' in request.POST:
        UPDATE_ERROR_FLAG = update(request)

    # The conditional to handle a POST request from the Delete Existing Product from on the site
    if 'delete' in request.POST:
        DELETE_ERROR_FLAG = delete(request)

    # Generate an updated list of all the products
    product_list = Product.objects.order_by('product_name')

    # Assign the variables to reference in index.html
    context = {'product_list': product_list,
               'create_product_form': CreateProductForm,
               'update_product_form': UpdateProductForm,
               'delete_product_form': DeleteProductForm,
               'create_error_flag': CREATE_ERROR_FLAG,
               'update_error_flag': UPDATE_ERROR_FLAG,
               'delete_error_flag': DELETE_ERROR_FLAG,
               }
    
    #Attempt to fix unwarranted alert() bug
    CREATE_ERROR_FLAG = False
    UPDATE_ERROR_FLAG = False
    DELETE_ERROR_FLAG = False

    # Render the view
    return render(request, 'Database/index.html', context)



# The function that handles POST requests from the Create New Product form on the home page
#   With the POST request, it creates a product form containing the sent data
#   Given that data is valid in relation to the inventory (checked with is_valid()),
#       product quesntity is checked, and an email is sent if need be.
#   Returns True to the CREATE_ERROR_FLAG if error, otherwise returns False

def create(request):
    create_product_form = CreateProductForm(request.POST or None)

    #Ensures the submitted product does not exist already
    if create_product_form.is_valid():
        new_product_quantity = create_product_form.cleaned_data['product_quantity']

        #If the product quantity is 0 an alert is set to the configured email
        if new_product_quantity == 0:
            outOfStockAlert(
                create_product_form.cleaned_data['product_name'])
        
        #The new product is saved
        create_product_form.save()
        return False
    else:
        return True




# The function that handles POST requests from the Update Existing Product form on the home page
#   Given the POST request, it gets the product name and the product quantity
#   If a product with that name exists, its quantity is updated to the new product 
#          quantity and false is returned to the UPDATE_ERROR_FLAG
#   Else, true is returned to the UPDATE_ERROR_FLAG
def update(request):

    #Name and Quantity are extracted from the request
    product_name = request.POST.__getitem__('product_name')
    new_product_quantity = int(
        request.POST.__getitem__('product_quantity'))

    #If the product quantity is 0 an alert is set to the configured email
    if new_product_quantity == 0:
        outOfStockAlert(product_name)
    try:
        
        #If a product of the given name exists in the inventory, its new
        #   quantity is assigned and it is saved
        product = Product.objects.get(pk=product_name)
        product.product_quantity = new_product_quantity
        product.save()

        #No error so false is returned
        return False

    except ObjectDoesNotExist as e:
        #There is no object with a matching name, so an True is returned
        #   to signify an error
        return True



# The function that handles POST requests from the Delete Existing Product form on the home page
#   Given the POST request, it gets the product name
#   If a product with that name exists, it is deleted and false is returned to the DELETE_ERROR_FLAG
#   Else, true is returned to the DELETE_ERROR_FLAG
def delete(request):
    product_name = request.POST.__getitem__('product_name')
    try:
        product = Product.objects.get(pk=product_name)
        product.delete()

        #No error so false is returned
        print('no error')
        return False

    except ObjectDoesNotExist as e:
        #No object with a matchin name exists in the inventory so true is
        #   returned to signify an error
        return True



# Given the name of the product (str) that the store has run out of
#   Sends an email using the parameters subject, message, host_email, recipient_list
#   Subject: The subject of the email (str)
#   Message: The message contained in the email (str)
#   Host Email: The email from which the massage is sent (str) NOTE: This email must be configured in settings.py
#   Recipient List: The list of emails to which the messsage will be sent (str)
def outOfStockAlert(product_name):
    subject = 'Product Alert: ' + product_name
    message = 'This is an automated message' + ' from your inventory system' + \
        ' to notify you that ' + product_name + ' is out of stock.'
    host_email = "wpk235@gmail.com"
    recipient_list = ["wpk235@gmail.com"]

    send_mail(
        subject,
        message,
        host_email,
        recipient_list,
        fail_silently=True,
    )
