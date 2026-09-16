"""Classificação do consumo mensal de água."""

import math


TIPOS_VALIDOS = {"comercial", "casa", "apartamento"}


def classificar_consumo(tipo, consumo):
    """Retorna a mensagem correspondente ao tipo de imóvel e ao consumo."""
    if tipo == "comercial":
        return "Tarifa comercial aplicada – consulte o plano corporativo."

    if tipo == "apartamento" and consumo < 10:
        return "Consumo econômico – excelente controle de água!"

    if tipo in {"apartamento", "casa"} and consumo <= 25:
        return "Consumo moderado – dentro do padrão residencial."

    return "Consumo excessivo – adote medidas de economia e verifique vazamentos."


def obter_tipo():
    """Solicita um tipo de imóvel válido."""
    while True:
        tipo = input(
            "Digite o tipo de imóvel (comercial, casa ou apartamento): "
        ).strip().lower()

        if tipo in TIPOS_VALIDOS:
            return tipo

        print("Tipo de imóvel inválido. Escolha comercial, casa ou apartamento.")


def obter_consumo():
    """Solicita um consumo numérico não negativo."""
    while True:
        entrada = input("Digite o consumo mensal de água em m³: ").strip()

        try:
            consumo = float(entrada.replace(",", "."))
        except ValueError:
            print("Consumo inválido. Digite um número, por exemplo: 12,5.")
            continue

        if math.isfinite(consumo) and consumo >= 0:
            return consumo

        print("Digite um consumo finito e não negativo.")


def main():
    print("💧 SISTEMA DE CLASSIFICAÇÃO DO CONSUMO DE ÁGUA 💧")

    print("\nExemplos:")
    print("- Apartamento com 8 m³: consumo econômico")
    print("- Casa com 20 m³: consumo moderado")
    print("- Apartamento com 30 m³: consumo excessivo")
    print("- Imóvel comercial: tarifa comercial")
    print()

    tipo = obter_tipo()
    consumo = obter_consumo()

    print(classificar_consumo(tipo, consumo))


if __name__ == "__main__":
    main()
