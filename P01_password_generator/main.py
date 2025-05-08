from utils import get_integer_in_range_from_user, get_true_or_false_from_user, save_password_to_txt
import string
import random

def main():
    print("¡¡Bienvenido al generador de contraseñas seguras!!")

    # Obtener parámetros de generación
    password_length = get_integer_in_range_from_user(
        query="¿Qué longitud quieres que tenga la contraseña segura? ",
        min_val=6, max_val=50
    )
    with_capital_letters = get_true_or_false_from_user(
        query="¿Quieres que tenga letras mayúsculas? (si/no) ", true_str="si", false_str="no"
    )
    with_numbers = get_true_or_false_from_user(
        query="¿Quieres que tenga números? (si/no) ", true_str="si", false_str="no"
    )
    with_symbols = get_true_or_false_from_user(
        query="¿Quieres que tenga símbolos? (si/no) ", true_str="si", false_str="no"
    )

    # Obtener lista de caracteres que podrá contener la contraseña
    full_list_of_chars = list(string.ascii_lowercase)
    if with_capital_letters:
        full_list_of_chars += list(string.ascii_uppercase)
    if with_numbers:
        full_list_of_chars += list(string.digits)
    if with_symbols:
        full_list_of_chars += list(string.punctuation)

    # Generar la contraseña y mostrarla en pantalla
    safe_password = ''.join(random.choices(full_list_of_chars, k=password_length))
    print(f"Esta es la contraseña generada: {safe_password}")

    # Proceso de guardado en .txt
    want_to_save_password = get_true_or_false_from_user(
        query="¿Quieres guardar la contraseña? (si/no) ", true_str="si", false_str="no"
    )
    if want_to_save_password:
        service = input("¿Para que servicio es esta contraseña? ")
        save_password_to_txt(service=service, password=safe_password)

if __name__ == "__main__":
    main()
