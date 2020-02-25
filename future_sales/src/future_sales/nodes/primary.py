def build_primary(sales, raw_item_categories, raw_items, raw_shops):
    df = (
        sales.join(raw_items.set_index("item_id"), on="item_id")
        .join(raw_item_categories.set_index("item_category_id"), on="item_category_id")
        .join(raw_shops.set_index("shop_id"), on="shop_id")
    )[
        [
            "shop_id",
            "item_id",
            "item_category_id",
            "item_name",
            "item_category_name",
            "shop_name",
            "item_cnt_day",
            "item_price",
            "date",
            "date_block_num",
        ]
    ]
    return df


def build_primary_test(sales, raw_item_categories, raw_items, raw_shops):
    df = (
        sales.join(raw_items.set_index("item_id"), on="item_id")
        .join(raw_item_categories.set_index("item_category_id"), on="item_category_id")
        .join(raw_shops.set_index("shop_id"), on="shop_id")
    )[
        [
            "shop_id",
            "item_id",
            "item_category_id",
            "item_name",
            "item_category_name",
            "shop_name",
        ]
    ]
    return df
