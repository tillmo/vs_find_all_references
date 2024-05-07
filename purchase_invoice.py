import supplier_item 
class PurchaseInvoice:
    def __init__(self,items): # works if we annotate items : list[SupplierItem]
        self.items = items # works if we instead use: [SupplierItem()]
    def process(self):    
        self.items = [i.process_item() for i in self.items]

