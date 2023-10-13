# Desafio Guido's Gorgeous Lasagna

## Descrição do Desafio

Este desafio envolve a criação de funções para calcular o tempo restante de assar uma lasanha, o tempo de preparo para um número específico de camadas e o tempo total decorrido de cozimento.

As variáveis-chave são as seguintes:

- `EXPECTED_BAKE_TIME`: Representa o tempo de assar esperado para a lasanha (40 minutos).
- `TEMPO_POR_CAMADA`: Representa o tempo de preparo para cada camada adicionada à lasanha (2 minutos por camada).

### Funções a serem Implementadas:

1. **`bake_time_remaining(elapsed_time)`**
   - Calcula o tempo restante de assar para a lasanha com base no tempo decorrido até o momento.

2. **`preparation_time_in_minutes(number_of_layers)`**
   - Calcula o tempo total de preparo para o número especificado de camadas a serem adicionadas à lasanha.

3. **`elapsed_time_in_minutes(number_of_layers, elapsed_bake_time)`**
   - Calcula o tempo total decorrido de cozimento, incluindo o tempo de preparo e o tempo de assar.

## Como Usar

```python
import lasagna

# Exemplo de uso da função bake_time_remaining
elapsed_time = 30
remaining_time = lasagna.bake_time_remaining(elapsed_time)
print(f"Tempo restante de assar: {remaining_time} minutos")

# Exemplo de uso da função preparation_time_in_minutes
number_of_layers = 3
preparation_time = lasagna.preparation_time_in_minutes(number_of_layers)
print(f"Tempo total de preparo: {preparation_time} minutos")

# Exemplo de uso da função elapsed_time_in_minutes
elapsed_bake_time = 20
total_elapsed_time = lasagna.elapsed_time_in_minutes(number_of_layers, elapsed_bake_time)
print(f"Tempo total decorrido: {total_elapsed_time} minutos")


# Observações
Certifique-se de ajustar as variáveis e os parâmetros conforme necessário para a sua receita de lasanha específica. As funções fornecem uma maneira fácil de calcular tempos importantes no processo de cozimento da lasanha.