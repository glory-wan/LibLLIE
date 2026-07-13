"""Top-level convenience API for_teach LibLLIE."""

from pathlib import Path
from typing import Any, Dict, List, Mapping, Optional, Type, Union


_PREDICT_CALL_KWARGS = {
    "progress_bar",
    "output_name",
    "output_ext",
    "save",
    "ext",
    "timeout",
    "headers",
    "verify_ssl",
}

_MISSING = object()


def _split_predict_kwargs(kwargs: Dict[str, Any]):
    """Split predictor construction kwargs from prediction-call kwargs.

    Args:
        kwargs: Keyword arguments passed to the top-level ``predict`` API.

    Returns:
        Tuple of ``(predictor_kwargs, call_kwargs)``. ``predictor_kwargs`` are
        used to construct ``Predictor`` and ``call_kwargs`` are forwarded to
        the predictor call.
    """
    predictor_kwargs = {}
    call_kwargs = {}

    for key, value in kwargs.items():
        if key in _PREDICT_CALL_KWARGS:
            call_kwargs[key] = value
        else:
            predictor_kwargs[key] = value

    return predictor_kwargs, call_kwargs


def predict(
    target,
    source,
    output: Optional[Union[str, Path]] = None,
    **kwargs: Any,
):
    """Enhance a single image or folder with a deep-learning model or
    traditional method.

    Args:
        target: Deep-learning model name or traditional method name.
        source: Image source or folder path.
        output: Optional output file path or directory path.
        **kwargs: Keyword arguments used by ``Predictor`` construction or the
            prediction call.

    Returns:
        Prediction result returned by ``Predictor``.

    Examples:
        libllie.predict("ZeroDCE", "input.jpg", output="out.png")
        libllie.predict("he", "images", output="results/he")
    """
    from libllie.Predictor import Predictor

    predictor_kwargs, call_kwargs = _split_predict_kwargs(kwargs)
    predictor = Predictor(target, **predictor_kwargs)
    return predictor(source, output=output, **call_kwargs)

def enhance(target, source, output: Optional[Union[str, Path]] = None, **kwargs: Any,):
    """Enhance a source image or folder.

    Args:
        target: Deep-learning model name or traditional method name.
        source: Image source or folder path.
        output: Optional output file path or directory path.
        **kwargs: Keyword arguments forwarded to ``predict``.

    Returns:
        Prediction result returned by ``predict``.
    """
    return predict(target, source, output=output, **kwargs)

def train(config: Optional[Union[str, Path, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
    """Train a model through the unified top-level API.

    Args:
        config: YAML path or config dictionary. Keyword arguments are forwarded
            to Trainer and can override config values.
        **kwargs: Additional keyword arguments forwarded to ``Trainer``.

    Returns:
        Training result dictionary returned by ``Trainer.train``.
    """
    from libllie.deepLearning import Trainer

    trainer = Trainer(config, **kwargs)
    return trainer.train()


def evaluate(
    en_img_dir: Any = _MISSING,
    ref_img_dir: Any = _MISSING,
    metrics: Optional[Union[str, List[str]]] = None,
    save_path: Optional[Union[str, Path]] = None,
    return_evaluator: bool = False,
    *,
    en: Any = _MISSING,
    ref: Any = _MISSING,
    **kwargs: Any,
):
    """Evaluate enhanced images through the unified top-level API.

    Args:
        en_img_dir: Directory containing enhanced images.
        ref_img_dir: Optional reference image directory.
        metrics: Metric name or list of metric names.
        save_path: Optional JSON result path.
        return_evaluator: Return the Evaluator instance instead of results.
        en: Backward-compatible alias for ``en_img_dir``.
        ref: Backward-compatible alias for ``ref_img_dir``.
        **kwargs: Additional keyword arguments forwarded to ``Evaluator``.

    Returns:
        Evaluation results, or the evaluator instance when
        ``return_evaluator`` is ``True``.
    """
    from libllie.evaluation import Evaluator
    import libllie.evaluation.metrics  # noqa: F401

    if en is not _MISSING:
        if en_img_dir is not _MISSING:
            raise TypeError(
                "evaluate() received both 'en_img_dir' and its alias 'en'"
            )
        en_img_dir = en

    if ref is not _MISSING:
        if ref_img_dir is not _MISSING:
            raise TypeError(
                "evaluate() received both 'ref_img_dir' and its alias 'ref'"
            )
        ref_img_dir = ref

    if en_img_dir is _MISSING:
        raise TypeError("evaluate() missing required argument: 'en_img_dir'")

    if ref_img_dir is _MISSING:
        ref_img_dir = None

    evaluator = Evaluator(
        en_img_dir=str(en_img_dir),
        ref_img_dir=str(ref_img_dir) if ref_img_dir is not None else None,
        metrics=metrics,
        save_path=save_path,
        **kwargs,
    )
    return evaluator if return_evaluator else evaluator.results


def eval(*args: Any, **kwargs: Any):
    """Evaluate enhanced images through the alias API.

    Args:
        *args: Positional arguments forwarded to ``evaluate``.
        **kwargs: Keyword arguments forwarded to ``evaluate``.

    Returns:
        Evaluation result returned by ``evaluate``.
    """
    return evaluate(*args, **kwargs)


def imread(source: Any, output_format: str = "pil", **kwargs: Any) -> Any:
    """Read an image through the unified top-level API.

    Args:
        source: Image source accepted by ``read_image``.
        output_format: Desired output format.
        **kwargs: Additional keyword arguments forwarded to ``read_image``.

    Returns:
        Image object in the requested output format.
    """
    from libllie.data.image_io import read_image

    return read_image(source, output_format=output_format, **kwargs)


def imwrite(
    image: Any,
    output: Optional[Union[str, Path]] = None,
    *,
    save_format: Optional[str] = None,
    output_name: Optional[str] = None,
    **kwargs: Any,
) -> Path:
    """Write an image through the unified top-level API.

    Args:
        image: Image object accepted by ``write_image``.
        output: Optional output file path or directory path.
        save_format: Optional output format override.
        output_name: Optional output filename used when saving to a directory.
        **kwargs: Additional keyword arguments forwarded to ``write_image``.

    Returns:
        Saved image path.
    """
    from libllie.data.image_io import write_image

    return write_image(
        image,
        output=output,
        save_format=save_format,
        output_name=output_name,
        **kwargs,
    )


read_image = imread
write_image = imwrite


def list_models() -> List[str]:
    """List available deep-learning model names.

    Returns:
        List of model names registered in the unified predictor.
    """
    from libllie.Predictor import Predictor

    return Predictor.list_available_models()


def list_algorithms() -> List[str]:
    """List available traditional enhancement algorithm names.

    Returns:
        List of traditional algorithm names registered in the unified predictor.
    """
    from libllie.Predictor import Predictor

    return Predictor.list_available_methods()


def list_metrics() -> List[str]:
    """List available evaluation metric names.

    Returns:
        List of registered evaluation metric names.
    """
    import libllie.evaluation.metrics  # noqa: F401
    from libllie.evaluation import Evaluator

    return Evaluator.list_available_metrics()

def list_losses() -> List[str]:
    """List available deep-learning loss names.

    Returns:
        List of registered loss names.
    """
    from libllie.deepLearning import BaseLoss

    return BaseLoss.list_registered_losses()

def list_datasets() -> List[str]:
    """List available dataset names.

    Returns:
        List of registered dataset names.
    """
    from libllie.data import BaseDataset

    return BaseDataset.list_registered_datasets()


def _component_rows(registry: Mapping[str, Type[Any]]) -> List[Dict[str, Any]]:
    """Build display rows from a component registry.

    Registries contain one entry for every accepted lookup key, so a component
    class usually appears more than once through its class name, configured
    name, and aliases. Rows are therefore deduplicated by class object.

    Args:
        registry: Mapping of normalized lookup keys to component classes.

    Returns:
        Component rows sorted by implementation class name. Each row contains
        the class ``name`` and the aliases declared by that class.
    """
    component_classes = set(registry.values())
    rows: List[Dict[str, Any]] = []

    for component_class in sorted(
        component_classes,
        key=lambda value: value.__name__.casefold(),
    ):
        aliases = getattr(component_class, "aliases", [])
        if isinstance(aliases, str):
            aliases = [aliases]
        else:
            aliases = list(aliases)

        rows.append(
            {
                "name": component_class.__name__,
                "aliases": aliases,
            }
        )

    return rows


def list_available() -> Dict[str, List[Dict[str, Any]]]:
    """List public component classes and their declared aliases.

    The returned rows are grouped by component category. Unlike the individual
    ``list_*`` functions, registry lookup keys are not flattened into one list:
    each implementation class appears exactly once and keeps its aliases as a
    separate field.

    Returns:
        Dictionary containing model, algorithm, metric, loss, and dataset rows.
        Every row has ``name`` and ``aliases`` keys.
    """
    from libllie.data import BaseDataset
    from libllie.deepLearning.loss import BaseLoss
    from libllie.deepLearning.models import LLIEModel
    from libllie.evaluation import BaseMetric
    from libllie.traditional.algorithms import LLIEnhancer

    return {
        "models": _component_rows(LLIEModel._model_registry),
        "algorithms": _component_rows(LLIEnhancer._enhancer_registry),
        "metrics": _component_rows(BaseMetric._metric_registry),
        "losses": _component_rows(BaseLoss._loss_registry),
        "datasets": _component_rows(BaseDataset._dataset_registry),
    }
