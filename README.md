# pycones23-hackaton-conciliation

## Install
Add `OPENAI_API_KEY` to **.env** file

Run the following command to execute it:

``` shell
python main.py    
```

## Description

Demo de como el core de IA de la aplicación TuTiempo debería de funcionar.

La aplicación proporciona al Usuario recomendaciones para completar su rutina diaria. 
Así, le ayuda a mantener unos objetivos, permitiendo tener un horario semanal ordenado.

Un usuario en la plataforma dará de alta una serie de actividades que ayudarán a la IA a predecir los 
mejores tiempos y huecos para incluir nuevas actividades. Además, se pueden seleccionar rangos de fechas
para esas actividades.

En este código vemos como un input, de información básica de un Usuario, es capaz de ayudar a la IA a generar
una propuesta para añadir 3 actividades más a la rutina del Usuario.

---

## ToDo

**TODO:** Es posible generar respuestas y parsear los resultados. Más infomación en los templates de la librería [langchain](https://python.langchain.com/docs/get_started/introduction).

Uno de los apartados más interesantes para esta app, podría ser lo siguiente: 

``` python
from langchain.prompts import PromptTemplate
```

`PromptTemplate` ayuda a gestionar una salida deseada de los modelos de LLM



# Diseño
- [Diseño en Figma](https://www.figma.com/file/sq5xjCohE5riEJLMWFexVC/PROYECTO_PYCON?type=design&node-id=1302%3A103&mode=design&t=phU23g5DxGcKACIf-1)
