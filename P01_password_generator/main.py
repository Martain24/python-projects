import utils
import string
import random

def password_generator():
    print("¡¡Bienvenido al generador de contraseñas seguras!!")

    # Obtener parámetros de generación
    password_length = utils.get_integer_in_range_from_user(
        query="Indica la longitud que deseas para tu contraseña (entre 6 y 50 caracteres): ",
        min_val=6, max_val=50
    )
    with_capital_letters = utils.get_true_or_false_from_user(
        query="¿Deseas incluir letras mayúsculas? (si/no): ", true_str="si", false_str="no"
    )
    with_numbers = utils.get_true_or_false_from_user(
        query="¿Deseas incluir números? (si/no): ", true_str="si", false_str="no"
    )
    with_symbols = utils.get_true_or_false_from_user(
        query="¿Deseas incluir símbolos especiales? (si/no): ", true_str="si", false_str="no"
    )

    # Obtener lista de caracteres que podrá contener la contraseña
    all_valid_chars = string.ascii_lowercase
    if with_capital_letters:
        all_valid_chars += string.ascii_uppercase
    if with_numbers:
        all_valid_chars += string.digits
    if with_symbols:
        all_valid_chars += string.punctuation

    # Generar la contraseña y mostrarla en pantalla
    safe_password = ''.join(random.choices(all_valid_chars, k=password_length))
    print(f"\nContraseña generada: {safe_password}")

    # Proceso de guardado en .txt
    want_to_save_password = utils.get_true_or_false_from_user(
        query="¿Te gustaría guardar esta contraseña en un archivo? (si/no): ", 
        true_str="si", false_str="no"
    )
    if want_to_save_password:
        service = input("¿Para qué servicio o aplicación es esta contraseña?: ")
        utils.save_password_to_txt(service=service, password=safe_password)

if __name__ == "__main__":
    password_generator()
