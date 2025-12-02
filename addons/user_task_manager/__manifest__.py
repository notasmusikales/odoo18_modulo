{
    'name': 'User Task Manager',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Manage user task efficiently',
    'description': """ Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
    Donec ut ante fermentum, mattis ante in, ornare arcu. Lorem ipsum dolor sit amet, 
    consectetur adipiscing elit.""",
    'author': 'Noel',
    'website': 'http://miweb.com',
    'depends': ["base"],
    'data': [
        "security/task_security.xml",
        "security/ir.model.access.csv",
        "views/task_views.xml",
    ],
    'installable': True,
    'application': True,


}