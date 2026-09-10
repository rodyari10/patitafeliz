# 🐾 PatitaFeliz

Aplicación web para facilitar la adopción responsable de mascotas en Paraná, Argentina.

## 📋 Descripción

PatitaFeliz es una plataforma que centraliza la información de animales en busca de hogar (perros, gatos y otros animales) bajo el cuidado de refugios, veterinarias y rescatistas independientes de la ciudad de Paraná.

### Objetivos

- Facilitar el encuentro entre mascotas y familias adoptantes
- Organizar el proceso de adopción desde la publicación hasta el seguimiento
- Promover la tenencia responsable
- Unificar información que hoy está dispersa en redes sociales

## ✨ Características

- **Catálogo de mascotas**: Listado de animales disponibles leído directamente de la base de datos
- **Detalle de mascota**: Ficha completa de cada animal
- **Formulario de adopción**: Sistema de postulación que guarda las solicitudes en la base de datos y confirma el envío mostrando una plantilla de agradecimiento
- **Información organizada**: Datos de cada animal disponible para adopción
- **Diseño responsive**: Optimizado para dispositivos móviles

## 🗺️ URLs de la aplicación

| URL | Descripción |
|---|---|
| `/` | Página de inicio |
| `/mascotas/` | Listado de mascotas en adopción |
| `/mascotas/&lt;id&gt;/` | Detalle de una mascota |
| `/adoptar/` | Formulario de solicitud de adopción |
| `/nosotros/` | Información sobre el proyecto |
| `/admin/` | Panel de administración de Django |

## 🔧 Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/rodyari10/patitafeliz.git
cd patitafeliz
