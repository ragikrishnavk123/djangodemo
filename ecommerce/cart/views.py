from django.shortcuts import render
from cart.models import Cart,Order,Account
from shop.models import Product
from django.http import HttpResponse
def cartview(request):
    total=0
    u=request.user
    try:
        cart=Cart.objects.filter(user=u)
        for i in cart:
             total+=i.quantity*i.product.price
    except:
        pass
    return render(request,'cartview.html',{'c':cart,'total':total})
def addtocart(request,n):
    p=Product.objects.get(name=n)
    u=request.user

    try:
        cart=Cart.objects.get(user=u,product=p)
        if(cart.quantity<cart.product.stock):

             cart.quantity+=1
             cart.save()

    except:
        if(p.stock > 0):
             cart=Cart.objects.create(product=p,user=u,quantity=1)
             cart.save()

    return cartview(request)
def cart_remove(request,n):
    p = Product.objects.get(name=n)
    u = request.user
    try:
        cart = Cart.objects.get(user=u, product=p)
        if (cart.quantity>1):
            cart.quantity -= 1
            cart.save()
        else:
            cart.delete()

    except:
        pass

    return cartview(request)
def full_remove(request,n):
    p = Product.objects.get(name=n)
    u = request.user
    try:
        cart = Cart.objects.get(user=u, product=p)
        cart.delete()

    except:
        pass
    return cartview(request)

def orderform(request):
    if(request.method=="POST"):
        a=request.POST['a']
        p=request.POST['p']
        n=request.POST['n']

        u=request.user
        cart=Cart.objects.filter(user=u)
        total=0
        for i in cart:
            total+=i.quantity*i.product.price

        try:
            ac=Account.objects.get(acctnum=n) #to retrieve accto object
            if(ac.amount >= total):
                ac.amount = ac.amount-total
                ac.save()
                for i in cart:
                    o=Order.object.create(user=u,product=i.product,address=a,phone=p,no_of_items=i.quantity,order_status="paid")
                    o.save()
                cart.delete()
                msg="You Order placed successfully"
                return render(request,'order_details.html',{'msg':msg})
            else:
                msg="Insufficient Amount. You can't placed Order"
                return render(request,'order_details.html',{'msg':msg})
        except:
            pass

    return render(request,'orderform.html')
