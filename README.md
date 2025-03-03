# 📊 **Análisis de Abandono de Clientes - BlueBank**

## 📌 **Descripción del Proyecto**

Este proyecto analiza los factores que influyen en el **abandono de clientes en BlueBank**, una entidad financiera ficticia. Se busca identificar patrones y estrategias de retención basadas en datos para minimizar la pérdida de clientes. Los datos utilizados en este análisis provienen del dataset [Bank Customer Churn Dataset](https://www.kaggle.com/datasets/gauravtopre/bank-customer-churn-dataset/data), disponible en Kaggle. Este dataset contiene información sobre clientes de un banco, incluyendo datos demográficos, financieros y su historial de permanencia o abandono.

## 🎯 **Objetivos**

- Obtener un **perfil general de los clientes** de BlueBank.
- Identificar **factores clave que afectan el abandono**.
- Proponer **estrategias basadas en datos** para mejorar la fidelización.

## 🛠 **Tecnologías utilizadas**

- **Python** (Pandas, Matplotlib, Seaborn, MySQL Connector, Dotenv)
- **MySQL** (Almacenamiento de datos)
- **Power BI** (Visualización y Dashboard)

## 📂 **Estructura del repositorio**

### **📁 datos/**

- **bruto/** → Contiene el dataset original.
  - `Bank_Customer_Churn_Prediction.csv`
- **procesado/** → Contiene el dataset limpio y transformado.
  - `EDA_Bank_Customer_Churn_Prediction.csv`

### **📁 documentacion/**

- `analisis_resultados.md` → Contiene los hallazgos y estrategias de retención.

### **📁 imagenes/**

Contiene los gráficos generados durante el análisis:

- `piecharts_categoricas.jpg` → Distribución de variables categóricas.
- `distribucion_numericas.jpg` → Histogramas de variables numéricas.
- `boxplots_var_numericas.jpg` → Boxplots para detectar outliers.
- `histograma_abandono_edad.jpg` → Distribución de edad según abandono.
- `boxplot_abandono_saldo.jpg` → Comparación de saldo según abandono.
- `barras_abandono_pais.jpg` → Distribución de clientes por país según abandono.
- `barras_abandono_miembro_activo.jpg` → Comparación de miembros activos según abandono.

### **📁 notebooks/**

Contiene los notebooks utilizados para pruebas:

- `01_EDA.ipynb` → Exploración inicial del dataset.
- `02_analisis.ipynb` → Pruebas de visualización y análisis.

### **📁 presentaciones/**

- `proyecto-analisis-abandono-clientes.pdf` → Archivo PDF con la presentación del proyecto.
- `analisis-clientes-bluebank.pbix` → Archivo de Power BI con el dashboard final.

### **📁 src/**

Contiene los scripts en Python:

- `eda.py` → Funciones de exploración de datos.
- `analisis.py` → Funciones de análisis y visualización.
- `base_datos.py` → Funciones para gestionar la base de datos MySQL.
- `variables.py` → Configuración de variables y queries SQL.

### **Archivos principales**

- `main.py` → Script principal que ejecuta todo el análisis.
- `README.md` → Documentación del proyecto.
- `requirements.txt` → Lista de dependencias necesarias para ejecutar el código.
- `.gitignore` → Archivos a excluir en el repositorio.

## 🚀 **Ejecución del Proyecto**

### 🔹 **1️⃣ Clonar el repositorio**

```bash
git clone https://github.com/mpenacasares/Analisis_Abandono_Clientes.git
cd Analisis_Abandono_Clientes
```

### 🔹 **2️⃣ Crear y activar un entorno virtual**

```bash
python -m venv venv
source venv/bin/activate  # Para MacOS/Linux
venv\Scripts\activate    # Para Windows
```

### 🔹 **3️⃣ Instalar dependencias**

```bash
pip install -r requirements.txt
```

### 🔹 **4️⃣ Configurar credenciales MySQL**

Crear un archivo `.env` en la raíz del proyecto con la siguiente información:

```
DB_HOST=localhost
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
DB_NAME=BlueBank
```

### 🔹 **5️⃣ Ejecutar el script principal**

```bash
python main.py
```

Este script realizará el análisis exploratorio de datos, generará visualizaciones y permitirá cargar la base de datos en MySQL.

## 📊 **Dashboard en Power BI**

El dashboard en Power BI proporciona una visualización interactiva del análisis realizado. Para abrirlo, usa el archivo `analisis-clientes-bluebank.pbix` dentro de la carpeta `presentaciones/`. Este archivo se ha generado cargando el csv procesado `EDA_Bank_Customer_Churn_Prediction.csv` pero puedes importar estos mismos datos desde MySQL.

## 📌 **Conclusiones del análisis**

✅ **Los clientes inactivos tienen mayor tasa de abandono**, lo que sugiere implementar estrategias de fidelización.  
✅ **Los clientes que han abandonado suelen ser más mayores**, indicando que la edad es un factor relevante en la retención.  
✅ **El país influye en el abandono**, con Alemania mostrando una mayor tasa de clientes que abandonan.  
✅ **El saldo no parece ser un factor determinante**, aunque podría influir en estrategias de segmentación.

---

## 🚀 **Next Steps**

El análisis actual proporciona una base sólida para comprender los factores que influyen en el abandono de clientes en **BlueBank**. Como siguientes pasos, se plantean mejoras y optimizaciones en el proyecto:

✅ **📊 Definir consultas SQL clave:**

- Elaborar consultas SQL que respondan preguntas estratégicas sobre el comportamiento de los clientes.
- Automatizar la ejecución de estas consultas y almacenar los resultados en un archivo `.txt` para su posterior análisis.

✅ **📟 Visualización de consultas en la terminal:**

- Seleccionar una consulta clave y mostrar los resultados directamente en la terminal.
- Facilitar una vista rápida sin necesidad de abrir archivos adicionales.

✅ **☁ Implementar la opción de base de datos en la nube:**

- Ampliar el flujo del proyecto para permitir la **creación de la base de datos en la nube** (AWS RDS, Azure SQL Database, etc.).
- De esta forma, el usuario podrá elegir entre:
  - 🛢 **Crear la base de datos en MySQL local.**
  - ☁ **Crear la base de datos en la nube.** → Pregunta a incluir
  - ❌ **No generar la base de datos.**

Con estas mejoras, el proyecto no solo permitirá analizar el **abandono de clientes**, sino también **automatizar consultas, optimizar la gestión de datos y ampliar la infraestructura a la nube**. 🚀

---

📌 **Autora:** Macarena Peña Casares  
📌 **LinkedIN:** [Ver perfil](https://www.linkedin.com/in/mpenacasares/)
📌 **Contacto:** m.penacasares@gmail.com
📌 **Fecha:** Febrero 2025
