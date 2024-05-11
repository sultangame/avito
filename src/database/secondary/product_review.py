from sqlalchemy import ForeignKey, Table, Column
from src.database import Base


products_review = Table(
    "products_review",
    Base.metadata,
    Column(
        "product_id",
        ForeignKey("products.id", ondelete="CASCADE"),
        primary_key=True
    ),
    Column(
        "review_id",
        ForeignKey("reviews.id", ondelete="CASCADE"),
        primary_key=True
    )
)
