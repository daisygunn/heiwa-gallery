from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.views import View
from django.contrib import messages
from .models import Product, Category
from .forms import ProductForm, EditProductForm, StockForm


class AllProducts(View):
    """ A view to return the all_products page """
    def get(self, request):
        """ get request """
        category = None
        products = Product.objects.all().order_by('name')
        # make sure the correct label is showing
        # for stock level
        for product in products:
            product.change_stock_label()
        if 'category' in request.GET:
            # get the category id from url
            category = request.GET['category']
            # if the id is not in the category model
            if int(category) > len(Category.objects.all()) or 0:
                messages.error(request, "That category does exist.")
                return redirect(reverse('all_products'))
            # filter using this id
            products = products.filter(category=category).order_by('name')

        # paginate by 12 products
        paginator = Paginator(products, 12)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'products/all_products.html',
                      {'products': products,
                       'page_obj': page_obj})


class AddProduct(View):
    """ A view to return the all_products page """
    def get(self, request):
        """ get request """
        # if not superuser
        if not request.user.is_superuser:
            messages.error(request,
                           "You are not authorised to view that page.")
            return redirect(reverse('home'))
        else:
            # render empty product form
            add_product_form = ProductForm()
            return render(request, 'products/add_product.html',
                          {'add_product_form': add_product_form, })

    def post(self, request, *args, **kwargs):
        """ post view """
        # get data from POST request & the files
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            # save product
            product = form.save(commit=False)
            product.change_stock_label()
            product.save()
            messages.success(
                request, f"success, {product.name} has been added.")
            return redirect(
                reverse('all_products'), kwargs={'not_shopping': True})
        else:
            # if form is not valid
            messages.success(request, "Sorry, something is not right with"
                             " your form. Please check the information.")
            return redirect(
                reverse('add_product'), kwargs={'not_shopping': True})


class ProductManagement(View):
    """ A view to return the product_management page """
    def get(self, request):
        """ get request, returning all products """
        # IF NOT SUPERUSER
        if not request.user.is_superuser:
            messages.error(request,
                           "You are not authorised to view that page.")
            return redirect(reverse('home'))
        else:
            # get all products from database
            products = Product.objects.all()
            # make sure the correct label is showing
            # for stock level
            for product in products:
                product.change_stock_label()
            return render(request, 'products/product_management.html',
                          {'products': products, })


class EditProduct(View):
    """ A view to return the edit_product page """
    def get(self, request, pk):
        """ get request """
        # if not superuser redirect home
        if not request.user.is_superuser:
            messages.error(request,
                           "You are not authorised to view that page.")
            return redirect(reverse('home'))
        else:
            # get producut using pk
            product = get_object_or_404(Product, pk=pk)
            # fill product form using product instance
            edit_product_form = EditProductForm(instance=product)
            return render(request, 'products/edit_product.html',
                          {'edit_product_form': edit_product_form,
                           'product': product})

    def post(self, request, pk, *args, **kwargs):
        """ post view """
        product = get_object_or_404(Product, pk=pk)
        # get POST data to update product instance
        form = EditProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            # change stock label
            product.change_stock_label()
            messages.success(
                request, f"success, {product.name} has been updated.")
            # redirect back to product management
            return redirect(
                reverse('product_management'), kwargs={'not_shopping': True})
        else:
            # if form is not valid then redirect back to edit product page
            # with same information from post request
            form = EditProductForm(instance=product)
            messages.success(request, "Sorry, something is not right with"
                             " your form. Please check the information.")
            return redirect(
                reverse('edit_product'), kwargs={'not_shopping': True})


class DeleteProduct(View):
    """ A view to return the edit_product page """
    def get(self, request, pk):
        """ get request """
        # if not superuser redirect home
        if not request.user.is_superuser:
            messages.error(request,
                           "You are not authorised to view that page.")
            return redirect(reverse('home'))
        else:
            # get product to render on page
            product = get_object_or_404(Product, pk=pk)
            return render(request, 'products/delete_product.html',
                          {'product': product})

    def post(self, request, pk, *args, **kwargs):
        """ post view """
        product = get_object_or_404(Product, pk=pk)
        # delete product
        product.delete()
        messages.success(
            request, f"success, {product.name} has been deleted.")
        # redirect back to product management
        return redirect(
            reverse('product_management'), kwargs={'not_shopping': True})


class StockManagement(View):
    """ A view to return the stock page """
    def get(self, request, pk):
        """ get request """
        # if not superuser redirect back to home
        if not request.user.is_superuser:
            messages.error(
                request, "You are not authorised to view that page.")
            return redirect(reverse('home'))
        else:
            # get product to render on page
            product = get_object_or_404(Product, pk=pk)
            # fill form using product instance
            form = StockForm(instance=product)
            return render(request, 'products/stock.html',
                          {'product': product,
                           'form': form})

    def post(self, request, pk, *args, **kwargs):
        """ post view """
        product = get_object_or_404(Product, pk=pk)
        # get POST data
        form = StockForm(request.POST, instance=product)
        if form.is_valid():
            # if the form has changed
            if form.has_changed():
                # get POST data for quantity in stock
                updated_quantity_in_stock = int(
                    request.POST.get('quantity_in_stock'))
                form.save(commit=False)
                # update the quantity in stock in database
                product.quantity_in_stock = updated_quantity_in_stock
                # change stock label
                product.change_stock_label()
                form.save()
                messages.success(
                    request, f"success, {product.name} has been updated,\
                    there are now {product.quantity_in_stock} available.")
                # redirect back to product management
                return redirect(
                    reverse(
                        'product_management'), kwargs={'not_shopping': True})
            else:
                # if no changes were made redirect back to product management
                messages.warning(
                    request, f"You made no changes to {product.name}.")
                return redirect(
                    reverse(
                        'product_management'), kwargs={'not_shopping': True})
        else:
            # fill form using product instance
            form = StockForm(instance=product)
            messages.error(request, "Sorry, something went wrong, the stock"
                           " level has not been updated...")
        # redirect back to stock page using product pk
        return redirect(
            reverse('stock', args=[product.pk], kwargs={'not_shopping': True}))
