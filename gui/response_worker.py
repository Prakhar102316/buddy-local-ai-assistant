import threading


class ResponseWorker(threading.Thread):

    def __init__(self, backend, prompt, on_chunk, on_complete):

        super().__init__(daemon=True)

        self.backend = backend
        self.prompt = prompt

        self.on_chunk = on_chunk
        self.on_complete = on_complete

    def run(self):

        try:

            for chunk in self.backend.stream_ask(self.prompt):

                self.on_chunk(chunk)

        finally:

            self.on_complete()