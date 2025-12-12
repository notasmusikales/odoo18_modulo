#### Archivo ir.model.access.csv: define permisos de acceso a modelos
- Columnas:
- id -> identificador único de la regla de acceso
- name -> nombre legible de la regla
- model_id:id -> modelo al que aplican los permisos (referencia al modelo)
- group_id:id -> grupo de usuarios al que se aplican los permisos
- perm_read -> permiso de lectura (1 = sí, 0 = no)
- perm_write -> permiso de escritura (1 = sí, 0 = no)
- perm_create -> permiso de creación (1 = sí, 0 = no)
- perm_unlink -> permiso de borrado (1 = sí, 0 = no)
- id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink

#### Regla de acceso para el modelo user.task:
- Aplica al modelo "user.task" (model_user_task)
- Solo para usuarios internos (base.group_user)
- Puede leer, escribir, crear y borrar registros
- access_user_task_user,user.task usuario,model_user_task,base.group_user,1,1,1,1