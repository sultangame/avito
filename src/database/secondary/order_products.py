from sqlalchemy import ForeignKey, Table, Column
from src.database import Base


orders_products = Table(
    "orders_products",
    Base.metadata,
    Column(
        "product_id",
        ForeignKey("products.id", ondelete="CASCADE"),
        primary_key=True
    ),
    Column(
        "order_id",
        ForeignKey("orders.id", ondelete="CASCADE"),
        primary_key=True
    )
)
