import codecs
import pickle

from dash.dependencies import Input, Output
from dash_html_components import Div
from dash_infra.core import Callback, Component


class Storage(Component):
    """
    A storage component modifies a callback so
    it writes into a single serialized dictionary.
    This dictionary (state) has one key per registered
    callback, storing the output of the callback.
    """

    def __init__(self, id):
        self.callback_map = dict()
        self.storage_funcs = []
        self.state = {}
        self.store = Callback(self._store, outputs=(f"{id}", "value"), to_api=False)
        super().__init__(id)

    def _store(self, *inputs):
        """
        This is the storage main callback.
        It calls every registered callbacks and
        have them record into the state. 
        This state is then recorded into the hidden layout. 
        """
        start = 0
        for key, func, num_inputs in self.storage_funcs:
            end = start + num_inputs
            self.state[key] = func(*inputs[start:end])
            start += num_inputs

        return self._serializer(self.state)

    def layout(self):
        return Div(id=self.id, className="hide")

    def _serializer(self, *outputs):
        raise NotImplementedError

    def _deserializer(self, encoded_input):
        raise NotImplementedError

    def register_callback(self, callback, key=None):
        storage_key = key or callback.name
        self.callback_map[storage_key] = callback.name
        inputs = callback.dash_inputs

        self.storage_funcs.append((storage_key, callback.func, len(inputs)))

        self.store.add_inputs(
            [(i.component_id, i.component_property) for i in callback.dash_inputs]
        )

        return callback

    def add_deserializer(self, callback, *keys):
        if keys:

            def pre_hook(_, encoded_input):
                state = self._deserializer(encoded_input)
                return tuple(state[key] for key in keys)

        else:

            def pre_hook(_, encoded_input):
                return (self._deserializer(encoded_input),)

        callback._pre_function_hooks.append(pre_hook)


class PickleStorage(Storage):
    def _serializer(self, *outputs):
        if not outputs:
            outputs = ""

        if len(outputs) == 1:
            outputs = outputs[0]

        return codecs.encode(pickle.dumps(outputs), "base64").decode()

    def _deserializer(self, encoded_state):
        if encoded_state is None:
            return None

        d = pickle.loads(codecs.decode(encoded_state.encode(), "base64"))
        return d
