"""
Nigiri auto-generated file
"""
from sdkboil.object import SdkObject
from .paid_status import PaidStatus
from .paid_status import PaidStatus
from .paid_status import PaidStatus


class PaymentOrderState(SdkObject):
    schema = {
        "rules": [],
        "schema": {
            "blockchain_status": {
                "rules": [
                    "in:pending,partial,mempool_unconfirmed,unconfirmed,paid,cancelled,expired,network_dispute,mempool_network_dispute,possible_chargeback,chargeback",
                    "required"
                ],
                "type": "string"
            },
            "in_confirmation": {
                "rules": [
                    "required",
                    "nullable"
                ],
                "schema": {
                    "crypto": {
                        "rules": [
                            "required"
                        ],
                        "type": "integer"
                    },
                    "fiat": {
                        "rules": [
                            "required",
                            "decimal"
                        ],
                        "type": "string"
                    }
                },
                "type": "object"
            },
            "paid": {
                "rules": [
                    "required",
                    "nullable"
                ],
                "schema": {
                    "crypto": {
                        "rules": [
                            "required"
                        ],
                        "type": "integer"
                    },
                    "fiat": {
                        "rules": [
                            "required",
                            "decimal"
                        ],
                        "type": "string"
                    }
                },
                "type": "object"
            },
            "status": {
                "rules": [
                    "in:pending,paid,cancelled,expired,network_dispute,chargeback",
                    "required"
                ],
                "type": "string"
            },
            "unpaid": {
                "rules": [
                    "required",
                    "nullable"
                ],
                "schema": {
                    "crypto": {
                        "rules": [
                            "required"
                        ],
                        "type": "integer"
                    },
                    "fiat": {
                        "rules": [
                            "required",
                            "decimal"
                        ],
                        "type": "string"
                    }
                },
                "type": "object"
            }
        },
        "type": "object"
    }
    sub_objects = {
        'unpaid': PaidStatus,
        'paid': PaidStatus,
        'in_confirmation': PaidStatus,

    }

    def __init__(self, blockchain_status, status, unpaid=None, paid=None, in_confirmation=None):
        super().__init__()
        self.unpaid = unpaid
        self.paid = paid
        self.blockchain_status = blockchain_status
        self.in_confirmation = in_confirmation
        self.status = status
