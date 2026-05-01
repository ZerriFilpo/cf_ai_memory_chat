from workers import WorkerEntrypoint, Response

import json


class Default(WorkerEntrypoint):
    async def fetch(self, request):
        if request.method == 'POST':
            body = await request.json()
            return Response(json.dumps(body))
        return Response('Method not allowed', status=405)
