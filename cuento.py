"""Modulo para narrar un cuento interactivo."""

def narrar_cuento(personaje="Arturo", lugar="el bosque misterioso", objeto="una llave dorada"):
    historia = f"""
    ##################################################
                 LA LEYENDA DEL REINO
    ##################################################
    Habia una vez un valiente explorador llamado {personaje}.
    Un dia decidio adentrarse en {lugar} en busca de aventuras.
    
    Explorando entre los arbustos, encontro un viejo cofre oculto
    bajo las raices de un arbol milenario. Al acercarse, descubrio
    que para abrirlo necesitaba {objeto}.
    
    Con gran ingenio logro descifrar el acertijo, abrio el cofre
    y encontro el conocimiento antiguo que salvo a su pueblo.
    Fin.
    ################################################
    """
    return historia

def mostrar_moraleja():
    return "Moraleja: La curiosidad acompanada de sabiduria siempre abre las puertas correctas."
