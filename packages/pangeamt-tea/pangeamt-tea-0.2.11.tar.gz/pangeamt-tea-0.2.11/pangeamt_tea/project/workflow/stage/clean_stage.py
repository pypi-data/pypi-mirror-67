import tempfile
import shutil
import os
from pathos.multiprocessing import Pool
import click
from pangeamt_tea.project.workflow.stage.base_stage import BaseStage
from pangeamt_nlp.processor.pipeline_training import PipelineTraining
from pangeamt_nlp.seg import Seg
from pangeamt_nlp.multilingual_resource.tmx.tmx_reader_bilingual import (
    TmxReaderBilingualText,
)
from pangeamt_nlp.multilingual_resource.af.af_reader import AfReader
from pangeamt_nlp.multilingual_resource.bilingual.bilingual_reader import (
    BilingualReader,
)
from pangeamt_nlp.multilingual_resource.dataset.dataset_reader import (
    DatasetReader,
)
from pangeamt_nlp.multilingual_resource.dataset.dataset import Dataset


def process(data, pipeline):
    seg = Seg(data[0], data[1])
    try:
        pipeline.process(seg)
        data = (seg.src, seg.tgt)
        return data
    except Exception as e:
        return e


def post(data, src_file, tgt_file, debug, log_file):
    if not isinstance(data, Exception):
        src_file.write(data[0] + "\n")
        tgt_file.write(data[1] + "\n")
    elif debug:
        log_file.write(str(data) + "\n")


class CleanStage(BaseStage):
    NAME = "clean"
    DIR = "01_cleaned"

    def __init__(self, workflow):
        super().__init__(workflow, self.NAME)

    async def run(self, max_workers: int, debug: bool):
        project = self.workflow.project
        project_dir = project.config.project_dir

        src_lang = project.config.src_lang
        tgt_lang = project.config.tgt_lang

        data_dir = self.create_data_directory()

        dataset = Dataset(data_dir)

        processors = project.config.processors

        # Make preparation Directory
        workflow_dir = self.workflow.get_dir(project_dir)
        self.stage_dir = os.path.join(workflow_dir, CleanStage.DIR)

        if os.path.isdir(self.stage_dir):
            raise Exception("Workflow stage folder already exists.")

        os.mkdir(self.stage_dir)

        af_reader = AfReader(src_lang, tgt_lang)
        bilingual_reader = BilingualReader(src_lang, tgt_lang)
        tmx_reader = TmxReaderBilingualText(src_lang, tgt_lang)

        dataset_reader = DatasetReader(tmx_reader, af_reader, bilingual_reader)
        dataset_length = dataset.get_num_trans_units()

        pipeline = PipelineTraining.create_from_dict(
            src_lang, tgt_lang, processors
        )

        src_file = open(os.path.join(self.stage_dir, "data_src.txt"), "w+")
        tgt_file = open(os.path.join(self.stage_dir, "data_tgt.txt"), "w+")
        if debug:
            log_file = open(
                os.path.join(self.stage_dir, "clean_log.txt"), "w+"
            )
        else:
            log_file = None

        with Pool(max_workers) as pool:
            with click.progressbar(
                pool.imap(
                    lambda x: process(x, pipeline),
                    dataset.read(dataset_reader),
                    chunksize=500,
                ),
                length=dataset_length,
                label="Cleaning: ",
            ) as bar:
                for result in bar:
                    post(result, src_file, tgt_file, debug, log_file)

        src_file.close()
        tgt_file.close()
        if log_file:
            log_file.close()

        shutil.rmtree(data_dir)

        num_lines = 0
        with open(
            os.path.join(self.stage_dir, "data_src.txt"), "r"
        ) as src_file:
            for line in src_file:
                num_lines += 1

        output = {
            "useful": num_lines,
            "dropped": dataset_length - num_lines,
        }

        return output

    def create_data_directory(self):
        config = self.workflow.config
        path = tempfile.mkdtemp()
        for resource in config.init["report"]["resources"]:
            files = resource["file"]
            if isinstance(files, str):
                files = [files]
            for file in files:
                dst = os.path.join(path, os.path.basename(file))
                os.symlink(file, dst)
        return path
