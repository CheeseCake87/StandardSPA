from flask_imp import ImpBlueprint
from flask_imp.config import ImpBlueprintConfig

bp = ImpBlueprint(__name__, ImpBlueprintConfig(
    enabled=True,
    url_prefix="/testing",
    static_folder="static",
    template_folder="templates"
))

bp.import_resources("routes")
