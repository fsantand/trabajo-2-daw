import json
from zoomus import ZoomClient

from .models import Atencion, Sesion

API_KEY = "ShFBmRNaTSGeYE0TZ0Q5dQ"
API_SECRET = "5g6A2dKnPf7cOvZP2si06OB2HxZF8WmBqM0D"
USER_ID = "EboF2WLOTIam_YbtyA8j6g"

client = ZoomClient(API_KEY, API_SECRET)

# meeting_response = client.meeting.create(user_id=USER_ID, topic = 'Reunion pulenta de 5 minutos', type=1)
# meeting = json.loads(meeting_response.content)

# meeting_id = meeting['id']
# start_url = meeting['start_url']
# join_url = meeting['join_url']

# client.meeting.end(id=meeting_id, host_id=USER_ID)

def iniciar_sesion_instantanea(atencion):
    meeting_response = client.meeting.create(user_id=USER_ID, topic = atencion.titulo, type=1)
    meeting = json.loads(meeting_response.content)

    meeting_id = meeting['id']
    start_url = meeting['start_url']
    join_url = meeting['join_url']

    sesion = Sesion.objects.create(
        sesion_id = meeting_id,
        atencion = atencion,
        host_url = start_url,
        join_url = join_url
    )

    return sesion


def iniciar_sesion_reservada(atencion):
    pass

def finalizar_sesion(sesion):
    client.meeting.end(id = sesion.sesion_id, host_id = USER_ID)