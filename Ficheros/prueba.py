frases_comida ={
    "El carnaval es una festividad anual llena de color y alegría que se celebra antes de la cuaresma.": "carnaval",
    "Las máscaras del carnaval se utilizan para ocultar la identidad y permitir a las personas actuar con libertad.": "máscaras",
    "Las comparsas son grupos de personas que desfilan por las calles durante el carnaval, mostrando coreografías y disfraces llamativos.": "comparsas",
    "Los trajes del carnaval suelen ser extravagantes y coloridos, con diseños elaborados y temáticas variadas.": "trajes",
    "Los desfiles son eventos principales durante el carnaval, donde se exhiben los disfraces y se disfruta de la música y la danza.": "desfiles",
    "La música del carnaval suele ser alegre y festiva, con ritmos animados como samba, cumbia o merengue.": "música",
    "Los disfraces del carnaval pueden representar desde personajes de cuentos de hadas hasta figuras históricas o caricaturas populares.": "disfraces",
    "El ambiente durante el carnaval es festivo y bullicioso, con calles llenas de gente, música y celebración.": "ambiente",
    "Las tradiciones del carnaval varían según la región, pero todas comparten la idea de diversión, desfiles y disfraces.": "tradiciones",
    "El carnaval fortalece los lazos comunitarios al proporcionar una oportunidad para que la gente se reúna y celebre juntos.": "comunidad",
    "Las máscaras permiten a las personas expresar su creatividad y jugar con su identidad durante el carnaval.": "identidad",
    "Los desfiles reflejan la riqueza cultural y la diversidad de la comunidad, mostrando trajes y bailes tradicionales.": "riqueza cultural",
    "Durante el carnaval, se disfrutan platos típicos como feijoada, empanadas, arepas y bebidas como caipirinha o pisco sour.": "comida típica",
    "Las festividades del carnaval pueden durar varios días e incluir eventos como bailes, concursos y espectáculos de fuegos artificiales.": "duración de las festividades",
    "El carnaval promueve la inclusión y el sentido de pertenencia a una comunidad, fomentando la interacción social y la diversión.": "promoción de la inclusión",
    "Las máscaras del carnaval son una forma de liberación y expresión artística para quienes las utilizan.": "expresión artística",
    "Los desfiles del carnaval muestran la diversidad cultural y la historia de una comunidad a través de sus trajes y bailes.": "diversidad cultural",
    "Durante el carnaval, la comida y la bebida son abundantes, con platos tradicionales y bebidas refrescantes para disfrutar.": "abundancia de comida y bebida",
    "Las celebraciones del carnaval son una oportunidad para reunirse con amigos y familiares y celebrar la vida con alegría.": "celebración de la vida",
    "El carnaval es una manifestación cultural que trasciende las fronteras y une a personas de diferentes orígenes y creencias.": "trascendencia cultural",
    "Las máscaras del carnaval permiten a las personas liberarse de inhibiciones y experimentar la vida de manera diferente.": "liberación de inhibiciones",
    "Los desfiles del carnaval son una forma de arte callejero que celebra la creatividad y la imaginación de una comunidad.": "arte callejero",
    "Durante el carnaval, las calles se llenan de música y baile, con personas de todas las edades participando en la diversión.": "participación de todas las edades",
    "Las festividades del carnaval son una forma de escapar de la rutina diaria y sumergirse en un mundo de fantasía y diversión.": "escape de la rutina",
    "El carnaval es una tradición arraigada en muchas culturas que celebra la vida y la energía de la comunidad.": "tradición arraigada"
}


claves_texto = []
for i in frases_comida: 
    claves_texto.append(frases_comida[i]) #si tiene punto añadir [:frases_comida[i].index(".")]

# Imprimir los valores como texto
print("Claves del diccionario como texto:")
for i in claves_texto: 
    print(i.capitalize())