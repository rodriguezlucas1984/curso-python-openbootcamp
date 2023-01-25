from jornadaLaboral import JornadaLaboral


def main():
    # Trabajo nocturno de Lunes a Lunes
    jornadaLaboral = JornadaLaboral(0, 7)
    esHorarioLaboral = jornadaLaboral.esHorarioLaboral()
    if esHorarioLaboral == 0:
        print(
            f'Sigue trabajando!! te que dan {round(jornadaLaboral.tiempoFinTrabajo()/3600,2)} horas para finalizar')
    else:
        print("Estas en tu tiempo libre, disfrutalo!")


if __name__ == "__main__":
    main()
