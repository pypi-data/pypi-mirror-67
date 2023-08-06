from enum import Enum, unique, auto


"""
Numerical designation (I, II, or III) that is assigned by FDA to a particular product recall that indicates the
relative degree of health hazard.
"""
@unique
class Classification(Enum):
    """
    Dangerous or defective products that predictably could cause serious health problems or death. Examples
    include: food found to contain botulinum toxin, food with undeclared allergens, a label mix-up on a
    lifesaving drug, or a defective artificial heart valve.
    """
    ClassI = auto()
    """
    Products that might cause a temporary health problem, or pose only a slight threat of a serious nature.
    Example: a drug that is under-strength but that is not used to treat life-threatening situations.
    """
    ClassII = auto()
    """
    Products that are unlikely to cause any adverse health reaction, but that violate FDA labeling or
    manufacturing laws. Examples include: a minor container defect and lack of English labeling in a retail
    food.
    """
    ClassIII = auto()