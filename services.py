#!/usr/bin/env python

import nudge.arg as args
from nudge import serve, Endpoint, Args
from nudge.renderer import HTML

class ExampleException(Exception): pass

class RmlApplication():
    """
    An initial nudge powered application for my personal
    www.raymleyva.com site.
    """
    def index(self):
        """
        The default entry point renderer for a semi static site.
        NOTE: This is NOT the way to use nudge, just doing this
              to have something to look at.
        """
        return """
            <html>
            <head><title>Ray M. Leyva ( NUDGE EDITION )<title></head>
            <body>
            <h1>Ray M. Leyva - The Nudge Years</h1>
            </html>
            """

rml = RmlApplication()

service_description = [
    Endpoint(name='Semi-static site entry point.',
        method='GET',
        uri='/$',
        function=rml.index,
        renderer=HTML(),
    ),
]

if __name__ == "__main__":
    serve(service_description)

