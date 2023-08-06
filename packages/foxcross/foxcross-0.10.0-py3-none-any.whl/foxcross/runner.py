import importlib
import inspect
import logging
import re
import sys
from typing import Any, Tuple

import uvicorn
from slugify import slugify
from starlette.applications import Starlette
from starlette.types import ASGIApp

from .constants import SLUGIFY_REGEX, SLUGIFY_REPLACE
from .endpoints import _index_endpoint
from .exceptions import NoModelServingFoundError

logger = logging.getLogger(__name__)


class ModelServingRunner:
    def __init__(self, base_class: Any, excluded_classes: Tuple):
        self._excluded_classes = excluded_classes
        self._base_class = base_class

    def compose(self, module_name: str = "models", **kwargs) -> ASGIApp:
        try:
            python_module = importlib.import_module(module_name)
            logger.debug(f"Found python module {python_module} for model serving")
        except ModuleNotFoundError as exc:
            err_msg = f"Cannot find Python module named {module_name}: {exc}"
            logger.exception(err_msg)
            raise ModuleNotFoundError(err_msg)
        class_members = inspect.getmembers(sys.modules[module_name], inspect.isclass)
        serving_models = [
            class_
            for _, class_ in class_members
            if issubclass(class_, self._base_class)
            and class_ not in self._excluded_classes
        ]
        if not serving_models:
            err_msg = f"Could not find any model serving in {python_module}"
            logger.error(err_msg)
            raise NoModelServingFoundError(err_msg)
        elif len(serving_models) == 1:
            model_serving = serving_models[0](**kwargs)
            logger.debug(f"Initialized single model serving for {serving_models[0]}")
        else:
            model_serving = Starlette(**kwargs)
            for asgi_app in serving_models:
                slugified_app_name = slugify(
                    re.sub(SLUGIFY_REGEX, SLUGIFY_REPLACE, asgi_app.__name__)
                )
                model_serving.mount(f"/{slugified_app_name}", asgi_app(**kwargs))
            model_serving.add_route("/", _index_endpoint, methods=["GET"])
            logger.debug(f"Initialized multiple model serving for {serving_models}")
        return model_serving

    def run_model_serving(self, module_name: str = "models", **kwargs):
        debug = kwargs.get("debug", False)
        asgi_app = self.compose(module_name, **kwargs)
        uvicorn.run(asgi_app, debug=debug)
