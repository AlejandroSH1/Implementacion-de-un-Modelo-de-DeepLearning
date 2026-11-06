# Implementación de un Modelo de DeepLearning

En este repositorio se encuentra todo lo relacionado a la creación de un modelo para poder clasificar imágenes de modelos de autos deportivos, concretamente de 10 modelos: Audi R8, Audi RS5, BMW M3, BMW M5, Chevrolet Camaro, Ford Mustang, Mercedes AMG-GT, Nissan GT-R, Porsche 911, Toyota Supra.

### Contenido

---

- Models
  - B_capas_seed42.keras: Modelo mejorado del de Transfer learning, es un modelo más largo y con 100 capas descongeladas.
  - cnn_base_v1.keras: Modelo inicial utilizando una CNN propia.
  - modelo2_effnetb0_seed42.keras: Segundo modelo pero haciendo uso de Transfer learning para tener un mejor modelo, siguiendo con EfficientNetB0.
- Scripts
  - Modelo_CNN.ipynb: Archivo en el que se entrena el primer modelo usando CNN.
  - Modelo_TransferLearning.ipynb: Archivo en el que se entrena el segundo modelo usando EfficientNet0.
  - ModeloTL_Mejora.ipynb: Archivo en el que se hacen diversos experimentos para llegar a una mejora del modelo de Tranfer Learning.
- EDA_ETL.ipynb: Archivo en donde se hace el análisis exploratorio de los datos y en base a ello, realizar el ETL de los datos.
- Paper_Explicativo.pdf: Archivo pdf en donde se redacta el paso a paso del trabajo.
- prueba.py: Es la interfaz que se tiene para probar el modelo seleccionado.

### Autor

---

Alfredo Alejandro Soto Herrera
