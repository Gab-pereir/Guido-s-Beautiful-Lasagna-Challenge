EXPECTED_BAKE_TIME = 40
TEMPO_POR_CAMADA = 2

def bake_time_remaining(elapsed_time):
    """
    Calcula o tempo restante de assar para a lasanha.

    :param elapsed_time: int - tempo decorrido até o momento.
    :return: int - tempo restante de assar para a lasanha.
    """
    remaining_time = EXPECTED_BAKE_TIME - elapsed_time
    return remaining_time

def preparation_time_in_minutes(number_of_layers):
    """
    Calcula o tempo de preparo para o número especificado de camadas.

    :param number_of_layers: int - o número de camadas a serem adicionadas à lasanha.
    :return: int - tempo total de preparo para o número especificado de camadas.
    """
    total_preparation_time = number_of_layers * TEMPO_POR_CAMADA
    return total_preparation_time

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Calcula o tempo total decorrido de cozimento.

    :param number_of_layers: int - o número de camadas na lasanha.
    :param elapsed_bake_time: int - tempo decorrido de cozimento.
    :return: int - tempo total decorrido (em minutos) de preparo e cozimento.
    """
    preparation_time = preparation_time_in_minutes(number_of_layers)
    total_elapsed_time = preparation_time + elapsed_bake_time
    return total_elapsed_time
