class Translation(object):
    START_TEXT = """Hola,
Mi nombre es Rename Bot!

<b>Por favor reenvíame un archivo de Telegram y luego responde éste con /rename Nuevo nombre.apk</b>

/help para más detalles..."""
    RENAME_403_ERR = "Perdona, tú no tienes permitido editar este archivo"
    ABS_TEXT = "Por favor, no seas egoísta."
    UPGRADE_TEXT = "<b>👉 Para crear tu propio bot contacta a @DKzippO</b>  /help para más detalles"
    DOWNLOAD_START = "intentando descargar..."
    UPLOAD_START = "intentando subir..."
    RCHD_TG_API_LIMIT = "Descargado en {} segundos.\nTamaño de archivo detectado: {}\nLo siento. Pero no puedo subir archivos de más de 1,5 GB debido a las limitaciones de la API de Telegram."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "**Gracias por usarme🤓.**"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Descargado en {} segundos.\nSubido en {} segundos."
    NOT_AUTH_USER_TEXT = "Porfavor, utiliza el comando /upgrade para aumentar tu suscripción."
    NOT_AUTH_USER_TEXT_FILE_SIZE = "Tamaño de archivo detectado: {}. Los usuarios gratuitos solo pueden cargar: {}\nPorfavor, utiliza el comando /upgrade para aumentar tu suscripción.\nSi cree que se trata de un error, comuníquese con <a href='https://t.me/DKzippO'>Skueletor</a>"
    SAVED_CUSTOM_THUMB_NAIL = "✅ Se guardó la miniatura del archivo personalizado. Esta imagen se utilizará en el archivo."
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Miniatura personalizada borrada con éxito."
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Las miniaturas se borraron correctamente."
    SAVED_RECVD_DOC_FILE = "Documento descargado exitosamente."
    CUSTOM_CAPTION_UL_FILE = " "
    NO_CUSTOM_THUMB_NAIL_FOUND = "No se encontró ninguna miniatura personalizada."
    USER_ADDED_TO_DB = "Usuario <a href='tg://user?id={}'>{}</a> añadido a {} hasta {}."
    HELP_USER = """Hola nuevo amigo, soy Rename Bot...
    
1. Envíame algún archivo de Telegram.
2. Responde a ese mensaje con /rename nuevo nombre.extensión.
   
<b>👉 Creado por :</b> 👉 <a href="https://t.me/DKzippO">Skueletor</a>

--------

Support Group : @BotsDeSkueletor
©"""
    REPLY_TO_DOC_FOR_RENAME_FILE = "Responde al archivo de Telegram con `/rename Nuevo Nombre.extensión` Ahora con soporte de miniaturas personalizadas ..."
    ABUSIVE_USERS = "No está autorizado a utilizar este bot. Si cree que se trata de un error, escriba /me para eliminar esta restricción."
    FREE_USER_LIMIT_Q_SZE = """No se puede procesar.
Usuarios gratuitos solo 1 solicitud cada 30 minutos.
Escribe /upgrade o inténtalo de nuevo en 30 minutos."""
    IFLONG_FILE_NAME = """El límite de nombre de archivo permitido por Telegram es {alimit} caracteres.
El nombre de archivo dado tiene {num} caracteres.

<b>¡Ensayos no permitidos en el nombre de archivo de Telegram!</b>
©️ <code>@RenameArchive_bot</code>
Por favor, abre el nombre de tu archivo y vuelve a intentarlo."""
