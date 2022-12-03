from dataclasses import dataclass
from enum import Enum


class Category(Enum):
    All_departments = 'All Departments'
    Arts_and_crafts = 'Arts & Crafts'
    Books = 'Books'
    # TODO: implement more categories


class Country(Enum):
    United_Kingdom = 'United Kingdom'
    Japan = 'Japan'
    # TODO: implement more countries


@dataclass
class User:
    first_name: str
    last_name: str
    phone: str
    products: list[str]
    password: str = ...
    email: str = ...
    category:  Category = Category.All_departments
    country: Country = Country.United_Kingdom
