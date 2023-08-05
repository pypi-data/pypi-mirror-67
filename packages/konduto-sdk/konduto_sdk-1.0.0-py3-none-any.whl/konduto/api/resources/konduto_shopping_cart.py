from dataclasses import dataclass, asdict
from datetime import date
from decimal import Decimal
from typing import Optional


@dataclass
class KondutoProduct:
    sku: Optional[str] = None
    product_code: Optional[str] = None
    category: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    unit_cost: Optional[Decimal] = None
    quantity: Optional[int] = None
    created_at: Optional[date] = None
    discount: Optional[Decimal] = None

    @property
    def to_dict(self) -> [dict]:
        return asdict(self)
