Contexto del problema

Este proyecto busca representar la estructura del campus universitario, permitiendo registrar zonas y edificios, así como consultar información relevante de manera organizada. La primera versión utilizaba listas lineales, lo que generaba limitaciones al trabajar con jerarquías, conexiones entre lugares y rutas dentro del campus. Para esta segunda entrega se implementó una solución basada en árboles, con el propósito de mejorar la administración de la información y la eficiencia en las búsquedas.

Descripción de los cambios respecto a la versión anterior

En esta nueva versión, los datos ya no se organizan en una lista, sino en una estructura de árbol. Esto permite reflejar de forma más adecuada la organización real del campus, compuesto por zonas principales y subzonas relacionadas jerárquicamente. Gracias al uso de árboles, es posible visualizar toda la estructura del campus de forma jerárquica, realizar búsquedas más rápidas y mantener una relación natural entre las ubicaciones.

Nueva funcionalidad implementada

Se añadió una funcionalidad destinada a buscar rutas jerárquicas entre dos ubicaciones del campus. El sistema puede determinar el camino desde el lugar de origen hasta el lugar de destino identificando el ancestro común más cercano y reconstruyendo el trayecto completo. Esta mejora permite obtener rutas más precisas y coherentes con la estructura del campus.

Librerías y herramientas utilizadas

El desarrollo del sistema está implementado en Python y utiliza la librería “bigtree”, la cual facilita la creación y manipulación de estructuras tipo árbol. Esta herramienta permitió mejorar la representación interna del campus y las búsquedas de información asociada.

Integrantes del proyecto

David Santiago Sandoval Mancilla — 2242009
Luiggy Ivan Rios Enrique — 2243166
Maria Alejandra Hernandez Perez — 2242001
Vicktor Josué David Ardila Carreño — 2230266
