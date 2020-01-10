# -*- coding: utf-8 -*-
import os
# 1. Obtener lista
clases = ["¿Qué significa ser un profesional de JavaScript","Aspectos que destacan a un profesional","Inicio del proyecto","Cómo llega un script al navegador","Scope","Closures","El primer plugin","this","Los métodos call, apply y bind","Prototype","Herencia Prototipal","Parsers y el Abstract Syntax Tree", "Abstract Syntax Tree en Práctica","Cómo funciona el JavaScript Engine","Event Loop","Promesas","Getters y setters","Proxy","Generators","Fetch - Cómo cancelar peticiones","IntersectionObserver","VisibilityChange","Service Workers","Introducción","Tipos básicos","Funciones","Interfaces","Clases","Convertir el proyecto a TypeScript","Qué es un patrón de diseño","Categorías de patrones de diseño","Patrón Singleton y Casos de Uso","Implementación del patrón Singleton","¿Cómo funciona el Patrón Observer","Implementación del patrón Observer","Casos de Uso del patrón Observer: Redux","Patrón Decorator y Casos de Uso","Implementación del patrón Decorator","Implementación de plugin de Ads: Desplegando en consola","Implementación de plugin de Ads: Desplegando en pantalla","Publicar en npm","Conclusiones"]
curso = "ProfesionalJS/"
#¿Qué significa ser un profesional de JavaScript- en Curso Profesional de JavaScript
bloques = os.listdir(curso)
for bloque in bloques:
    for clase in clases:
        sourcePath = (curso + bloque + "/" + clase + " en Curso Profesional de JavaScript"+ ".ts")
        if (os.path.exists(sourcePath)):
            newSourceName =  (curso + bloque + "/0"+ str(clases.index(clase)+1)+" - " + clase+ ".ts")
            os.rename(sourcePath, newSourceName)

