from supplier_item import SupplierItem, process_item
class PurchaseInvoice:
    def __init__(self,items): 
        self.items = [SupplierItem()]
    def process(self):    
        self.items = [i.process_item() for i in self.items]

