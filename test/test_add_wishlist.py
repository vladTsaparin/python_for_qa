# -*- coding: utf-8 -*-
from model.user import User


def test_add_valid_wishlist(app):
    app.navigation.open_wishlist_page_from_menu()
