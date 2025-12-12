{
    'name': 'User Examen Práctico',          # Nombre del módulo tal como aparecerá en Odoo
    'version': '1.0',                     # Versión del módulo
    'category': 'Tools',                  # Categoría en el listado de apps de Odoo
    'summary': 'Examen práctico efficiently',  # Resumen corto (se muestra en la ficha del módulo)

    'description': """ 
    Descripcion del módulo de User Examen Práctico
    """,                                 # Descripción larga del módulo (texto informativo)
    
    'author': 'Noel',                  # Autor del módulo
    'website': 'https://miweb.com',      # Web del autor o del proyecto

    'depends': ["base"],                 # Módulos de los que depende (base es el mínimo en casi todos)
    
    'data': [
        "security/task_security.xml",    # Reglas de seguridad (grupos, permisos de menú, etc.)
        "security/ir.model.access.csv",  # Permisos de acceso al modelo (lectura, escritura, etc.)
        "views/task_views.xml",          # Vistas (formularios, árboles, menús) del módulo
    ],

    'installable': True,                 # Indica que el módulo se puede instalar
    'application': True,                 # Aparece como aplicación en el menú principal de Odoo
    "assets": {
        "web.assets_backend": [
            "/user_task_manager/static/src/css/task_kanban.css",
        ],
    },
}