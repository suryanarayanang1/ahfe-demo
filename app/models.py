# app/models.py

from dataclasses import dataclass
from typing import List

@dataclass
class Ciphertext:
    iv: str
    ciphertext: str
    attributes: List[int]
