from enum import Enum


class EntryStrategyNames(Enum):
    BalancePriceRange = "BalancePriceRange"
    Breaker = "Breaker"
    FVG = "FVG"
    IFVG = "IFVG"
    MitigationBlock = "MitigationBlock"
    Orderblock = "Orderblock"
    RejectionBlock = "RejectionBlock"
    VolumeImbalance = "VolumeImbalance"
