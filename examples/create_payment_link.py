import payfect

# payfect.api_key = 'Tan2glfr.YFigW4Xx37Lbj6d4x6iXtw7pzUaNTHKk'
payfect.api_key = 'W8RMk4t7.HtfJQ6UREs3Mc56vfpvStiBQQRIohsgq'  # Testmode


PRODUCT_NAME = '金雨樹'
PRODUCT_DESCRIPTION = '5m²•森林景觀•禁煙房•網路存取•壁爐•免費衛浴用品•戶外環境•提供空調\n四人價格(一泊二食)'
PRODUCT_IMAGE_URL = 'https://tbb-prod-apac.imgix.net/attachments/room_type_photos/images/675130/675130/%E9%87%91%E9%9B%A8%E6%A8%B91.jpg?auto=format,compress&fit=crop&crop=entropy&w=300&h=200&q=55'

PRICE_CURRENCY = 'twd'
PRICE_UNIT_AMOUNT = '8800'

product_data = payfect.Product.create(
    name=PRODUCT_NAME,
    description=PRODUCT_DESCRIPTION,
    images=[
        PRODUCT_IMAGE_URL,
    ]
)

product_id = product_data['id']

price_data = payfect.Price.create(
    product=product_id,
    currency=PRICE_CURRENCY,
    unit_amount=PRICE_UNIT_AMOUNT,
)

price_id = price_data['id']

payment_link = payfect.PaymentLink.create(
    name_collection=True,
    email_collection=True,
    phone_number_collection=True,
    shipping_address_collection=['TW'],
    invoice_items=[{
        "price": price_id,
        "quantity": 1
    }]
)

print(payment_link)
