from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# class Customer(models.Model):
#     user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
#     name = models.CharField(max_length=200, null=True)
#     phone = models.CharField(max_length=200, null=True)
#     email = models.CharField(max_length=200, null=True)
#     date_created = models.DateTimeField(auto_now_add=True, null=True)

#     def __str__(self):
#         return self.name

# class Tag(models.Model):
#     name = models.CharField(max_length=200, null= True)

#     def __str__(self):
#         return self.name

# class Product(models.Model):
#     CATEGORY = (
#         ('Indoor', 'Indoor'),
#         ('Out Door', 'Out Door'),
#     )

#     name = models.CharField(max_length=200, null=True)
#     price = models.FloatField(null=True)
#     catrgory = models.CharField(max_length=200, null=True,choices=CATEGORY)
#     description = models.CharField(max_length=200,null=True,blank=True)
#     date_created = models.DateTimeField(auto_now_add=True, null=True)
#     tags = models.ManyToManyField(Tag)

#     def __str__(self):
#         return self.name

# class Order(models.Model):
#     STATUS = (
#             ('Pending', 'Pending'),
#             ('Out for delivery', 'Out for delivery'),
#             ('Delivered', 'Delivered'),
#             )
    
#     customer = models.ForeignKey(Customer, null=True,on_delete= models.SET_NULL)
#     product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
#     date_created = models.DateTimeField(auto_now_add=True, null=True)
#     status = models.CharField(max_length=200, null=True, choices=STATUS)
#     note = models.CharField(max_length=1000, null=True)

#     def __str__(self):
#         return self.product.name


# For Justin's Project

class OrderDetail(models.Model):
    order_detail_pk = models.CharField(max_length=25,primary_key=True)
    ic = models.CharField(max_length=6)
    delivery = models.CharField(max_length=6)
    date_placed = models.DateField()
    cust_fty_code = models.CharField(max_length=3)
    destination = models.CharField(max_length=20)
    buyer = models.CharField(max_length=10, default="")
    consol_num = models.CharField(max_length=15)
    dept = models.CharField(max_length=2)
    style = models.CharField(max_length=4)
    colour = models.CharField(max_length=2)
    size = models.CharField(max_length=3)
    description = models.CharField(max_length=150)
    qty = models.IntegerField()
    carton_qty_on_order = models.IntegerField()
    no_of_cartons_per_sku = models.FloatField()
    uk_cost_price_on_order = models.FloatField()
    pricing_type_on_order = models.CharField(max_length=50)
    selling_price_on_order = models.FloatField()
    ticket_price_on_order = models.FloatField()
    ticket_type_on_order = models.CharField(max_length=50)
    ticket_type_id_on_order = models.CharField(max_length=50)

    def __str__(self):
        return self.order_detail_pk

class Order(models.Model):
    penalty_choice = (
        ('Yes','Yes'),
        ('No','No')
    )
    currency_choice = (
        ('$','$'),
        ('EU','EU'),
        ('CNY','CNY')
    )

    order_pk = models.CharField(max_length=400,primary_key=True)
    retailer = models.CharField(max_length=3, blank=True)
    ic = models.CharField(max_length=6, blank=True)
    delivery = models.IntegerField(blank=True)
    date_placed = models.DateField(null=True)
    consol_num = models.CharField(max_length=20, blank=True)
    destination = models.CharField(max_length=80, blank=True)
    fob = models.DateField(null=True, blank=True)
    due = models.DateField(null=True, blank=True)
    account = models.CharField(max_length=10, blank=True)
    currency = models.CharField(max_length=20, choices=currency_choice, blank=True)
    comm_value = models.FloatField( blank=True)
    order_value = models.FloatField(blank=True)
    sda_comm = models.FloatField(blank=True)
    penalty_yes_no = models.CharField(max_length=4,choices=penalty_choice, blank=True)
    penalty_amt = models.FloatField(blank=True)
    date_booked = models.DateField(null=True, blank=True)
    booking_mail_uploaded = models.CharField(max_length=4, blank=True)
    crd = models.DateField(null=True, blank=True)
    forwarder_given_etd = models.DateField(null=True, blank=True)
    forwarder_given_eta = models.DateField(null=True, blank=True)
    vessel_details = models.CharField(max_length=30, blank=True)
    handover_date = models.DateField(null=True, blank=True)
    asn_no = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=20, blank=True)
    units = models.IntegerField(blank=True)
    total_cartons_in_order = models.IntegerField(blank=True)
    delivery_ean = models.CharField(max_length=20, blank=True)
    container_number = models.CharField(max_length=11, blank=True)
    arrival_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.order_pk

class Buyer(models.Model):
    buyer = models.CharField(max_length=20)
    payment = models.CharField(max_length=30)
    term_days = models.IntegerField()


class Product(models.Model):
    knit_wov_others_acc_choices = (
        ('knit','knit'),
        ('wov','wov'),
        ('others','others'),
        ('acc','acc'),
    )
    gender_choices = (
        ('Snr','Snr'),
        ('Lds','Lds'),
        ('Jnr','Jnr'),
        ('Inf','Inf'),
        ('Baby','Baby')
    )
    
    country_choice_list = ['China', 'Myanmar', 'BD', 'PK', 'India', 'Laos', 'Cambodia', 'Indonesia', 'Taiwan', 'HK', 'Vietnam', 'Msia', 'SriLanka', 'Africa', 'Korea']
    country_of_manufacture_choices = tuple((i,i) for i in country_choice_list)


    port_of_loading_list = ['Bangkok', 'Chattogram', 'Chennai', 'Chittagong', 'Chittagong ', 'Chittaong', 'Dalian',
                            'Dongguan', 'Fuzhou', 'Ho Chi Minh', 'Hong Kong', 'Huangpu', 'Kaohsiung', 'Karachi', 'Keelung', 
                            'Mumbai', 'Nantong', 'Nhava Sheva', 'Ningbo', 'Nanjing', 'Port Kelang', 'Qingdao', 'Semarang', 
                            'Shanghai', 'Shenzhen', 'Shenzhen ', 'Sihanoukville', 'Taichung', 'Tianjin', 'Tuticorin', 
                            'Wuhan', 'Xiamen', 'Yangon', 'Yantian', 'Zhejiang', 'Zhongshan']

    port_of_loading_choices = tuple((i,i) for i in port_of_loading_list)

    currency_choice = (
        ('$','$'),
        ('EU','EU'),
        ('CNY','CNY')
    )

    carton_type_choice = (
        ('58 x 37.5 x 37.5','2/3 SS'),
        ('58 x 37.5 x 20','1/3 SS'),
        ('58 x 58 x 37.5', 'Full SS'),
        ('A5BE','A5BE')
    )

    product_pk = models.CharField(max_length=20, primary_key=True)
    dept = models.CharField(max_length=2, blank=True)
    styl = models.CharField(max_length=4, blank=True)
    colour = models.CharField(max_length=2, blank=True)
    size = models.CharField(max_length=3, blank=True)
    description = models.CharField(max_length=150, blank=True)
    date_created = models.DateField(blank=True)
    user_verified = models.CharField(max_length=5, blank=True)
    chkdigit = models.CharField(max_length=2, blank=True)
    supplier_code = models.CharField(max_length=10, blank=True)
    account = models.CharField(max_length=10, blank=True)
    tla_fty_code = models.CharField(max_length=3, blank=True)
    cust_fty_code = models.CharField(max_length=3, blank=True)
    barcode = models.CharField(max_length=13, blank=True)
    trading_code = models.CharField(max_length=20, blank=True)
    fabrication = models.CharField(max_length=250, blank=True)
    main_fabric_gsm = models.IntegerField(blank=True)
    fabric_type = models.CharField(max_length=25, blank=True)
    knit_wov_others_acc = models.CharField(max_length=25, choices=knit_wov_others_acc_choices, blank=True)
    gender = models.CharField(max_length=10, choices=gender_choices, blank=True)
    season_code = models.CharField(max_length=2, blank=True)
    carton_qty_in_tla_portal = models.IntegerField(blank=True)
    cost_price_currency = models.CharField(max_length=10,choices=currency_choice, blank=True)
    uk_cost_price_in_tla_portal = models.FloatField(blank=True)
    fty_price = models.FloatField(blank=True)
    unit_commission = models.FloatField(blank=True)
    unit_commission_percent = models.FloatField(blank=True)
    pricing_type_in_tla_portal = models.CharField(max_length=5, blank=True)
    selling_price_in_tla_portal = models.FloatField(blank=True)
    ticket_type_in_tla_portal = models.CharField(max_length=5, blank=True)
    ticket_type_id_in_tla_portal = models.CharField(max_length=5, blank=True)
    ticket_price_in_tla_portal = models.FloatField()
    last_price_change_detected = models.DateTimeField()
    country_of_manufacture = models.CharField(max_length=20, choices=country_of_manufacture_choices, blank=True)
    port_of_loading = models.CharField(max_length=20, choices=port_of_loading_choices, blank=True)
    carton_length = models.FloatField(blank=True)
    carton_breadth = models.FloatField(blank=True)
    carton_height = models.FloatField(blank=True)
    carton_type = models.CharField(max_length=20, blank=True, choices=carton_type_choice)
    photo_sample_date = models.DateField(blank=True)
    last_shipped = models.DateField(blank=True)
    status = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.product_pk

class FtyTable(models.Model):
    status_choices = (
                        ('Approved','Approved'),
                        ('Pending','Pending')
    )
    any_transaction_choices = (
                                    ('Yes', 'Yes'),
                                    ('No','No')                            
    )
    grade_choices = (
                        ('A','A'),
                        ('B','B'),
                        ('C','C'),
                        ('D','D')
    )
    type_choices = (
                        ('Factory','Factory'),
                        ('IMP-EX','IMP-EX'),
                        ('Agent','Agent'),
                        ('Service','Service')

    )
    source_choices = (
                        ('Internet','Internet'),
                        ('Introduced','Introduced'),
                        ('Fair','Fair'),
                        ('Old Supp','Old Supp'),
                        ('New Supp','New Supp'),
                        ('Cust Acquired Biz Supp','Cust Acquired Biz Supp')
    )
    
    transaction_currency_choice = (
        ('$','$'),
        ('EU','EU'),
        ('CNY','CNY')
    )
    
    trading_terms_choices = (
                                ('FOB','FOB'),
                                ('CNF','CNF'),
                                ('Domestic','Domestic'),
                                ('CIF','CIF'),
                                ('FCA','FCA'),
                                ('Ex Works','Ex Works'),
                                ('DDP','DDP')
    )

    payment_choices = (
                        ('TT','TT'),
                        ('LC','LC'),
                        ('DP','DP'),
                        ('adv + rest payment before shipment','adv + rest payment before shipment'),
                        ('adv + rest payment after shipment','adv + rest payment after shipment')
    )

    payment2_choices = (
                        ('TT','TT'),
                        ('LC','LC'),
                        ('DP','DP'),
                        ('adv + rest payment before shipment','adv + rest payment before shipment'),
                        ('adv + rest payment after shipment','adv + rest payment after shipment')
    )

    country_choice_list = ['China', 'Myanmar', 'BD', 'PK', 'India', 'Laos', 'Cambodia', 'Indonesia', 'Taiwan', 'HK', 'Vietnam', 'Msia', 'SriLanka', 'Africa', 'Korea']

    country_choices = tuple((i,i) for i in country_choice_list)
    country_of_manufacture_choices = tuple((i,i) for i in country_choice_list)

    compliance_grade_choices = (
                        ('A','A'),
                        ('B','B'),
                        ('C','C'),
                        ('D','D')
    )

    port_of_loading_list = ['Bangkok', 'Chattogram', 'Chennai', 'Chittagong', 'Chittagong ', 'Chittaong', 'Dalian',
                            'Dongguan', 'Fuzhou', 'Ho Chi Minh', 'Hong Kong', 'Huangpu', 'Kaohsiung', 'Karachi', 'Keelung', 
                            'Mumbai', 'Nantong', 'Nhava Sheva', 'Ningbo', 'Nanjing', 'Port Kelang', 'Qingdao', 'Semarang', 
                            'Shanghai', 'Shenzhen', 'Shenzhen ', 'Sihanoukville', 'Taichung', 'Tianjin', 'Tuticorin', 
                            'Wuhan', 'Xiamen', 'Yangon', 'Yantian', 'Zhejiang', 'Zhongshan']

    port_of_loading_choices = tuple((i,i) for i in port_of_loading_list)

    status = models.CharField(max_length=20, choices=status_choices, blank=True)
    any_transactions = models.CharField(max_length=20, choices=any_transaction_choices, blank=True)
    grade = models.CharField(max_length=20, choices= grade_choices, blank=True)
    type =models.CharField(max_length=20, choices = type_choices, blank=True)
    source = models.CharField(max_length=30, choices=source_choices, blank=True)
    tla_fty_code = models.CharField(max_length=3, blank=True)
    cust_fty_code = models.CharField(max_length=3, primary_key=True, blank=True)
    product_type = models.CharField(max_length=250, blank=True)
    chinese_name = models.CharField(max_length=100, blank=True)
    chinese_name_po = models.CharField(max_length=30, blank=True)
    chinese_alias = models.CharField(max_length=100, blank=True)
    english_name = models.CharField(max_length=100, blank=True)
    english_name_po = models.CharField(max_length=100, blank=True)
    english_alias = models.CharField(max_length=30, blank=True)
    port_of_loading_1 = models.CharField(max_length=50, choices=port_of_loading_choices, blank=True)
    port_of_loading_2 = models.CharField(max_length=50, choices=port_of_loading_choices, blank=True)
    contract = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    mobile = models.CharField(max_length=20, blank=True)
    fax = models.CharField(max_length=20, blank=True)
    chinese_addr = models.TextField(max_length=250, blank=True)
    postcode = models.CharField(max_length=20, blank=True)
    english_addr = models.TextField(max_length=250, blank=True)
    beneficiary = models.CharField(max_length=100, blank=True)
    bank_name = models.CharField(max_length=100, blank=True)
    bank_acc = models.CharField(max_length=100, blank=True)
    transaction_currency = models.CharField(max_length=20, choices= transaction_currency_choice, blank=True)
    trading_terms = models.CharField(max_length=20, choices= trading_terms_choices, blank=True)
    payment = models.CharField(max_length=35, choices= payment_choices, blank=True)
    term = models.IntegerField(blank=True)
    payment2 = models.CharField(max_length=35, choices=payment2_choices, blank=True)
    term2 = models.IntegerField(blank=True)
    country = models.CharField(max_length=20, choices=country_choices, blank=True)
    city = models.CharField(max_length=20, blank=True)
    country_of_manufacture = models.CharField(max_length=20, choices=country_of_manufacture_choices, blank=True)
    leadtime = models.CharField(max_length=20, blank=True)
    normal_production_leadtime = models.CharField(max_length=20, blank=True)
    peak_period_production_leadtime = models.CharField(max_length=20, default='', blank=True)
    peak_months = models.CharField(max_length=20, blank=True)
    year_first_used = models.IntegerField(blank=True)
    compliance = models.CharField(max_length=20, blank=True)
    merch_dept = models.CharField(max_length=20, blank=True)
    compliance_grade = models.CharField(max_length=20, choices = compliance_grade_choices, blank=True)
    compliance_expiry = models.DateField(blank=True)

    # def __str__(self):
    #     return self.order_detail_pk

class OfficeMapping(models.Model):
    cust_fty_code = models.CharField(max_length=3)
    office = models.CharField(max_length=20)




