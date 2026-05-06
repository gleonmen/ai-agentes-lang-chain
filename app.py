"""
Entrada ASGI para despliegue en la nube.

Permite iniciar el servicio con:
uvicorn app:app --host 0.0.0.0 --port $PORT
"""

from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import sys


MODULE_PATH = Path(__file__).with_name("main_chatwoot-ia_off.py")
spec = spec_from_file_location("main_chatwoot_ia_off", MODULE_PATH)

if spec is None or spec.loader is None:
    raise RuntimeError(f"No se pudo cargar el modulo FastAPI desde {MODULE_PATH}")

module = module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)

app = module.app
