# Copyright 2016, 2022 John J. Rofrano. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# pylint: disable=too-few-public-methods

"""
Test Factory to make fake objects for testing
"""
import factory
from factory.fuzzy import FuzzyChoice, FuzzyDecimal
from service.models import Product, Category


class ProductFactory(factory.Factory):
    """Creates fake products for testing"""

    class Meta:
        """Maps factory to data model"""

        model = Product

    id = factory.Sequence(lambda n: n)
    # Add code to create Fake Products
    # Generate random choices for the 'name' field
    name = FuzzyChoice(choices=['Hat', 'Pants', 'Shirt', 'Apple', 'Banana', 'Pots',
                                'Towels', 'Ford', 'Chevy', 'Hammer', 'Wrench'])

    # Generate fake text for the 'description' field
    description = factory.Faker('text')

    # Generate a random price between 0.5 and 2000.0 with 2 decimal places
    price = FuzzyDecimal(0.5, 2000.0, precision=2)

    # Generate a random boolean value for 'available'
    available = FuzzyChoice(choices=[True, False])

    # Generate random choices for the 'category' field
    category = FuzzyChoice(choices=[Category.UNKNOWN, Category.CLOTHS, Category.FOOD,
                                    Category.HOUSEWARES, Category.AUTOMOTIVE, Category.TOOLS])
