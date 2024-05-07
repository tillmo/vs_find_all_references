import supplier_item
class PurchaseInvoice:
    def __init__(self,items): 
        self.items = [supplier_item.SupplierItem()]
    def process(self):    
        self.items = [i.process_item() for i in self.items]

