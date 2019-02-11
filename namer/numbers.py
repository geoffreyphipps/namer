from random import randint
from typing import List, Tuple, Any


def random_bucket(probabilities: List[Tuple[int, Any]]) -> Any:
    d = randint(0, 99)
    for i in range(len(probabilities)):
        if d < probabilities[i][0]:
            return probabilities[i][1]
        else:
            d -= probabilities[i][0]
    return None
