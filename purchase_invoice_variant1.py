from supplier_item import SupplierItem, process_item
class PurchaseInvoice:
    def __init__(self,items : list[SupplierItem]):
        self.items = items 
    def process(self):    
        self.items = [i.process_item() for i in self.items]

