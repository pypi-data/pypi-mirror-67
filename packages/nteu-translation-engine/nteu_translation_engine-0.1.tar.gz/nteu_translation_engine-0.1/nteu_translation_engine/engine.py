from pangeamt_nlp.translation_model.translation_model_factory import (
    TranslationModelFactory,
)
from pangeamt_nlp.seg import Seg
from pipeline import Pipeline
from typing import Dict, List


class Engine:
    def __init__(self, config: Dict):
        self._config = config
        self._model = self.load_model()
        self._pipeline = Pipeline(config)

    def load_model(self):
        name = self._config["translation_model"]["name"]
        args = self._config["translation_model"]["args_decoding"]
        if self._config["translation_engine_server"]["gpu"]:
            args["gpu"] = 0
        model_path = self._config["translation_engine_server"]["model_path"]
        translation_model = TranslationModelFactory.get_class(name)
        return translation_model(model_path, **args)

    async def translate(self, srcs: List):
        return self._model.translate(srcs)

    async def process_batch(self, batch: List, lock):
        srcs = []
        segs = []
        ans = []
        for src in batch:
            seg = Seg(src)
            await self._pipeline.preprocess(seg)
            srcs.append(seg.src)
            segs.append(seg)
        async with lock:
            translations = await self.translate(srcs)
        for translation, seg in zip(translations, segs):
            seg.tgt = seg.tgt_raw = translation
            await self._pipeline.postprocess(seg)
            ans.append(seg.tgt)
        return ans
