import payfect

payfect.api_key = 'Y4yiR6Rl.1hLmslmMHvWW8SJscVvjxx4INsMmtcF1'  # livemode
# payfect.api_key = 'W8RMk4t7.HtfJQ6UREs3Mc56vfpvStiBQQRIohsgq'  # testmode


PRODUCT_NAME = '儲值金'
PRODUCT_DESCRIPTION = '馬上儲值'
PRODUCT_IMAGE_URL = 'https://yt3.ggpht.com/ytc/AKedOLQRT9ywEEg9eRoW3SwJ0onY4bjvGyck18nJRaLHvhY=s900-c-k-c0x00ffffff-no-rj'

PRICE_CURRENCY = 'usdt'
PRICE_UNIT_AMOUNT = '1000'

SUCCESS_URL = "https://example.com/success"
CANCEL_URL = "https://example.com/cancel",


# 建立新產品（僅第一次需要）
product_data = payfect.Product.create(
    name=PRODUCT_NAME,
    description=PRODUCT_DESCRIPTION,
    images=[
        PRODUCT_IMAGE_URL,
    ]
)

product_id = product_data['id']


# 建立新價格
price_data = payfect.Price.create(
    product=product_id,
    currency=PRICE_CURRENCY,
    unit_amount=PRICE_UNIT_AMOUNT,
)

price_id = price_data['id']


# 建立結帳
order_id = "order_0001"

checkout = payfect.Checkout.create(
    client_reference_id=order_id,
    invoice_items=[{
        "price": price_id,
        "quantity": 1
    }],
    currency=PRICE_CURRENCY,
    payment_method_types=[
        'crypto',
        'card',
    ],
    success_url=SUCCESS_URL,
    cancel_url=CANCEL_URL,
)

# 導向結帳網址
print(checkout['url'])

# 結帳後，Payfect 透過 webhook 通知結帳成功！
