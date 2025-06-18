# 🚀 Streamlit Community Cloud Demo

[![Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://sccdemo.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.45.1-red.svg)](https://streamlit.io/)
[![Pandas](https://img.shields.io/badge/Pandas-2.2.0+-green.svg)](https://pandas.pydata.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-brightgreen.svg)](https://github.com/franksunye/StreamlitCCDemo)

## 🌐 Leer en otros idiomas: [English](README.md) | [中文](README.zh.md)

> 🌐 **Demo en línea**: [https://community-cloud-demo.streamlit.app/](https://community-cloud-demo.streamlit.app/)

Una demo de aplicación Streamlit totalmente funcional, que muestra cómo desplegar rápidamente aplicaciones web interactivas en Streamlit Community Cloud. **Soporta inglés, chino y español (i18n)**, incluyendo interacción de usuario, procesamiento de archivos, visualización de datos y base de datos.

## ✨ Características

- 🎯 **Diseño minimalista** - Interfaz de usuario limpia y clara
- 🔄 **Interacción en tiempo real** - Entrada de texto, botón, deslizador, selectbox
- 📁 **Carga de archivos** - Soporta múltiples formatos y vista previa de contenido
- 📂 **Lectura de archivos estáticos** - Lee archivos JSON y CSV del proyecto
- 📊 **Visualización de datos** - Tablas, estadísticas y visualización
- 📱 **Diseño responsivo** - Se adapta a cualquier dispositivo
- 🌐 **Cambio de idioma** - Selector de idioma en la barra lateral para English/中文/Español
- ☁️ **Despliegue en la nube** - Un clic para desplegar en Streamlit Community Cloud
- 🚀 **Inicio rápido** - Dependencias mínimas, ejecución rápida

## 🛠️ Stack Tecnológico

- **Python** - 3.13+
- **Streamlit** - 1.45.1 (última)
- **Pandas** - 2.2.0+ (soporta Python 3.13)
- **GitHub** - Hospedaje de código
- **Streamlit Community Cloud** - Despliegue en la nube

## 📦 Instalación y Ejecución

### Requisitos
- Python 3.13 o superior
- Gestor de paquetes pip

### Ejecutar localmente

1. **Clonar el repositorio**
```bash
git clone https://github.com/franksunye/StreamlitCCDemo.git
cd StreamlitCCDemo
```

2. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

3. **Iniciar la app**
```bash
streamlit run app.py
```

4. **Visitar la app**
Abre tu navegador y ve a `http://localhost:8501`

## ☁️ Despliegue en la Nube

### Desplegar en Streamlit Community Cloud

1. **Haz fork de este repo** en tu cuenta de GitHub
2. **Ve a** [Streamlit Community Cloud](https://share.streamlit.io/)
3. **Inicia sesión** con tu cuenta de GitHub
4. **Crea una nueva app**:
   - Repository: `tu-usuario/StreamlitCCDemo`
   - Branch: `main`
   - Main file path: `app.py`
5. **Haz clic en Deploy** y espera a que termine

### Despliegue personalizado

También puedes modificar el código y volver a desplegar:
```bash
git add .
git commit -m "feat: agregar nueva funcionalidad"
git push origin main
```

## 📁 Estructura del Proyecto

```
StreamlitCCDemo/
├── app.py                    # Archivo principal de la app
├── translations.json         # Traducciones multilingües
├── requirements.txt          # Dependencias de Python
├── README.md                # Descripción del proyecto (inglés)
├── README.zh.md             # Descripción del proyecto (chino)
├── README.es.md             # Descripción del proyecto (español)
├── LICENSE                  # Licencia MIT
├── sample.txt               # Archivo de texto de ejemplo
└── data/                    # Archivos de datos
    ├── sample_data.json     # Datos de ejemplo en JSON
    └── weather_data.csv     # Datos meteorológicos en CSV
```

## 🎮 Uso

### Cambio de idioma
- **Selector de idioma en la barra lateral**: Cambia instantáneamente entre English/中文/Español, toda la interfaz y funciones se actualizan al instante.
- **Idioma por defecto**: Inglés al cargar por primera vez, puedes cambiarlo en cualquier momento.

### Funciones interactivas básicas
- **Entrada de texto** - Ingresa tu nombre, soporta session state
- **Botón de saludo** - Haz clic para un saludo personalizado
- **Deslizador de edad** - Selecciona edad (0-100)
- **Selector de color** - Elige tu color favorito

### Procesamiento de archivos
- **Carga de archivos** - Soporta txt, md, py, json, csv
- **Vista previa** - Muestra el contenido del archivo en tiempo real
- **Estadísticas** - Muestra líneas, palabras y caracteres
- **Soporte de codificación** - Maneja UTF-8 y Latin-1

### Visualización de datos estáticos
- **Datos JSON** - Información de la app, usuarios, estadísticas
- **Datos CSV** - Tabla de clima y análisis
- **Diseño de dos columnas** - Muestra diferentes tipos de datos lado a lado

## 🔧 Detalles Técnicos

### Internacionalización (i18n)
- Todos los textos gestionados en `translations.json`, fácil de extender a más idiomas
- El cambio de idioma es instantáneo, sin recargar la página
- Usa session state de Streamlit para recordar la elección del usuario

### Session State
La app usa session state de Streamlit para persistir la entrada del usuario:
```python
# Inicializar session state
if 'user_name' not in st.session_state:
    st.session_state.user_name = "Mundo"

# Usar session state
user_name = st.text_input("Ingresa tu nombre:", value=st.session_state.user_name, key="user_name_input")
```

### Lectura de archivos
Lectura segura para múltiples formatos:
```python
# Decodificación segura
try:
    text_content = file_content.decode('utf-8')
except UnicodeDecodeError:
    text_content = file_content.decode('latin-1')
```

### Visualización de datos
Usa pandas para procesar y mostrar datos:
```python
# Estadísticas de datos
st.write(f"- Total de registros: {len(df)}")
st.write(f"- Temperatura promedio: {df['Temperatura'].mean():.1f}°C")
```

## 🚀 Historial de Versiones

### v0.1.0 (Actual)
- ✅ Soporte para inglés, chino y español (i18n)
- ✅ Toda la interfaz y funciones pueden cambiar de idioma al instante
- ✅ Añadido translations.json para gestión unificada de textos
- ✅ Actualizado a Streamlit 1.45.1
- ✅ Actualizado a Pandas 2.2.0+ (soporte Python 3.13)
- ✅ Mejorada la compatibilidad de session state
- ✅ Añadida lectura de archivos estáticos
- ✅ Mejorado el manejo de errores

### Actualizaciones principales
- **Actualización de dependencias** - Últimas versiones estables
- **Corrección de compatibilidad** - Soporte para Python 3.13
- **Mejoras de funcionalidad** - Visualización de datos y procesamiento de archivos
- **Internacionalización** - Soporte multilingüe
- **Optimización de código** - Mejor manejo de errores y experiencia de usuario

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas!

1. Haz fork de este repo
2. Crea una rama de funcionalidad (`git checkout -b feature/AmazingFeature`)
3. Haz commit de tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Haz push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver [LICENSE](LICENSE) para más detalles.

## 🔗 Enlaces útiles

- [Documentación de Streamlit](https://docs.streamlit.io/)
- [Guía de Streamlit Community Cloud](https://docs.streamlit.io/streamlit-community-cloud)
- [Documentación de Pandas](https://pandas.pydata.org/docs/)
- [Repositorio GitHub](https://github.com/franksunye/StreamlitCCDemo)

## 📞 Contacto

- **GitHub**: [@franksunye](https://github.com/franksunye)
- **Demo en línea**: [https://community-cloud-demo.streamlit.app/](https://community-cloud-demo.streamlit.app/) 