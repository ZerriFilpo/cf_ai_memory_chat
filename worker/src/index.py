from workers import WorkerEntrypoint, Response
from pyodide.ffi import to_js
from js import Object
class Default(WorkerEntrypoint):

    async def fetch(self, request):

        if request.method == 'POST':

            body = await request.json()
            message = body['message']
            response = await self.env.AI.run(
                "@cf/meta/llama-3.3-70b-instruct-fp8-fast",
                to_js({"messages": [{"role": "user", "content": message}]}, dict_converter=Object.fromEntries)
            )
            return Response(response.response)
        
        return Response('Method not allowed', status=405)