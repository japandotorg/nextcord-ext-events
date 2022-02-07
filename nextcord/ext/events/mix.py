import asyncio

import nextcord

from ._events import _ALL

class EventsMix(nextcord.Client):
    
    async def on__event(self, event, *args, **kwargs):
        for event_name, event_check in _ALL.items():
            asyncio.ensure_future(event_check(self, event, *args, **kwargs))
            
    def dispatch(self, event, *args, **kwargs):
        super().dispatch(event, *args, **kwargs)
        super().dispatch('_event', event, *args, **kwargs)