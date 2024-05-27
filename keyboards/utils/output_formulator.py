def format_sizes(sizes_dict: dict, include_keys=True) -> str:
    keys = []
    values = []

    for k, v in sizes_dict.items():
        keys.append(k)
        values.append('✅ ' if v > 0 else '⬜️ ')

    formatted_string = '|'.join(values)

    if include_keys:
        formatted_string = f"{' | '.join(keys)}\n{formatted_string}"

    return formatted_string


def format_message(found_model) -> str:
    return (
        f"{found_model['name']} \n"
        f"`{found_model['sku']}` \n"
        f"_{found_model['material']}_ \n\n"
        f"*Available sizes:* \n\n"
        f"*All providers:* \n {format_sizes(found_model['total_sizes'])} \n\n"
        f"[DROP EXPERT](https://t.me/dropshipping_expert): \n"
        f"{format_sizes(found_model['sizes'], include_keys=False)} \n\n"
    )
