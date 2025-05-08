def get_integer_from_user(query: str,) -> int:
    while True:
        try:
            return int(input(query))
        except:
            print("> NO has escrito un entero válido.")


def get_integer_in_range_from_user(query: str, min_val: int = 0, max_val: int = 100) -> int:
    if min_val >= max_val:
        raise Exception("El valor mínimo no puede ser mayor o igual que el máximo")
    while True:
        user_int = get_integer_from_user(query)
        if user_int > max_val:
            print(f"> El número no puede ser mayor que {max_val}")
        elif user_int < min_val:
            print(f"> El número no puede ser menor que {min_val}")
        else:
            return user_int


def get_response_from_user_in_list(query: str, valid_responses: list[str]) -> str:
    while True:
        user_response = input(query).lower().strip()  # Normalizamos la entrada
        if user_response in valid_responses:
            return user_response  # Si es válida, la devolvemos
        else:
            print(f"> No has escrito una opción válida. Opciones válidas: {valid_responses}")


def get_true_or_false_from_user(query: str, true_str: str, false_str: str) -> bool:
    user_str = get_response_from_user_in_list(query, [true_str, false_str])
    return True if user_str == true_str else False


def save_password_to_txt(service: str, password: str):
    with open("passwords.txt", "a") as f:
        f.write(f"\n{service} :: {password}")
