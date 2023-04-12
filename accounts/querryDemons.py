customers=customer.objects.all()
firstCustomer=customer.objects.first()
lastCustomer=customer.objects.last()
customerByName=customer.objects.get(name='bruce')
firstCustomer.order_set.all()
order=order.objects.first()
parentName=order.objects.name
products=product.objects.filter(category='outdoor')
leastTOGreatest=product.objects.all().order_by('id')
greatesToLeast=product.objects.all().order_by('-id')
productsFiltered=product.objects.filtered(tags__name='sports')
ballOrders=firstCustomer.order_set.filter(product__name='Ball').count()
allOrders={}
for order in firstCustomer.order_set.all():
    if order.product.name in allOrders:
        allOrders[order.product.name] +=1
    else :
        allOrders[order.product.name]=1

class parentalModel(modesl.Models):
    name=models.charField(max_length=200,null=True)
    class childModel(models.Models) :
     parent=models.ForeignKey(parentalModel)
     name=models.charField(max_length=200,null=True)
     parent=parentalModel.objects.first()
     parent.childmodel_set.all()