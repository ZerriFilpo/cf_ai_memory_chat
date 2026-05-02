from workers import WorkerEntrypoint, Response
from pyodide.ffi import to_js
import json
from js import Object
class Default(WorkerEntrypoint):

    async def fetch(self, request):

        headers = {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "POST, OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type"
        }

        if request.method == 'POST':

            body = await request.json()
            message = body['message']

            history = await self.env.MEMORY.get("conversation")

            if not history:
              history = []
            else:
                history = json.loads(history)

            #test code to check if memory is working and to see the format of the history object
            'return Response(json.dumps({"history": history, "type": str(type(history))}))'

            history.append({"role": "user", "content": message})
    
            response = await self.env.AI.run(
                "@cf/meta/llama-3.3-70b-instruct-fp8-fast",
                to_js({"messages": history}, dict_converter=Object.fromEntries)
            )

            response = str(response.response)

            history.append({"role": "assistant", "content": response})

            await self.env.MEMORY.put("conversation", json.dumps(history))

            """Testing memory functionality:
               curl -X POST ... -H "Content-Type: application/json" -d '{"message": "my name is Zerri"}'
               curl -X POST ... -H "Content-Type: application/json" -d '{"message": "what is my name?"}'
               It forgot my name! :( 
               Fixed adding str() arround response.response, because it was a JavaScript string and it was not 
               being serialized properly when stored in memory, now it works fine!:
            """

            return Response(response, headers=to_js(headers, dict_converter=Object.fromEntries))


        # Check if it's a preflight request
        if request.method == 'OPTIONS':
            return Response(status=204, headers=to_js(headers, dict_converter=Object.fromEntries))
        
        return Response('Method not allowed', status=405)